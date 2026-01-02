from django import forms
from .models import ChaiVarity

class ChaiVarityForm(forms.Form):
    # modelchoicefield can querry in existing models
    chai_varity = forms.ModelChoiceField(queryset=ChaiVarity.objects.all(), label='select chai variety')
    
    
