import re as reg

filename=R"D:\piplo025 py\exercicios18-11-26\dados.txt"

with open(filename, "r", encoding="utf-8") as ficheiro:
    texto = ficheiro.read()

nomes = reg.findall(r"Nome:\s*([^,|\n]+)", texto)

print(nomes)