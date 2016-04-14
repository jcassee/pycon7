from datetime import datetime, time

from django.db import models
from django.db.models import Q
from django.utils import timezone


class Company(models.Model):
    name = models.CharField(max_length=255)

    class Meta:
        verbose_name_plural = "companies"

    @property
    def ships(self):
        return self.get_ships()

    def get_ships(self, at_time=None):
        if at_time is None: at_time = timezone.now()
        begin = Q(ownerships__begin__lte=at_time)
        end = Q(ownerships__end__gt=at_time) | Q(ownerships__end__isnull=True)
        return Ship.objects.filter(begin, end, ownerships__company=self)

    def __str__(self):
        return self.name


class Ship(models.Model):
    imo = models.PositiveIntegerField(db_index=True, unique=True)
    name = models.CharField(max_length=255)

    @property
    def owner(self):
        return self.get_owner()

    def get_owner(self, at_time=None):
        if at_time is None: at_time = timezone.now()
        begin = Q(begin__lte=at_time)
        end = Q(end__gt=at_time) | Q(end__isnull=True)
        try:
            return self.ownerships.get(begin, end, ship=self).company
        except ShipOwnership.DoesNotExist:
            return None

    def __str__(self):
        return "{} ({})".format(self.name, self.imo)


class ShipOwnership(models.Model):
    company = models.ForeignKey(Company, related_name='ownerships')
    ship = models.ForeignKey(Ship, related_name='ownerships')
    begin = models.DateTimeField()
    end = models.DateTimeField(blank=True, null=True)

    def __str__(self):
        str = "{} owned by {} from {}".format(self.ship, self.company, self.begin)
        if self.end is not None:
            str += " until {}".format(self.end)
        return str
