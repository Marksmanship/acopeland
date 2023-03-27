# Generated by Django 2.0.4 on 2018-05-10 18:10

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('accounts_app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('city', models.CharField(blank=True, max_length=100, null=True)),
                ('phone', models.IntegerField(blank=True, default=0, null=True)),
                ('avatar', models.ImageField(blank=True, null=True, upload_to='user_avatar')),
                ('banner', models.ImageField(blank=True, null=True, upload_to='user_banner')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]