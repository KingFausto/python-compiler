from __future__ import annotations
from ast import Num
from expresion import *
from token_ import Token
from anytree import Node, RenderTree
from anytree.exporter import DotExporter


class AnalizadorSintactico:
    def __init__(self):
        self.tokens: list[Token] = []
        self.pos: int = 0

    def _token_actual(self):
        return self.tokens[self.pos]

    def _token_siguiente(self):
        if self.pos < len(self.tokens) - 1:
            self.pos += 1
        return self._token_actual()

    def crear_arbol(self, tokens: list[Token]):
        arbol = []
        self.tokens = tokens
        while self._token_actual().tipo != "EOF":
            declaracion = self.definir_declaracion()
            if declaracion is None:
                return None
            arbol.append(declaracion)
            if self._token_actual().tipo == "SEP4":
                self._token_siguiente()
        return arbol

    def crear_factor(self) -> Numero:
        token_actual = self._token_actual()
        if token_actual.tipo in ["SUM", "SUB", "NOT"]:
            self._token_siguiente()
            factor = self.crear_factor()
            return ExpresionPrefijo(token_actual, factor)

        elif token_actual.tipo in ["INT", "FLOAT"]:
            self._token_siguiente()
            return Numero(token_actual)

        elif token_actual.tipo == "STRING":
            self._token_siguiente()
            return Cadena(token_actual)

        elif token_actual.tipo == "BOOL":
            self._token_siguiente()
            return Booleano(token_actual)

        elif token_actual.tipo == "VAR":
            self._token_siguiente()
            return Variable(token_actual)

        elif token_actual.tipo == "OPENSEP1":
            self._token_siguiente()
            expresion = self.crear_comparacion_booleana()
            if self._token_actual().tipo == "CLOSESEP1":
                self._token_siguiente()
                return expresion
        return None

    def crear_termino(self):
        return self.definir_infijo(self.crear_factor, ["MULT", "DIV"])

    def crear_expresion(self):
        return self.definir_infijo(self.crear_termino, ["SUM", "SUB"])

    def crear_comparacion(self):
        return self.definir_infijo(
            self.crear_expresion, ["MENOR", "MAYOR", "MENIG", "MAYIG"]
        )

    def crear_comparacion_igualdad(self):
        return self.definir_infijo(self.crear_comparacion, ["IGUAL", "NIGUAL"])

    def crear_comparacion_booleana(self):
        return self.definir_infijo(
            self.crear_comparacion_igualdad, ["AND", "OR", "NOT"]
        )

    def definir_infijo(self, expresion: function, tipos: list[str]):
        left = expresion()

        while self._token_actual().tipo in tipos:
            operador = self._token_actual()
            self._token_siguiente()
            right = expresion()
            left = ExpresionInfijo(left, operador, right)

        return left

    def definir_condicion(self) -> ExpresionCondicion:
        if_ = ExpresionCondicion(self._token_actual(), None, None, None)
        self._token_siguiente()
        if_.condicion = self.crear_comparacion_booleana()
        if self._token_actual().tipo != "OPENSEP3":
            return None
        self._token_siguiente()
        if_.cuerpo = self.definir_bloque()
        if if_.cuerpo is None:
            return None
        self._token_siguiente()
        if self._token_actual().tipo == "ELSE":
            self._token_siguiente()
            if self._token_actual().tipo != "OPENSEP3":
                return None
            self._token_siguiente()
            if_.else_ = self.definir_bloque()
            self._token_siguiente()
        return if_

    def definir_asignacion(self) -> ExpresionAsignacion:
        asignacion = ExpresionAsignacion(None, None)
        if self._token_actual().tipo != "VAR":
            return None
        asignacion.identificador = self._token_actual()
        self._token_siguiente()
        if self._token_actual().tipo != "ASIGN":
            return None
        self._token_siguiente() 
        asignacion.expresion = self.crear_comparacion_booleana()
        if asignacion.expresion is None:
            return None
        return asignacion

    def definir_auxiliares(self) -> ExpresionAuxiliar:
        declaracion = ExpresionAuxiliar(None, None)
        if self._token_actual().tipo not in ["PRINT", "RETURN", "BREAK"]:
            return None
        declaracion.funcion = self._token_actual()
        self._token_siguiente()
        declaracion.expresion = self.crear_comparacion_booleana()
        return declaracion

    def definir_declaracion(self) -> Expresion:
        if self._token_actual().tipo == "VAR":
            return self.definir_asignacion()
        elif self._token_actual().tipo in ["IF", "WHILE"]:
            return self.definir_condicion()
        elif self._token_actual().tipo == "SWITCH":
            return self.definir_switch()
        else:
            return self.definir_auxiliares()

    def definir_switch(self) -> ExpresionSwitch:
        switch = ExpresionSwitch(None, None)
        self._token_siguiente()
        condiciones = []
        declaracion = self.crear_comparacion_booleana()
        if declaracion is None:
            return None
        if self._token_actual().tipo != "OPENSEP3":
            return None
        self._token_siguiente()
        switch.match = declaracion
        while self._token_actual().tipo != "CLOSESEP3":
            print(self._token_actual())
            case = self.definir_condicion()
            if case is None:
                return None
            condiciones.append(case)
        self._token_siguiente()
        switch.cases = condiciones
        return switch

    def definir_bloque(self) -> list[Expresion]:
        bloque = Bloque(None)
        expresiones = []
        while self._token_actual().tipo not in ["EOF", "CLOSESEP3"]:
            expresiones.append(self.definir_declaracion())
            if self._token_actual().tipo == "SEP4":
                self._token_siguiente()
        bloque.expresiones = expresiones
        return bloque
