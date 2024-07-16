
from django.db import models
from django.db import models
from django.utils import timezone

# Create your models here.
class CalendarEvents(models.Model):

 
    title = models.CharField(max_length=255, null=True, blank =True)
    start = models.DateTimeField(default=timezone.now, null=True, blank =True)
    end = models.DateTimeField(default=timezone.now, null=True, blank =True)
    
    def __str__(self):
        return self.title
    