# Generated by Django 2.2 on 2019-05-19 20:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0024_remove_died_price_d'),
    ]

    operations = [
        migrations.AlterField(
            model_name='coffin',
            name='price_C',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=7, null=True),
        ),
        migrations.AlterField(
            model_name='flowers',
            name='price_F',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=7, null=True),
        ),
        migrations.AlterField(
            model_name='music',
            name='level',
            field=models.CharField(choices=[('B', 'Beginner'), ('S', 'Semi-Advanced'), ('A', 'Advanced'), ('P', 'Professional')], max_length=1),
        ),
        migrations.AlterField(
            model_name='order',
            name='costs',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=8, null=True),
        ),
    ]
