from django.db import models

# Create your models here.

class matchingLearningModels(models.Model):
    title = models.CharField(max_length=50)
    description = models.CharField(max_length=250)
    architecture = models.FileField(upload_to='matchingLearningModels/') # JSON file
    weights = models.FileField(upload_to='matchingLearningModels/') # H5 file
    priority = models.PositiveSmallIntegerField(null=True)