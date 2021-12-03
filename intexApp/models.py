# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class PdDrugs(models.Model):
    drugid = models.IntegerField(primary_key=True)
    drugname = models.CharField(max_length=30)
    isopioid = models.CharField(max_length=5)

    class Meta:
        #managed = False
        db_table = 'pd_drugs'


class PdPrescriber(models.Model):
    npi = models.IntegerField(primary_key=True)
    fname = models.CharField(max_length=11)
    lname = models.CharField(max_length=11)
    gender = models.CharField(max_length=1)
    state = models.CharField(max_length=2)
    specialty = models.CharField(max_length=62)
    isopioidprescriber = models.CharField(max_length=5)
    totalprescriptions = models.IntegerField()

    class Meta:
        #managed = False
        db_table = 'pd_prescriber'


class PdPrescribersCredentials(models.Model):
    npi = models.IntegerField(primary_key=True)
    credentials = models.CharField(max_length=20)

    class Meta:
        #managed = False
        db_table = 'pd_prescribers_credentials'
        unique_together = (('npi', 'credentials'),)


class PdStatedata(models.Model):
    state = models.CharField(primary_key=True, max_length=14)
    stateabbrev = models.CharField(max_length=2)
    population = models.IntegerField()
    deaths = models.IntegerField()

    class Meta:
        #managed = False
        db_table = 'pd_statedata'


class PdTriple(models.Model):
    id = models.IntegerField(primary_key=True)
    prescriberid = models.IntegerField()
    drugname = models.CharField(max_length=30)
    qty = models.IntegerField()

    class Meta:
        #managed = False
        db_table = 'pd_triple'
