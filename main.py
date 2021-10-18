from compilador import Compilador

if __name__ == "__main__":
    compilador = Compilador()

    with open("test.txt", "r") as f:
        for i in f.readlines():
            print(i)
            print(compilador.crear_tokens(i))