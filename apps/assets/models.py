from django.db import models

from company.models import CompanyModel
from users.models import UserModel


class AssetModel(models.Model):
    """  update every 15 min; cmc api OK """
    ASSET_TYPES = (
        ('coin', 'Coin'),
        ('token', 'Token')
    )

    company = models.ForeignKey(
        CompanyModel, related_name='assets',
        null=True, blank=True, on_delete=models.CASCADE)
    asset_type = models.CharField(max_length=255, choices=ASSET_TYPES)
    cmc_id = models.CharField(max_length=255, unique=True)
    name = models.CharField(max_length=255)
    description = models.TextField(default='', null=True, blank=True)
    symbol = models.CharField(max_length=50, null=True, blank=True)
    website = models.CharField(max_length=255, null=True, blank=True)
    explorer = models.CharField(max_length=255, null=True, blank=True)
    recent_cmc_rank = models.IntegerField(null=True, blank=True)
    trading_volume = models.FloatField(default=0.0, null=True, blank=True)  # 24 hour
    total_supply = models.FloatField(default=0.0, null=True, blank=True)
    max_supply = models.FloatField(default=0.0, null=True, blank=True)
    circulating_supply = models.FloatField(default=0.0, null=True, blank=True)
    market_capital = models.FloatField(default=0.0, null=True, blank=True)
    latest_price = models.FloatField(default=0.0, null=True, blank=True)
    max_price = models.FloatField(default=0.0, null=True, blank=True)
    min_price = models.FloatField(default=0.0, null=True, blank=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'asset'
        ordering = ['-cmc_id']

    def __str__(self):
        return self.name


class AssetMediaModel(models.Model):
    """ update every 1 hour """
    MEDIA_TYPES = (
        ('social', 'Social'),
        ('news', 'News')
    )
    asset = models.ForeignKey(
        AssetModel, related_name='medias', on_delete=models.CASCADE)
    ref_id = models.CharField(max_length=255)
    source = models.CharField(max_length=255)
    media_type = models.CharField(max_length=255, choices=MEDIA_TYPES)
    title = models.TextField(default='', null=True, blank=True)
    url = models.CharField(max_length=255)
    description = models.TextField(default='', null=True, blank=True)
    sentiment_score = models.FloatField(default=0.0, null=True, blank=True)
    backlinks_count = models.FloatField(default=0.0, null=True, blank=True)
    scam_score = models.FloatField(default=0.0, null=True, blank=True)
    fud_score = models.FloatField(default=0.0, null=True, blank=True)

    published_at = models.DateTimeField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'asset_media'
        ordering = ['-published_at']

    def __str__(self):
        return '%s - %s' % (self.source, self.asset)


class DomainMediaModel(models.Model):
    """ common domain news """
    MEDIA_TYPES = (
        ('social', 'Social'),
        ('news', 'News')
    )
    TOPICS = (
        ('blockchain', 'Blockchain'),
        ('cryptocurrency', 'Cryptocurrency'),
        ('initial coin offerings', 'ICO'),
        ('cryptocurrency exchange', 'Cryptocurrency Exchange')
    )
    topic = models.CharField(max_length=255)
    ref_id = models.CharField(max_length=255)
    source = models.CharField(max_length=255)
    media_type = models.CharField(max_length=255, choices=MEDIA_TYPES)
    title = models.TextField(default='', null=True, blank=True)
    url = models.CharField(max_length=255)
    description = models.TextField(default='', null=True, blank=True)
    sentiment_score = models.FloatField(default=0.0, null=True, blank=True)
    backlinks_count = models.FloatField(default=0.0, null=True, blank=True)
    scam_score = models.FloatField(default=0.0, null=True, blank=True)
    fud_score = models.FloatField(default=0.0, null=True, blank=True)

    published_at = models.DateTimeField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'domain_media'
        ordering = ['-published_at']

    def __str__(self):
        return '%s - %s' % (self.source, self.topic)


class MediaReactionModel(models.Model):
    """ rating by users """
    REACTIONS = (
        ('agree', 'Agree'),
        ('disagree', 'Disagree'),
        ('scam', 'Scam'),
        ('fud', 'FUD'),
        ('fake', 'Fake')
    )
    user = models.ForeignKey(
        UserModel, related_name='user_reactions',
        null=True, blank=True, on_delete=models.SET_NULL)
    media = models.ForeignKey(
        AssetMediaModel, related_name='media_reactions',
        on_delete=models.CASCADE)
    reaction = models.CharField(max_length=255, choices=REACTIONS)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'media_reaction'
        ordering = ['-created_at']


class AssetVoteModel(models.Model):
    # voting will be allowed every 1 hour UTC interval
    POSITIONS = (
        ('put', 'PUT'),
        ('call', 'CALL')
    )
    SENTIMENTS = (
        ('bearish', 'Bearish'),
        ('bullish', 'Bullish')
    )
    user = models.ForeignKey(
        UserModel, related_name='user_votes',
        null=True, blank=True, on_delete=models.SET_NULL)
    asset = models.ForeignKey(
        AssetModel, related_name='asset_votes',
        null=True, blank=True, on_delete=models.SET_NULL)
    position = models.CharField(max_length=255, choices=POSITIONS)
    sentiment = models.CharField(max_length=50, choices=SENTIMENTS)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'asset_vote'
        ordering = ['-created_at']


class MarketModel(models.Model):
    """ update every 24 hour """
    name = models.CharField(max_length=255)
    market_type = models.CharField(max_length=255, null=True, blank=True)
    website = models.CharField(max_length=255, null=True, blank=True)
    trade_volume = models.FloatField(default=0.0, null=True, blank=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'market'
        ordering = ['name']

    def __str__(self):
        return '%s' % self.name


class MarketAssetModel(models.Model):
    """ update every 10 min """
    # concurrent selenium scrapper
    # https://coinmarketcap.com/currencies/ripple/#markets
    market = models.ForeignKey(MarketModel, related_name='market_assets',
                               on_delete=models.CASCADE)
    asset = models.ForeignKey(AssetModel, related_name='asset_markets',
                              on_delete=models.CASCADE)
    latest_price = models.FloatField(default=0.0, null=True, blank=True)
    volume = models.FloatField(default=0.0, null=True, blank=True)
    pair = models.CharField(max_length=255, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'market_asset'
        ordering = ['-volume']


class AssetHistoryModel(models.Model):
    """ update every hour; cmc api OK """
    asset = models.ForeignKey(
        AssetModel, related_name='asset_histories', on_delete=models.CASCADE)
    price = models.FloatField(default=0.0, null=True, blank=True)
    popularity_score = models.FloatField(default=0.0, null=True, blank=True)
    cmc_rank = models.FloatField(default=0.0, null=True, blank=True)
    circulating_supply = models.FloatField(default=0.0, null=True, blank=True)
    max_supply = models.FloatField(default=0.0, null=True, blank=True)
    total_supply = models.FloatField(default=0.0, null=True, blank=True)
    trading_volume = models.FloatField(default=0.0, null=True, blank=True)
    market_capital = models.FloatField(default=0.0, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'asset_history'
        ordering = ['-created_at']


class PriceHistoryModel(models.Model):
    """  update every 15 min;  cmc api OK """
    asset = models.ForeignKey(
        AssetModel, related_name='asset_price_histories',
        on_delete=models.CASCADE)
    price = models.FloatField(default=0.0, null=True, blank=True)
    price_at = models.DateTimeField()
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'price_history'
        ordering = ['-price_at']


class PriceFutureModel(models.Model):
    asset = models.ForeignKey(
        AssetModel, related_name='asset_price_futures',
        on_delete=models.CASCADE)
    price = models.FloatField(default=0.0, null=True, blank=True)
    price_at = models.DateTimeField()
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'price_future'
        ordering = ['price_at']
