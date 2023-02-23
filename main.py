import tkinter as tk
import csv
import random
import nltk
from nltk.tokenize import word_tokenize

# cargar respuestas del archivo csv
responses = {}
with open('responses.csv') as csvfile:
    reader = csv.reader(csvfile)
    for row in reader:
        key, val = row
        responses[key] = val

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
    chat_log.insert(tk.END, "Chatbot: " + response + "\n\n")
    chat_log.config(state=tk.DISABLED)
    chat_log.yview(tk.END)

# crear ventana de chat
root = tk.Tk()
root.title("Friendchat")
root.configure(bg='white')

# Crear cuadro de chat
chat_frame = tk.LabelFrame(root, text=" Chat ", font=("Cambria", 12))
chat_frame.grid(row=0, column=0, padx=10, pady=10, sticky="nsew")

chat_log = tk.Text(chat_frame, height=20, width=50, state=tk.DISABLED, font=("Cambria", 12))
chat_log.grid(row=0, column=0, padx=10, pady=10, sticky="nsew")

scrollbar = tk.Scrollbar(chat_frame, command=chat_log.yview)
scrollbar.grid(row=0, column=1, padx=5, pady=5, sticky="nse")

chat_log.config(yscrollcommand=scrollbar.set)

# Crear campo de entrada
input_frame = tk.LabelFrame(root, text=" Escribir mensaje ", font=("Cambria", 12))
input_frame.grid(row=1, column=0, padx=10, pady=10, sticky="nsew")

input_field = tk.Entry(input_frame, width=50, font=("Cambria", 12))
input_field.bind("<Return>", send_message)
input_field.pack(padx=10, pady=10, ipady=5, fill=tk.X, expand=True)

# Crear botón de envío
send_button = tk.Button(input_frame, text="Enviar", command=send_message, font=("Cambria", 12), bg='#4E4C67')
send_button.pack(padx=10, pady=10, ipadx=10, ipady=5)

input_field.focus()

root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)

chat_frame.columnconfigure(0, weight=1)
chat_frame.rowconfigure(0, weight=1)

input_frame.columnconfigure(0, weight=1)

# iniciar aplicación
root.mainloop()
