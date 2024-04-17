# -*- coding: utf-8 -*-

import requests
import time
from urllib.parse import urlparse
from bs4 import BeautifulSoup


def requestUrl(url):
    # =============================================================================
    #     # 1 - Fazendo a requisição para obter o conteúdo da página   
    # =============================================================================
    # response = requests.get(url)
    
    # =============================================================================
    #    OBS: Um erro 403 geralmente indica que o servidor está recusando a 
    #    solicitação, muitas vezes porque o site pode estar protegido contra 
    #    raspagem ou pode exigir algum tipo de autenticação para acessar o conteúdo. 
    # =============================================================================
    #
    #     # 2 - Adicionar um User-Agent: Simular um cabeçalho User-Agent na 
    #    requisição (requests) para simular um navegador web "real".
    # =============================================================================
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'
        }
    response = requests.get(url, headers=headers)
    
    # =============================================================================
    #     3 - Usar uma sessão persistente
    #     Ela mantém as informações de cookies entre as solicitações
    # =============================================================================
    # session = requests.Session()
    # response = session.get(url)

    return response
 
    
def extrair_texto_e_imagens(url):
        
    response = requestUrl(url)
    
    # Verificar se a requisição foi bem-sucedida
    if response.status_code == 200:
        # Criando o objeto BeautifulSoup com o conteúdo da página
        soup = BeautifulSoup(response.content, 'html.parser')
        # Identifica a tag inicial do documento (pode ser 'content', 'section', 'article', 'main', 'section', 'div', etc.)
        tagsPai = soup.find(['content', 'section', 'article', 'main', 'section', 'body', 'div'])
        
        # Cria um novo objeto BeautifulSoup com o conteúdo da tag inicial
        tagsPai = BeautifulSoup(tagsPai.encode(), 'html.parser')
        
        # Exclui as tags a qual nao queremos (pode ser 'head','meta', 'style', 'link', 'script', 'header', 'nav', 'footer', 'aside' etc.)
        for data in tagsPai(['head','meta', 'style', 'link', 'script', 'nav', 'path', 'footer', 'aside']):
            # Remove tags
            data.decompose()

    return tagsPai


def imgGetUpdate(tagImg, atribImg, url, pathImg):
    # tagImg = tag
    # atribImg = 'src'
    # Analise a URL para extrair o domínio principal
    parsed_url = urlparse(url)
    
    if parsed_url.scheme:
        domain = parsed_url.scheme + '://' + parsed_url.netloc
    elif parsed_url.netloc[:4] =="www.": 
        domain = parsed_url.netloc
    else:
        domain = "www." + parsed_url.netloc
    
    
    imageSrc = tagImg[atribImg].replace(domain,'')
    
    # Acessa o link da imagem                            
    responseIMG = requestUrl(domain + imageSrc)
    print('')
    print('')
    print(domain + tagImg[atribImg])
    print('')
    print(tagImg)

    # Verifique se a solicitação foi bem-sucedida
    if responseIMG.status_code == 200:
        # Salva o conteúdo da resposta (imagem) em um arquivo local
        with open(pathImg + tagImg[atribImg][tagImg[atribImg].rfind('/'):], "wb") as f:
            f.write(responseIMG.content)
        f.close()
    else:
        print("Falha ao fazer a solicitação para:", domain + tagImg[atribImg])

    time.sleep(3)

    tagImg['src'] = "./img" + tagImg[atribImg][tagImg[atribImg].rfind('/'):]
    # Remover outros atributos, mantendo apenas 'style' e 'width'
    for atributo in list(tagImg.attrs.keys()):
        if atributo not in ['alt', 'src', 'style', 'width', 'height']:
            del tagImg[atributo]
            
    print('')
    print(tagImg['src'])
    print(tagImg)
    print(type)
    print('+='*25)
    return tagImg