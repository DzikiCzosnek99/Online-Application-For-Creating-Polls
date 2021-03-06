from django import forms
from .models import *
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm


class QuestionnaireForm(forms.ModelForm):
    class Meta:
        model = Questionnaire
        fields = ['text', 'password', 'publicResults']
        widgets = {
            'text': forms.TextInput(attrs={'class': 'col-xl-6 col-md-12 col-form-label', 'style': 'margin-top: 20px;'}),
            'password': forms.PasswordInput(
                attrs={'class': 'col-xl-6 col-md-12 col-form-label', 'style': 'margin-top: 20px;'}),
            'publicResults': forms.CheckboxInput(attrs={'class': 'form-check-input'})
        }


class QuestionForm(forms.ModelForm):
    class Meta:
        model = Question
        fields = ['text', 'multiple_choice']
        widgets = {
            'text': forms.TextInput(attrs={
                'class': 'col-10 col-form-label', 'placeholder': 'Dodaj nowe pytanie',
            }),
            'multiple_choice': forms.CheckboxInput(attrs={'class': 'form-check-input'})
        }


class AnswerForm(forms.ModelForm):
    class Meta:
        model = Answer
        fields = ['text']
        widgets = {
            'text': forms.TextInput(attrs={'class': 'col-10 col-form-label', 'placeholder': 'Dodaj odpowiedz'
                                           })
        }

