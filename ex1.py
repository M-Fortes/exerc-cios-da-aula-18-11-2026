import os

filename=R"D:\piplo025 py\exercicios18-11-26"

with open("dados.txt", "r", encoding="utf-8") as ficheiro:
    texto = ficheiro.read()

print(texto)