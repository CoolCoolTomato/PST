# Generated by Django 4.0.4 on 2022-07-17 23:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('index', '0003_alter_feedback_id_alter_feedback_kind'),
    ]

    operations = [
        migrations.AlterField(
            model_name='feedback',
            name='kind',
            field=models.CharField(blank=True, default='没有联系方式', max_length=10),
        ),
    ]