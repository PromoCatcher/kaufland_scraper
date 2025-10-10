from config import logger
from scraper import scrape_url_links
from image_downloader import download_images
from utils import normalize_date_range
from uploader import upload_iamges_to_gcs


def main():
    logger.info("Starting the process.")

    links, dates = scrape_url_links()

    logger.info("Normalize dates.")
    normalized_dates = normalize_date_range(dates)

    download_images(links, normalized_dates)

    upload_iamges_to_gcs(normalized_dates)

    logger.info("Process executed.")


if __name__ == "__main__":
    main()
