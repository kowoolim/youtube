from django.db import models

class Youtube(models.Model):
    In_idx = models.AutoField(primary_key=True)
    view_sub = models.IntegerField(default=0)
    video_nums = models.IntegerField(default=0)
    male = models.IntegerField(default=0)
    multisex = models.IntegerField(default=0)
    contents = models.CharField(max_length=50, null=True, blank=True)



