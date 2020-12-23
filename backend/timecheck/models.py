from django.db import models

class Record(models.Model):
    name = models.CharField(max_length=100)
    in_at = models.DateTimeField(auto_now_add=True)
    out_at = models.DateTimeField(auto_now=True)
    objects = models.Manager()