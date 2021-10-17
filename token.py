import re

KEYWORDS = {
    "+": "SUM",
    "-": "SUB",
    "/": "DIV",
    "(": "OPENSEP1",
    ")": "CLOSESEP1",
    "[": "OPENSEP2",
    "]": "CLOSESEP2",
    "{": "OPENSEP3",
    "}": "CLOSESEP3",
    ":V": "MENOR",
    "V:": "MAYOR",
    "=V": "MENIG",
    "V=": "MAYIG",
    "=_=": "IGUAL",
    "=n=": "NIGUAL",
    "&_&": "AND",
    "¬_¬": "OR",
    "T_T": "NOT",
    "@_@": "WHILE",
    "#_#": "FOR",
    "o_O?": "IF",
    "O_O?": "ELIF",
    "$_$": "RETURN",
    ">:O": "PRINT",
    ":O": "COMMENT",
    ">.>": "IN",
    ":S": "BREAK",
    "♥_♥": "FUN",
    ";": "SEP4",
    ",": "SEP5"
}

separadores = "[](){};,"
class Token:
    def __init__(self, tipo, valor=None):
        self.tipo = tipo
        self.valor = valor

    def __repr__(self):
        return f"({self.tipo}, {self.valor})"

def putSpace(codigo):
    for i in separadores:
        codigo = re.sub(rf"\{i}", rf" {i} ", codigo)
    return codigo

def fixString(codigo):
    codigo = putSpace(codigo)
    codigo = codigo.split()
    new_code = []
    value = ""  
    isString = False
    for i in codigo:
        if i[0] == '"' and i[-1] == '"' and isString == False and len(i) > 1:
            new_code.append(i)
        elif i[0] == '"' and isString == False:
           isString = True
           value += i
        elif isString == True and i[-1] == '"':
            value += " " + i
            isString = False      
            new_code.append(value)
            value = ""
        elif isString == True:
            value += " " + i
        else:
            new_code.append(i)
    return new_code

def tokenizar(codigo):
    new_code = fixString(codigo)
    tokens = []
    for i in new_code:
        if i in KEYWORDS:
            tokens.append(Token(KEYWORDS[i], i))
        elif re.search(r'^\d+$', i):
            tokens.append(Token('INT', i))
        elif re.search(r'^\d+\.\d+$', i):
            tokens.append(Token('FLOAT', i))
        elif i[0] == '"':
            tokens.append(Token('STRING', i))
        else:
            tokens.append(Token('VAR', i))
    return tokens

with open("test-2-1.txt", "r") as f:
    for i in f.readlines():
        print(tokenizar(i))
