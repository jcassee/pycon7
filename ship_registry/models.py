from django.db import models


class Company(models.Model):
    name = models.CharField(max_length=255)

    class Meta:
        verbose_name_plural = "companies"

    def __str__(self):
        return self.name


class Ship(models.Model):
    imo = models.PositiveIntegerField(db_index=True, unique=True)
    name = models.CharField(max_length=255)
    owner = models.ForeignKey(Company, related_name='ships')

    class Meta:
        pass

    def __str__(self):
        return "{} ({})".format(self.name, self.imo)
