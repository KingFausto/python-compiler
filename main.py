from compilador import Compilador


def main():
    compilador = Compilador()
    codigo = compilador.compilar_codigo("test-2.txt")
    print(codigo)


if __name__ == "__main__":
    main()
