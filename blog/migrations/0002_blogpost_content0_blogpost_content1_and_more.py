# Generated by Django 5.0 on 2024-07-05 11:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='blogpost',
            name='content0',
            field=models.CharField(default='', max_length=500),
        ),
        migrations.AddField(
            model_name='blogpost',
            name='content1',
            field=models.CharField(default='', max_length=500),
        ),
        migrations.AddField(
            model_name='blogpost',
            name='content2',
            field=models.CharField(default='', max_length=500),
        ),
    ]
