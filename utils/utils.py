from openai import OpenAI
from dotenv import load_dotenv
import os

class WineLabelGenerator:
    def __init__(self):
        load_dotenv()
        self.client = OpenAI(api_key=os.getenv('OPENAI_API_KEY'))
        self.descriptionprompt = """

        #1 Actúa como un ingeniero de Prompts dedicado a hacer prompts para el modelo de generacion de imagen DALL E 3
        #2 Revisa el siguiente Prompt para mi
        #3 Optimizar para mejorarlo, y no confundir al generador de imagenes
        #4 Asegurarse de que esto genere una etiqueta para vino.
        #5 Captar bien lo que quiere el usuario
        
        """

    def generate_label_and_images(self, user_input):
        # Generar el prompt de la etiqueta de vino
        completion = self.client.chat.completions.create(
            model="gpt-4o",
            messages=[
                {"role": "developer", "content": self.descriptionprompt},
                {"role": "user", "content": user_input}
            ]
        )
        
        prompt_etiqueta = completion.choices[0].message.content
        print(prompt_etiqueta)
        prompt = prompt_etiqueta.replace('"', "'")

        # Retornar las URLs de las 3 imágenes generadas
        image_urls = []
        for _ in range(3):
            response = self.client.images.generate(
                model="dall-e-3",
                prompt=prompt,
                quality='hd',
                size="1024x1024",
                n=1,
            )
            image_urls.append(response.data[0].url)
        
        # Retornar las URLs de las 3 imágenes generadas
        return image_urls
    
    # Instrucciones de diseño para etiquetas de vino

