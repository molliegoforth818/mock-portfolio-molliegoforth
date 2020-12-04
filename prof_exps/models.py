from django.db import models

class Prof_Exp(models.Model):
    image = models.ImageField(upload_to = 'images/')
    summary = models.CharField(max_length=400)

    def __str__(self):
        return self.summary

