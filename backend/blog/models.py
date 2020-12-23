from django.db import models
from django.utils import timezone
import datetime
class Usergroup(models.Model):
    eng_name = models.CharField(max_length=100, null=False)
    kor_name = models.CharField(max_length=100,null=False)
    position = models.CharField(max_length=100,null=True)
    department = models.CharField(max_length=100, null=True)
    regi_date = models.DateTimeField(auto_now_add=True)
    pin = models.CharField(max_length=12,null=False)

# Create your models here.
class Access(models.Model):
    user_pk = models.ForeignKey(Usergroup,on_delete=models.CASCADE)
    enter_at = models.DateTimeField(default=datetime.datetime.now())
    out_at = models.DateTimeField(null=True,blank=True)
    recent = models.DateTimeField(default=datetime.datetime.now())
