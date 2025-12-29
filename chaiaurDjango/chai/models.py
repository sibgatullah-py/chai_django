from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User # default user model form django 

# Create your models here.
class ChaiVarity(models.Model):
    '''
    This is called enums. enums (enumerations) are a way to define a related set of named constant values,
    which can then be used to provide clear, type-safe choices for model fields
    '''
    CHAI_TYPE_CHOICE = [
        ('MLT', 'MASALA TEA'),
        ('GRT', 'GINGER TEA'),
        ('KLT', 'KIWI TEA'),
        ('ELT', 'ELACHI TEA'),
        ('GT', 'GREEN TEA'),
        ('BLT', 'BLACK TEA'),
        ('HET', 'HERBAL TEA'),
        ('MLT', 'MILK TEA'),
    ]
    
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to='chais/')
    date = models.DateTimeField(default=timezone.now)
    tea_type = models.CharField(max_length=5, choices= CHAI_TYPE_CHOICE)
    description = models.TextField(default='', null=True)
    price = models.IntegerField(default=0,null=False)


    def __str__(self): # This dunder method is returning the name of the item in the database 
        return self.name
   
   
# ORM Object Relational Models---> 
# One to Many
class ChaiReview(models.Model):
    chai = models.ForeignKey(ChaiVarity, on_delete=models.CASCADE, related_name='reviews')
    user = models.ForeignKey(User, on_delete = models.CASCADE)
    rating = models.IntegerField()
    comment = models.TextField()
    date_added = models.DateTimeField(default=timezone.now)
    
    def __str__(self):
        return f'{self.user.username} review for {self.chai.name}'
    
# Many to Many
class Store(models.Model):
    name = models.CharField(max_length=100) 
    location = models.CharField(max_length=200)
    chai_varieties = models.ManyToManyField(ChaiVarity, related_name='stores')
    
    def __str__(self):
        return self.name
    
# One to One 
class ChaiCertificate(models.Model):
    chai = models.OneToOneField(ChaiVarity, on_delete=models.CASCADE, related_name='certificate')
    certificate_number = models.CharField(max_length=100)
    issue_date = models.DateTimeField(default=timezone.now)
    
    def __str__(self):
        return f'Certificate for {self.name.chai}'