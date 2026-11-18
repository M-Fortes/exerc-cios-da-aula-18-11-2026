import re as reg

filename=R"D:\piplo025 py\exercicios18-11-26\dados.txt"

with open(filename, "r", encoding="utf-8") as ficheiro:
    texto = ficheiro.read()

emailpt = reg.findall(r"[\w.-]+@[\w.-]+\.pt\b", texto)

print(emailpt)