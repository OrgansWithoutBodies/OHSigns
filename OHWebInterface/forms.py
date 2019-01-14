
from django import forms
from django.forms import formset_factory

opts=(('OLDSOLD-FRONT','Front'),
      ('OLDSOLD-BACK','Back'),
      ('NEWSOLD','New Sold Sign'),
      ('TAG','Pricetag'))
lbls=(('RND2','Random Letters (2)'),
      ('RND3','Random Letters (3)'),
      ('NO','No Labels'))
class SoldTagForm(forms.Form):#@todo gets connected to chapter/book parse function
    nx=forms.IntegerField(min_value=1,max_value=4,label="Signs per Sheet (horizontal)",initial=2)
    ny=forms.IntegerField(min_value=1,max_value=10,label="Signs per Sheet (vertical)",initial=6)
    lw=forms.IntegerField(min_value=0,max_value=10,label="Width of Dividing Lines",initial=3)
    numsheets=forms.IntegerField(min_value=1,max_value=100,label="Number of Sheets to render",initial=1)
    
    sides=forms.MultipleChoiceField(choices=opts,label="Which templates to use")
    orientation=forms.ChoiceField(choices=(('landscape','Landscape'),('portrait','Portrait')),label='Orientation')
    lblmethod=forms.ChoiceField(choices=lbls,label="How to label tags (TBD)")
    