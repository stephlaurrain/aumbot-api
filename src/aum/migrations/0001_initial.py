# Generated by Django 3.2.5 on 2022-07-14 17:13

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Ban',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('aum_id', models.CharField(max_length=25)),
                ('done', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='Charm',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('aum_id', models.CharField(max_length=25)),
                ('date_charm', models.DateTimeField(null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('aum_id', models.CharField(max_length=25)),
            ],
        ),
        migrations.CreateModel(
            name='Distance',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('city', models.CharField(max_length=100)),
                ('km', models.IntegerField(null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Favorite',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('aum_id', models.CharField(max_length=25)),
            ],
        ),
        migrations.CreateModel(
            name='Keyword',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('word', models.CharField(max_length=25)),
                ('weight', models.IntegerField(null=True)),
            ],
        ),
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
                ('description', models.TextField(blank=True, null=True)),
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
