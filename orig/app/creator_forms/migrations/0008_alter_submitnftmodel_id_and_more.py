# Generated by Django 4.0.3 on 2022-04-27 00:24

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('creator_forms', '0007_alter_submitnftmodel_id_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='submitnftmodel',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='submitnftmodel',
            name='username',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.SET_DEFAULT, to=settings.AUTH_USER_MODEL, verbose_name='username'),
        ),
    ]
