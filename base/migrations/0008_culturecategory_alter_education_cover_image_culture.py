# Generated by Django 4.1.7 on 2024-01-10 09:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0007_alter_educationcategory_default'),
    ]

    operations = [
        migrations.CreateModel(
            name='CultureCategory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, unique=True)),
                ('default', models.BooleanField(default=False)),
            ],
        ),
        migrations.AlterField(
            model_name='education',
            name='cover_image',
            field=models.ImageField(blank=True, null=True, upload_to='base/education_cover/'),
        ),
        migrations.CreateModel(
            name='Culture',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=250)),
                ('short_description', models.TextField()),
                ('cover_image', models.ImageField(blank=True, null=True, upload_to='base/culture_cover/')),
                ('description', models.TextField()),
                ('date', models.DateField(auto_now=True)),
                ('location', models.CharField(blank=True, max_length=255, null=True)),
                ('link_to_orignal', models.URLField(max_length=1000)),
                ('category', models.ManyToManyField(to='base.culturecategory')),
            ],
        ),
    ]
