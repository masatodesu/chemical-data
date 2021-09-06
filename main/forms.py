from django import forms
from .models import Chemical


class ChemicalModelForm(forms.ModelForm):
    class Meta:
        model = Chemical
        fields = ('name', 'SMILES', 'comment', 'boilingpoint', 'meltingpoint')

#a. フォームを定義
class ChemicalForm(forms.Form):
    #b. 個々の項目を定義
    name = forms.CharField(label='Compaund name', required = True, max_length=30)
    SMILES = forms.CharField(label='SMILES', required = True, max_length=30)
    comment = forms.CharField(label='comment', required = True, max_length=255)
    boilingpoint = forms.IntegerField(label='b.p.(K)', required = True)
    meltingpoint = forms.IntegerField(label ='m.p.(K)', required = True)