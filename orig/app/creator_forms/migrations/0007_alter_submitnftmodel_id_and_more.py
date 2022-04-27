# Generated by Django 4.0.3 on 2022-04-27 00:21

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('creator_forms', '0006_alter_submitnftmodel_username'),
    ]

    operations = [
        migrations.AlterField(
            model_name='submitnftmodel',
            name='id',
            field=models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='submitnftmodel',
            name='username',
            field=models.ForeignKey(default='<function uuid1 at 0x7fceb13e9', on_delete=django.db.models.deletion.SET_DEFAULT, to=settings.AUTH_USER_MODEL, verbose_name='username'),
        ),
    ]
