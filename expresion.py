from __future__ import annotations
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
        return f"ASIGN({self.identificador.valor},{self.expresion})"


class ExpresionCondicion(Expresion):
    def __init__(self, tipo: Token, condicion: Expresion, cuerpo: Bloque, else_: Bloque):
        self.tipo = tipo
        self.condicion = condicion
        self.cuerpo = cuerpo
        self.else_ = else_

    def __repr__(self):
        return f"{self.tipo.tipo}({self.condicion},{self.cuerpo},{self.else_})"


class ExpresionSwitch(Expresion):
    def __init__(self, match: Expresion, cases: list[Expresion]):
        self.match = match
        self.cases = cases

    def __repr__(self):
        return f"SWITCH({self.match},CASES{self.cases})"


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
            f"{self.operador.tipo}({self.primera_expresion},{self.segunda_expresion})"
        )


class ExpresionPrefijo(Expresion):
    def __init__(self, operador: Token, expresion: Expresion):
        self.operador = operador
        self.expresion = expresion

    def __repr__(self):
        return f"{self.operador.tipo}({self.expresion})"


class ExpresionAuxiliar(Expresion):
    def __init__(self, funcion: Token, expresion: Expresion):
        self.funcion = funcion
        self.expresion = expresion

    def __repr__(self):
        return f"{self.funcion.tipo}({self.expresion})"


class Bloque(Expresion):
    def __init__(self, expresiones: list[Expresion]):
        self.expresiones = expresiones

    def __repr__(self):
        return f"BLOQUE{self.expresiones}"


class Numero(Expresion):
    def __init__(self, numero: Token):
        self.numero = numero

    def __repr__(self):
        return str(self.numero.valor)


class Cadena(Expresion):
    def __init__(self, cadena: Token):
        self.cadena = cadena

    def __repr__(self):
        return self.cadena.valor


class Booleano(Expresion):
    def __init__(self, booleano: Token):
        self.booleano = booleano

    def __repr__(self):
        return str(self.booleano.valor)


class Variable(Expresion):
    def __init__(self, variable: Token):
        self.variable = variable

    def __repr__(self):
        return str(self.variable.valor)
