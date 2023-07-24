from django.db import models

class Address(models.Model):
    zip_code = models.CharField(
        verbose_name='郵便番号', max_length=8, blank=True,
    )

    address1 = models.CharField(
        verbose_name='都道府県', max_length=40, blank=True,
    )

    address2 = models.CharField(
        verbose_name='市区町村番地', max_length=40, blank=True,
    )

    address3 = models.CharField(
        verbose_name='建物名', max_length=40, blank=True,
    )

    