from django.db import models


class TimeStampedModel(models.Model):

    """ Time Stamped Model """

    #auto_now_add = django saves the time when is first created
    #auto_now = django saves the time everytime the model is saved.
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True