from models import (
    Image, PNG, JPG
)
from enum import Enum

class ImageType(Enum):
    PNG = "png"
    JPG = "jpg"

def create_image(image_type: ImageType) -> Image:
    """ Factory method """
    if image_type.PNG.value == image_type.value: 
        return PNG() #retorna um instanciamento do tipo png
    elif image_type.JPG.value == image_type.value: 
        return JPG(0.9) #valor padrao(default) pra qualidade
    else:
        #caso o cliente passar um tipo desconhecido ao factory
        raise ValueError("Unknown image type: {image_type}")
