# Generated by Django 4.0.4 on 2022-07-12 18:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_1', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='contents',
            name='name',
            field=models.CharField(default='name', max_length=20),
            preserve_default=False,
        ),
    ]