# Generated by Django 4.1.4 on 2024-04-16 18:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0005_mainmenu_order'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mainmenu',
            name='order',
            field=models.SmallIntegerField(blank=True, null=True),
        ),
    ]