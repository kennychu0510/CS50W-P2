# Generated by Django 4.0.2 on 2022-02-19 11:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0010_bidlist_item'),
    ]

    operations = [
        migrations.AddField(
            model_name='auctionlist',
            name='startingPrice',
            field=models.DecimalField(decimal_places=2, max_digits=64, null=True),
        ),
    ]