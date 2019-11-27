from django.db import models

class Classifier(models.Model):
    title = models.CharField(max_length = 200)

    textdata = models.FileField(upload_to = 'textdata/')

    # pub_date = models.DateTimeField('date published')

    def __str__(self):
        return self.title