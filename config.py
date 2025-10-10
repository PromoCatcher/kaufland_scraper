import logging
from os import environ

from dotenv import load_dotenv


load_dotenv()

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(message)s",
    datefmt="%Y-%m-%d %H:%M:%S",
)

logger = logging.getLogger(__name__)


SA_KEY_PATH = environ["SA_KEY_PATH"]
BUCKET_NAME = environ["BUCKET_NAME"]
