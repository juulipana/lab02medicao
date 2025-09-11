import csv
import os
import subprocess
from datetime import datetime

CSV_FILE = "top1000_java_repos_20250910_210138.csv"
CK_JAR = r"C:\Projects\lab02medicao\qualidade_de_sistemas_java\app\tools\ck-0.7.1-SNAPSHOT-jar-with-dependencies.jar"

OUTPUT_DIR = r"C:\Users\pedro.oliveira_onfly\Desktop\precisarei"

def clone_repo(repo_url, repo_name):
    repo_path = os.path.join(OUTPUT_DIR, repo_name)
    if not os.path.exists(repo_path):
        print(f"Clonando {repo_name}...")
        subprocess.run(["git", "clone", repo_url, repo_path])
    return repo_path

def run_ck(repo_path, repo_name):
    print(f"Rodando CK no {repo_name}...")
    ck_output = os.path.join("ck_results", repo_name)
    os.makedirs(ck_output, exist_ok=True)

    JAVA_PATH = r"C:\Program Files\Java\jdk-24\bin\java.exe"
    subprocess.run([
        JAVA_PATH, "-jar", CK_JAR, repo_path, "true", "0", "false"
    ], cwd=ck_output)

def main():
    os.makedirs(OUTPUT_DIR, exist_ok=True)

    with open(CSV_FILE, newline="", encoding="utf-8") as csvfile:
        reader = csv.DictReader(csvfile)
        for i, row in enumerate(reader):
            if i >= 1:
                break

            repo_url = row["html_url"]
            repo_name = row["name"]

            repo_path = clone_repo(repo_url, repo_name)
            run_ck(repo_path, repo_name)

if __name__ == "__main__":
    main()