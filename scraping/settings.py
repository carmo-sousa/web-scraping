import os

from dotenv import load_dotenv
import logging

load_dotenv()

logging.basicConfig(
    format="%(asctime)s: [%(module)s] %(message)s",
    level=logging.INFO,
    datefmt="%m-%d-%Y %H:%M:%S",
)

USER = os.getenv("MAIL_FROM")
PASSWORD = os.getenv("PASSWORD")
TO = os.getenv("MAIL_TO")
URL = os.getenv("URL")
