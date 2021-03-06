# Generated by Django 3.2.5 on 2022-07-13 22:59

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Visit',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('aum_id', models.CharField(max_length=25)),
                ('username', models.CharField(max_length=255, null=True)),
                ('city', models.CharField(max_length=255, null=True)),
                ('distance', models.IntegerField(null=True)),
                ('age', models.IntegerField(null=True)),
                ('title', models.CharField(max_length=255, null=True)),
                ('measurement', models.CharField(max_length=255, null=True)),
                ('nb_photo', models.IntegerField(null=True)),
                ('desc', models.TextField(blank=True, null=True)),
                ('shopping', models.TextField(blank=True, null=True)),
                ('crack', models.TextField(blank=True, null=True)),
                ('cant_stand', models.TextField(blank=True, null=True)),
                ('popularity', models.IntegerField(null=True)),
                ('hot', models.DecimalField(decimal_places=2, max_digits=3, null=True)),
                ('score', models.IntegerField(null=True)),
                ('date_visit', models.DateTimeField(null=True)),
                ('date_first_visit', models.DateTimeField(null=True)),
                ('full_desc', models.TextField(blank=True, null=True)),
                ('full_shopping', models.TextField(blank=True, null=True)),
            ],
        ),
    ]
