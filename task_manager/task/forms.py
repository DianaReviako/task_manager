from django.core.exceptions import ValidationError
from django import forms
from .models import Task
from datetime import date


class TaskForm(forms.Form):
    deadline_date = forms.DateField()
    text = forms.CharField(widget=forms.Textarea)

    def clean_deadline_date(self):
        data = self.cleaned_data['deadline_date']
        if data < date.today():
            raise ValidationError("Deadline can't be in the past")
        return data

    class Meta:
        model = Task
