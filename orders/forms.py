from django.forms import ModelForm
from .models import Size, PizzaStyle, PizzaType, PizzaTopping, Pizza

class PizzaForm(ModelForm):
  class Meta:
    model = Pizza
    fields = ['style', 'size', 'type', 'toppings']
    