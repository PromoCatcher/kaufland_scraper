import os

from config import logger
from google_config import bucket


def upload_iamges_to_gcs(date_range: str):
    logger.info("Getting all files")
    all_files = os.listdir(f"output/{date_range}")

    logger.info("Uploading files")
    for file in all_files:
        blob = bucket.blob(f"Kaufland/{date_range}/{file}")
        blob.upload_from_filename(f"output/{date_range}/{file}")

    logger.info("Files uploadeddaj li")
