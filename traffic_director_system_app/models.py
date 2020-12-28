from django.db import models
from django_countries.fields import CountryField


class RedirectLink(models.Model):
    short_url_identifier = models.CharField(max_length=5, null=False)


class LandingPage(models.Model):
    url = models.CharField(max_length=255, null=False)
    country = CountryField(blank_label='(select country)', blank=True)
    weight = models.FloatField(blank=True, null=True)
    redirect_link = models.ForeignKey(RedirectLink, on_delete=models.CASCADE, null=False)

    class Meta:
        unique_together = ("redirect_link", "url", "country")


class Click(models.Model):
    ip_address = models.GenericIPAddressField(null=True)
    created_at = models.DateTimeField(auto_now_add=True, null=True)
    redirect_link = models.ForeignKey(RedirectLink, on_delete=models.CASCADE, null=False)
    country = CountryField(blank=True)






