import os
basedir = os.path.abspath(os.path.dirname(__file__))


class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY') or '2409j1-0935ged[rgaehrga983]'

    UPLOAD_PATH = os.path.join(basedir, 'upload')
    DOWNLOAD_PATH = os.path.join(basedir, 'download')
