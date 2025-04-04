# Generated by Django 4.2 on 2023-06-09 09:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appagri', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='subproduct',
            old_name='ftype',
            new_name='product_type',
        ),
        migrations.AlterField(
            model_name='subproduct',
            name='avilability',
            field=models.CharField(choices=[('in_stock', 'In stock'), ('not_available', 'Out of stock')], max_length=255),
        ),
    ]
