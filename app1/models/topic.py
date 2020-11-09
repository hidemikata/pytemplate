from django.db import models

class Topic(models.Model):
    value = models.IntegerField()
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')


