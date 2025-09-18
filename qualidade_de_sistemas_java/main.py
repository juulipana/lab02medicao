import csv
import os
import subprocess
from datetime import datetime
import pandas as pd
import matplotlib.pyplot as plt

CSV_FILE = "top1000_java_repos_20250910_210138.csv"
CK_JAR = r"C:\Projects\lab02medicao\qualidade_de_sistemas_java\app\tools\ck-0.7.1-SNAPSHOT-jar-with-dependencies.jar"
OUTPUT_DIR = r"C:\Users\pedro.oliveira_onfly\Desktop\precisarei"
CK_RESULTS_DIR = os.path.join(OUTPUT_DIR, "ck_results")
JAVA_PATH = r"C:\Program Files\Java\jdk-24\bin\java.exe"

def clone_repo(repo_url, repo_name):
    repo_path = os.path.join(OUTPUT_DIR, repo_name)
    if not os.path.exists(repo_path):
        print(f"Clonando {repo_name}...")
        subprocess.run(["git", "clone", repo_url, repo_path], check=True)
    else:
        print(f"{repo_name} já existe, pulando clone.")
    return repo_path

def run_ck(repo_path, repo_name):
    print(f"Rodando CK no {repo_name}...")
    ck_output = os.path.join(CK_RESULTS_DIR, repo_name)
    os.makedirs(ck_output, exist_ok=True)

    subprocess.run([
        JAVA_PATH, "-jar", CK_JAR, repo_path, "true", "0", "false"
    ], cwd=ck_output, check=True)

    class_csv = os.path.join(ck_output, "class.csv")
    if os.path.exists(class_csv):
        df_ck = pd.read_csv(class_csv)
        loc_total = df_ck['LOC'].sum() if 'LOC' in df_ck.columns else 0
    else:
        loc_total = 0
    return loc_total

def analisar_repositorios(csv_file, ck_results_summary_file):
    df_repos = pd.read_csv(csv_file)
    df_repos['created_at'] = pd.to_datetime(df_repos['created_at'])
    df_repos['updated_at'] = pd.to_datetime(df_repos['updated_at'])
    df_repos['idade_dias'] = (df_repos['updated_at'] - df_repos['created_at']).dt.days
    df_repos['atividade'] = df_repos['stargazers_count'] + df_repos['open_issues']

    df_ck = pd.read_csv(ck_results_summary_file)
    df = pd.merge(df_repos, df_ck, left_on='name', right_on='repo_name', how='inner')

    corr_atividade = df['idade_dias'].corr(df['atividade'])
    corr_loc = df['idade_dias'].corr(df['loc_total'])
    print(f"Correlação Idade x Atividade: {corr_atividade:.3f}")
    print(f"Correlação Idade x LOC: {corr_loc:.3f}")

    plt.figure(figsize=(12,5))
    plt.subplot(1,2,1)
    plt.scatter(df['idade_dias'], df['atividade'], alpha=0.6)
    plt.xlabel("Idade do Repositório (dias)")
    plt.ylabel("Atividade (stars + issues)")
    plt.title("Idade x Atividade")

    plt.subplot(1,2,2)
    plt.scatter(df['idade_dias'], df['loc_total'], alpha=0.6, color='orange')
    plt.xlabel("Idade do Repositório (dias)")
    plt.ylabel("LOC Total")
    plt.title("Idade x Tamanho (LOC)")
    plt.tight_layout()
    plt.show()

    bins = [0, 365, 3*365, 5*365, 10*365, df['idade_dias'].max()]
    labels = ["0-1a", "1-3a", "3-5a", "5-10a", ">10a"]
    df['faixa_idade'] = pd.cut(df['idade_dias'], bins=bins, labels=labels)

    plt.figure(figsize=(12,5))
    plt.subplot(1,2,1)
    df.boxplot(column='atividade', by='faixa_idade', grid=False)
    plt.title("Atividade por Faixa de Idade")
    plt.suptitle("")

    plt.subplot(1,2,2)
    df.boxplot(column='loc_total', by='faixa_idade', grid=False)
    plt.title("LOC por Faixa de Idade")
    plt.suptitle("")
    plt.tight_layout()
    plt.show()


def main():
    os.makedirs(OUTPUT_DIR, exist_ok=True)
    os.makedirs(CK_RESULTS_DIR, exist_ok=True)

    ck_summary = []

    with open(CSV_FILE, newline="", encoding="utf-8") as csvfile:
        reader = csv.DictReader(csvfile)
        for i, row in enumerate(reader):
            repo_url = row["html_url"]
            repo_name = row["name"]

            repo_path = clone_repo(repo_url, repo_name)
            loc_total = run_ck(repo_path, repo_name)

            ck_summary.append({"repo_name": repo_name, "loc_total": loc_total})

    ck_summary_file = os.path.join(OUTPUT_DIR, "ck_results_summary.csv")
    pd.DataFrame(ck_summary).to_csv(ck_summary_file, index=False)

    analisar_repositorios(CSV_FILE, ck_summary_file)

if __name__ == "__main__":
    main()
