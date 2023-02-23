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
root.title("Chatbot")

# crear cuadro de chat
chat_log = tk.Text(root, height=20, width=50, state=tk.DISABLED)
chat_log.grid(row=0, column=0, padx=10, pady=10, sticky="w")

# crear campo de entrada
input_field = tk.Entry(root, width=50)
input_field.bind("<Return>", send_message)
input_field.grid(row=1, column=0, padx=10, pady=10, sticky="w")

# crear botón de envío
send_button = tk.Button(root, text="Enviar", command=send_message)
send_button.grid(row=1, column=1, padx=10, pady=10, sticky="e")

# iniciar aplicación
root.mainloop()
