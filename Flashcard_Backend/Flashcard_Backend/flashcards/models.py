from django.db import models


# Create your models here.
class Collection(models.Model):
    name = models.CharField(max_length=50)


class Flashcard(models.Model):
    collection = models.ForeignKey(Collection, on_delete=models.CASCADE)
    front = models.CharField(max_length=250, null=True, blank=True)
    back = models.CharField(max_length=250, null=True, blank=True)