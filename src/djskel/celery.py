from __future__ import absolute_import
import os
from celery import Celery
from django.conf import settings
from django.contrib import admin

app = Celery('proj')

app.config_from_object(settings)
app.autodiscover_tasks(lambda: settings.INSTALLED_APPS)

@app.task(bind=True)
def debug_task(self):
    print('Request: {0!r}'.format(self.request))
    return "Done"

from djcelery.models import TaskMeta
class TaskMetaAdmin(admin.ModelAdmin):
    readonly_fields = ('result',)
admin.site.register(TaskMeta, TaskMetaAdmin)