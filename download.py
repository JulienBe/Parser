from bs4 import BeautifulSoup

import requests


def tag_to_str(tag):
    return tag.get_text()


def get_page(id):
    url = "https://www.proprietes-equestres.com/propriete-equestre-" + str(id) + ".html"
    r = requests.get(url)
    print("\t" + str(id) + ": " + str(r.status_code))
    if r.status_code == 500:
        return
    data = r.text
    soup = BeautifulSoup(data, 'html.parser')

    title = soup.select("div#gauche table tr td h2")[0].get_text()

    superficie_terrain = soup.select("div#gauche div#option1")[0].get_text()
    superficie_habitation = soup.select("div#gauche div#option1")[1].get_text()

    options = '\n'.join(tag_to_str(e) for e in soup.select("div#gauche div#option1")[2:])
    # sellerie = soup.select("div#gauche div#option1")[2]
    # local_douche = soup.select("div#gauche div#option1")[3]
    # nb_boxes = soup.select("div#gauche div#option1")[4]
    # stabulation = soup.select("div#gauche div#option1")[5]
    # hangar = soup.select("div#gauche div#option1")[6]
    # abris = soup.select("div#gauche div#option1")[7]

    description = soup.select("div#gauche div#description")[0].get_text()
    photos = '\n'.join(str(e['src']) for e in soup.select("div#gauche div#photo img")[:-1])
    prix = soup.select("div#gauche span.prix")[0].get_text()
    peb = soup.select("div#gauche div#description img")[0].get_text()
    tel_mobile = soup.select("div#gauche div#description tr td")[-2].get_text()
    tel_fixe = soup.select("div#gauche div#description tr td").pop().get_text()

    print("= = = = = = = = = = = = = = = = = = = = = = = = = = = = = =")
    print("\n" + str(url) + "title: " + title)
    print("===========")
    print(str(url) + "superficie_terrain: " + superficie_terrain)
    print("===========")
    print(str(url) + "superficie_habitation: " + superficie_habitation)
    print("===========")
    print(str(url) + "options: " + options)
    print("===========")
    print(str(url) + "description: " + description)
    print("===========")
    print(str(url) + "photos: " + photos)
    print("===========")
    print(str(url) + "prix: " + prix)
    print("===========")
    print(str(url) + "peb: " + peb)
    print("===========")
    print(str(url) + "tel_mobile: " + tel_mobile)
    print("===========")
    print(str(url) + "tel_fixe: " + tel_fixe)
    print("= = = = = = = = = = = = = = = = = = = = = = = = = = = = = =")


for x in range(18, 100):
    get_page(x)
