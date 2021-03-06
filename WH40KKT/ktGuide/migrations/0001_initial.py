# Generated by Django 3.0.6 on 2020-07-14 21:04

from django.conf import settings
import django.contrib.auth.models
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0011_update_proxy_permissions'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('first_name', models.CharField(blank=True, max_length=30, verbose_name='first name')),
                ('last_name', models.CharField(blank=True, max_length=150, verbose_name='last name')),
                ('is_staff', models.BooleanField(default=False, help_text='Designates whether the user can log into this admin site.', verbose_name='staff status')),
                ('is_active', models.BooleanField(default=True, help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.', verbose_name='active')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date joined')),
                ('username', models.CharField(max_length=26, unique=True)),
                ('email', models.EmailField(max_length=100, unique=True, verbose_name='email address')),
                ('admin', models.BooleanField(default=False)),
                ('bio', models.CharField(default='Bio goes here', max_length=800)),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.Group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.Permission', verbose_name='user permissions')),
            ],
            options={
                'verbose_name': 'user',
                'verbose_name_plural': 'users',
                'abstract': False,
            },
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.CreateModel(
            name='Ability',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('description', models.CharField(max_length=1000)),
            ],
        ),
        migrations.CreateModel(
            name='Army',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('bio', models.CharField(max_length=1000)),
            ],
        ),
        migrations.CreateModel(
            name='Guide',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(default='Title', max_length=100)),
                ('guide_desc', models.CharField(default='stuff goes here', max_length=10000)),
                ('point_value', models.IntegerField(default=0)),
                ('votes', models.IntegerField(default=0)),
                ('date_created', models.DateTimeField()),
                ('army', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ktGuide.Army')),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Specialist',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Weapon',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('weapon_range', models.CharField(max_length=50)),
                ('weapon_type', models.CharField(max_length=50)),
                ('s', models.CharField(max_length=50)),
                ('ap', models.CharField(max_length=50)),
                ('d', models.CharField(max_length=50)),
                ('abilities', models.CharField(max_length=1000)),
                ('pts', models.IntegerField()),
                ('army', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='ktGuide.Army')),
            ],
        ),
        migrations.CreateModel(
            name='Unit',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('m', models.IntegerField()),
                ('ws', models.IntegerField()),
                ('bs', models.IntegerField()),
                ('s', models.IntegerField()),
                ('t', models.IntegerField()),
                ('w', models.IntegerField()),
                ('a', models.IntegerField()),
                ('ld', models.IntegerField()),
                ('sv', models.IntegerField()),
                ('max_units', models.CharField(max_length=50)),
                ('point_value', models.IntegerField()),
                ('ability_list', models.ManyToManyField(related_name='ability', to='ktGuide.Ability')),
                ('army', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='ktGuide.Army')),
                ('specialist_list', models.ManyToManyField(related_name='specialist', to='ktGuide.Specialist')),
                ('weapons_list', models.ManyToManyField(related_name='weapon', to='ktGuide.Weapon')),
            ],
        ),
        migrations.CreateModel(
            name='GuideUnit',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('guide', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ktGuide.Guide')),
                ('role', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='ktGuide.Specialist')),
                ('unit', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='ktGuide.Unit')),
                ('weapon', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='ktGuide.Weapon')),
            ],
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.CharField(max_length=500)),
                ('date_created', models.DateTimeField()),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('guide', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ktGuide.Guide')),
            ],
        ),
    ]
