# Generated by Django 4.0.4 on 2022-05-02 12:48

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0006_product_rename_reviews_review_delete_shop'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='news',
            options={},
        ),
        migrations.AddField(
            model_name='news',
            name='imagenews',
            field=models.ImageField(default=django.utils.timezone.now, upload_to='products/'),
            preserve_default=False,
        ),
    ]
