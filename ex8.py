import re as reg

filename=R"D:\piplo025 py\exercicios18-11-26\registos.txt"

with open(filename, "r", encoding="utf-8") as ficheiro:
    texto = ficheiro.read()

datas = reg.findall(r"\b\d{2}/\d{2}/\d{4}\b", texto)

print(datas)