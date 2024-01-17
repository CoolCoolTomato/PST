from django.db import models

# Create your models here.


#  公告的模型
class Notice(models.Model):
    id = models.IntegerField(primary_key=True)
    title = models.CharField(max_length=30)
    content = models.TextField()
    times = models.CharField(max_length=15)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = '公告'
        verbose_name_plural = '公告'


#  反馈的模型
class Feedback(models.Model):
    id = models.AutoField(primary_key=True)
    kind = models.CharField(max_length=10)
    contact = models.CharField(max_length=35, blank=True)
    content = models.TextField()

    def __str__(self):
        return self.kind

    class Meta:
        verbose_name = '反馈'
        verbose_name_plural = '反馈'

