from django.db import models
from phone.models import Contact
from model_utils.models import TimeStampedModel
from json_field import JSONField

class Device(models.Model):
    """
    A device may be a physical sensor device, or it may be a unique
    virtual sensor, likely identified partly by the physical computer
    it lives on.
    """
    id = models.CharField(max_length=100, primary_key=True)
    owner = models.ForeignKey(Contact, null=True)

class SensedEvent(TimeStampedModel):
    """
    A SensedEvent may be a raw sensor reading or it may be a more abstract
    event, e.g. fire, flood, etc.
    """
    #TODO:
    #class Meta:
        #abstract = True

    device = models.ForeignKey(Device)
    type = models.CharField(max_length=100)
    #TODO: self.priority = priority
    data = JSONField()
