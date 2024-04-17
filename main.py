# -*- coding: utf-8 -*-


from bs4 import BeautifulSoup, Tag
import sys
sys.path.append('./utils')  # Adiciona o diretório 'utils' ao caminho de busca de módulos

import tools  # Importa o módulo 'tools'


pathImg = "./files/img"

# URL do site que você deseja acessar
url = "https://developer.mozilla.org/en-US/docs/Learn/HTML/Introduction_to_HTML/Document_and_website_structure"

tagsPai = tools.extrair_texto_e_imagens(url)

def processTag(tags):
    for tag in tags.descendants: 
        # Verifica se a tag é uma instância de Tag
        if isinstance(tag, Tag):
            try:
                if tag.name == 'img': 
                    # Verifica se possui o atributo href
                    if 'srcset' in tag.attrs:
                        tag = tools.imgGetUpdate(tag, 'srcset', url, pathImg)
                    elif 'data-src' in tag.attrs:
                        tag = tools.imgGetUpdate(tag, 'data-src', url, pathImg)
                    elif 'data-lazy-src' in tag.attrs:
                        tag = tools.imgGetUpdate(tag, 'data-lazy-src', url, pathImg)
                    elif 'data-original' in tag.attrs:
                        tag = tools.imgGetUpdate(tag, 'data-original', url, pathImg)
                    elif 'data-srcset' in tag.attrs:
                        tag = tools.imgGetUpdate(tag, 'data-srcset', url, pathImg)
                    elif 'src' in tag.attrs:
                        tag = tools.imgGetUpdate(tag, 'src', url, pathImg)
            except:
                pass

processTag(tagsPai)

tagsFinal = ''
for tag in tagsPai:
    try:
        tagsFinal += str(tag).replace("\n","")
    except:
        pass

# Analise a string HTML com BeautifulSoup
html = BeautifulSoup(tagsFinal, 'html.parser').prettify()

html = """<!DOCTYPE html>
<html lang="pt-br">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title></title>
</head>
<body>
"""+html+"""
</body>
</html>"""

with open("./files/index.html", "w", encoding="utf-8") as f:
    f.write(html)
f.close()