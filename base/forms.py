from django import forms

class GameUploadForm(forms.Form):
    name = forms.CharField(label='Name')
    genre = forms.CharField(label='Genre')
    description = forms.CharField(label='Description', widget=forms.Textarea)
    platform = forms.CharField(label='Platform')
    image = forms.ImageField(label='Image')
    game_file = forms.FileField(label='Game File')
    price = forms.DecimalField(label='Price')
    wallet_address = forms.CharField(label='Wallet Address')
