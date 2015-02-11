Getting started

git clone https://github.com/techietek/tools.api.git 

once cloned in order to start install all the required packages:

pip install -r tools.api/requirements.txt

once you have that completed, create the production settings file:
touch tools.api/settings/production.py

you will need to setup database parameters, to get started with a sql-lite db you can do the following:

'''
vim tools.api/settings/production.py
from base import *
#
# ensure you also add your static path this is where your html files will be served otherwise it will be taken from the base config
#

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}
'''

once you have that setup you can run the tests to ensure all the apps are working:

python tools.api/manage.py syncdb
python tools.api/manage.py collectstatic
python tools.api/manage.py test

if all passes you should be ready to run:
python tools.api/manage.py runserver 0:8080

open your browser to: http://localhost:8080/v1/f5/cookie/decode

if you are looking to set this up in production here is an example of how i did it:
http://www.techietek.com/2015/02/11/setup-pyenv-ubuntu-apache-use/