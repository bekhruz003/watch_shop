# Generated by Django 4.1.2 on 2022-11-07 14:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_profilemodel_first_name_profilemodel_last_name_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='profilemodel',
            name='email',
            field=models.EmailField(blank=True, max_length=254, null=True, verbose_name='email'),
        ),
    ]
