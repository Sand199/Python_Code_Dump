import requests, bs4, logging

logging.basicConfig(
    filename="mylogfile.txt",
    level=logging.DEBUG,
    format="%(asctime)s - %(levelname)s  - %(message)s",
)

# logging.disable(logging.CRITICAL)
logging.debug("Start of program")


i = 405

while True:
    comic_url = f"http://xkcd.com/{i}/"
    res = requests.get(comic_url)
    res.raise_for_status()

    soup = bs4.BeautifulSoup(res.text, "html.parser")
    name = soup.select("#ctitle")[0].text
    img_url = soup.select("#middleContainer > a:nth-child(8)")[0].text

    file = open(f"xkcd/{name}.jpg", "wb")

    img = requests.get(img_url)

    for chunk in img.iter_content(10000):
        file.write(chunk)

    logging.info(f"Downloaded image {i}")
    i += 1

logging.debug("End of Program")
