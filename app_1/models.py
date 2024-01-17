from django.db import models

# Create your models here.


class Titles(models.Model):
    id = models.IntegerField(primary_key=True)
    title = models.CharField(max_length=20)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = '目录'
        verbose_name_plural = '目录'


class Contents(models.Model):
    headline = models.ForeignKey(Titles, on_delete=models.CASCADE, verbose_name='所属标题')
    name = models.CharField(max_length=20)
    content = models.CharField(max_length=60)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = '内容'
        verbose_name_plural = '内容'