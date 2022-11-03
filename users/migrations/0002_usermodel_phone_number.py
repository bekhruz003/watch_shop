# Generated by Django 4.1.2 on 2022-11-03 14:17

from django.db import migrations, models
import users.validators


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='usermodel',
            name='phone_number',
            field=models.CharField(default=None, max_length=13, unique=True, validators=[users.validators.PhoneValidator()]),
            preserve_default=False,
        ),
    ]