# Generated by Django 4.0.6 on 2022-08-30 11:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_3', '0002_alter_content_options_mode_brief'),
    ]

    operations = [
        migrations.AlterField(
            model_name='content',
            name='name',
            field=models.CharField(max_length=30),
        ),
    ]
