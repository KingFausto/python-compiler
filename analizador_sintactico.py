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
        self.pos += 1
        return self._token_actual()

    def crear_arbol(self, tokens: list[Token]):
        root: Node = None
        nodes: list[Node] = []
        for token in tokens:
            if not root:
                root = Node(token.valor)
                continue
            # nodes.append(Node(i.valor, parent=root))
            if token.tipo == "IF":
                self.analizar_if()
        #@TODO: export to image
        # DotExporter(root).to_picture("arbol.png")

        #@TODO: print tree
        # for pre, fill, node in RenderTree(root):
        #     print(f"{pre}{node.name}")

    def analizar_if(self):
        argumento = self.analizar_argumento_condicional()
        cuerpo = self.analizar_cuerpo()
        else_ = self.analizar_else()  # mismo que el cuerpo

    # def analizar_infijo(self) -> ExpresionInfijo:
    #    pass

    def analizar_argumento_condicional(self) -> ExpresionInfijo:
        if self._token_actual().tipo not in ["INT", "FLOAT", "STRING", "VAR"]:
            return None

        if self._token_siguiente().tipo not in ["MENOR", "MAYOR", "MENIG", "MAYIG", "IGUAL", "NIGUAL"]:
            return None

        if self._token_siguiente().tipo not in ["INT", "FLOAT", "STRING", "VAR"]:
            return None


"""num operador Num
bool operador bool
variable operador 
string operador string 

if statement = if <exeprsion> then <expresion> else <expresion> |
               if <expresion> then <expresion>

            if x < 5:
                x = 0
            else:
                x = 1
            
            if
    x < 5       x = 0 .    x = 1

            if
        >
    +      10
 x    5

"""
