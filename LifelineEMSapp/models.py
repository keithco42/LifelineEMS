from datetime import datetime, timedelta

from django.db import models


class Content(models.Model):
    value = models.TextField(max_length=1000)
    priority = models.IntegerField()
    dtime = models.DateTimeField("Timestamp", default=datetime.now() + timedelta(hours=8))
    phash = models.CharField("Hash", max_length=4)
    red = models.IntegerField(default=0)
    green = models.IntegerField(default=0)
    blue = models.IntegerField(default=0)
    speed = models.IntegerField(default=0)

    def __str__(self):
        return "Content {}".format(self.phash + " " + self.value + " Priority: " + str(self.priority))