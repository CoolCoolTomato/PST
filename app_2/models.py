from django.db import models

# Create your models here.


class Section(models.Model):
    id = models.IntegerField(primary_key=True)
    title = models.CharField(max_length=15)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = '目录'
        verbose_name_plural = '目录'


class Chapter(models.Model):
    headline = models.ForeignKey(Section, on_delete=models.CASCADE)
    title = models.CharField(max_length=15)
    content = models.TextField()
    codes = models.TextField()

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = '章节'
        verbose_name_plural = '章节'
