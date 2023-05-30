from django.shortcuts import render
from .forms import GameUploadForm

# from scripts_for_ipfs.create_metadata import create_metadata
from base.scripts_for_ipfs import create_metadata


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
            images = request.FILES.getlist("images")
            game_file = request.FILES.getlist("game_file")
            price = form.cleaned_data["price"]
            wallet_address = form.cleaned_data["wallet_address"]
            # Process the form data or call your Python script
            # ...
            # print(name)
            # print(genre)
            # print(platform)
            # print(description)
            # for i in images:
            #     print(i)

            # for f in game_files:
            #     print(f)

            (
                game_file_uri,
                encrypted_message,
                key,
            ) = create_metadata.convert_game_file_to_metadata(game_file)

            # Here will be code which create nft token, and we will take nft address from this script,
            # after that we will add this address to json

            metadata_json = create_metadata.create_metadata_json(
                name,
                genre,
                description,
                platform,
                None,  # icon,
                images,
                price,
                wallet_address,
                None,  # nft_address
            )

            # keys, game_file_uri = create_metadata.create_metadata_json(
            #     name,
            #     genre,
            #     description,
            #     platform,
            #     images,
            #     game_files,
            #     price,
            #     wallet_address,
            # )
            # print("----------")
            # print(keys)
            # print("----------")
            # print(game_file_uri)
            return render(request, "success.html")
    else:
        form = GameUploadForm()

    return render(request, "game_uploading.html", {"form": form})


def game_catalog(request):
    pass
