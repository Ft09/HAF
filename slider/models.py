from django.db import models



class Slide(models.Model):
    image=models.ImageField()
    title=models.CharField(max_length=100)
    sub_title=models.CharField(max_length=100)