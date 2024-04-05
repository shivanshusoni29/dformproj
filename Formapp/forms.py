from django import forms

class Studentform(forms.Form):
    name=forms.CharField(max_length=20)
    age=forms.IntegerField()
    gender=forms.CharField(max_length=10)
    created_at=forms.DateField()