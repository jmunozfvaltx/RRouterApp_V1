#models.py

from django.db import models

class Device(models.Model):
    ip = models.CharField(max_length=20)
    hostname = models.CharField(max_length=100)
    syslog = models.BooleanField() 
    web_access = models.BooleanField()
    ssh = models.BooleanField()
    snmp = models.BooleanField()
    users = models.BooleanField()
    ntp = models.BooleanField() 
    no_telnet = models.BooleanField()
    inactivity = models.BooleanField()
    interfaces = models.BooleanField()
    protocols = models.BooleanField()
    policies = models.BooleanField()
