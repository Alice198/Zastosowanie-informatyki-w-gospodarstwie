# Generated by Django 2.2 on 2019-04-28 21:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0006_auto_20190427_1455'),
    ]

    operations = [
        migrations.AlterField(
            model_name='flowers',
            name='color',
            field=models.CharField(choices=[('Wh', 'White flowers'), ('Bl', 'Blue flowers'), ('Pi', 'Pink flowers'), ('Mi', 'Mix color flowers')], max_length=2),
        ),
    ]