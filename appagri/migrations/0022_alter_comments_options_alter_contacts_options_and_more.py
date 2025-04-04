# Generated by Django 4.2 on 2024-02-08 12:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('appagri', '0021_alter_banner_options_alter_blogs_options_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='comments',
            options={'verbose_name': 'q. Get Blogs Comments', 'verbose_name_plural': 'q. Get Blogs Comments'},
        ),
        migrations.AlterModelOptions(
            name='contacts',
            options={'verbose_name': 'r. Get User Messages', 'verbose_name_plural': 'r. Get User Messages'},
        ),
        migrations.AlterModelOptions(
            name='kitcomponent',
            options={'verbose_name': "n. Enter Kit's Product details", 'verbose_name_plural': "n. Enter Kit's Product details"},
        ),
        migrations.AlterModelOptions(
            name='kitcomponentselected',
            options={'verbose_name': 'o. User Selected Kit Products', 'verbose_name_plural': 'o. User Selected Kit Products'},
        ),
        migrations.AlterModelOptions(
            name='product',
            options={'ordering': ['order_no'], 'verbose_name': 'k. Enter Product Categories', 'verbose_name_plural': 'k. Enter Product Categories'},
        ),
        migrations.AlterModelOptions(
            name='review',
            options={'verbose_name': 'p. Get Product Reviews', 'verbose_name_plural': 'p. Get Product Reviews'},
        ),
        migrations.AlterModelOptions(
            name='subproduct',
            options={'verbose_name': 'l. Enter Products', 'verbose_name_plural': 'l. Enter Products'},
        ),
        migrations.AlterModelOptions(
            name='subproduct_external_links',
            options={'verbose_name': 'm. Enter Product SEO Contents', 'verbose_name_plural': 'm. Enter Product SEO Contents'},
        ),
    ]
