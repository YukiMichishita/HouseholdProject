from django.urls import path
from .views import Refrigeratorview
from .views import RefrigeratorAddview
from .views import GroceryAddview
from .views import UnitAddview
from .forms import RefrigeratorForm
import sys

print(sys.executable)


app_name = 'Householdapp'
urlpatterns = [
    path('refrigerator/', Refrigeratorview, name='refrigerator'),
    path('refrigeratorAdd/', RefrigeratorAddview, name='refrigeratorAdd'),
    path('groceryAdd/', GroceryAddview, name='groceryAdd'),
    path('unitAdd/', UnitAddview, name='UnitAdd'),
    path('', RefrigeratorForm, name='RefrigeratorForm'),
]
