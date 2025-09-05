from django.db import models
from django.utils import timezone
class ChaiVaraity(models.Model):
    CHAI_TYPE_CHOICE = [ # a list (array) of tuples. Each tuple represents a choice, with a value and a human-readable name.
        ('PL', 'PLAIN'),
        ('GI', 'GINGER'),
        ('ML', 'MASALA'),
        ('GR', 'GREEN'),
        ('KL', 'KIWI'),
        ('LE', 'LEMON'),
    ]
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to='chais/', blank=True, null=True)
    date_added = models.DateTimeField(default=timezone.now)# adding the time when the model was added in database
    type = models.CharField(max_length=2,choices=CHAI_TYPE_CHOICE)\
        
        
        
    def __str__(self):
        return self.name # dunder method . this will show the name of the objects we are creating in the database
    
