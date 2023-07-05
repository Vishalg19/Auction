# Generated by Django 4.0.4 on 2022-05-22 11:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bid_app', '0010_product_interval_price_alter_product_endsession'),
    ]

    operations = [
        migrations.AddField(
            model_name='auctionuser',
            name='account_number',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='auctionuser',
            name='adhar_card',
            field=models.FileField(blank=True, null=True, upload_to=''),
        ),
        migrations.AddField(
            model_name='auctionuser',
            name='adhar_number',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='auctionuser',
            name='agree',
            field=models.BooleanField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='auctionuser',
            name='bank_statement',
            field=models.FileField(blank=True, null=True, upload_to=''),
        ),
        migrations.AddField(
            model_name='auctionuser',
            name='pan_card',
            field=models.FileField(blank=True, null=True, upload_to=''),
        ),
        migrations.AddField(
            model_name='auctionuser',
            name='pan_number',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]