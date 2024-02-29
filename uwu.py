import ply.lex as lex
import tkinter as tk
from parser_uwu import AnalizadorSintactico

import sys
from io import StringIO


tokens = [
    'IDENTIFICADOR',
    'TIPO_DE_DATO',
    'ASIGNACION',
    'ENTERO',
    'FLOTANTE',
    'CADENA',
    'PALABRA_RESERVADA',
    'OPERADOR_ARITMETICO',
    'DOS_PUNTOS',
    'PARENTESIS_IZQ',
    'PARENTESIS_DER',
    'PUNTO_COMA',
    'SIMBOLOS',
    'CONTENIDO',
]

t_IDENTIFICADOR = r'[a-z][a-z0-9_]*'
t_TIPO_DE_DATO = r'UwU-(int|float|var)'
t_ASIGNACION = r'='
t_ENTERO = r'\d+'
t_FLOTANTE = r'\d+\.\d+'
t_CADENA = r'\".*?\"'
t_PALABRA_RESERVADA = r'UwU-(def|if|else|for|print)'
t_OPERADOR_ARITMETICO = r'\++|--'
t_DOS_PUNTOS = r':'
t_PARENTESIS_IZQ = r'\('
t_PARENTESIS_DER = r'\)'
t_PUNTO_COMA = r';'
t_SIMBOLOS = r'<|>|≤|≥|==|!='
t_CONTENIDO = r'C'

t_ignore = ' \t'

caracteres_no_validos = set()

def t_error(t):
    caracteres_no_validos.add(t.value[0])
    t.lexer.skip(1)

lexer = lex.lex()

def analizar_cadena(input_string):
    lexer.input(input_string)
    tokens_y_lexemas = []
    while True:
        token = lexer.token()
        if not token:
            break
        tokens_y_lexemas.append((token.type, token.value))
    return tokens_y_lexemas

def analizar_entrada():
    result_text.delete("1.0", tk.END)

    input_text = input_entry.get("1.0", tk.END)

    tokens_y_lexemas = analizar_cadena(input_text)
    analizador = AnalizadorSintactico(tokens_y_lexemas)
    output_message = StringIO()
    sys.stdout = output_message
    analizador.analizar()
    sys.stdout = sys.__stdout__

    result_text.insert(tk.END, output_message.getvalue() + "\n")

    result_text.insert(tk.END, "Tokens y Lexemas:\n")
    for i, (token, lexema) in enumerate(tokens_y_lexemas, start=1):
        result_text.insert(tk.END, f"{i}. Token: {token}, Lexema: {lexema}\n")



# interfaz gráfica
root = tk.Tk()
root.title("Analizador Léxico")

root.geometry("500x400")

input_label = tk.Label(root, text="Ingrese una cadena:")
input_label.pack(pady=5)

input_entry = tk.Text(root, height=2, width=40)
input_entry.pack(pady=5)

analizar_button = tk.Button(root, text="Analizar", command=analizar_entrada)
analizar_button.pack(pady=5)

result_text = tk.Text(root, height=15, width=50)
result_text.pack(pady=5)

root.mainloop()
