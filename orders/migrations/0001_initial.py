# Generated by Django 4.1.2 on 2022-11-08 04:07

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('shop', '0002_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='OrderHistoryModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('phone', models.CharField(max_length=13, verbose_name='phone')),
                ('first_name', models.CharField(max_length=50, verbose_name='first name')),
                ('last_name', models.CharField(max_length=50, verbose_name='last name')),
                ('country', models.CharField(max_length=125, verbose_name='country')),
                ('address1', models.CharField(max_length=255, verbose_name='address1')),
                ('address2', models.CharField(blank=True, max_length=255, null=True, verbose_name='address2')),
                ('city', models.CharField(max_length=100, verbose_name='city')),
                ('district', models.CharField(max_length=100, verbose_name='district')),
                ('zip_code', models.CharField(max_length=6, verbose_name='zip_code')),
                ('email', models.EmailField(max_length=254, verbose_name='email')),
                ('state', models.CharField(max_length=50, verbose_name='state')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='created at')),
                ('product', models.ManyToManyField(to='shop.productmodel')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='user')),
            ],
            options={
                'verbose_name': 'order',
                'verbose_name_plural': 'orders',
            },
        ),
    ]