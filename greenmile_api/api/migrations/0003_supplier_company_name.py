# Generated by Django 3.2.6 on 2021-08-31 08:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_supplier'),
    ]

    operations = [
        migrations.AddField(
            model_name='supplier',
            name='company_name',
            field=models.CharField(default='company-name', max_length=200),
        ),
    ]
