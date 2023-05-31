from django.shortcuts import render
from .forms import GameUploadForm

# from scripts_for_ipfs.create_metadata import create_metadata
from base.scripts_for_ipfs import create_metadata
from base.scripts_for_contract import connect_to_contract


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
            # Process the form data or call your Python script
            # ...
            # print(name)
            # print(genre)
            # print(platform)
            # print(description)

            (
                game_file_uri,
                encrypted_message,
                key,
            ) = create_metadata.convert_game_file_to_metadata(game_file)

            # u should write real address here, owerwise there will be an error
            wallet_address = "0x99bc949975C4bd87D2a6d2a5043112C121EC68D1"
            token_id = connect_to_contract.main(game_file_uri, wallet_address)

            metadata_json = create_metadata.create_metadata_json(
                name,
                genre,
                description,
                platform,
                poster,
                images,
                price,
                wallet_address,
                token_id,
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
