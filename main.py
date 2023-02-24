import tkinter as tk
import csv
import random
import nltk
import time
from nltk.tokenize import word_tokenize

# cargar respuestas del archivo csv
responses = {}

def get_response(user_input):
    # Obtener la hora actual
    hora_actual = time.strftime('%H')
    minutos_actuales = time.strftime('%M')

    # Obtener información del clima
    # Aquí se debería usar una API real para obtener la información del clima
    clima = "soleado"

    with open('responses.csv', 'r', encoding='utf-8') as file:
        reader = csv.reader(file)
        next(reader) # Se salta la primera fila que contiene los encabezados
        responses = {rows[0]: rows[1] for rows in reader}

    for question, answer in responses.items():
        if question.lower() in user_input.lower():
            if '{hora}' in answer:
                answer = answer.replace('{hora}', hora_actual).replace('{minutos}', minutos_actuales)
            if '{clima}' in answer:
                answer = answer.replace('{clima}', clima)
            return answer

    return "Lo siento, no te entendí. ¿Podrías repetirlo de otra manera?"

# funciones auxiliares
def respond(input_text):
    """Función que devuelve una respuesta a partir del texto de entrada."""
    response = get_response(input_text)
    if '{clima}' in response:
        clima_actual = random.choice(['soleado', 'lluvioso', 'nublado', 'nevado'])
        response = response.replace('{clima}', clima_actual)
    return response

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
root.configure(bg="#E6E6E6")
root.title("Friendchat")

# Crear cuadro de chat
chat_frame = tk.LabelFrame(root, text=" Chat ", font=("Arial", 12))
chat_frame.grid(row=0, column=0, padx=10, pady=10, sticky="nsew")

chat_log = tk.Text(chat_frame, height=20, width=50, state=tk.DISABLED, font=("Arial", 12))
chat_log.grid(row=0, column=0, padx=10, pady=10, sticky="nsew")

scrollbar = tk.Scrollbar(chat_frame, command=chat_log.yview)
scrollbar.grid(row=0, column=1, padx=5, pady=5, sticky="nse")

chat_log.config(yscrollcommand=scrollbar.set)

# Crear campo de entrada
input_frame = tk.LabelFrame(root, text=" Escribir mensaje ", font=("Arial", 12))
input_frame.grid(row=1, column=0, padx=10, pady=10, sticky="nsew")

input_field = tk.Entry(input_frame, width=50, font=("Arial", 12))
input_field.bind("<Return>", send_message)
input_field.pack(padx=10, pady=10, ipady=5, fill=tk.X, expand=True)

# Crear botón de envío
send_button = tk.Button(input_frame, text="Enviar", command=send_message, font=("Arial", 12))
send_button.pack(padx=10, pady=10, ipadx=10, ipady=5)

input_field.focus()

root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)

chat_frame.columnconfigure(0, weight=1)
chat_frame.rowconfigure(0, weight=1)

input_frame.columnconfigure(0, weight=1)

root.mainloop()
