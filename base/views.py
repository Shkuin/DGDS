from django.shortcuts import render
from .forms import GameUploadForm

def main_page(request):
    return render(request, 'main_page.html')

def game_uploading(request):
    if request.method == 'POST':
        form = GameUploadForm(request.POST, request.FILES)
        if form.is_valid():
            name = form.cleaned_data['name']
            genre = form.cleaned_data['genre']
            description = form.cleaned_data['description']
            platform = form.cleaned_data['platform']
            image = form.cleaned_data['image']
            game_file = form.cleaned_data['game_file']
            price = form.cleaned_data['price']
            wallet_address = form.cleaned_data['wallet_address']
            
            # Process the form data or call your Python script
            # ...

            return render(request, 'success.html')
    else:
        form = GameUploadForm()
    
    return render(request, 'game_uploading.html', {'form': form})

def game_catalog(request):
    pass