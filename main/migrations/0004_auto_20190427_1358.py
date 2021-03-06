# Generated by Django 2.2 on 2019-04-27 11:58

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_auto_20190426_2342'),
    ]

    operations = [
        migrations.AddField(
            model_name='coffin',
            name='user',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='main.User'),
        ),
        migrations.AddField(
            model_name='died',
            name='user',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='main.User'),
        ),
        migrations.AddField(
            model_name='flowers',
            name='user',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='main.User'),
        ),
        migrations.AddField(
            model_name='music',
            name='user',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='main.User'),
        ),
    ]
