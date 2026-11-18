import re as reg

filename=R"D:\piplo025 py\exercicios18-11-26\dados.txt"

with open(filename, "r", encoding="utf-8") as ficheiro:
    texto = ficheiro.read()

telefone = reg.findall(r"\b(?:\d{9}|\d{3}-\d{3}-\d{3}|\d{3} \d{3} \d{3})\b", texto)

print(telefone)