# Generated by Django 5.1.3 on 2024-12-13 08:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('world_wallet_expence_app', '0006_rename_restaurantname_restauranttable_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='roomtable',
            name='roomservice',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
    ]
