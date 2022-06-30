# Generated by Django 4.0.4 on 2022-04-26 12:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0005_news_shop'),
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=15)),
                ('description', models.TextField()),
                ('price', models.PositiveIntegerField()),
                ('image', models.ImageField(upload_to='products/')),
            ],
        ),
        migrations.RenameModel(
            old_name='Reviews',
            new_name='Review',
        ),
        migrations.DeleteModel(
            name='Shop',
        ),
    ]
