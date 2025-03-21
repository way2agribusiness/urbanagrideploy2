# Generated by Django 4.2 on 2024-02-07 05:13

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('appagri', '0019_alter_banner_options_alter_blogs_options_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='banner',
            options={'verbose_name': 's3. Upload Banner Images', 'verbose_name_plural': 'a3. Upload Banner Images'},
        ),
        migrations.AlterModelOptions(
            name='blogs',
            options={'verbose_name': 'a9. Enter Blogs', 'verbose_name_plural': 'a9. Enter Blogs'},
        ),
        migrations.AlterModelOptions(
            name='brands',
            options={'verbose_name': 'a7. Upload Collaboration Images', 'verbose_name_plural': 'a7. Upload Collaboration Images'},
        ),
        migrations.AlterModelOptions(
            name='credentials',
            options={'verbose_name': 'a8. Upload Credential Images', 'verbose_name_plural': 'a8. Upload Credential Images'},
        ),
        migrations.AlterModelOptions(
            name='highlights',
            options={'verbose_name': 'a4. Upload Website Highlights', 'verbose_name_plural': 'a4. Upload Website Highlights'},
        ),
        migrations.AlterModelOptions(
            name='home_information',
            options={'verbose_name': 'a5. Upload Website Info & Images', 'verbose_name_plural': 'a5. Upload Website Info & Images'},
        ),
        migrations.AlterModelOptions(
            name='kcenter',
            options={'verbose_name': 'a10. Enter K Center Data', 'verbose_name_plural': 'a10. Enter K Center Data'},
        ),
        migrations.AlterModelOptions(
            name='logo',
            options={'verbose_name': 'a2. Upload Website Logo Image', 'verbose_name_plural': 'a3. Upload Website Logo Image'},
        ),
        migrations.AlterModelOptions(
            name='seopageextlinks',
            options={'verbose_name': 'a1. Enter SEO Contents', 'verbose_name_plural': 'a1. Enter SEO Contents'},
        ),
        migrations.AlterModelOptions(
            name='webinfo',
            options={'verbose_name': 'a6. Enter Our Brand Details', 'verbose_name_plural': 'a6. Enter Our Brand Details'},
        ),
    ]
