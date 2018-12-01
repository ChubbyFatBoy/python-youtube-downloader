import configparser
import os

config = configparser.ConfigParser()
config.read('config.ini')
print(config.get('main', 'url'))

def create_requirements():
	os.makedirs(os.path.join(os.path.dirname(os.path.abspath(__file__)), config.get('main', 'dl_folder')), exist_ok=True)
	os.environ["SECRET_KEY"] = config.get('main', 'flask_key')
	
url = config.get('main', 'url')
port = config.get('main', 'port')
debug = config.get('main', 'debug')
download_folder = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'testdownload')