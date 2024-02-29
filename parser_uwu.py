class AnalizadorSintactico:
    def __init__(self, tokens):
        self.tokens = tokens
        self.token_actual = None
        self.indice_token = 0

    def analizar(self):
        try:
            if not self.tokens:
                raise SyntaxError("No hay tokens para analizar")

            self.token_actual = self.tokens[self.indice_token]
            # print(self.token_actual)
            if self.token_actual[0] == 'TIPO_DE_DATO':
                self.declaracion_variable()
            elif self.token_actual[0] == 'PALABRA_RESERVADA' and self.token_actual[1] == 'UwU-if':
                self.sentencia_if()
            elif self.token_actual[0] == 'PALABRA_RESERVADA' and self.token_actual[1] == 'UwU-def':
                self.declaracion_funcion()
            elif self.token_actual[0] == 'PALABRA_RESERVADA' and self.token_actual[1] == 'UwU-for':
                self.declaracion_for()
            elif self.token_actual[0] == 'PALABRA_RESERVADA' and self.token_actual[1] == 'UwU-print':
                self.declaracion_print()
            else:
                raise SyntaxError("Token inesperado")

            if self.indice_token < len(self.tokens):
                raise SyntaxError("Tokens inesperados después de la declaración")
            print("La cadena de entrada es válida.")
        except SyntaxError as e:
            print("Error de sintaxis:", e)

    def coincidir(self, tipo_token):
        if self.token_actual and self.token_actual[0] == tipo_token:
            self.consumir_token()
        else:
            raise SyntaxError(f"Token inesperado: {self.token_actual}")

    def consumir_token(self):
        self.indice_token += 1
        if self.indice_token < len(self.tokens):
            self.token_actual = self.tokens[self.indice_token]
        else:
            self.token_actual = None

    def declaracion_variable(self):
        tipo_dato = self.token_actual[1]
        self.coincidir('TIPO_DE_DATO')
        self.coincidir('IDENTIFICADOR')
        self.coincidir('ASIGNACION')

        if tipo_dato == 'UwU-int':
            self.coincidir('ENTERO')
        elif tipo_dato == 'UwU-float':
            self.coincidir('FLOTANTE')
        elif tipo_dato == 'UwU-var':
            self.coincidir('CADENA')
        else:
            raise SyntaxError("Tipo de dato no válido")
        
    def declaracion_funcion(self):
        self.coincidir('PALABRA_RESERVADA')
        self.coincidir('IDENTIFICADOR')
        self.coincidir('PARENTESIS_IZQ')
        self.coincidir('PARENTESIS_DER')
    
    def declaracion_print(self):
        self.coincidir('PALABRA_RESERVADA')
        self.coincidir('ASIGNACION')
        self.coincidir('CADENA')

    def sentencia_if(self):
        self.coincidir('PALABRA_RESERVADA')
        self.expresion()
        self.coincidir('DOS_PUNTOS')
        self.coincidir('CONTENIDO')
        if self.token_actual and self.token_actual[0] == 'PALABRA_RESERVADA' and self.token_actual[1] == 'UwU-else':
            self.consumir_token()
            self.coincidir('DOS_PUNTOS')
            self.coincidir('CONTENIDO')

    def declaracion_for(self):
        self.coincidir('PALABRA_RESERVADA')
        self.coincidir('IDENTIFICADOR')
        self.coincidir('ASIGNACION')
        self.coincidir('ENTERO')
        self.coincidir('PUNTO_COMA')
        self.coincidir('IDENTIFICADOR')
        self.coincidir('SIMBOLOS')
        if self.token_actual[0] == 'IDENTIFICADOR' or self.token_actual[0] == 'ENTERO':
            self.consumir_token()
        else:
            raise SyntaxError("Se esperaba un identificador o un entero en la expresión")
        self.coincidir('PUNTO_COMA')
        self.coincidir('IDENTIFICADOR')
        self.coincidir('OPERADOR_ARITMETICO')
        self.coincidir('DOS_PUNTOS')
        self.coincidir('CONTENIDO')

    def expresion(self):
        self.coincidir('IDENTIFICADOR')
        self.coincidir('SIMBOLOS')
        if self.token_actual[0] == 'IDENTIFICADOR' or self.token_actual[0] == 'CADENA' or self.token_actual[0] == 'ENTERO':
            self.consumir_token()
        else:
            raise SyntaxError("Se esperaba un identificador o una cadena en la expresión")
