# Generated by Django 3.2.6 on 2021-08-31 08:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Supplier',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('registration_date', models.DateTimeField(auto_now=True, verbose_name='registration date')),
                ('full_name', models.CharField(max_length=200)),
                ('email', models.EmailField(help_text='Required. Inform a valid email address.', max_length=254)),
                ('phone', models.CharField(max_length=200)),
                ('date_of_birth', models.CharField(max_length=200)),
                ('password', models.CharField(max_length=200)),
                ('confirm_password', models.CharField(max_length=200)),
            ],
        ),
    ]
