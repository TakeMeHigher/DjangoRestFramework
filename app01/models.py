from django.db import models

# Create your models here.
class Userinfo(models.Model):
    name=models.CharField(max_length=32,verbose_name='用户名')
    pwd=models.CharField(max_length=32,verbose_name='密码')
    token=models.CharField(max_length=64,null=True)

    def __str__(self):
        return self.name