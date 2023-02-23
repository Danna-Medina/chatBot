import nltk
import numpy as np
import pandas as pd
from nltk.stem import WordNetLemmatizer
from nltk import word_tokenize, pos_tag

nltk.download('punkt')
nltk.download('wordnet')
nltk.download('averaged_perceptron_tagger')

class ChatBot:
    def __init__(self):
        self.responses_df = pd.read_csv('responses.csv')
        self.responses_dict = self.responses_df.set_index('Input')['Response'].to_dict()

    def generate_response(self, input_text):
        # Procesar la entrada del usuario
        processed_input = self.process_input(input_text)

        # Buscar una respuesta en el diccionario de respuestas
        response = self.responses_dict.get(processed_input)

        # Si no hay una respuesta, devolver una respuesta predeterminada
        if not response:
            response = "Lo siento, no entendí lo que dijiste. ¿Podrías ser más específico?"

        return response

    def add_response(self, input_text, response):
        # Agregar una respuesta a la base de datos de respuestas
        self.responses_df = self.responses_df.append({'Input': input_text, 'Response': response}, ignore_index=True)
        self.responses_dict = self.responses_df.set_index('Input')['Response'].to_dict()
        self.responses_df.to_csv('responses.csv', index=False)

    def process_input(self, input_text):
        lemmatizer = WordNetLemmatizer()

        # Tokenize la entrada del usuario
        tokens = word_tokenize(input_text.lower())

        # Lemmatize los tokens
        lemmatized_tokens = [lemmatizer.lemmatize(token) for token in tokens]

        # Etiqueta de las partes del discurso de los tokens
        pos_tokens = pos_tag(lemmatized_tokens)

        # Cree una lista de tuplas (palabra, POS) para cada palabra en la entrada del usuario
        processed_input = [(word, pos) for word, pos in pos_tokens]

        return processed_input


def run_chatbot():
    chatbot = ChatBot()

    print('Hola, soy un chatbot. ¿En qué puedo ayudarte?')

    while True:
        user_input = input('Tú: ')
        
        if user_input.lower() == 'salir':
            print('Chatbot: ¡Hasta luego!')
            break
        
        response = chatbot.generate_response(user_input)
        print('Chatbot:', response)


if __name__ == '__main__':
    run_chatbot()
