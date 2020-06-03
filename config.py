import datetime
import os
from dotenv import load_dotenv

basedir = os.path.abspath(os.path.dirname(__file__))
load_dotenv(dotenv_path=os.path.join(basedir, '.env'))

class Config(object):
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'very-secure-token-key'
    OIDC_REDIRECT_URI = os.environ.get('OIDC_REDIRECT_URI') or 'http://localhost:5000/redirect_uri'
    PERMANENT_SESSION_LIFETIME = datetime.timedelta(days=7).total_seconds()
