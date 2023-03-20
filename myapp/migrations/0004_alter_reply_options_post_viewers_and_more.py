# Generated by Django 4.1.6 on 2023-03-17 09:03

from django.conf import settings
from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('myapp', '0003_reply_likes'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='reply',
            options={'ordering': ['-created_at']},
        ),
        migrations.AddField(
            model_name='post',
            name='viewers',
            field=models.ManyToManyField(editable=False, related_name='post_view', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='comment',
            name='created_date',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
        migrations.AlterField(
            model_name='reply',
            name='created_at',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]