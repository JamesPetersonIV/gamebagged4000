# Generated by Django 4.1.3 on 2022-11-23 14:17

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, null=True)),
                ('description', models.TextField()),
                ('img', models.ImageField(null=True, upload_to='images/')),
                ('slug', models.SlugField(max_length=255, null=True)),
                ('price', models.DecimalField(decimal_places=2, max_digits=7, null=True)),
                ('category', models.CharField(blank=True, choices=[('Video Games', 'Video Games'), ('Accessories', 'Accessories'), ('Mobile Phones', 'Mobile Phones'), ('Consoles', 'Consoles')], default=False, max_length=200)),
            ],
            options={
                'ordering': ('name',),
            },
        ),
        migrations.CreateModel(
            name='OrderPro',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_on', models.DateTimeField(auto_now_add=True, null=True)),
                ('price', models.DecimalField(decimal_places=2, max_digits=7, null=True)),
                ('status', models.CharField(blank=True, choices=[('Pending', 'Pending'), ('Out for delivery', 'Out for delivery'), ('Delivered', 'Delivered')], default=False, max_length=200)),
                ('customer', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL, verbose_name='user')),
                ('items', models.ManyToManyField(blank=True, null=True, to='accounts.product', verbose_name='product')),
            ],
            options={
                'ordering': ('created_on',),
            },
        ),
    ]
