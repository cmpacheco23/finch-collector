from django.db import models
from django.urls import reverse
from datetime import date

# Create your models here.
TIMING = (
  ('M', 'Morning'),
  ('A', 'Afternoon'),
  ('E', 'Evening')
)

class Bowl(models.Model):
  size = models.CharField(max_length=50)
  color = models.CharField(max_length=20)
  
  def __str__(self):
      return self.name
  
  def get_absolute_url(self):
      return reverse("bowl-detail", kwargs={"pk": self.id})
  
class Dog(models.Model):
  name = models.CharField(max_length=100)
  breed = models.CharField(max_length=100)
  description = models.TextField(max_length=250)
  age = models.IntegerField()
  bowls = models.ManyToManyField(Bowl)

  def __str__(self):
      return self.name
  
  def get_absolute_url(self):
      return reverse("dog-detail", kwargs={"dog_id": self.id})
  
  def walked_for_today(self):
    return self.walk_set.filter(date=date.today()).count() >= len(TIMING)

class Walk(models.Model):
  date = models.DateField('Walk Date')
  timing = models.CharField(max_length=1, choices=TIMING, default=TIMING[0][0])

  dog = models.ForeignKey(Dog, on_delete=models.CASCADE)

  def __str__(self):
    return f"{self.get_timing_display()} on {self.date}"
  
  class Meta:
    ordering = ['-date']