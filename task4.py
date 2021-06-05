from bs4 import BeautifulSoup
import requests
array = []
for x in range(1, 6):
    url = "https://planetdesert.com/collections/cactus"
    r = requests.get(url)

    content = r.text
    soup = BeautifulSoup(content, "html.parser")

    cactus_item = soup.findAll("div", class_="grid-product__content")

    filename = "Pdoduct.csv"
    f = open(filename, "w")

    header = "Title, Price \n"
    f.write(header)


    for cactus in cactus_item:
        title = cactus.find("div", class_="grid-product__title").text
        price = cactus.find("div", class_="grid-product__price").text
        f.write(title + "," + price)

        property_into = {
            "title": title,
            "price": price
        }
        array.append(property_into)
    print(len(array))

    f.close()