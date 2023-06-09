# Generated by Django 4.2 on 2023-04-06 17:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Game', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='nivel',
            name='den',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='nivel',
            name='num',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='nivel',
            name='respuesta',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='pregunta',
            name='den1',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='pregunta',
            name='den2',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='pregunta',
            name='num1',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='pregunta',
            name='num2',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='pregunta',
            name='operacion',
            field=models.CharField(max_length=1, null=True),
        ),
        migrations.AlterField(
            model_name='pregunta',
            name='texto',
            field=models.CharField(max_length=255, null=True),
        ),
    ]
