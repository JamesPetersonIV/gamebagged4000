# Generated by Django 4.1.3 on 2022-11-23 14:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='orderpro',
            name='items',
            field=models.ManyToManyField(blank=True, to='accounts.product', verbose_name='product'),
        ),
    ]
