from django.db import models

# Create your models here.
class Period(models.Model):
    title = models.CharField(max_length=64)
    floor = models.IntegerField()
    time = models.IntegerField()

    def __repr__(self):
        return '<Period %s: %d>' %(self.title, self.time)

    def __str__(self):
        return '<Period %s: %d>' %(self.title, self.time)

class Audience(models.Model):
    title = models.CharField(max_length=64)

    def __repr__(self):
        return '<Audience %s>' %self.title

    def __str__(self):
        return '<Audience %s>' %self.title
