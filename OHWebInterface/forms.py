
from django import forms
from django.forms import formset_factory

opts=(('OLDSOLD-FRONT','Old Sold Sign - Front'),
      ('OLDSOLD-BACK','Old Sold Sign - Back'),
      ('NEWSOLD','New Sold Sign'),
      ('FURN','Furniture Pricetag'),
      ('TAG','Pricetag'))
lbls=((2,'Random Letters (2)'),
      (3,'Random Letters (3)'),
      (0,'No Labels'))
class SoldTagForm(forms.Form):#@todo gets connected to chapter/book parse function
    orientation=forms.ChoiceField(choices=(('portrait','Portrait'),('landscape','Landscape')),initial="landscape",label='Orientation')
    nx=forms.IntegerField(min_value=1,max_value=4,label="Signs per Sheet (horizontal)",initial=2)
    ny=forms.IntegerField(min_value=1,max_value=10,label="Signs per Sheet (vertical)",initial=1)
    lw=forms.IntegerField(min_value=0,max_value=10,label="Width of Dividing Lines",initial=1)
    numsheets=forms.IntegerField(min_value=1,max_value=100,label="Number of Sheets",initial=1)
    res=forms.IntegerField(min_value=50,max_value=500,label="Resolution of sheet (200 - high quality)",initial=200)
    sides=forms.MultipleChoiceField(choices=opts,label="Which templates to use (note - all selected will have same labels)",initial=['NEWSOLD'], 
      widget = forms.SelectMultiple(attrs = {
            'onclick' : "togglePricetagForm()",
            })
      )
    numrandspots=forms.ChoiceField(choices=lbls,label="How to label tags",initial=2)
    # barcode=forms.CharField(label="Barcode (Furn & Pricetag Only)",required=False)
    # price=forms.CharField(label="Price (Furn & Pricetag Only - should match epos)",required=False)

class PriceTagForm(forms.Form):
    barcode=forms.CharField(label="Barcode",required=False)
    price=forms.CharField(label="Price (should match ePos)",required=False)
    category=forms.CharField(label="Pricetag Category",required=False)
