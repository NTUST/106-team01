from django.db import models
from multiselectfield import MultiSelectField

# Create your models here.
class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')

    def __str__(self):
    	return self.question_text

class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)

    def __str__(self):
    	return self.choice_text

class Store(models.Model):
    store_name = models.CharField(max_length=20)
    # origin = models.CharField(max_length=20)

    def __str__(self):
    	return self.store_name

class Cate(models.Model):
    category = models.CharField(max_length=20)

    def __str__(self):
        return self.category

class Drink(models.Model):
    CATEGORY_CHOICES=(
        ('招牌','招牌'),
        ('茶類','茶類'),
        ('奶茶類','奶茶類'), 
        ('果茶類','果茶類'),
        ('特調茶類','特調茶類'),
        ('抹茶類','抹茶類'),
        ('嚼勁口感類','嚼勁口感類'),
        ('果汁類','果汁類'),
        ('水果類','果汁類'),
        ('奶,果昔類','奶,果昔類'),
        ('鮮奶類','鮮奶類'),
        ('拿鐵類','拿鐵類'),       
    )

    drink_name = models.CharField(max_length=20)
    price = models.DecimalField(max_digits=3, decimal_places=0)
    category = MultiSelectField(choices = CATEGORY_CHOICES)
    store = models.ForeignKey(Store)
    comment = models.CharField(max_length=50, blank=True)
    
    def __str__(self):
        return self.drink_name