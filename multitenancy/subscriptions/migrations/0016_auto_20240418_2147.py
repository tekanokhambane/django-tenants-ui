# Generated by Django 3.2.18 on 2024-04-18 19:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('subscriptions', '0015_alter_plan_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='plan',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
        migrations.AddField(
            model_name='plan',
            name='is_active',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='plan',
            name='updated_at',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
