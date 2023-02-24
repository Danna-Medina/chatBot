import tkinter as tk
import csv
import random
import nltk
import time
from nltk.tokenize import word_tokenize

# cargar respuestas del archivo csv
responses = {}
def get_response(user_input):
    with open('responses.csv', 'r', encoding='utf-8') as file:
        reader = csv.reader(file)
        responses = [row for row in reader]

    for row in responses:
        if row[0].lower() in user_input.lower():
            if '{hora}' in row[1]:
                hora_actual = time.strftime('%H')
                minutos_actuales = time.strftime('%M')
                row[1] = row[1].replace('{hora}', hora_actual).replace('{minutos}', minutos_actuales)
            return row[1]

    return "Lo siento, no te entendí. ¿Podrías repetirlo de otra manera?"

# funciones auxiliares
def respond(input_text):
    """Función que devuelve una respuesta a partir del texto de entrada."""
    input_text = input_text.lower()
    tokens = word_tokenize(input_text)
    for token in tokens:
        if token in responses:
            return responses[token]
    return "Lo siento, no entiendo lo que estás diciendo."

def send_message(event=None):
    """Función que maneja el envío de mensajes."""
    # obtener texto de entrada
    input_text = input_field.get()
    input_field.delete(0, tk.END)

    # mostrar mensaje de entrada en la ventana de chat
    chat_log.config(state=tk.NORMAL)
    chat_log.insert(tk.END, "Tú: " + input_text + "\n\n")

    # obtener respuesta y mostrarla en la ventana de chat
    response = respond(input_text)
    if '{clima}' in response:
        clima_actual = random.choice(['soleado', 'lluvioso', 'nublado', 'nevado'])
        response = response.replace('{clima}', clima_actual)
    chat_log.insert(tk.END, "Chatbot: " + response + "\n\n")
    chat_log.config(state=tk.DISABLED)
    chat_log.yview(tk.END)

# Crear ventana de chat
root = tk.Tk()
root.title("Mi chat")
root.configure(bg="#E6E6E6")

# Crear marco para el chat
chat_frame = tk.LabelFrame(root, text=" Chat ", font=("Cambria", 14), bg='#FFFFFF', bd=2, relief=tk.SOLID)
chat_frame.grid(row=0, column=0, padx=10, pady=10, sticky="nsew")

# Crear ventana de chat
chat_log = tk.Text(chat_frame, height=10, width=50, state=tk.DISABLED, font=("Cambria", 12), bg='#F6F6F6', padx=10, pady=10)
chat_log.grid(row=0, column=0, padx=10, pady=10, sticky="nsew")

# Crear scrollbar para el chat
scrollbar = tk.Scrollbar(chat_frame, command=chat_log.yview, bg='#FFFFFF', troughcolor='#CCCCCC')
scrollbar.grid(row=0, column=1, padx=5, pady=5, sticky="nse")

chat_log.config(yscrollcommand=scrollbar.set)

# Crear campo de entrada de mensajes
input_frame = tk.LabelFrame(root, text=" Escribir mensaje ", font=("Cambria", 14), bg='#FFFFFF', bd=2, relief=tk.SOLID)
input_frame.grid(row=1, column=0, padx=10, pady=10, sticky="nsew")

input_field = tk.Entry(input_frame, width=50, font=("Cambria", 12), bg='#F6F6F6')
input_field.bind("<Return>", send_message)
input_field.pack(padx=10, pady=10, ipady=5, fill=tk.X, expand=True)

# Crear botón de envío
send_button = tk.Button(input_frame, text="Enviar", command=send_message, font=("Cambria", 12), bg='#4E4C67', fg='#FFFFFF', activebackground='#5C5A7E', activeforeground='#FFFFFF')
send_button.pack(padx=10, pady=10, ipadx=10, ipady=5)

# Establecer foco en el campo de entrada de mensajes
input_field.focus()

# Establecer configuración de pesos de columnas y filas
root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)
root.rowconfigure(1, weight=0)  # Evita que el cuadro de entrada se estire demasiado

chat_frame.columnconfigure(0, weight=1)
chat_frame.rowconfigure(0, weight=1)

input_frame.columnconfigure(0, weight=1)

# Hacer que la ventana sea responsive
root.update()
min_width, min_height = root.minsize()
root.geometry(f"{min_width}x{min_height}")

# Hacer que la ventana se ajuste automáticamente al contenido
def resize_window(event):
    root.geometry("")
    root.update()
    new_width = max(min_width, root.winfo_width())
    new_height = max(min_height, root.winfo_height())
    root.geometry(f"{new_width}x{new_height}")
root.bind("<Configure>", resize_window)

root.mainloop()
