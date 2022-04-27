from django.db import models
from django.contrib.auth.models import User
import uuid
# Create your models here.
class SubmitNFTModel(models.Model):
    #id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(verbose_name="Name of NFT", max_length = 300)
    username = models.CharField(verbose_name="Username", max_length = 300)
    location = models.CharField(verbose_name="Location of NFT Souvenir", max_length = 300)
    link = models.CharField(verbose_name="Link to NFT Souvenir (preferably through OpenSea)", max_length = 300)
    def __str__(self):
        return self.name