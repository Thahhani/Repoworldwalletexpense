# Generated by Django 5.1.3 on 2024-12-12 07:39

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('world_wallet_expence_app', '0005_delete_roomprofiletable'),
    ]

    operations = [
        migrations.RenameField(
            model_name='restauranttable',
            old_name='restaurantname',
            new_name='name',
        ),
    ]