from us_visa.logger import logging
from us_visa.exception import USvisaException
logging.info("Welcome to our custom log")
import sys
try:
    a=2/0
except Exception as e:
    raise USvisaException(e,sys)
