# Generated by Django 4.0.6 on 2022-08-31 10:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_3', '0003_alter_content_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='content',
            name='way',
            field=models.CharField(max_length=150),
        ),
    ]