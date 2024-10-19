

from django import forms

from todos.models import Task


class TaskCreate(forms.Form):
    name=forms.CharField(max_length=150)
    start_date=forms.DateTimeField(widget=forms.SelectDateWidget,required=False )
    end_date=forms.DateTimeField(widget=forms.SelectDateWidget,required=False)
    description=forms.CharField(max_length=1000, required=False)
    
    def clean_name(self):
        name=self.cleaned_data.get('name')
        if len(name)<5:
            raise forms.ValidationError("El nombre debe tener al menos 5 caracteres")
        return name
    
class TaskModelFormCreate(forms.ModelForm):
        class Meta:
             model=Task
             fields=['name','start_date','end_date','description','level','done']