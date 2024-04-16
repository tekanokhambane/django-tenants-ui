# Generated by Django 3.2.12 on 2022-10-17 13:13

from django.db import migrations, models
import tenant_users.permissions.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('apps', '0001_initial'),
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='TenantUser',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('email', models.EmailField(db_index=True, max_length=254, unique=True, verbose_name='Email Address')),
                ('is_active', models.BooleanField(default=True, verbose_name='active')),
                ('is_verified', models.BooleanField(default=False, verbose_name='verified')),
                ('type', models.CharField(choices=[('Admin', 'Admin'), ('Staff', 'Staff'), ('Customer', 'Customer')], default='Admin', max_length=255, verbose_name='Type')),
                ('first_name', models.CharField(blank=True, max_length=300, null=True)),
                ('last_name', models.CharField(blank=True, max_length=300, null=True)),
                ('username', models.CharField(blank=True, max_length=250, null=True)),
                ('signup_confirmation', models.BooleanField(default=False)),
                ('groups', models.ManyToManyField(blank=True, to='auth.Group')),
                ('tenants', models.ManyToManyField(blank=True, help_text='The tenants this user belongs to.', related_name='user_set', to='apps.Tenant', verbose_name='tenants')),
            ],
            options={
                'abstract': False,
            },
            bases=(models.Model, tenant_users.permissions.models.PermissionsMixinFacade),
        ),
        migrations.CreateModel(
            name='Admin',
            fields=[
            ],
            options={
                'proxy': True,
                'indexes': [],
                'constraints': [],
            },
            bases=('users.tenantuser',),
        ),
        migrations.CreateModel(
            name='Customer',
            fields=[
            ],
            options={
                'proxy': True,
                'indexes': [],
                'constraints': [],
            },
            bases=('users.tenantuser',),
        ),
        migrations.CreateModel(
            name='Staff',
            fields=[
            ],
            options={
                'proxy': True,
                'indexes': [],
                'constraints': [],
            },
            bases=('users.tenantuser',),
        ),
    ]
