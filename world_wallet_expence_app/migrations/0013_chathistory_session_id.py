# Generated by Django 5.1.3 on 2025-01-15 09:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('world_wallet_expence_app', '0012_remove_chathistory_session_id_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='chathistory',
            name='session_id',
            field=models.CharField(default=23, max_length=255),
            preserve_default=False,
        ),
    ]
