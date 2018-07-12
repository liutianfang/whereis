from django.db import models

class JD_Whereis_Log(models.Model):
    request=models.TextField("请求")
    ip=models.CharField('IP', max_length=16)
    header=models.TextField("Header")
    response = models.TextField("响应")


