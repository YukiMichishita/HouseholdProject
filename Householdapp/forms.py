from django import forms
#from .models import Refrigerator, Grocery, Unit


#class RefrigeratorForm(forms.Form):
#    grocery_names = [(g.id, g.name) for g in Grocery.objects.all()]
#    unit_names = [(u.id, u.name) for u in Unit.objects.all()]
#    grocery = forms.ChoiceField(choices=grocery_names, label='種類')
#    quantity = forms.IntegerField(label='数量')
#    unit = forms.ChoiceField(choices=unit_names, label='単位')
#
#    # def save(self):
#    #     id = self.cleaned_data.get('input_name')
#    #     selected_grocery = Grocery.objects.get(pk=id)
#
#
#class UnitForm(forms.Form):
#    unit_name = forms.CharField(label='名称')
#
#
#class GroceryForm(forms.Form):
#    grocery_name = forms.CharField(label='名称')
