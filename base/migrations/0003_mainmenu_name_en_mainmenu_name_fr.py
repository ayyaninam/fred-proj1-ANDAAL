# Generated by Django 4.1.4 on 2024-04-16 17:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0002_shippingmethod_countries'),
    ]

    operations = [
        migrations.AddField(
            model_name='mainmenu',
            name='name_en',
            field=models.CharField(max_length=200, null=True, verbose_name='name'),
        ),
        migrations.AddField(
            model_name='mainmenu',
            name='name_fr',
            field=models.CharField(max_length=200, null=True, verbose_name='name'),
        ),
    ]
