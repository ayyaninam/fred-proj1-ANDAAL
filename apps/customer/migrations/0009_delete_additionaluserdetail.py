# Generated by Django 4.1.4 on 2024-02-16 02:17

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("customer", "0008_additionaluserdetail"),
    ]

    operations = [
        migrations.DeleteModel(
            name="AdditionalUserDetail",
        ),
    ]
