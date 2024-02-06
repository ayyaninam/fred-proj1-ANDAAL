# Generated by Django 4.1.4 on 2024-02-06 07:17

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        ("base", "0011_alter_mainmenu_redirect_to_link_shippingmethod"),
    ]

    operations = [
        migrations.AlterField(
            model_name="shippingmethod",
            name="charge_excl_tax",
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name="shippingmethod",
            name="charge_incl_tax",
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name="shippingmethod",
            name="child_of",
            field=models.ForeignKey(
                blank=True,
                help_text="If you choose this, then this will become a child (not a parent)",
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                to="base.shippingmethod",
            ),
        ),
        migrations.AlterField(
            model_name="shippingmethod",
            name="code",
            field=models.CharField(
                blank=True,
                help_text="Please don't give any space in this field",
                max_length=250,
                null=True,
            ),
        ),
    ]