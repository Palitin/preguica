nome = "ao"
campos = ["dog", "gatinhow"]

comando = f"CREATE TABLE {nome} (ID int AUTO_INCREMENT"
for campo in campos:
    comando += f", {campo} varchar"
comando += ")"

print(comando)