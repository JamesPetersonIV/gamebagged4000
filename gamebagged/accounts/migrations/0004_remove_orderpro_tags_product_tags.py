# Generated by Django 4.1.3 on 2022-11-23 14:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0003_tag_orderpro_tags'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='orderpro',
            name='tags',
        ),
        migrations.AddField(
            model_name='product',
            name='tags',
            field=models.ManyToManyField(to='accounts.tag'),
        ),
    ]
