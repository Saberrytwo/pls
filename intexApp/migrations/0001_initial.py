# Generated by Django 3.2.8 on 2021-12-03 00:47

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='PdDrugs',
            fields=[
                ('drugid', models.IntegerField(primary_key=True, serialize=False)),
                ('drugname', models.CharField(max_length=30)),
                ('isopioid', models.CharField(max_length=5)),
            ],
            options={
                'db_table': 'pd_drugs',
            },
        ),
        migrations.CreateModel(
            name='PdPrescriber',
            fields=[
                ('npi', models.IntegerField(primary_key=True, serialize=False)),
                ('fname', models.CharField(max_length=11)),
                ('lname', models.CharField(max_length=11)),
                ('gender', models.CharField(max_length=1)),
                ('state', models.CharField(max_length=2)),
                ('specialty', models.CharField(max_length=62)),
                ('isopioidprescriber', models.CharField(max_length=5)),
                ('totalprescriptions', models.IntegerField()),
            ],
            options={
                'db_table': 'pd_prescriber',
            },
        ),
        migrations.CreateModel(
            name='PdStatedata',
            fields=[
                ('state', models.CharField(max_length=14, primary_key=True, serialize=False)),
                ('stateabbrev', models.CharField(max_length=2)),
                ('population', models.IntegerField()),
                ('deaths', models.IntegerField()),
            ],
            options={
                'db_table': 'pd_statedata',
            },
        ),
        migrations.CreateModel(
            name='PdTriple',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('prescriberid', models.IntegerField()),
                ('drugname', models.CharField(max_length=30)),
                ('qty', models.IntegerField()),
            ],
            options={
                'db_table': 'pd_triple',
            },
        ),
        migrations.CreateModel(
            name='PdPrescribersCredentials',
            fields=[
                ('npi', models.IntegerField(primary_key=True, serialize=False)),
                ('credentials', models.CharField(max_length=20)),
            ],
            options={
                'db_table': 'pd_prescribers_credentials',
                'unique_together': {('npi', 'credentials')},
            },
        ),
    ]