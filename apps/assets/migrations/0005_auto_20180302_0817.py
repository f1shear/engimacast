# Generated by Django 2.0 on 2018-03-02 08:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('assets', '0004_assetmodel_max_supply'),
    ]

    operations = [
        migrations.RenameField(
            model_name='assethistorymodel',
            old_name='created_on',
            new_name='created_at',
        ),
        migrations.RenameField(
            model_name='assetmediamodel',
            old_name='created_on',
            new_name='created_at',
        ),
        migrations.RenameField(
            model_name='assetmodel',
            old_name='created_on',
            new_name='created_at',
        ),
        migrations.RenameField(
            model_name='assetmodel',
            old_name='volume',
            new_name='trading_volume',
        ),
        migrations.RenameField(
            model_name='assetmodel',
            old_name='updated_on',
            new_name='updated_at',
        ),
        migrations.RenameField(
            model_name='assetvotemodel',
            old_name='created_on',
            new_name='created_at',
        ),
        migrations.RenameField(
            model_name='marketassetmodel',
            old_name='created_on',
            new_name='created_at',
        ),
        migrations.RenameField(
            model_name='marketassetmodel',
            old_name='updated_on',
            new_name='updated_at',
        ),
        migrations.RenameField(
            model_name='marketmodel',
            old_name='created_on',
            new_name='created_at',
        ),
        migrations.RenameField(
            model_name='marketmodel',
            old_name='updated_on',
            new_name='updated_at',
        ),
        migrations.RenameField(
            model_name='mediareactionmodel',
            old_name='created_on',
            new_name='created_at',
        ),
        migrations.RenameField(
            model_name='pricefuturemodel',
            old_name='created_on',
            new_name='created_at',
        ),
        migrations.RenameField(
            model_name='pricefuturemodel',
            old_name='price_on',
            new_name='price_at',
        ),
        migrations.RenameField(
            model_name='pricehistorymodel',
            old_name='created_on',
            new_name='created_at',
        ),
        migrations.RenameField(
            model_name='pricehistorymodel',
            old_name='price_on',
            new_name='price_at',
        ),
        migrations.RemoveField(
            model_name='assethistorymodel',
            name='updated_on',
        ),
        migrations.RemoveField(
            model_name='assetmediamodel',
            name='updated_on',
        ),
        migrations.RemoveField(
            model_name='marketassetmodel',
            name='exchange_asset',
        ),
        migrations.RemoveField(
            model_name='marketassetmodel',
            name='latest_rate',
        ),
        migrations.AddField(
            model_name='assethistorymodel',
            name='total_supply',
            field=models.FloatField(blank=True, default=0.0, null=True),
        ),
        migrations.AddField(
            model_name='assetmediamodel',
            name='published_at',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='assetmediamodel',
            name='ref_id',
            field=models.CharField(default='', max_length=255),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='assetmodel',
            name='description',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='assetmodel',
            name='explorer',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='assetmodel',
            name='recent_cmc_rank',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='marketassetmodel',
            name='pair',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='assetmodel',
            name='symbol',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='assetmodel',
            name='website',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='marketmodel',
            name='website',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]