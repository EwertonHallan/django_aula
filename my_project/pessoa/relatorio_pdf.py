from aetypes import Enum

from django.http import HttpResponse
from django.template.loader import get_template
from xhtml2pdf import pisa
import io

class Orientacao(Enum):
    Paisagem = 'landscape'
    Retrato = 'portrait'

class Page(Enum):
    # font-family: "Arial"
    Times = 'Times New Roman'
    Arial = 'Arial'
    Colibri = 'Colibri'
    Courier = 'Courier'
    Verdana = 'Verdana'
    Sans_Serif = 'sans-serif'
    Georgia = 'Georgia'

class FonteName(Enum):
    A4 = 'A4'          #/*  larg=570 alt=[40,740,15] top=[10, 55, 805] */
    Letter = 'letter'  #/*  larg=770 alt=[40,520,15] top=[10, 55, 580] */

class EstiloFonte(Enum):
    #font-style: "normal" | "italic" | "bold |
    Normal = ''
    Negrito = 'bold'
    Italico = 'italic'
    Sublinhado = 's'
    NegritoItalico = 'bold italic'
    NegritoSublinhado = 'bs'
    ItalicoSublinhado = 'is'
    NegritoItalicoSublinhado = 'bis'

class Fonte():
    def __init__(self, name, style=EstiloFonte.Normal, size=10):
        self.name = name
        self.estilo = style
        self.tamanho = size

class RelatorioPFD:
    @staticmethod
    def render(path, params, filename):
        template = get_template(path)
        html = template.render(params)
        response = io.BytesIO()
        pdf = pisa.pisaDocument(
            io.BytesIO(html.encode("UTF-8")), response
        )

        if not pdf.err:
            response = HttpResponse(
                response.getvalue(),content_type='application/pdf'
            )

            response['content-disposition'] = 'attachment; filename=%s.pdf' %filename
            return response
        else:
            return HttpResponse('Error Rendering PDF', status=400)


class Relatorio:
    def __init__(self, titulo, tamanho=Page.A4, orientacao=Orientacao.Retrato):
        self.titulo = titulo
        self.tamanho = tamanho
        self.orientacao = orientacao


class Coluna:
    def __init__(self, titulo, campo, largura=50, altura=20):
        self.titulo = titulo
        self.campo = campo
        self.largura = largura
        self.altura = altura

class Totalizador:
    pass
