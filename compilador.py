import re
from analizador_lexico import AnalizadorLexico
from analizador_sintactico import AnalizadorSintactico
from analizador_semantico import AnalizadorSemantico


class Compilador:
    def __init__(self):
        self.analizador_lexico = AnalizadorLexico()
        self.analizador_sintactico = AnalizadorSintactico()
        self.analizador_semantico = AnalizadorSemantico()

    def _arreglar_separadores(self, codigo: str) -> str:
        for i in "[](){};,":
            codigo = re.sub(rf"\{i}", rf" {i} ", codigo)
        return codigo

    def _arreglar_strings(self, codigo: str) -> list:
        codigo: list = codigo.split()
        nuevo_codigo: list = []
        value: str = ""
        creando_string: bool = False

        for i in codigo:
            if creando_string:
                if i.endswith('"'):
                    nuevo_codigo.append(value + " " + i)
                    value = ""
                    creando_string = False
                else:
                    value += " " + i
            else:
                if i.startswith('"'):
                    if i.endswith('"') and len(i) > 1:
                        nuevo_codigo.append(i)
                    else:
                        creando_string = True
                        value += i
                else:
                    nuevo_codigo.append(i)

        return nuevo_codigo

    def _preprocesar_codigo(self, codigo: str) -> list:
        codigo: str = self._arreglar_separadores(codigo)
        codigo: list = self._arreglar_strings(codigo)
        return codigo

    def crear_tokens(self, codigo: str) -> list:
        codigo: list = self._preprocesar_codigo(codigo)
        tokens: list = self.analizador_lexico.crear_tokens(codigo)
        return tokens
