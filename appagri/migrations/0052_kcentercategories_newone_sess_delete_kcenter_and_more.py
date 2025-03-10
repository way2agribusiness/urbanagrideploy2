# Generated by Django 5.1.5 on 2025-01-30 06:58

import cloudinary.models
import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appagri', '0051_alter_kitcomponent1_component_image_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='kcentercategories',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('categories', models.CharField(max_length=200)),
                ('categoriesslug', models.SlugField(blank=True, null=True, unique=True)),
            ],
            options={
                'verbose_name': 'Enter KCenter Category',
                'verbose_name_plural': 'Enter KCenter Category',
            },
        ),
        migrations.CreateModel(
            name='Newone',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('number', models.IntegerField()),
                ('place', models.CharField(blank=True, max_length=30, null=True)),
                ('message', models.CharField(blank=True, max_length=40, null=True)),
                ('email', models.EmailField(max_length=50)),
                ('date', models.DateField(auto_now=True)),
                ('course', models.CharField(choices=[('python', 'python'), ('sql', 'sql'), ('django', 'django')], default='python', max_length=20)),
            ],
            options={
                'verbose_name': 'New data',
                'verbose_name_plural': 'New data',
            },
        ),
        migrations.CreateModel(
            name='sess',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=30, null=True)),
            ],
            options={
                'verbose_name': 'session_data',
                'verbose_name_plural': 'session_data',
            },
        ),
        migrations.DeleteModel(
            name='KCenter',
        ),
        migrations.RemoveField(
            model_name='kitcomponentselected',
            name='kit',
        ),
        migrations.RemoveField(
            model_name='subproduct_external_links',
            name='subproduct',
        ),
        migrations.RemoveField(
            model_name='kcentertopic',
            name='text1',
        ),
        migrations.RemoveField(
            model_name='kcentertopic',
            name='text2',
        ),
        migrations.RemoveField(
            model_name='kcentertopic',
            name='text3',
        ),
        migrations.RemoveField(
            model_name='kcentertopic',
            name='text4',
        ),
        migrations.RemoveField(
            model_name='kcentertopic',
            name='text5',
        ),
        migrations.RemoveField(
            model_name='kcentertopic',
            name='text6',
        ),
        migrations.RemoveField(
            model_name='kcentertopic',
            name='text7',
        ),
        migrations.RemoveField(
            model_name='kcentertopic',
            name='text8',
        ),
        migrations.RemoveField(
            model_name='subproduct',
            name='Highlight_image1',
        ),
        migrations.RemoveField(
            model_name='subproduct',
            name='Highlight_image2',
        ),
        migrations.RemoveField(
            model_name='subproduct',
            name='Highlight_image3',
        ),
        migrations.RemoveField(
            model_name='subproduct',
            name='background_gif',
        ),
        migrations.RemoveField(
            model_name='subproduct',
            name='date',
        ),
        migrations.RemoveField(
            model_name='subproduct',
            name='exclusive_highlight_text',
        ),
        migrations.RemoveField(
            model_name='subproduct',
            name='exclusive_img',
        ),
        migrations.RemoveField(
            model_name='subproduct',
            name='exclusive_img_alt',
        ),
        migrations.RemoveField(
            model_name='subproduct',
            name='image',
        ),
        migrations.RemoveField(
            model_name='subproduct',
            name='pinfo',
        ),
        migrations.RemoveField(
            model_name='subproduct',
            name='sub_category_name',
        ),
        migrations.RemoveField(
            model_name='subproduct',
            name='text1',
        ),
        migrations.RemoveField(
            model_name='subproduct',
            name='text2',
        ),
        migrations.RemoveField(
            model_name='subproduct',
            name='text3',
        ),
        migrations.AddField(
            model_name='kcentertopic',
            name='ktopictext',
            field=models.TextField(null=True),
        ),
        migrations.AlterField(
            model_name='kitcomponent1',
            name='component_image',
            field=cloudinary.models.CloudinaryField(max_length=255),
        ),
        migrations.AlterField(
            model_name='product1',
            name='spimage',
            field=models.ImageField(null=True, upload_to=''),
        ),
        migrations.AlterField(
            model_name='sub_cat',
            name='Highlight_image1',
            field=models.ImageField(null=True, upload_to=''),
        ),
        migrations.AlterField(
            model_name='sub_cat',
            name='Highlight_image2',
            field=models.ImageField(null=True, upload_to=''),
        ),
        migrations.AlterField(
            model_name='sub_cat',
            name='Highlight_image3',
            field=models.ImageField(null=True, upload_to=''),
        ),
        migrations.AlterField(
            model_name='sub_cat',
            name='exclusive_img',
            field=models.ImageField(null=True, upload_to=''),
        ),
        migrations.AlterField(
            model_name='sub_cat',
            name='image',
            field=models.ImageField(null=True, upload_to=''),
        ),
        migrations.AddField(
            model_name='kcentertopic',
            name='category',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='appagri.kcentercategories'),
        ),
        migrations.DeleteModel(
            name='KitComponent',
        ),
        migrations.DeleteModel(
            name='KitComponentSelected',
        ),
        migrations.DeleteModel(
            name='Subproduct_External_links',
        ),
    ]
