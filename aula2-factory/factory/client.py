from image_factory import create_image, ImageType
#acoplamento no JPG E PNG, dependencia
#from models import Image, JPG, PNG 

#python3 factory/client.py 

if __name__ == "__main__":
    ### CLASSE CLIENTE (1 of 50) ###
    # Define em tempo de execução:
    #   (a) caminho do arquivo da imagem origem
    #   (b) formato para exportação 
    image_path = "/tmp/image.jpg"
    export_type = ImageType.PNG
    # Cliente desconhece quais são as classes concretas
    # de imagens disponíveis, portanto pede ao factory
    # pela instância delegando a responsabilidade a este

    #com factory
    image = create_image(export_type)
    
    image.export(image_path, rgba=True)

    #sem factory, alto acoplamento
    #image.export(image_path)
    #image=PNG(channels=16)