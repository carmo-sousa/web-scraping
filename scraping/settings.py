import logging
import os

from dotenv import load_dotenv

load_dotenv()

logging.basicConfig(
    format="%(asctime)s: [%(module)s] %(message)s",
    level=logging.INFO,
    datefmt="%m-%d-%Y %H:%M:%S",
)


class Config:
    USER = os.getenv("MAIL_FROM")
    PASSWORD = os.getenv("PASSWORD")
    TO = os.getenv("MAIL_TO")
    URL = os.getenv("URL")
