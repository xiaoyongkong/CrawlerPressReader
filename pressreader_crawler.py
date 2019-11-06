#https://www.pressreader.com/catalog
# 1 - Pegar o título, sub-título (se tiver), texto, imagem da noticia
# 2 - pegar foto da página toda

import scrapy


def first(sel, xpath):
    return sel.xpath(xpath).extract_first()

class Noticia(scrapy.Item):
    titulo = scrapy.Field()
    conteudo = scrapy.Field()
    link = scrapy.Field()
    data_publicacao = scrapy.Field()

#https://www.pressreader.com/catalog
class PressReaderCrawler(scrapy.Spider):
    name = 'PressReader'

    def __init__(self, tag=None):
        start_urls = 'https://www.pressreader.com/catalog'
        if tag:
            start_urls += '/%s' % tag
 
        self.start_urls = [start_urls]

    # def parse(self, response):
    # #Recebe a pagina com as noticias destaques, encontra os links das noticias e gera requisicoes para a pagina de cada uma
    #     for sel in response.css("ul#channels-browse-content-grid > li"):
    #         yield {
    #             'link': response.urljoin(first(sel, './/h3/a/@href')),
    #             'title': first(sel, './/h3/a/text()'),
    #             'views': first(sel, ".//ul/li[1]/text()"),
    #         }