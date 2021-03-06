# Generated by Django 2.1.5 on 2019-01-21 20:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('basic_app', '0006_workmodel'),
    ]

    operations = [
        migrations.CreateModel(
            name='LogoModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, null=True)),
                ('extension', models.CharField(max_length=255, null=True)),
            ],
        ),
        migrations.RemoveField(
            model_name='workmodel',
            name='logo',
        ),
        migrations.AddField(
            model_name='workmodel',
            name='logo',
            field=models.ManyToManyField(related_name='logos', to='basic_app.LogoModel'),
        ),
    ]
