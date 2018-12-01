import configparser
import os

config = configparser.ConfigParser()
config.read('config.ini')

flask_key = config.get('main', 'flask_key')
url = config.get('main', 'host')
port = config.get('main', 'port')
debug = config.get('main', 'debug')
download_folder = os.path.join(os.path.dirname(os.path.abspath(__file__)), config.get('main', 'dl_folder'))