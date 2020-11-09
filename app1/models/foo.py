from django.db import models

class Foo(models.Model):
    value = models.IntegerField()

    class Meta:
        app_label = 'app1'

