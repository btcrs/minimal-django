import sys

from django.conf.urls import url
from django.conf import settings
from django.http import HttpResponse
from django.core.management import execute_from_command_line

if not settings.configured:
    settings.configure(
         DEBUG=True,
         SECRET_KEY='A-random-secret-key!',
         ROOT_URLCONF=sys.modules[__name__],
         DATABASES = {
            'default': {
            'ENGINE': 'django.db.backends.sqlite3',
            'NAME': '',
            'USER': '',
            'PASSWORD': '',
            'HOST': '', 
            'PORT': '',
            }
        }
    )

def index(request):
    return HttpResponse('<h1> minimal </h1>')

urlpatterns = [
    url(r'^$', index),
]

if __name__ == '__main__':
   execute_from_command_line(sys.argv)
