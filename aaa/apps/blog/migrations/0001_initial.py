# Generated by Django 2.1.3 on 2018-11-08 16:13

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True, help_text='Date and time the post was created')),
                ('updated', models.DateTimeField(auto_now=True, help_text='Date and time the post was last updated')),
                ('publish_date', models.DateTimeField(blank=True, help_text='(optional) If set, when to publish the post', null=True)),
                ('title', models.CharField(help_text='Title of the post', max_length=255)),
                ('content', models.TextField(help_text='Content of the post')),
                ('author', models.ForeignKey(help_text='Author of the post', on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.SlugField(help_text='Tag name', max_length=32, unique=True)),
            ],
        ),
        migrations.AddField(
            model_name='post',
            name='tags',
            field=models.ManyToManyField(help_text='Tags', to='blog.Tag'),
        ),
        migrations.AddField(
            model_name='post',
            name='slug',
            field=models.SlugField(blank=True, help_text='Slug of the post', null=True, unique=True),
        ),
    ]
