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
        self.tokens = tokens
        expresion = self.definir_if()
        return expresion
        # root: Node = None
        # nodes: list[Node] = []
        # for token in tokens:
        #     if not root:
        #         root = Node(token.valor)
        #         continue
        #     # nodes.append(Node(i.valor, parent=root))
        #     if token.tipo == "IF":
        #         self.analizar_if()

    def crear_factor(self) -> Numero:
        token_actual = self._token_actual()
        if token_actual.tipo in ["SUM", "SUB", "NOT"]:
            self._token_siguiente()
            factor = self.crear_factor()
            return ExpresionPrefijo(token_actual, factor)

        elif token_actual.tipo in ["INT", "FLOAT", "VAR"]:
            self._token_siguiente()
            return Numero(token_actual)

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

    def definir_if(self):
        if_ = ExpresionIF(None, None, None)
        self._token_siguiente()
        if_.condicion = self.crear_comparacion_booleana()
        if_.cuerpo = None
        if_.else_ = None
        return if_

    # def analizar_expresion(self) -> Expresion:
    #     left: Numero = self.crear_factor()

    # def analizar_argumento_condicional(self) -> ExpresionInfijo:
    #     if self._token_actual().tipo not in ["INT", "FLOAT", "STRING", "VAR"]:
    #         return None

    #     if self._token_siguiente().tipo not in ["MENOR", "MAYOR", "MENIG", "MAYIG", "IGUAL", "NIGUAL"]:
    #         return None

    #     if self._token_siguiente().tipo not in ["INT", "FLOAT", "STRING", "VAR"]:
    #         return None
