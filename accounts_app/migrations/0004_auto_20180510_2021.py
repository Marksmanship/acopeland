# Generated by Django 2.0.4 on 2018-05-11 00:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts_app', '0003_auto_20180510_2016'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='banner',
            field=models.ImageField(blank=True, default='static/Images/Banner/default.png', null=True, upload_to='user_banner'),
        ),
    ]
