# Generated by Django 2.2.6 on 2019-10-20 16:47

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('projectapp', '0002_auto_20190930_0737'),
    ]

    operations = [
        migrations.RenameField(
            model_name='studentformsave',
            old_name='applicant_name',
            new_name='studentformsave',
        ),
        migrations.CreateModel(
            name='viewtype',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_Type', models.CharField(default='student', max_length=30)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='worktype', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
