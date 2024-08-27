from django.db import models

# Create your models here.
# class Plant(models.Model):
#     name = models.CharField(max_length=255)
#     image = models.ImageField(upload_to='images/')
#     scientific_name = models.CharField(max_length=255)
#     family = models.CharField(max_length=255)
#     genus = models.CharField(max_length=255)
#     species = models.CharField(max_length=255)
#     location = models.CharField(max_length=255)
#     collection_date = models.DateField()
#     collector = models.CharField(default='Nil',max_length=255)
#     def __str__(self):
#         return self.name
    
class NewPlant(models.Model):
    name = models.CharField(max_length=255)
    image = models.ImageField(upload_to='images255/')
    description = models.TextField()
    family = models.CharField(max_length=255)
    type = models.CharField(max_length=255)

    def __str__(self):
        return self.name
    

class NewAllPlant(models.Model):
    name = models.CharField(max_length=255)
    image = models.ImageField(upload_to='images/')
    scientific_name = models.CharField(max_length=255)
    family = models.CharField(max_length=255)
    genus = models.CharField(max_length=255)
    species = models.CharField(max_length=255)
    location = models.CharField(max_length=255)
    collection_date = models.DateField(default='1021-01-01')
    collector = models.CharField(default='Nil',max_length=255)
    classification = models.CharField(max_length=255)
    def __str__(self):
        return self.name