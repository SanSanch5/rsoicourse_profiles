import os

DEBUG_MODE = False
PORT = 5002

BACKEND_PATH = os.path.dirname(os.path.abspath(__file__))
DB_PATH = os.path.join(BACKEND_PATH, 'profiles.db')
DB_URI = 'sqlite:////' + DB_PATH
