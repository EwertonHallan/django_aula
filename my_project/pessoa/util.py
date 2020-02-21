#util:http://www.devfuria.com.br/python/strings/
def firstChar(texto):
    return str(texto)[0].upper()



#shell
#from pessoa.models from *
from sys import *
from PIL import Image

class Imagem():
    def __init__(self, name, width=300, height=400):
        self.path = name
        self.largura = width
        self.altura = height

    def __str__(self):
        return self.path + ' [' + self.largura + 'x' + self.altura

    def redefine(self, largura, altura):
        try:
            img = Image.open(self.path)
        except IOError:
            return 'arquivo nao localizado'
        else:
            larg_img = img.size[0]
            alt_img = img.size[1]
            proporcao = float(larg_img) / float(largura)

            if larg_img > largura or alt_img > altura:
                new_largura = int(larg_img / proporcao)
                new_altura = int(alt_img / proporcao)
            else:
                new_largura = larg_img
                new_altura = alt_img

            img = img.resize((new_largura, new_altura), Image.ANTIALIAS)
            img.save(self.path)

            return img

