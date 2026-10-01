from tkinter import Text

texto = "Este texto quebra de linha \naqui. Porém aqui temos uma \ttabulação"
print(texto)

texto = ("texto em minusculas AINDA É texto")
print(texto.capitalize())

print(texto.upper())
print(texto.lower())
print(texto.startswith("tex"))
print(texto.startswith("Tex"))
print(texto.endswith("!"))
print(texto.endswith("to"))
print(texto.count("1"))
print(texto.count("t"))
print("em" in texto)
print(texto.replace("AINDA","com certeza"))