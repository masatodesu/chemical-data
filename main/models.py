from django.db import models



class Chemical(models.Model):
    name = models.CharField(
        verbose_name='Compound name',
        max_length=30
    )

    SMILES = models.CharField(
        verbose_name ='SMILES',
        max_length=30
    )

    comment = models.TextField(
        verbose_name = 'comment'
    )

    boilingpoint = models.DecimalField(
        verbose_name = 'b.p.(K)',
        max_digits = 5,
        decimal_places =2,
        default = 0
    )

    meltingpoint = models.DecimalField(
        verbose_name = 'm.p.(K)',
        max_digits = 5,
        decimal_places =2,
        default = 0

    )

    def __str__(self):
        return f'{self.name}'

