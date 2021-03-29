# Generated by Django 3.1.7 on 2021-03-29 17:27

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('voucherMe', '0015_auto_20210329_2252'),
    ]

    operations = [
        migrations.AlterField(
            model_name='business',
            name='user_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='auth.user'),
        ),
    ]