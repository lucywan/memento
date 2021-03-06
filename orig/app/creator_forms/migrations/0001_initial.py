# Generated by Django 4.0.3 on 2022-04-26 23:51

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='SubmitNFTModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=300, verbose_name='Name of NFT')),
                ('location', models.CharField(max_length=300, verbose_name='Location of NFT Souvenir')),
                ('link', models.CharField(max_length=300, verbose_name='Link to NFT Souvenir (preferably through OpenSea)')),
                ('username', models.ForeignKey(default='', on_delete=django.db.models.deletion.SET_DEFAULT, to=settings.AUTH_USER_MODEL, verbose_name='username')),
            ],
        ),
    ]
