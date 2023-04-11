array = []

for i in range(3):
    n = int(input("Introduzca un número: "))
    array.append(n)

media = sum(array) / len(array)
print(f"La media es {media}")