from waitress import serve
import dirt
from config2.config import config as config2
import os

app = dirt.create_app()

listen = "*:%s"%(config2['port'])

serve(app, listen=listen)
