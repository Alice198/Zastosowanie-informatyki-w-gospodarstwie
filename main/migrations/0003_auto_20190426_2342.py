# Generated by Django 2.2 on 2019-04-26 21:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_auto_20190419_1510'),
    ]

    operations = [
        migrations.AlterField(
            model_name='died',
            name='makeup',
            field=models.CharField(choices=[('Y', 'Yes'), ('L', 'Light'), ('N', 'No')], max_length=1),
        ),
    ]
