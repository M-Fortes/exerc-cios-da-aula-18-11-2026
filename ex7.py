import re as reg

filename=R"D:\piplo025 py\exercicios18-11-26\registos.txt"

with open(filename, "r", encoding="utf-8") as ficheiro:
    texto = ficheiro.read()

nif = reg.findall(r"\b\d{9}\b", texto)

print(nif)