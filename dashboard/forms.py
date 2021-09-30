from django import forms
from .models import TradersCategory, Trader,Currency,Stock,FuturesSubcription,Crypto

class CurrencyForm(forms.ModelForm):
    
    class Meta:
        model = Currency
        fields = ("pair","lots_traded","proit_n_loss","pips")


class StockForm(forms.ModelForm):
    class Meta:
        model = Stock
        fields = ("pair","lots_traded","proit_n_loss","pips")


class FuturesForm(forms.ModelForm):
    class Meta:
        model = FuturesSubcription
        fields = ("instrument","proit_n_loss","pips")


class CryptoForm(forms.ModelForm):
    class Meta:
        model = Crypto
        fields = ("crypo_name","daily_change")