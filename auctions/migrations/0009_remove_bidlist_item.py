# Generated by Django 4.0.2 on 2022-02-19 11:48

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0008_alter_auctionlist_winner'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='bidlist',
            name='item',
        ),
    ]
