# Generated by Django 3.0.3 on 2020-04-25 20:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('property', '0002_auto_20200425_2012'),
    ]

    operations = [
        migrations.AddField(
            model_name='property',
            name='image',
            field=models.ImageField(null=True, upload_to='propery/'),
        ),
    ]
