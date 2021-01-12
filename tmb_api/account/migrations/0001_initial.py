# Generated by Django 3.1.5 on 2021-01-12 16:28

from django.conf import settings
import django.contrib.auth.validators
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='Account',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('username', models.CharField(error_messages={'unique': 'A user with that username already exists.'}, help_text='Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.', max_length=150, unique=True, validators=[django.contrib.auth.validators.UnicodeUsernameValidator()], verbose_name='username')),
                ('email', models.EmailField(blank=True, db_index=True, max_length=255, null=True, verbose_name='Email address')),
                ('code', models.CharField(db_index=True, default=None, max_length=32)),
                ('title', models.CharField(blank=True, max_length=64)),
                ('first_name', models.CharField(blank=True, db_index=True, max_length=120)),
                ('middle_name', models.CharField(blank=True, db_index=True, max_length=120)),
                ('last_name', models.CharField(blank=True, db_index=True, max_length=120)),
                ('id_card', models.CharField(blank=True, max_length=255, null=True)),
                ('department', models.CharField(blank=True, default='', max_length=255, null=True)),
                ('salary', models.CharField(db_index=True, max_length=255)),
                ('phone', models.CharField(db_index=True, max_length=10)),
                ('is_active', models.BooleanField(db_index=True, default=True)),
                ('is_admin', models.BooleanField(default=False)),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date joined')),
                ('datetime_create', models.DateTimeField(auto_now_add=True, db_index=True)),
                ('datetime_update', models.DateTimeField(auto_now=True, db_index=True)),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.Group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.Permission', verbose_name='user permissions')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Session',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('session_key', models.CharField(db_index=True, max_length=255)),
                ('token', models.TextField(blank=True, null=True)),
                ('datetime_create', models.DateTimeField(auto_now_add=True, db_index=True)),
                ('account', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='+', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='MemberType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.IntegerField(choices=[(1, 'Silver'), (2, 'Gold'), (3, 'Platinum'), (9001, 'hyper_diamond')], default=1)),
                ('datetime_create', models.DateTimeField(auto_now_add=True, db_index=True)),
                ('datetime_update', models.DateTimeField(auto_now=True, db_index=True)),
                ('account', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]