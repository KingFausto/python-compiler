
# TIPOS DE DATOS
TOKEN_INT = "INT"
TOKEN_FLOAT = "FLOAT"
TOKEN_STRING = "STRING"
TOKEN_BOOL = "BOOL"

# OPERADORES ARITMETICOS
TOKEN_SUM = "SUM"
TOKEN_RES = "RES"
TOKEN_MULT = "MULT"
TOKEN_DIV = "DIV"

# NUMEROS
NUMS = "0123456789"

# OPERADORES DE COMPARACION
TOKEN_MENOR =  "TOKEN_MENOR"  # :V
TOKEN_MAYOR =  "TOKEN_MAYOR"  # V:
TOKEN_MENIG =  "TOKEN_MENIG"  # =V
TOKEN_MAYIG =  "TOKEN_MAYIG"  # V=
TOKEN_IGUAL =  "TOKEN_IGUAL"  # =_=
TOKEN_NIGUAL = "TOKEN_NIGUAL" # =n=

# OPERADORES LOGICOS
TOKEN_AND = "TOKEN_AND"       # &_&
TOKEN_OR  = "TOKEN_OR"        # ¬_¬
TOKEN_NOT = "TOKEN_NOT"       # T_T


class Token:
    def __init__(self, tipo, valor=None):
        self.tipo = tipo
        self.valor = valor

    def __repr__(self):
        return f"({self.tipo}, {self.valor})"


class AnalizadorLexico:
    def __init__(self, txt):
        self.txt = txt
        self.pos = -1
        self.actual = None


    def siguiente(self):
        self.pos += 1
        if self.pos < len(self.txt):
            self.actual = self.txt[self.pos]
        else:
            self.actual = None


    def crear_numero(self):
        numero = ""
        punto = False

        while self.actual is not None and self.actual in NUMS or self.actual == '.':
            if self.actual == '.':
                if punto:
                    # ERROR: invalid syntax
                    break
                else:
                    punto = True
                    numero += '.'
            else:
                numero += self.actual
            self.siguiente()

        if punto:
            return Token(TOKEN_FLOAT, float(numero))
        else:
            return Token(TOKEN_INT, int(numero))


    def crear_string(self, quotes="\""):
        string_ = ""
        self.siguiente()

        while self.actual is not None:
            if self.actual == quotes:
                break
            else:
                string_ += self.actual
            self.siguiente()
        
        return Token(TOKEN_STRING, string_)


    def crear_oplogico(self):
        operador = ""
        und = False
        
        while self.actual is not None and self.actual in "&¬T_":
            if self.actual == "_":
                if not und:
                    operador += self.actual
                    und = True
                else:
                    break
            elif self.actual in "&¬T":
                if not operador or operador[0] == self.actual:
                    operador += self.actual
                else:
                    break
            self.siguiente()
            print(operador)

        if operador == "&_&":
            return Token(TOKEN_AND, operador)
        elif operador == "¬_¬":
            return Token(TOKEN_OR, operador)
        elif operador == "T_T":
            return Token(TOKEN_NOT, operador)


    def crear_while(self):
        # while_ = ""
        pass



    def tokenizar(self):
        tokens = []

        self.siguiente()

        while self.actual != None:
            if self.actual == " " or self.actual == "\t":
                self.siguiente()
            elif self.actual == "+":
                tokens.append(Token(TOKEN_SUM, self.actual))
                self.siguiente()
            elif self.actual == "-":
                tokens.append(Token(TOKEN_RES, self.actual))
                self.siguiente()
            elif self.actual == "*":
                tokens.append(Token(TOKEN_MULT, self.actual))
                self.siguiente()
            elif self.actual == "/":
                tokens.append(Token(TOKEN_DIV, self.actual))
                self.siguiente()
            elif self.actual in NUMS:
                tokens.append(self.crear_numero())
                self.siguiente()
            elif self.actual == "\"":
                tokens.append(self.crear_string(quotes="\""))
                self.siguiente()
            elif self.actual == "\'":
                tokens.append(self.crear_string(quotes="\'"))
                self.siguiente()
            elif self.actual in "&¬T":    # and self.txt[self.pos+1] == "_"
                tokens.append(self.crear_oplogico())
                self.siguiente()
            elif self.actual == "@":
                tokens.append(self.crear_while())
                self.siguiente()

        return tokens



