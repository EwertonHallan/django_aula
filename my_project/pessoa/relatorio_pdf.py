import math
from aetypes import Enum
from django.db import connection

from django.http import HttpResponse
from django.template.loader import get_template
from xhtml2pdf import pisa
import io

class FonteName(Enum):
    # font-family: "Arial"
    Times = 'Times New Roman'
    Arial = 'Arial'
    Colibri = 'Colibri'
    Courier = 'Courier'
    Verdana = 'Verdana'
    Sans_Serif = 'sans-serif'
    Georgia = 'Georgia'

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

class Orientacao(Enum):
    Paisagem = 'landscape'
    Retrato = 'portrait'

class Page(Enum):
    A4 = 'A4'          #/*  larg=570 alt=[40,740,15] top=[10, 55, 805] */
    Letter = 'letter'  #/*  larg=770 alt=[40,520,15] top=[10, 55, 580] */

class Coluna():
    def __init__(self, titulo, valor, largura=50, altura=20):
        self.titulo = titulo
        self.valor = valor
        self.largura = largura
        self.altura = altura
    def getTitulo(self):
        return self.titulo
    def getValor(self):
        return self.valor
    def __str__(self):
        return self.titulo + ' = ' + str(self.valor)


class Relatorio:
    def __init__(self, titulo, tamanho=Page.A4, orientacao=Orientacao.Retrato):
        self.titulo = titulo
        self.tamanho = tamanho
        self.orientacao = orientacao
        self.pages = []
        self.paginas = 0
        self.reg_pagina = 0
        self.registros = []
        self.lin = 0
        self.col = 0
    def queryDados(self, tituloColuna, comandoSQL):
        sql = connection.cursor()
        sql.execute(comandoSQL)
        result = sql.fetchall()
        if len(tituloColuna) == len(result[0]):
            self.lin = len(result)
            self.col = len(result[0])
            for i in range(self.lin):
                coluna = []
                for j in range(self.col):
                    coluna.append(Coluna(tituloColuna[j], result[i][j]))
                self.registros.append(coluna)
    def paginador(self, num_reg=33):
        self.reg_pagina = num_reg
        self.paginas = math.trunc(self.lin/self.reg_pagina)
        if (self.lin%self.reg_pagina) > 1:
            self.paginas = self.paginas + 1
    def mostraDados(self, index=0):
        txt = ''
        for j in range(self.col):
            objColuna = self.registros[index][j]
            txt = txt + objColuna.__str__() + ' | '
        return (txt)
    def montaPages(self):
        pass


r = Relatorio('Rel de Usuarios')
titulo = ['id','nome']
comando = 'SELECT id, nome FROM pessoa_pessoa WHERE id < 20'
r.queryDados(titulo, comando)
r.mostraDados(1)
r.paginador(9)

class Totalizador:
    pass
