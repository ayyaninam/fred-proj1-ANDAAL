# Generated by Django 4.1.4 on 2024-03-03 07:14

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    initial = True

    dependencies = [
        ("catalogue", "0028_category_main_book_category"),
    ]

    operations = [
        migrations.CreateModel(
            name="CultureCategory",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=255, unique=True)),
                ("default", models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name="EducationCategory",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=255, unique=True)),
                ("default", models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name="RateOfEuro",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("base", models.CharField(blank=True, max_length=200, null=True)),
                (
                    "date",
                    models.DateField(default=datetime.date.today, verbose_name="Date"),
                ),
                ("xaf_to_euro", models.FloatField()),
            ],
            options={
                "ordering": ["-date"],
            },
        ),
        migrations.CreateModel(
            name="TextbookClasses",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=255)),
                (
                    "products_category",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="catalogue.category",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="TextbookLanguages",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=255, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name="TextbooksCategories",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=255, unique=True)),
                ("child_classes", models.ManyToManyField(to="base.textbookclasses")),
                (
                    "language_associated",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="base.textbooklanguages",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="MainMenu",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=200)),
                (
                    "icons_link",
                    models.TextField(
                        blank=True,
                        help_text='Please go to the link: fonts.google.com/icons and attach the code which is under the "Inserting the icon" menu after slecting the icon.',
                        max_length=200,
                        null=True,
                    ),
                ),
                (
                    "redirect_to_link",
                    models.CharField(
                        blank=True,
                        help_text='Please write the url like /abc/abc/1, do not include any domain or IP address before the URL. This url will redirect users to this LINK. Please keep it blank if you want to attached any category to the main menu and select the category in below field(name "Category Attached")',
                        max_length=1000,
                        null=True,
                    ),
                ),
                (
                    "category_attached",
                    models.ForeignKey(
                        blank=True,
                        help_text="Please choose the Category if you don't attach any redirect link, if you will attach the both, priority will be for Category field.",
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        to="catalogue.category",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Education",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("title", models.CharField(max_length=250)),
                ("short_description", models.TextField()),
                (
                    "cover_image",
                    models.ImageField(
                        blank=True, null=True, upload_to="base/education_cover/"
                    ),
                ),
                ("description", models.TextField()),
                ("date", models.DateField(auto_now=True)),
                ("location", models.CharField(blank=True, max_length=255, null=True)),
                ("link_to_orignal", models.URLField(max_length=1000)),
                ("category", models.ManyToManyField(to="base.educationcategory")),
            ],
        ),
        migrations.CreateModel(
            name="Culture",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("title", models.CharField(max_length=250)),
                ("short_description", models.TextField()),
                (
                    "cover_image",
                    models.ImageField(
                        blank=True, null=True, upload_to="base/culture_cover/"
                    ),
                ),
                ("description", models.TextField()),
                ("date", models.DateField(auto_now=True)),
                ("location", models.CharField(blank=True, max_length=255, null=True)),
                ("link_to_orignal", models.URLField(max_length=1000)),
                ("category", models.ManyToManyField(to="base.culturecategory")),
            ],
        ),
    ]
