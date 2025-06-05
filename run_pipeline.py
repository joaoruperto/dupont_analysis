import os
import subprocess

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

scripts = [
    "00-RUN_ONLY_FIRST_TIME---Downloading_all_data_CVM.py",
    "01-Updating_Data_CVM.py",
    "02-Merging_data_CVM.py",
    "04-Creating_All_Companies_DataFrame.py",
    "05-Updating_Prices_DataFrame.py"
]

print("=" * 60)
print("🚀 Iniciando pipeline de dados financeiros brasileiros")
print("=" * 60)

for script in scripts:
    path_script = os.path.join(BASE_DIR, script)
    if os.path.exists(path_script):
        print(f"\n▶️ Executando {script}...\n")
        try:
            subprocess.run(["python", path_script], check=True)
        except subprocess.CalledProcessError:
            print(f"❌ Erro ao executar {script}")
            break
    else:
        print(f"⚠️ Script não encontrado: {script}")

print("\n✅ Pipeline finalizado.")
print("📁 Verifique o arquivo final em: clean_data/final_data/df_principal.pkl")
