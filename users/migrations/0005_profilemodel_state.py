# Generated by Django 4.1.2 on 2022-11-07 15:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0004_profilemodel_email'),
    ]

    operations = [
        migrations.AddField(
            model_name='profilemodel',
            name='state',
            field=models.CharField(blank=True, max_length=50, null=True, verbose_name='state'),
        ),
    ]