from django.db import models

# Create your models here.


class Chapter(models.Model):
    id = models.IntegerField(primary_key=True)
    chapter = models.CharField(max_length=20)

    def __str__(self):
        return self.chapter

    class Meta:
        verbose_name = "章节"
        verbose_name_plural = "章节"


class Section(models.Model):
    chapter = models.ForeignKey(Chapter, on_delete=models.CASCADE)
    section = models.CharField(max_length=20)
    content = models.TextField()

    def __str__(self):
        return self.section

    class Meta:
        verbose_name = "内容"
        verbose_name_plural = "内容"

