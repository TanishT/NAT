# Generated by Django 3.1.2 on 2021-01-13 00:47

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('gui', '0005_auto_20210112_1642'),
    ]

    operations = [
        migrations.RenameField(
            model_name='note',
            old_name='ProviderTitleDSC',
            new_name='LicenseDisplayDSC',
        ),
    ]
