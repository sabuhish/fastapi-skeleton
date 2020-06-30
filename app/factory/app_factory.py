
import  os
from app.config.production import prod_settings
from app.config.development import  dev_settings



class Customexception(Exception):
    def __init__(self, error):
        self.error = error


def app_setting():

    setting = os.getenv("setting")

    return dev_settings if setting == "dev" else  prod_settings if setting == "prod" else None
    
  