import os
from dotenv import load_dotenv

load_dotenv()

MY_SECRET_KEY = os.getenv('MY_SECRET_KEY')
