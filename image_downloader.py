import os
import requests

from config import logger


def download_images(image_links: list[str], dates: str):
    logger.info("Check is the folder existing")
    os.makedirs("output", exist_ok=True)

    logger.info("Start get the images")
    for i, link in enumerate(image_links):
        logger.info(f"Get image with link {link}")
        resp = requests.get(link)
        with open(f"output/{dates}/page_{i}.jpg", "wb") as file:
            file.write(resp.content)
        logger.info("Image downloaded")

    logger.info("Downloading images finished")
