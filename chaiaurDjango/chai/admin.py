from django.contrib import admin
from .models import ChaiVarity, ChaiReview,ChaiCertificate,Store

# Register your models here. any models you write needs to be regestered here first you import the model and then register

# These class will control which fields will be shown in the row of each objects 
class ChaiReviewInline(admin.TabularInline):# with TabularInline we are saying we have injected ChaiReview in Chai which is ChaiVarity
    model = ChaiReview # TabularInline says to show the ChaiReview model inside of ChaiVarity model. 
    extra = 1 # This says how many times the injected ChaiReview model will be repeated . 

class ChaiVarietyAdmin(admin.ModelAdmin):
    list_display = ('name','tea_type','date','price',)
    inlines = [ChaiReviewInline] # 

class StoreAdmin(admin.ModelAdmin):
    list_display= ('name', 'location',) # List display shows details of an object stored in database in the table 
    filter_horizontal = ('chai_varieties',) # This will filter all the chai when we add which chai is available in which store
    
class ChaiCertificateAdmin(admin.ModelAdmin):
    list_display = ('chai','certificate_number', 'issue_date',) # List_display is a tupple 


# registering models and custom class made above .     
admin.site.register(ChaiVarity, ChaiVarietyAdmin)
admin.site.register(Store, StoreAdmin)
admin.site.register(ChaiCertificate, ChaiCertificateAdmin)