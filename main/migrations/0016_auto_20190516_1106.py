# Generated by Django 2.2 on 2019-05-16 09:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0015_delete_reviews'),
    ]

    operations = [
        migrations.AlterField(
            model_name='flowers',
            name='description',
            field=models.CharField(max_length=200),
        ),
    ]
