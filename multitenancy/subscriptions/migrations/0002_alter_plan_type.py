# Generated by Django 3.2.12 on 2022-11-13 05:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('subscriptions', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='plan',
            name='type',
            field=models.CharField(choices=[('public', 'public'), ('personal', 'personal'), ('premium', 'premium'), ('business', 'business')], max_length=250),
        ),
    ]
