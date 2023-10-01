import os
import logging
from dotenv import load_dotenv

logging.basicConfig(level=os.environ.get("LOG_LEVEL", "ERROR"))
log = logging.getLogger("debug_logger")

# Demo API from https://petstore.swagger.io/
API_URL = 'http://localhost:8080/api/v3'

JIRA_PROJECT_ABBR = 'KEY-'

PAGES_DICT = {
    'bolt t-shirt details': '/inventory-item.html?id=1',
    'cart': '/cart.html',
    'checkout info':'/checkout-step-one.html',
    'checkout overview':'/checkout-step-two.html',
    'index': '/',
    'inventory':'/inventory.html'
}

default_headers = {
    'Accept-Charset': 'UTF-8',
    'Accept': 'application/json',
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.100 Safari/537.36, QA Tests'
}

log.info('Host url set to %', API_URL)
