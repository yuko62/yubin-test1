from django import forms
from .models import Address

class AddressForm(forms.ModelForm):
    class Meta:
        model = Address
        fields = ("zip_code", "address1", "address2", "address3")

        widgets = {
            'zip_code':
            forms.TextInput(
                attrs={'class': 'p-postal-code', 'placeholder': '記入例:000000',},
            ),

            'address1':
            forms.TextInput(
                attrs={'class': 'p-region', 'placeholder': '記入例:東京都',},
            ),

            'address2':
            forms.TextInput(
                attrs={'class': 'p-locality p-street-address p-extended-address',
                    'placeholder': '渋谷区渋谷1'},
            ),

            'address3':
            forms.TextInput(
                attrs={'class': '', 'placeholder': '記入例:スカイツリー'},
            ),
        }
