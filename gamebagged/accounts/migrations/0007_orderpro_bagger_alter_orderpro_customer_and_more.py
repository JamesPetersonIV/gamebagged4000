# Generated by Django 4.1.3 on 2022-11-25 22:24

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('accounts', '0006_alter_orderpro_status'),
    ]

    operations = [
        migrations.AddField(
            model_name='orderpro',
            name='bagger',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='bagger', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='orderpro',
            name='customer',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL, verbose_name='customer'),
        ),
        migrations.DeleteModel(
            name='BaggerDelivery',
        ),
    ]
