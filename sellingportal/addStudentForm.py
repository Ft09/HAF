from django import forms

class AddStudent(forms.Form):
    first_name = forms.CharField(required=True, widget=forms.TextInput( ))
    last_name = forms.CharField(required=True, widget=forms.TextInput( ))
    age = forms.CharField(required=True, widget=forms.TextInput( ))
    date_birth = forms.CharField(required=True, widget=forms.TextInput( ))