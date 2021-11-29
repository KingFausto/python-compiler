from re import X
from token_ import Token
from abc import ABC, abstractmethod


class Expresion(ABC):
    pass


class ExpresionAsignacion(Expresion):
    def __init__(self, identificador: Token, expresion: Expresion):
        self.identificador = identificador
        self.expresion = expresion

    def __repr__(self):
        return f"{self.identificador} = {self.expresion}"


class ExpresionIF(Expresion):
    def __init__(self, condicion: Expresion, cuerpo: Expresion, else_: Expresion):
        self.condicion = condicion
        self.cuerpo = cuerpo
        self.else_ = else_

    def __repr__(self):
        return f"if({self.condicion},{self.cuerpo},{self.else_})"


class ExpresionInfijo(Expresion):
    def __init__(
        self,
        primera_expresion: Expresion,
        operador: Token,
        segunda_expresion: Expresion,
    ):
        self.primera_expresion = primera_expresion
        self.operador = operador
        self.segunda_expresion = segunda_expresion

    def __repr__(self):
        return (
            f"{self.operador.valor}({self.primera_expresion},{self.segunda_expresion})"
        )


class ExpresionPrefijo(Expresion):
    def __init__(self, operador: Token, expresion: Expresion):
        self.operador = operador
        self.expresion = expresion

    def __repr__(self):
        return f"{self.operador.valor}({self.expresion})"


class Numero(Expresion):
    def __init__(self, numero: Token):
        self.numero = numero

    def __repr__(self):
        return str(self.numero.valor)


class Cadena(Expresion):
    def __init__(self, cadena: Token):
        self.cadena = cadena

    def __repr__(self):
        return self.cadena


class Booleano(Expresion):
    def __init__(self, booleano: Token):
        self.booleano = booleano

    def __repr__(self):
        return str(self.booleano)


"""expr -> IF | WHILE | FOR | RETURN 
IF -> if expr: expr | if expr: expr else expr | if expr: expr elif expr 
WHILE -> while expr: expr

if_ = Node("IF")
if x < 5:
    print("HELLO WORLD")

EXPRESIONCONDICIONAL 
| - CONDICION
|    | - (IDENTIFIACDOR, 3)
|    | - (MENIGUAL, +)
|    | - (NUMERO, 5)
| - CUERPO
|   | - 
"""
