from django import forms
from multiupload.fields import MultiFileField

class GameUploadForm(forms.Form):
    name = forms.CharField(label='Name')
    genre = forms.CharField(label='Genre')
    description = forms.CharField(label='Description', widget=forms.Textarea)
    platform = forms.CharField(label='Platform')
    images = MultiFileField(label='Images')
    game_files = MultiFileField(label='Game Files')
    price = forms.DecimalField(label='Price')
    wallet_address = forms.CharField(label='Wallet Address')