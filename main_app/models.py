from django.db import models
from django.urls import reverse
from datetime import date

# Create your models here.

class Tag(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name

class Restaurant(models.Model):
  name = models.CharField(max_length=100)
  type = models.CharField(max_length=100)
  review = models.TextField(max_length=250)
  stars = models.IntegerField()
  tags = models.ManyToManyField(Tag)

  def __str__(self):
    return self.name
  def get_absolute_url(self):
    return reverse('detail', kwargs={'restaurant_id': self.id})
  
  
class YourOrder(models.Model):
  date = models.DateField('Date you went')
  item = models.CharField(max_length=50)
  restaurant = models.ForeignKey(Restaurant, on_delete=models.CASCADE)

  def __str__(self):
        return f"{self.item}"
  class Meta:
    ordering = ['-date']
  
 