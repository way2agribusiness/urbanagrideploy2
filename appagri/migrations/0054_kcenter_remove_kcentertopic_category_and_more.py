# Generated by Django 5.1.6 on 2025-02-26 08:44

import cloudinary.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appagri', '0053_kitcomponent1_subproduct_kitcomponent_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='KCenter',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=500, null=True)),
                ('image', cloudinary.models.CloudinaryField(blank=True, max_length=255, null=True)),
                ('alt', models.CharField(blank=True, default='', max_length=500)),
                ('text1', models.CharField(blank=True, max_length=1000, null=True)),
                ('text2', models.CharField(blank=True, max_length=1000, null=True)),
                ('text3', models.CharField(blank=True, max_length=1000, null=True)),
                ('text4', models.CharField(blank=True, max_length=1000, null=True)),
                ('text5', models.CharField(blank=True, max_length=1000, null=True)),
                ('text6', models.CharField(blank=True, max_length=1000, null=True)),
                ('text7', models.CharField(blank=True, max_length=1000, null=True)),
                ('text8', models.CharField(blank=True, max_length=1000, null=True)),
                ('text9', models.CharField(blank=True, max_length=1000, null=True)),
                ('text10', models.CharField(blank=True, max_length=1000, null=True)),
            ],
            options={
                'verbose_name': 'Enter KCenter Details',
                'verbose_name_plural': 'Enter KCenter Details',
            },
        ),
        migrations.RemoveField(
            model_name='kcentertopic',
            name='category',
        ),
        migrations.RemoveField(
            model_name='kcentertopic',
            name='ktopictext',
        ),
        migrations.AddField(
            model_name='kcentertopic',
            name='alt',
            field=models.CharField(blank=True, max_length=110, null=True),
        ),
        migrations.AddField(
            model_name='kcentertopic',
            name='text1',
            field=models.CharField(blank=True, max_length=1000, null=True),
        ),
        migrations.AddField(
            model_name='kcentertopic',
            name='text2',
            field=models.CharField(blank=True, max_length=1000, null=True),
        ),
        migrations.AddField(
            model_name='kcentertopic',
            name='text3',
            field=models.CharField(blank=True, max_length=1000, null=True),
        ),
        migrations.AddField(
            model_name='kcentertopic',
            name='text4',
            field=models.CharField(blank=True, max_length=1000, null=True),
        ),
        migrations.AddField(
            model_name='kcentertopic',
            name='text5',
            field=models.CharField(blank=True, max_length=1000, null=True),
        ),
        migrations.AddField(
            model_name='kcentertopic',
            name='text6',
            field=models.CharField(blank=True, max_length=1000, null=True),
        ),
        migrations.AddField(
            model_name='kcentertopic',
            name='text7',
            field=models.CharField(blank=True, max_length=1000, null=True),
        ),
        migrations.AddField(
            model_name='kcentertopic',
            name='text8',
            field=models.CharField(blank=True, max_length=1000, null=True),
        ),
        migrations.DeleteModel(
            name='kcentercategories',
        ),
    ]
