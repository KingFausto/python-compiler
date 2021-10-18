import re
from analizador_lexico import AnalizadorLexico
from analizador_sintactico import AnalizadorSintactico
from analizador_semantico import AnalizadorSemantico

class Compilador:
    def __init__(self):
        self.analizador_lexico = AnalizadorLexico()
        self.analizador_sintactico = AnalizadorSintactico()
        self.analizador_semantico = AnalizadorSemantico()

    def _arreglar_separadores(self, codigo):
        for i in "[](){};,":
            codigo = re.sub(rf"\{i}", rf" {i} ", codigo)
        return codigo

    def _arreglar_strings(self, codigo):
        codigo = codigo.split()
        nuevo_codigo = []
        value = ""
        creando_string = False

        for i in codigo:
            if i[0] == '"' and i[-1] == '"' and not creando_string and len(i) > 1:
                nuevo_codigo.append(i)
            elif i[0] == '"' and not creando_string:
                creando_string = True
                value += i
            elif creando_string and i[-1] == '"':
                value += " " + i
                creando_string = False      
                nuevo_codigo.append(value)
                value = ""
            elif creando_string:
                value += " " + i
            else:
                nuevo_codigo.append(i)

        return nuevo_codigo

    def _preprocesar_codigo(self, codigo):
        codigo = self._arreglar_separadores(codigo)
        codigo = self._arreglar_strings(codigo)
        return codigo

    def crear_tokens(self, codigo):
        codigo = self._preprocesar_codigo(codigo)
        tokens = self.analizador_lexico.crear_tokens(codigo)
        return tokens