# Generated by Django 3.2.12 on 2023-01-01 04:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('apps', '0010_auto_20221210_1524'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='tenant',
            options={'verbose_name': 'Service', 'verbose_name_plural': 'Services'},
        ),
        migrations.AlterField(
            model_name='tenant',
            name='type',
            field=models.CharField(choices=[('personal', 'personal'), ('premium', 'premium'), ('business', 'business')], default='personal', max_length=200),
        ),
    ]
