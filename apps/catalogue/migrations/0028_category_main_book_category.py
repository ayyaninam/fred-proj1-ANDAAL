# Generated by Django 4.1.7 on 2024-01-10 10:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalogue', '0027_category_show_on_search_menu'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='main_book_category',
            field=models.BooleanField(default=False),
        ),
    ]
