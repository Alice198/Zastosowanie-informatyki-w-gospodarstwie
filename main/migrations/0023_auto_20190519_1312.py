# Generated by Django 2.2 on 2019-05-19 11:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0022_auto_20190519_1258'),
    ]

    operations = [
        migrations.AlterField(
            model_name='music',
            name='price_M',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=5, null=True),
        ),
    ]
