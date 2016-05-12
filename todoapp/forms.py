from todoapp.models import TodoItem
from django.forms import ModelForm
import datetime


class ToDoForm(ModelForm):
    class Meta:
        model = TodoItem
        fields = ['description','deadline','progress']
   # description = forms.CharField(max_length=1024)
   # deadline = forms.DateField(initial=datetime.date.today)
   # progress = forms.IntegerField()
