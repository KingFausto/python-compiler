from compilador import Compilador

if __name__ == "__main__":
    compilador = Compilador()
    codigo = compilador.compilar_codigo("test-3.txt")
    print(codigo)
