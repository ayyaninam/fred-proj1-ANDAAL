# Generated by Django 4.1.4 on 2024-01-24 17:22

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("base", "0009_mainmenu"),
    ]

    operations = [
        migrations.AlterField(
            model_name="mainmenu",
            name="icons_link",
            field=models.TextField(
                blank=True,
                help_text='Please go to the link: fonts.google.com/icons and attach the code which is under the "Inserting the icon" menu after slecting the icon.',
                max_length=200,
                null=True,
            ),
        ),
        migrations.AlterField(
            model_name="mainmenu",
            name="redirect_to_link",
            field=models.CharField(
                help_text='Please write the url like /abc/abc/1, do not include any domain or IP address before the URL. This url will redirect users to this LINK. Please keep it blank if you want to attached any category to the main menu and select the category in below field(name "Category Attached")',
                max_length=1000,
                null=True,
            ),
        ),
    ]