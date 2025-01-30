from openai import OpenAI
from dotenv import load_dotenv
import os

class WineLabelGenerator:
    def __init__(self):
        load_dotenv()
        self.client = OpenAI(api_key=os.getenv('OPENAI_API_KEY'))
        self.descriptionprompt = """Eres un agente que se encarga de crear una descripción para una etiqueta de vino, la etiqueta tiene que ser en 2d, no estar ya impresa. Esta etiqueta se mandará a dall-e-3 para que cree una imagen a partir del prompt que vas a crear. Este prompt debe de ser corto y preciso, ademas debe tener su seccion de reglas con sangria"""

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
   
