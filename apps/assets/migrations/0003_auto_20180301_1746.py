# Generated by Django 2.0 on 2018-03-01 17:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('assets', '0002_auto_20180218_0608'),
    ]

    operations = [
        migrations.AddField(
            model_name='assetmodel',
            name='market_capital',
            field=models.FloatField(blank=True, default=0.0, null=True),
        ),
        migrations.AddField(
            model_name='assetmodel',
            name='symbol',
            field=models.CharField(default='', max_length=50),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='assetmodel',
            name='total_supply',
            field=models.FloatField(blank=True, default=0.0, null=True),
        ),
        migrations.AlterField(
            model_name='assetmodel',
            name='name',
            field=models.CharField(max_length=255, unique=True),
        ),
    ]
