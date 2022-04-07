from django import forms
from .models import Book,Student

class BookModelForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = '__all__'

class StudentModelForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = '__all__'