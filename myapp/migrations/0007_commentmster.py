# Generated by Django 4.1.6 on 2023-03-18 08:11

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('myapp', '0006_alter_post_created_at'),
    ]

    operations = [
        migrations.CreateModel(
            name='Commentmster',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comment_name', models.CharField(max_length=500)),
                ('comment_body', models.TextField()),
                ('created_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('active', models.BooleanField(default=True)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('likes', models.ManyToManyField(blank=True, related_name='LikeComments', to=settings.AUTH_USER_MODEL)),
                ('parent_comment', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='replieses', to='myapp.commentmster')),
                ('post', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Commentmster', to='myapp.post')),
            ],
        ),
    ]
