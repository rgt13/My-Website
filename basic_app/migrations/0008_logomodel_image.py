# Generated by Django 2.1.5 on 2019-01-21 20:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('basic_app', '0007_auto_20190121_1512'),
    ]

    operations = [
        migrations.AddField(
            model_name='logomodel',
            name='image',
            field=models.ImageField(null=True, upload_to='uploads'),
        ),
    ]
