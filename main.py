import requests
import functions
from bs4 import BeautifulSoup

def main():
    # Coletando o HTML da URL
    urlG1 = "http://g1.globo.com/ultimas-noticias.html"
    htmlG1 = requests.get(urlG1).text
    soupG1 = BeautifulSoup(htmlG1, "html.parser")

    # i = índice para menu / news = array com as urls das matérias
    i = 1
    news = []

    # apresenta as 10 primeiras matérias listadas no site
    print("{:=^70}".format(" G1 "))
    for new in soupG1.find_all("div", class_="feed-post-body"):
        link = (new.find("a", class_="feed-post-link").get('href'))
        print(i," - ",  new.find("a", class_="feed-post-link").text)
        print("{:-^70}".format(""))
        news.append(link)
        i = i+1

    # Entrada do usuário
    print()
    choice = int(input("Entre com o nº da matéria que deseja detalhes (ou '0' para sair): "))
    print()

    # Verifica se o usuário entrou com um valor válido
    if choice > 0 and choice < 11:
        # Chama a função que retornará os dados da notícia
        functions.openNew(news[choice - 1])
        print()
        input("Aperte Enter para retornar ao menu de notícias!")
        print()
        main(),
    elif choice == 0:
        # Encerra execução
        print("Execução encerrada!")
    else:
        # reinicia o fluxo
        print("Matéria não emcontrada")
        input("Aperte Enter para retornar ao menu de notícias!")
        print()
        main()

main()