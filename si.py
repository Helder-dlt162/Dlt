import re
import requests
import pandas as pd
from bs4 import BeautifulSoup as bs

def anatel_noticias():
    url = "https://www.gov.br/anatel/pt-br/assuntos/noticias"
    dominio = requests.get(url)
    titulos_list = []
    subtitulos_list = []
    links_list = []
    data_list = []
    descricao_list = []

    if dominio.status_code == 200:
        sopa = bs(dominio.text, "html.parser")
        noticias = sopa.select('ul.noticias li')
            
        for noticia in noticias:                
            titulos_list.append(noticia.find('h2').text.strip())
            links_list.append(noticia.find('a').get('href'))
            subtitulo_element = noticia.select('div.subtitulo-noticia')
            subtitulos_list.append(subtitulo_element[0].text.strip() if subtitulo_element else "")
            data_match = re.search(r"\d{2}/\d{2}/\d{4}", noticia.select('span.data')[0].text)
            data_list.append(data_match.group() if data_match else '')
            descricao_element = noticia.select('span.descricao')
            if descricao_element:
                for span in descricao_element[0].find_all('span'):
                    span.decompose()
                descricao = descricao_element[0].text.strip()
            else:
                descricao = ''
            descricao_list.append(descricao)
            noticias_anatel = pd.DataFrame({ "Orgao": "ANATEL", "Titulo": titulos_list, "Data": data_list, "Link": links_list, "Descricao": descricao_list})
        return noticias_anatel
    else:
        print("Erro ao acessar a página (ANATEL):", dominio.status_code)

def anp_noticias():
    url = "https://www.gov.br/anp/pt-br/canais_atendimento/imprensa/noticias-comunicados"
    dominio = requests.get(url)
    titulos_list = []
    subtitulos_list = []
    links_list = []
    data_list = []
    descricao_list = []

    if dominio.status_code == 200:
        sopa = bs(dominio.text, "html.parser")
        noticias = sopa.select('ul.noticias li')
            
        for noticia in noticias:                
            titulos_list.append(noticia.find('h2').text.strip())
            links_list.append(noticia.find('a').get('href'))
            subtitulo_element = noticia.select('div.subtitulo-noticia')
            subtitulos_list.append(subtitulo_element[0].text.strip() if subtitulo_element else "")
            data_match = re.search(r"\d{2}/\d{2}/\d{4}", noticia.select('span.data')[0].text)
            data_list.append(data_match.group() if data_match else '')
            descricao_element = noticia.select('span.descricao')
            if descricao_element:
                for span in descricao_element[0].find_all('span'):
                    span.decompose()
                descricao = descricao_element[0].text.strip()
            else:
                descricao = ''
            descricao_list.append(descricao)
            noticias_anp = pd.DataFrame({'Orgao': 'ANP', "Titulo": titulos_list, "Data": data_list, "Link": links_list, "Descricao": descricao_list})
        return noticias_anp
    else:
        print("Erro ao acessar a página (ANP):", dominio.status_code)

def antt_noticias():
    url = "https://www.gov.br/antt/pt-br/assuntos/ultimas-noticias"
    dominio = requests.get(url)
    titulos_list = []
    subtitulos_list = []
    links_list = []
    data_list = []
    descricao_list = []

    if dominio.status_code == 200:
        sopa = bs(dominio.text, "html.parser")
        noticias = sopa.select('ul.noticias li')
            
        for noticia in noticias:                
            titulos_list.append(noticia.find('h2').text.strip())
            links_list.append(noticia.find('a').get('href'))
            subtitulo_element = noticia.select('div.subtitulo-noticia')
            subtitulos_list.append(subtitulo_element[0].text.strip() if subtitulo_element else "")
            data_match = re.search(r"\d{2}/\d{2}/\d{4}", noticia.select('span.data')[0].text)
            data_list.append(data_match.group() if data_match else '')
            descricao_element = noticia.select('span.descricao')
            if descricao_element:
                for span in descricao_element[0].find_all('span'):
                    span.decompose()
                descricao = descricao_element[0].text.strip()
            else:
                descricao = ''
            descricao_list.append(descricao)
            noticias_antt = pd.DataFrame({ "Orgao": "ANTT", "Titulo": titulos_list, "Data": data_list, "Link": links_list, "Descricao": descricao_list})
        return noticias_antt
    else:
        print("Erro ao acessar a página (ANTT):", dominio.status_code)

def anvisa_noticias():
    url = "https://www.gov.br/anvisa/pt-br/assuntos/noticias-anvisa"
    dominio = requests.get(url)
    titulos_list = []
    subtitulos_list = []
    links_list = []
    data_list = []
    descricao_list = []

    if dominio.status_code == 200:
        sopa = bs(dominio.text, "html.parser")
        noticias = sopa.select('ul.noticias li')
            
        for noticia in noticias:                
            titulos_list.append(noticia.find('h2').text.strip())
            links_list.append(noticia.find('a').get('href'))
            subtitulo_element = noticia.select('div.subtitulo-noticia')
            subtitulos_list.append(subtitulo_element[0].text.strip() if subtitulo_element else "")
            data_match = re.search(r"\d{2}/\d{2}/\d{4}", noticia.select('span.data')[0].text)
            data_list.append(data_match.group() if data_match else '')
            descricao_element = noticia.select('span.descricao')
            if descricao_element:
                for span in descricao_element[0].find_all('span'):
                    span.decompose()
                descricao = descricao_element[0].text.strip()
            else:
                descricao = ''
            descricao_list.append(descricao)
            noticias_anvisa = pd.DataFrame({"Orgao": "ANVISA", "Titulo": titulos_list, "Data": data_list, "Link": links_list, "Descricao": descricao_list})
        return noticias_anvisa
    else:
        print("Erro ao acessar a página (ANVISA):", dominio.status_code)

df1 = anatel_noticias()
df2 = anp_noticias()
df3 = antt_noticias()
df4 = anvisa_noticias()

df_list = [df1, df2, df3, df4]
df_geral = pd.concat(df_list, ignore_index=True)
df_geral.to_excel('noticias.xlsx', index=False)