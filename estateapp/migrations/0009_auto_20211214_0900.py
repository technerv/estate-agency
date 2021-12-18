# Generated by Django 3.2.9 on 2021-12-14 09:00

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('estateapp', '0008_delete_agtuser'),
    ]

    operations = [
        migrations.AddField(
            model_name='agent',
            name='description',
            field=models.TextField(default=1, verbose_name='Agent Description'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='agent',
            name='email',
            field=models.EmailField(default=1, max_length=254, verbose_name='Email Address'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='agent',
            name='name',
            field=models.CharField(default=1, max_length=60, verbose_name='Agent Name'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='agent',
            name='phone',
            field=models.IntegerField(default=1, verbose_name='Phone Number'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='agent',
            name='user',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='agentuser', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='property',
            name='user',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='agent', to=settings.AUTH_USER_MODEL),
        ),
    ]
