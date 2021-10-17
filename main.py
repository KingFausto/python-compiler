from token import AnalizadorLexico
x=5

if __name__ == "__main__":
    analizador = AnalizadorLexico(r"5 ¬_¬ 5")
    tokens = analizador.tokenizar()
    print(tokens)