# Generated by Django 4.2.5 on 2023-09-07 15:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vendorapp', '0002_alter_consignment_consignment_id'),
    ]

    operations = [
        migrations.CreateModel(
            name='Vendor_Account',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('vendor_name', models.CharField(max_length=200)),
                ('vendor_address', models.CharField(max_length=50)),
                ('vendor_contact1', models.CharField(max_length=10)),
                ('vendor_contact2', models.CharField(max_length=10)),
                ('vendor_id', models.CharField(blank=True, max_length=20, null=True, unique=True)),
            ],
        ),
    ]