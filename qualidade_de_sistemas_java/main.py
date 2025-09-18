import csv
import os
import shutil
import subprocess
import stat
import pandas as pd
import numpy as np
from concurrent.futures import ThreadPoolExecutor, as_completed

CSV_FILE = "top1000_java_repos_20250910_210138.csv"
CK_JAR = r"C:\Projects\lab02medicao\qualidade_de_sistemas_java\app\tools\ck-0.7.1-SNAPSHOT-jar-with-dependencies.jar"
AGGREGATED_CSV = r"C:\Users\pedro.oliveira_onfly\Desktop\precisarei\ck_aggregated_results.csv"

OUTPUT_DIR = r"C:\Users\pedro.oliveira_onfly\Desktop\precisarei"
CK_RESULTS_DIR = os.path.join(OUTPUT_DIR, "ck_results")
FINAL_CSV = os.path.join(OUTPUT_DIR, "ck_all_results.csv")
MAX_WORKERS = 4

JAVA_PATH = r"C:\Program Files\Java\jdk-24\bin\java.exe"

def clone_repo(repo_url, repo_name):
    repo_path = os.path.join(OUTPUT_DIR, repo_name)
    if not os.path.exists(repo_path):
        print(f"[INFO] Clonando {repo_name}...")
        subprocess.run(["git", "clone", "--depth", "1", repo_url, repo_path], check=True)
    else:
        print(f"[INFO] {repo_name} já existe, reutilizando.")
    return repo_path

def run_ck(repo_path, repo_name):
    ck_output = os.path.join(CK_RESULTS_DIR, repo_name)
    class_csv = os.path.join(ck_output, "class.csv")

    # se já tem resultados, pula
    if os.path.exists(class_csv):
        print(f"[INFO] {repo_name} já processado, pulando CK.")
        return ck_output

    print(f"[INFO] Rodando CK no {repo_name}...")
    os.makedirs(ck_output, exist_ok=True)
    subprocess.run([
        JAVA_PATH, "-jar", CK_JAR, repo_path, "true", "0", "false"
    ], cwd=ck_output, check=True)
    return ck_output

def append_results(repo_name, ck_output):
    class_csv = os.path.join(ck_output, "class.csv")
    if not os.path.exists(class_csv):
        print(f"[WARN] Não encontrei métricas em {repo_name}")
        return

    with open(class_csv, newline="", encoding="utf-8") as infile:
        reader = csv.DictReader(infile)

        # cria o final se não existir
        write_header = not os.path.exists(FINAL_CSV)
        with open(FINAL_CSV, "a", newline="", encoding="utf-8") as outfile:
            fieldnames = ["repository"] + reader.fieldnames
            writer = csv.DictWriter(outfile, fieldnames=fieldnames)

            if write_header:
                writer.writeheader()

            for row in reader:
                row["repository"] = repo_name
                writer.writerow(row)

def delete_repo(repo_path, repo_name):
    try:
        shutil.rmtree(repo_path, onerror=handle_remove_readonly)
        print(f"[INFO] Repositório {repo_name} removido com sucesso.")
    except Exception as e:
        print(f"[ERRO] Falha ao remover {repo_name}: {e}")

def handle_remove_readonly(func, path, exc_info):
    os.chmod(path, stat.S_IWRITE)
    func(path)

def process_repo(row):
    repo_url = row["html_url"]
    repo_name = row["name"]
    try:
        repo_path = clone_repo(repo_url, repo_name)
        ck_output = run_ck(repo_path, repo_name)
        append_results(repo_name, ck_output)
    except Exception as e:
        print(f"[ERRO] Falha ao processar {repo_name}: {e}")
    finally:
        delete_repo(os.path.join(OUTPUT_DIR, repo_name), repo_name)


def aggregate_ck_results(csv_file=FINAL_CSV, output_file=AGGREGATED_CSV):
    # Lê o CSV
    df = pd.read_csv(csv_file)

    # Substitui NaN por 0
    df = df.replace({np.nan: 0})

    # Identifica colunas numéricas para somar
    numeric_cols = df.columns.drop("repository")

    # Converte todas para float (ou int, dependendo da necessidade)
    df[numeric_cols] = df[numeric_cols].apply(pd.to_numeric, errors='coerce').fillna(0)

    # Agrupa por repository e soma as colunas
    aggregated = df.groupby("repository", as_index=False)[numeric_cols].sum()

    # Salva o CSV final
    aggregated.to_csv(output_file, index=False)
    print(f"[INFO] CSV agregado salvo em: {output_file}")
    return aggregated


def main():
    os.makedirs(OUTPUT_DIR, exist_ok=True)
    os.makedirs(CK_RESULTS_DIR, exist_ok=True)

    with open(CSV_FILE, newline="", encoding="utf-8") as csvfile:
        reader = list(csv.DictReader(csvfile))[:1000]

    with ThreadPoolExecutor(max_workers=MAX_WORKERS) as executor:
        futures = [executor.submit(process_repo, row) for row in reader]
        for future in as_completed(futures):
            try:
                future.result()
            except Exception as e:
                print(f"[ERRO] Exceção em thread: {e}")

if __name__ == "__main__":
    aggregate_ck_results()
    #main()
