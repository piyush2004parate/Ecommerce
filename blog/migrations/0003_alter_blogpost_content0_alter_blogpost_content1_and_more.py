# Generated by Django 5.0 on 2024-07-05 13:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_blogpost_content0_blogpost_content1_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blogpost',
            name='content0',
            field=models.CharField(default='', max_length=5000),
        ),
        migrations.AlterField(
            model_name='blogpost',
            name='content1',
            field=models.CharField(default='', max_length=5000),
        ),
        migrations.AlterField(
            model_name='blogpost',
            name='content2',
            field=models.CharField(default='', max_length=5000),
        ),
    ]
