# Generated by Django 5.1.3 on 2024-12-11 06:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('world_wallet_expence_app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='logintable',
            name='status',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
    ]