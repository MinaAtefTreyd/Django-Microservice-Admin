# Generated by Django 3.2.7 on 2022-10-11 10:20

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('microservice_admin', '0002_auto_20221011_1009'),
    ]

    operations = [
        migrations.RenameField(
            model_name='adminapps',
            old_name='redirect_url',
            new_name='redirect_path',
        ),
    ]
