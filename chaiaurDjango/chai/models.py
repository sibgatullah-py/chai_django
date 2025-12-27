from django.db import models
from django.utils import timezone

# Create your models here.
class ChaiVarity(models.Model):
    '''
    This is called enums. enums (enumerations) are a way to define a related set of named constant values,
    which can then be used to provide clear, type-safe choices for model fields
    '''
    CHAI_TYPE_CHOICE = [
        ('ML', 'MASALA TEA'),
        ('GR', 'GINGER TEA'),
        ('KL', 'KIWI TEA'),
        ('EL', 'ELACHI TEA'),
        ('PL', 'PLAIN TEA'),
    ]
    
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to='chais/')
    date = models.DateTimeField(default=timezone.now)
    tea_type = models.CharField(max_length=2, choices= CHAI_TYPE_CHOICE)
    description = models.TextField(default='', null=True)


    def __str__(self): # This dunder method is returning the name of the item in the database 
        return self.name