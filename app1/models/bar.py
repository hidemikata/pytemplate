from django.db import models

class Bar(models.Model):
    value = models.IntegerField()

    class Meta:
        app_label = 'app1'

