from django.db import models

class Prof_Exp(models.Model):
    image = models.ImageField(upload_to = 'images/')
    title = models.CharField(max_length=100, default = False)
    summary = models.CharField(max_length=400)

    def __str__(self):
        return self.title

class Education(models.Model):
    image = models.ImageField(upload_to = 'images/')
    title = models.CharField(max_length=100, default = False) 
    summary = models.CharField(max_length=400)
    
    def __str__(self):
        return self.title

class About_Me(models.Model):
    image = models.ImageField(upload_to = 'images/')
    title = models.CharField(max_length=100, default = False) 
    summary = models.CharField(max_length=1000)    

    def __str__(self):
        return self.title
    




         

