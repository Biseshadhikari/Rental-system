# Generated by Django 4.2.11 on 2024-03-13 03:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rentalapp', '0002_property_image'),
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('firstname', models.CharField(max_length=20)),
                ('middlename', models.CharField(blank=True, max_length=20, null=True)),
                ('lastname', models.CharField(max_length=20)),
                ('username', models.CharField(max_length=20)),
                ('password1', models.CharField(max_length=20)),
                ('password2', models.CharField(max_length=20)),
                ('contact', models.CharField(max_length=20)),
            ],
        ),
    ]
