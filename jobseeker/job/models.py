from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class UserSign(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    mobile = models.CharField(max_length=15, null=True)
    image = models.FileField(null=True)
    gender  = models.CharField(max_length=10,null=True)
    type = models.CharField(max_length=10, null=True)
    
    def __str__(self):
        return self.user.first_name

class RecruiterSign(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    mobile = models.CharField(max_length=15, null=True)
    image = models.FileField(null=True)
    company = models.CharField(max_length=100, null=True)
    gender  = models.CharField(max_length=10,null=True)
    type = models.CharField(max_length=10, null=True)
    status = models.CharField(max_length=10, null=True)    
    
    def __str__(self):
        return self.user.first_name