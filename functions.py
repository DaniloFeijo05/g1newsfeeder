import requests
from bs4 import BeautifulSoup
from datetime import datetime

def openNew(urlNew):
    try:
        # Apresenta URL
        print("{:=^70}".format(""))
        print(urlNew)
        print("{:=^70}".format(""))

        # Coletando o HTML da URL da notícia escolhida
        htmlNew = requests.get(urlNew).text
        soupNew = BeautifulSoup(htmlNew, "html.parser")
        # Coleta e formata a data
        dateTime = soupNew.find("time").text.strip()
        date = datetime.strptime(dateTime, "%d/%m/%Y %Hh%M")
        #Coleta o texto da notícia
        article = soupNew.find("article")
        text = article.find_all("p")

        # Imprime título, subtítulo e data
        print(soupNew.find("h1", class_="content-head__title").text)
        print(soupNew.find("h2", class_="content-head__subtitle").text)
        print(date.strftime("%Y-%m-%d %H:%M"))
        print("{:=^70}".format(""))

        # Imprime o tecxto da matéria
        for p in text:
            print(p.text)
        print("{:=^70}".format(""))

    # Tratando possível excessão de algumas páginas que são apenas vídeos sem nenhum conteúdo textual.
    except AttributeError:
        print("Algo deu errado! Talvez a matéria escolhida não possua conteúdo textual!")
    # Tratando outras possíveis exceções.
    except:
        print("Algo deu errado! Tente outra matéria!")