from django.db import models
import django.utils.timezone as timezone
# Create your models here.
# 所有的Model都需要继承models.Model



# Create your models here.
# 所有的Model都需要继承models.Model
class JD_DeviceOwner(models.Model):
    userid = models.CharField('ID',max_length = 256)
    create_time = models.DateTimeField(default=timezone.now)
    class Meta:
        ordering = ['pk']
        verbose_name = '设备所有者'
        verbose_name_plural = verbose_name
    def __str__(self):
        return self.userid



class JD_Device(models.Model):
    deviceid = models.CharField('设备ID',max_length = 256)
    # userid= models.IntegerField()
    ownerid = models.ForeignKey(JD_DeviceOwner, None, null=True)
    create_time = models.DateTimeField(default=timezone.now)

    class Meta:
        ordering = ['pk']
        verbose_name = '设备ID'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.deviceid


#
# class JD_User(models.Model):
#     # 创建2个字段，最大长度32，类型是char。
#     user = models.CharField('名称',max_length = 256)
#     userid= models.IntegerField()
#
#     class Meta:
#         ordering = ['userid']
#         verbose_name = '用户ID'
#         verbose_name_plural = verbose_name
#
#     def __str__(self):
#         return self.name
#
#



class JD_Whereis(models.Model):

    ownerid = models.ForeignKey(JD_DeviceOwner, None, null=True)
    deviceid = models.ForeignKey(JD_Device, None, null=True)

    input_itemname =models.CharField('输入物品名', max_length=256)
    processed_name =models.CharField('处理后物品名', max_length=256)
    input_positon =models.CharField('输入位置', max_length=256)
    processed_position =models.CharField('输入位置', max_length=256)
    other =models.CharField('其他属性', max_length=1024)

    # userid = models.IntegerField()
    create_time = models.DateTimeField(default=timezone.now)


    class Meta:
        ordering = ['pk']
        verbose_name = '在哪'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name

class JD_Whereis_History(models.Model):
    ownerid = models.ForeignKey(JD_DeviceOwner, None, null=True)
    deviceid = models.ForeignKey(JD_Device, None, null=True)

    input_itemname = models.CharField('输入物品名', max_length=256)
    processed_name = models.CharField('处理后物品名', max_length=256)
    input_positon = models.CharField('输入位置', max_length=256)
    processed_position = models.CharField('输入位置', max_length=256)
    other = models.CharField('其他属性', max_length=1024)

    # userid = models.IntegerField()
    create_time = models.DateTimeField()

    class Meta:
        ordering = ['pk']
        verbose_name = '在哪'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name

class JD_Whereis_Log(models.Model):
    request=models.TextField("请求")
    ip=models.CharField('IP', max_length=16)
    header=models.TextField("Header")
    response = models.TextField("响应")


