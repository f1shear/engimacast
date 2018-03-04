# Generated by Django 2.0 on 2018-03-02 16:06

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ('assets', '0008_auto_20180302_1035'),
    ]

    operations = [
        migrations.CreateModel(
            name='DomainMediaModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('topic', models.CharField(max_length=255)),
                ('ref_id', models.CharField(max_length=255)),
                ('source', models.CharField(max_length=255)),
                ('media_type', models.CharField(choices=[('social', 'Social'), ('news', 'News')], max_length=255)),
                ('title', models.TextField(blank=True, default='', null=True)),
                ('url', models.CharField(max_length=255)),
                ('description', models.TextField(blank=True, default='', null=True)),
                ('sentiment_score', models.FloatField(blank=True, default=0.0, null=True)),
                ('backlinks_count', models.FloatField(blank=True, default=0.0, null=True)),
                ('scam_score', models.FloatField(blank=True, default=0.0, null=True)),
                ('fud_score', models.FloatField(blank=True, default=0.0, null=True)),
                ('published_at', models.DateTimeField(blank=True, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'db_table': 'domain_media',
            },
        ),
        migrations.AddField(
            model_name='assetmodel',
            name='cmc_id',
            field=models.CharField(max_length=255, unique=True),
            preserve_default=False,
        ),
    ]
