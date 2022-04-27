from django import forms
from .models import SubmitNFTModel

class SubmitNFTForm(forms.ModelForm):

    class Meta:
        model = SubmitNFTModel
        fields = "__all__"