activate_this = '/home/aquametrics/.virtualenvs/env/bin/activate_this.py'

with open(activate_this) as file_:
    exec(file_.read(), dict(__file__=activate_this))

"""
WSGI config for www project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/2.0/howto/deployment/wsgi/
"""

import os,sys

sys.path.insert(0,'/home/aquametrics/www')


from django.core.wsgi import get_wsgi_application

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "www.settings")

application = get_wsgi_application()
