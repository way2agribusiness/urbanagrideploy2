# Generated by Django 4.2 on 2024-04-03 04:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appagri', '0023_alter_highlights_options_remove_highlights_text_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='meta_title',
            field=models.CharField(blank=True, choices=[('Terrace Gardening', 'Terrace Gardening'), ('Irrigation Solutions', 'Irrigation Solutions')], max_length=500, null=True),
        ),
    ]
