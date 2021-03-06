# Generated by Django 2.1.1 on 2018-09-30 01:03

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('offers', '0006_auto_20180930_0102'),
    ]

    operations = [
        migrations.AddField(
            model_name='offer',
            name='create_by',
            field=models.DateTimeField(default=datetime.datetime(2018, 9, 30, 1, 2, 56, 346070, tzinfo=utc), max_length=30, verbose_name='作成者'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='offer',
            name='create_date',
            field=models.DateTimeField(auto_now=True, verbose_name='作成日'),
        ),
        migrations.AddField(
            model_name='offer',
            name='last_modified_by',
            field=models.CharField(default=datetime.datetime(2018, 9, 30, 1, 3, 2, 721254, tzinfo=utc), max_length=30, verbose_name='最終更新者'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='offer',
            name='last_modified_date',
            field=models.DateTimeField(auto_now=True, verbose_name='最終更新日'),
        ),
        migrations.AddField(
            model_name='offer',
            name='pub_time',
            field=models.DateTimeField(null=True, verbose_name='公開日'),
        ),
    ]
