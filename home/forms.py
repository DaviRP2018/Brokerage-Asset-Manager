import datetime

from django import forms

from django_core import settings
from home.models import BrokerageAsset


class BrokerageAssetForm(forms.ModelForm):
    date = forms.DateField(
        initial=datetime.date.today().strftime("%d/%m/%Y"),
        input_formats=settings.DATE_INPUT_FORMATS,
    )

    class Meta:
        model = BrokerageAsset
        fields = "__all__"
