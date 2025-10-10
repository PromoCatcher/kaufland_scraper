from google.oauth2.service_account import Credentials
from google.cloud.storage import Client

from config import SA_KEY_PATH, BUCKET_NAME


credentials = Credentials.from_service_account_file(SA_KEY_PATH)
client = Client(credentials=credentials)
bucket = client.get_bucket(BUCKET_NAME)
