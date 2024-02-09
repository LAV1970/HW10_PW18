# Generated by Django 5.0.1 on 2024-02-09 18:46

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('quotes', '0003_author_age_author_book'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, unique=True)),
            ],
        ),
        migrations.AddField(
            model_name='quote',
            name='content',
            field=models.TextField(default=''),
        ),
        migrations.AddField(
            model_name='quote',
            name='user',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.RemoveField(
            model_name='quote',
            name='tags',
        ),
        migrations.AddField(
            model_name='quote',
            name='tags',
            field=models.ManyToManyField(to='quotes.tag'),
        ),
    ]
