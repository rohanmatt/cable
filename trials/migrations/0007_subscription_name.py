# Generated by Django 4.0.6 on 2022-07-26 09:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('trials', '0006_plans_subscription'),
    ]

    operations = [
        migrations.AddField(
            model_name='subscription',
            name='name',
            field=models.CharField(blank=True, default=None, max_length=1000, null=True, verbose_name=' NAME'),
        ),
    ]