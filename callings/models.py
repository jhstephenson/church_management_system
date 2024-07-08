from django.db import models
from django.contrib.auth.models import User

class Unit(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['name']

class Organization(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['name']

class Position(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['name']

class Leadership(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['name']

class Calling(models.Model):
    unit = models.ForeignKey(Unit, on_delete=models.SET_NULL, null=True, blank=True)
    organization = models.ForeignKey(Organization, on_delete=models.SET_NULL, null=True, blank=True)
    position = models.ForeignKey(Position, on_delete=models.SET_NULL, null=True, blank=True)
    person_being_released = models.CharField(max_length=100, blank=True)
    released_by = models.ForeignKey(Leadership, on_delete=models.SET_NULL, null=True, blank=True, related_name='released_by')
    released_date = models.DateField(null=True, blank=True)
    person_being_called = models.CharField(max_length=100)
    home_unit = models.ForeignKey(Unit, on_delete=models.SET_NULL, null=True, blank=True, related_name='home_unit')
    presidency_approved = models.BooleanField(default=False)
    unit_leader_to_be_consulted_by = models.ForeignKey(Leadership, on_delete=models.SET_NULL, null=True, blank=True, related_name='consulted_by')
    leadership_consulted = models.BooleanField(default=False)
    high_council_approved = models.DateField(null=True, blank=True)
    called_by = models.ForeignKey(Leadership, on_delete=models.SET_NULL, null=True, blank=True, related_name='called_by')
    date_called = models.DateField(null=True, blank=True)
    date_sustained = models.DateField(null=True, blank=True)
    date_set_apart = models.DateField(null=True, blank=True)
    leader_and_clerk_resources_updated = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.person_being_called} - {self.position}"

    class Meta:
        ordering = ['unit', 'organization', 'position']