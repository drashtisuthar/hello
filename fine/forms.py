from django import forms
from .models import member,Books

class memberform(forms.ModelForm):
    class Meta:
        model=member
        fields=['username','email','password','phn']

class bookform(forms.ModelForm):
    class Meta:
        model=Books
        fields=['bookname','discription','price']