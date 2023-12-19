from django.db import models
from django.urls import reverse


# A tuple of 2-tuples
MEALS = (
    ('B', 'Breakfast'),
    ('L', 'Lunch'),
    ('D', 'Dinner')
)
# Create your models here.
class Frog(models.Model):
    # models.CharField are called field types if you want to google others
    name = models.CharField(max_length=100)
    color = models.CharField(max_length=100)
    description = models.TextField(max_length=250)
    age = models.IntegerField()

    def get_absolute_url(self):
        return reverse('detail', kwargs={'frog_id': self.id})

class Feeding(models.Model):
  date = models.DateField('feeding date')
  meal = models.CharField(
    max_length=1,
	 choices=MEALS,
	 default=MEALS[0][0]
  )
  # Create a Frog_id FK
  frog = models.ForeignKey(Frog, on_delete=models.CASCADE)

  def __str__(self):
    return f"{self.get_meal_display()} on {self.date}"
  
