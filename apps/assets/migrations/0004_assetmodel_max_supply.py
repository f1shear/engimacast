# Generated by Django 2.0 on 2018-03-01 17:47

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ('assets', '0003_auto_20180301_1746'),
    ]

    operations = [
        migrations.AddField(
            model_name='assetmodel',
            name='max_supply',
            field=models.FloatField(blank=True, default=0.0, null=True),
        ),
    ]
