# Generated by Django 3.1.3 on 2020-11-21 18:57

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Url',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('slug', models.SlugField(unique=True, verbose_name='Slug')),
                ('title', models.CharField(max_length=255, verbose_name='Title')),
                ('url', models.URLField(verbose_name='URL')),
                ('keyword', models.CharField(db_index=True, max_length=255, verbose_name='Keyword')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Created at')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Updated at')),
            ],
        ),
        migrations.CreateModel(
            name='UrlView',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('referrer', models.CharField(max_length=255, verbose_name='Referrer')),
                ('ip_address', models.GenericIPAddressField(verbose_name='IP Address')),
                ('country_code', models.CharField(max_length=4, verbose_name='Country code')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Created at')),
                ('url', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='shortener.url')),
            ],
        ),
        migrations.CreateModel(
            name='UrlViewMeta',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('kind', models.CharField(max_length=255, verbose_name='Type/Kind')),
                ('value', models.TextField(verbose_name='Value')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Created at')),
                ('url_view', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='shortener.urlview')),
            ],
        ),
    ]
