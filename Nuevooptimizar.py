class Optimizar:
    array = []
    def inp(self):
        print("Introduce un numero ")
        return int(input())

    def add(self,n):
        self.array.append(n)

    def media(self):
        suma = sum(self.array)
        media = suma / len(self.array)
        return media