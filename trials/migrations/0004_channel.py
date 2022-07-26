# Generated by Django 4.0.6 on 2022-07-26 08:54

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('trials', '0003_delete_channel_remove_area_areacode_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Channel',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('name', models.CharField(blank=True, default=None, max_length=1000, null=True, verbose_name='CHANNEL NAME')),
                ('price', models.IntegerField(blank=True, default=None, null=True, verbose_name='CHANNEL PRICE')),
                ('number', models.CharField(blank=True, default=None, max_length=1000, null=True, verbose_name='CHANNEL NUMBER')),
            ],
        ),
    ]
