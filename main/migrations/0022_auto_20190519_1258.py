# Generated by Django 2.2 on 2019-05-19 10:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0021_auto_20190519_1214'),
    ]

    operations = [
        migrations.AlterField(
            model_name='music',
            name='price_M',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=4, null=True),
        ),
    ]
