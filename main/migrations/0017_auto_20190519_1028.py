# Generated by Django 2.2 on 2019-05-19 08:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0016_auto_20190516_1106'),
    ]

    operations = [
        migrations.AddField(
            model_name='coffin',
            name='price_C',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=5, null=True),
        ),
        migrations.AddField(
            model_name='died',
            name='price_D',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=4, null=True),
        ),
        migrations.AddField(
            model_name='flowers',
            name='price_F',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=4, null=True),
        ),
        migrations.AddField(
            model_name='music',
            name='level',
            field=models.CharField(choices=[('B', 'Beginner'), ('S', 'Semi-Advanced'), ('A', 'Advanced')], default='S', max_length=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='music',
            name='price_M',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=4, null=True),
        ),
        migrations.AlterField(
            model_name='flowers',
            name='description',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
    ]
