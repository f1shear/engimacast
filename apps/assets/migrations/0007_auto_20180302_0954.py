# Generated by Django 2.0 on 2018-03-02 09:54

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ('assets', '0006_assethistorymodel_market_capital'),
    ]

    operations = [
        migrations.AlterField(
            model_name='assetmediamodel',
            name='description',
            field=models.TextField(blank=True, default='', null=True),
        ),
    ]
