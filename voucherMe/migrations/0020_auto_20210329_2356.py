# Generated by Django 3.1.7 on 2021-03-29 18:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('voucherMe', '0019_post_visits'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='visits',
            field=models.IntegerField(blank=True, default=0),
        ),
    ]
