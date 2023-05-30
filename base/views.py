from django.shortcuts import render
from .forms import GameUploadForm

# from scripts_for_ipfs.create_metadata import create_metadata
from base.scripts_for_ipfs.create_metadata import create_metadata


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
            game_files = request.FILES.getlist("game_files")
            price = form.cleaned_data["price"]
            wallet_address = form.cleaned_data["wallet_address"]
            # for image in images:
            #     print("-----------------")
            #     print(image.read())
            #     print("-----------------")
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

            keys, metadata_uri = create_metadata(
                name,
                genre,
                description,
                platform,
                images,
                game_files,
                price,
                wallet_address,
            )
            print("----------")
            print(keys)
            print("----------")
            print(metadata_uri)
            return render(request, "success.html")
    else:
        form = GameUploadForm()

    return render(request, "game_uploading.html", {"form": form})


def game_catalog(request):
    pass
