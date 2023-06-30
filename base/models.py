from django.db import models
from jsonfield import JSONField
from django.shortcuts import redirect
from django.urls import reverse

from base.scripts_for_contract.aggregator_V3_contract.interaction_with_agregator_V3_contract import (
    get_latest_price,
)


# Create your models here.
class Game(models.Model):
    name = models.CharField(max_length=1000)
    genre = models.CharField(max_length=2000)
    description = models.TextField()
    platform = models.CharField(max_length=1000)
    poster = models.CharField(max_length=1000)  # ipfs addreess
    images = (
        JSONField()
    )  # it's gonna store like a json, we will convert it to python list which contain ipfs addresses
    price = models.FloatField()  # in ETH
    token_id = models.CharField(max_length=1000)  # NFT
    private_key = models.CharField(max_length=2000)  # from encrypted ipfs hash
    slug = models.SlugField(max_length=1500, unique=True)  # local url
    wallet_address = models.CharField(max_length=2000)  # game developer wallet address

    def get_absolute_url(self):
        return reverse("game_detail_url", kwargs={"slug": self.slug})

    def get_price_in_wei16(self):
        return str(hex(int(self.price * 1000000000000000000 / get_latest_price())))

    def get_price_in_wei(self):
        return int(self.price * 1000000000000000000 / get_latest_price())

    def __str__(self):
        return self.name

    def get_game_id(self):
        # print(f"token id = {self.token_id}")
        return self.token_id

    def get_game_developer(self):
        return self.wallet_address
