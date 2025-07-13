from django.db import models


class Producer(models.Model):
    name = models.TextField(max_length=100, unique=True)

    def __str__(self):
        return self.name


class SafetyProducer(models.Model):
    pass


class SafetyResponsible(models.Model):
    pass


class SafetyCertificates(models.Model):
    pass
