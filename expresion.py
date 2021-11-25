from re import X
from token import Token
from abc import ABC, abstractmethod

class Expresion(ABC):
    pass 


class ExpresionAsignacion(Expresion):
    def __init__(self, identificador: Token, expresion: Expresion):
        self.identificador = identificador
        self.expresion = expresion

    def __repr__(self):
        return f"{self.identificador} = {self.expresion}"

class ExpresionCondicional(Expresion):
    def __init__(self, condicion: Expresion, cuerpo: Expresion, else_: Expresion):
        self.condicion = condicion
        self.cuerpo = cuerpo
        self.else_ = else_

    def __repr__(self):
        return f"{self.condicion} {self.cuerpo} {self.else_}"


class ExpresionInfijo(Expresion):
    def __init__(self, primera_expresion: Expresion, operador: Token, segunda_expresion: Expresion):
       self.primera_expresion = primera_expresion
       self.operador = operador
       self.segunda_expresion = segunda_expresion

    def __repr__(self):
        return f"{self.operador}({self.operador},{self.segunda_expresion})"
        # SUM(3, 5)
        # EXPRARITMETICA(3, SUM, 5)

class ExpresionPrefijo(Expresion):
    def __init__(self, operador: Token, expresion: Expresion):
        self.operador = operador
        self.expresion = expresion

    def __repr__(self):
        return f"{self.operador} {self.expresion}"


"""expr -> IF | WHILE | FOR | RETURN 
IF -> if expr: expr | if expr: expr else expr | if expr: expr elif expr 
WHILE -> while expr: expr
"""

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
