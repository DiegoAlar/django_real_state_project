# Generated by Django 3.0.3 on 2020-05-03 23:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('property', '0008_reserve'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='image',
            field=models.ImageField(null=True, upload_to='category/'),
        ),
        migrations.AlterField(
            model_name='property',
            name='image',
            field=models.ImageField(null=True, upload_to='property/'),
        ),
    ]
