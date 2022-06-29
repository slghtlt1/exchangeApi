from django.db import models

class GetData(models.Model):
   open_Timee = models.CharField(max_length=100, null=True, blank=True)
   close_Time = models.CharField(max_length=100, null=True, blank=True)
   open_Field = models.CharField(max_length=100, null=True, blank=True)
   close_Field = models.CharField(max_length=100, null=True, blank=True)
   high_Field = models.CharField(max_length=100, null=True, blank=True)
   low_Field = models.CharField(max_length=100, null=True, blank=True)
   volume_Field = models.CharField(max_length=100, null=True, blank=True)
   count_Field = models.CharField(max_length=100, null=True, blank=True)
   sum_Field = models.IntegerField(null=True, blank=True)



