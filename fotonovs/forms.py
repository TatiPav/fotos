from django import forms

from .models import Shape, Entry

class ShapeForm(forms.ModelForm):
    # зарег.пользователь может создать запись о дате, которая ему подходит
    class Meta:
        model = Shape
        fields = ['text']
        labels = {'text': ''}

class EntryForm(forms.ModelForm):
    class Meta:
        model = Entry
        fields = ['text']
        labels = {'text': 'Запись:'}
        widgets = {'text': forms.Textarea(attrs={'cols': 50})}