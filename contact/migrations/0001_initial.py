# Generated by Django 5.0.3 on 2024-05-04 22:53

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Register',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=100)),
                ('last_name', models.CharField(max_length=100)),
                ('postion', models.CharField(max_length=100)),
                ('year_of_experience', models.CharField(max_length=100)),
                ('cv', models.TextField()),
                ('specialization', models.CharField(max_length=100)),
                ('photo', models.ImageField(upload_to='media/', validators=[django.core.validators.FileExtensionValidator(allowed_extensions=['jpg', 'jpeg', 'png', 'gif'])])),
                ('linkedin', models.CharField(max_length=100)),
                ('company', models.CharField(max_length=100)),
                ('company_web_address', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254, unique=True, verbose_name='email address')),
                ('phone_number', models.CharField(max_length=10)),
                ('country', models.CharField(max_length=100)),
            ],
        ),
    ]
