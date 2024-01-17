from django.db import models

# Create your models here.


class Mode(models.Model):
    id = models.IntegerField(primary_key=True)
    mode = models.CharField(max_length=30)
    brief = models.CharField(max_length=60)
    way = models.TextField()

    def __str__(self):
        return self.mode

    class Meta:
        verbose_name = '模块'
        verbose_name_plural = '模块'


class Title(models.Model):
    mode = models.ForeignKey(Mode, on_delete=models.CASCADE)
    title = models.CharField(max_length=20)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = '标题'
        verbose_name_plural = '标题'


class Content(models.Model):
    title = models.ForeignKey(Title, on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    content = models.CharField(max_length=60)
    way = models.CharField(max_length=150)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = '内容'
        verbose_name_plural = '内容'
