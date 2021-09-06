# Generated by Django 2.2.24 on 2021-09-01 02:38

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Chemical',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30, verbose_name='Compound name')),
                ('SMILES', models.CharField(max_length=30, verbose_name='SMILES')),
                ('comment', models.TextField(verbose_name='comment')),
                ('boilpoint', models.IntegerField(default=0, verbose_name='b.p.')),
                ('meltingpoint', models.DecimalField(decimal_places=2, max_digits=5, verbose_name='m.p.')),
            ],
        ),
    ]