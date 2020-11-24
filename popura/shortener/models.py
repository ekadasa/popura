from django.db import models


class Url(models.Model):
    slug = models.SlugField(verbose_name='Slug', unique=True)
    title = models.CharField(verbose_name='Title', max_length=255)
    url = models.URLField(verbose_name='URL')
    keyword = models.CharField(verbose_name='Keyword', max_length=255, db_index=True)
    created_at = models.DateTimeField(verbose_name='Created at', auto_now_add=True)
    updated_at = models.DateTimeField(verbose_name='Updated at', auto_now=True)

    def __str__(self):
        return f'{self.slug}::{self.url}'


class UrlView(models.Model):
    url = models.ForeignKey(Url, on_delete=models.CASCADE)
    referrer = models.CharField(verbose_name='Referrer', max_length=255)
    ip_address = models.GenericIPAddressField(verbose_name='IP Address')
    country_code = models.CharField(verbose_name='Country code', max_length=4)
    created_at = models.DateTimeField(verbose_name='Created at', auto_now_add=True)

    def __str__(self):
        return f'{self.url}'


class UrlViewMeta(models.Model):
    url_view = models.ForeignKey(UrlView, on_delete=models.CASCADE)
    kind = models.CharField(verbose_name='Type/Kind', max_length=255)
    value = models.TextField(verbose_name='Value')
    created_at = models.DateTimeField(verbose_name='Created at', auto_now_add=True)

    def __str__(self):
        return f'{self.url}'
