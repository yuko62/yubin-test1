# Generated by Django 4.1.7 on 2023-07-21 01:44

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Address",
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
                (
                    "zip_code",
                    models.CharField(blank=True, max_length=8, verbose_name="郵便番号"),
                ),
                (
                    "address1",
                    models.CharField(blank=True, max_length=40, verbose_name="都道府県"),
                ),
                (
                    "address2",
                    models.CharField(blank=True, max_length=40, verbose_name="市区町村番地"),
                ),
                (
                    "address3",
                    models.CharField(blank=True, max_length=40, verbose_name="建物名"),
                ),
            ],
        ),
    ]
