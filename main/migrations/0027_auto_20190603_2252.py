# Generated by Django 2.2 on 2019-06-03 20:52

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0026_auto_20190521_1537'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='coffin',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='main.Coffin'),
        ),
        migrations.AlterField(
            model_name='order',
            name='died',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='main.Died'),
        ),
    ]
