from __future__ import absolute_import, unicode_literals

import os

from celery import Celery
from exchangeDb.views import saveDateModified

# set the default Django settings module for the 'celery' program.
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'exchangeApi.settings')

app = Celery('celery_app')

# Using a string here means the worker doesn't have to serialize
# the configuration object to child processes.
# - namespace='CELERY' means all celery-related configuration keys
#   should have a `CELERY_` prefix.
app.config_from_object('django.conf:settings', namespace='CELERY')

# Load task modules from all registered Django app configs.
app.autodiscover_tasks()

@app.on_after_configure.connect
def setup_periodic_task(sender):
    sender.add_periodic_task(180.0, name='added every 3 minutes')


@app.task
def task():
    return saveDateModified

"""@app.task(bind=True)
def debug_task(self):
    print('Request: {0!r}'.format(self.request))"""