from django.db import models


# Create your models here.


class CompanyModel(models.Model):
    name = models.CharField(max_length=255)
    website = models.CharField(max_length=255)
    company_type = models.CharField(max_length=255)
    description = models.CharField(max_length=255)

    class Meta:
        db_table = 'company'


class CompanyEventModel(models.Model):
    company = models.ForeignKey(
        CompanyModel, related_name='company_events', on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    event_type = models.CharField(max_length=255)
    start = models.DateTimeField(null=True, blank=True)
    end = models.DateTimeField(null=True, blank=True)

    class Meta:
        db_table = 'company_event'
