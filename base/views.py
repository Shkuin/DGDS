from django.shortcuts import render
from .forms import GameUploadForm
from .models import Game
from base.scripts_for_ipfs import create_metadata
from base.scripts_for_contract import connect_to_contract


def add_new_game(name, genre, description, platform, images, price, token_id, private_key):
    new_game = Game.objects.create(name=name, genre=genre, description=description, platform=platform, images=images, price=price, token_id=token_id, private_key=private_key)
    new_game.save()

def main_page(request):
    return render(request, "main_page.html")


def game_uploading(request):
    if request.method == "POST":
        form = GameUploadForm(request.POST, request.FILES)
        if form.is_valid():
            name = form.cleaned_data["name"]
            genre = form.cleaned_data["genre"]
            description = form.cleaned_data["description"]
            platform = form.cleaned_data["platform"]
            poster = form.cleaned_data["poster"]
            images = request.FILES.getlist("images")
            game_file = form.cleaned_data["game_file"]
            price = form.cleaned_data["price"]
            wallet_address = form.cleaned_data["wallet_address"]

            (
                game_file_uri,
                encrypted_message,
                key,
            ) = create_metadata.convert_game_file_to_metadata(game_file)
            print(game_file_uri, key)
            # u should write real address here, owerwise there will be an error
            wallet_address = "0x99bc949975C4bd87D2a6d2a5043112C121EC68D1"
            token_id = connect_to_contract.main(game_file_uri, wallet_address)
            images_url = create_metadata.create_metadata_json(poster, images)
            print(token_id)
            print(images_url)
            add_new_game(name, genre, description, platform, images_url, price, token_id, key)

            return render(request, "main_page.html")
    else:
        form = GameUploadForm()

    return render(request, "game_uploading.html", {"form": form})


def game_catalog(request):
    pass
