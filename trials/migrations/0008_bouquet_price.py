# Generated by Django 4.0.6 on 2022-07-26 09:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('trials', '0007_subscription_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='bouquet',
            name='price',
            field=models.IntegerField(blank=True, default=None, null=True, verbose_name='CHANNEL PRICE'),
        ),
    ]
