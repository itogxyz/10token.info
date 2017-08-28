from .models import Startup
from django import forms

class StartupSearchForm(forms.Form):
    search_text =  forms.CharField(
                    required = False,
                    label='Search',
                    widget=forms.TextInput(attrs={'placeholder': 'Startup name ... '})
                  )

    # token_id_exact = forms.IntegerField(
    #                 required = False,
    #                 label='token_id (token_id)!'
    #               )
