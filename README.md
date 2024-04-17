# scraping-text-image-table-py #

Acesse e interaja com elementos HTML utilizando **requests** e **BeautifulSoup** com o algoritmo **scraping-text-image-table-py**, escrito em **python**.

## Biblioteca utilizadas no projeto:
**requests** é uma biblioteca para python que inclui métodos para enviar solicitações HTTP (requests).
```
python -m pip install requests
```
**BeautifulSoup** é uma biblioteca python que inclui métodos convenientes para interagir e navegar pela arvore de objetos em documentos HTML e XML.
```
python -m pip install beautifulsoup4
```

## TAGs utilizadas
A estrutura da arvore dos documentos HTML foram selecionadas a partir do documento [Document and website structure - Mozilla Developer Network](https://developer.mozilla.org/en-US/docs/Learn/HTML/Introduction_to_HTML/Document_and_website_structure) e [HTML elements reference - Mozilla Developer Network](https://developer.mozilla.org/en-US/docs/Web/HTML/Element)

# Estrutura comum de tags HTML
```
<html>: Define o elemento raiz do documento HTML.

<head>: Contém metadados sobre o documento HTML.

<title>: Define o título da página.

<meta>: Fornece metadados adicionais sobre a página.

<link>: Define a relação entre o documento atual e um recurso externo, como uma folha de estilo (CSS).

<script>: Define scripts embutidos ou links para scripts externos.

<body>: Contém o conteúdo visível da página.

<header>: Geralmente usado para o cabeçalho da página, que pode incluir logotipo, menu de navegação e outras informações importantes.

<nav>: Contém links de navegação principal.

<main>: Envolve o conteúdo principal da página.

<section>: Agrupa conteúdo relacionado semanticamente em uma página.

<article>: Representa uma peça de conteúdo independente e autônoma.

<aside>: Contém conteúdo relacionado, muitas vezes usado para barras laterais ou widgets.

<footer>: Contém informações de rodapé, como direitos autorais, links para políticas de privacidade e redes sociais
```


## img e seus atributos principais que especificam URL da imagem

```
srcset: Permite especificar várias URLs de imagem em diferentes resoluções ou tamanhos. Isso é útil para dispositivos com diferentes densidades de pixels.

data-src: Usado para adiar o carregamento da imagem até que seja necessária para economizar largura de banda ou melhorar o desempenho.

data-lazy-src: Similar ao data-src, usado para carregamento lento de imagens.

data-original: Às vezes usado para armazenar o URL da imagem original quando uma versão redimensionada é exibida.

data-srcset: Uma variação de srcset para uso com carregamento lento de imagens.
```


... 