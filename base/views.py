from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.contrib import messages
from .forms import GameUploadForm, TransactionCheckForm
from .models import Game
from base.scripts_for_ipfs import create_metadata
from base.helpful_scripts.interaction_with_transactions import *
from base.helpful_scripts import interaction_with_web3
from json import dumps, loads
from django.core.files.storage import FileSystemStorage
from web3 import Web3


def add_new_game(
    name,
    genre,
    description,
    platform,
    poster,
    images,
    price,
    token_id,
    private_key,
    wallet_address,
):
    new_game = Game.objects.create(
        name=name,
        genre=genre,
        description=description,
        platform=platform,
        poster=poster,
        images=images,
        price=price,
        token_id=token_id,
        private_key=private_key,
        slug=str(name).lower().replace(" ", "_"),
        wallet_address=wallet_address,
    )
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
            wallet_address = Web3.toChecksumAddress(form.cleaned_data["wallet_address"])

            poster_path = "/static/img/" + poster.name
            FileSystemStorage(location="static/img").save(poster.name, poster)

            images_path = []
            for i in images:
                images_path.append("/static/img/" + i.name)
                FileSystemStorage(location="static/img").save(i.name, i)

            (
                game_file_uri,
                encrypted_message,
                key,
            ) = create_metadata.convert_game_file_to_metadata(game_file)

            developer_contract = interaction_with_web3.return_contract("Developer")

            # sometimes u have to wait, because it takes time to load into blockchain, that's why sometimes token_id will be wrong
            token_id = developer_contract.create_developer_nft(
                encrypted_message, wallet_address
            )
            poster_uri, images_uri = create_metadata.create_metadata_json(
                poster, images
            )
            add_new_game(
                name,
                genre,
                description,
                platform,
                poster_path,
                dumps(images_path),
                price,
                token_id,
                key,
                wallet_address,
            )

            return render(request, "main_page.html")
    else:
        form = GameUploadForm()

    return render(request, "game_uploading.html", {"form": form})


def game_catalog(request):
    context = {"games": Game.objects.all()}
    return render(request, "catalog/game_catalog.html", context)


def give_copy_game_nft_to_customer(game_id, wallet_address):
    print(f"wallet = {wallet_address}")
    print(f"game_id = {type(game_id)}")
    customer_contract = interaction_with_web3.return_contract("Customer")
    token_id = customer_contract.create_customer_nft(int(game_id), wallet_address)
    return token_id - 1


def game_detail(request, slug):
    game = Game.objects.get(slug__iexact=slug)
    images = loads(game.images)

    if request.method == "POST":
        form = TransactionCheckForm(request.POST, request.FILES)
        if form.is_valid():
            transaction_address = form.cleaned_data["transaction_address"]
            developer_wallet = game.wallet_address
            game_price = game.get_price_in_wei()

            validity, message = check_validity_of_transaction(
                transaction_address, developer_wallet, game_price
            )

            messages.info(request, message)

        if validity:
            game_id = game.token_id
            customer_wallet = get_sender_wallet(transaction_address)
            copy_game_id = give_copy_game_nft_to_customer(game_id, customer_wallet)

            message = f"You got your game copy nft with id = {copy_game_id}!"
            messages.info(request, message)

        return HttpResponseRedirect(game.get_absolute_url())
    else:
        form = TransactionCheckForm()

    return render(
        request,
        "catalog/game_detail.html",
        context={"game": game, "images": images, "form": form},
    )
