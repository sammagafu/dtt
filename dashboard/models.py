from django.db import models
from django.conf import settings
from django.utils.translation import ugettext_lazy as _
from django.utils.text import slugify
from django.urls import reverse


# Create your models here.
class TradersCategory(models.Model):
    name  = models.CharField(max_length=50,verbose_name=_("Traders Category name"),help_text=_("Example currency,crypo,futures"))
    slug = models.SlugField(_("slug"),unique=True,editable=False)
    
    def __str__(self):
        return self.name
    
    def save(self,*args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        return super().save(*args, **kwargs)

    class Meta:
        verbose_name = _("Trading category")
        verbose_name_plural = _("Trading categories ")

class Trader(models.Model):
    trader = models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.SET_NULL,verbose_name=_("Traders Name"),null=True)
    category = models.ManyToManyField(TradersCategory)
    register_date = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = _("Trader")
        verbose_name_plural = _("Traders")
        # ordering = ['-order_date']

    def __str__(self):
        return str(self.trader)

    def get_absolute_url(self):
        return reverse("Trader_detail", kwargs={"pk": self.pk})


class TraderBalance(models.Model):
    trader = models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.SET_NULL,verbose_name=_("Traders Name"),null=True)
    date = models.DateTimeField(auto_now_add=True)
    startingbalance = models.DecimalField(max_digits=8, decimal_places=2)
    endbalance = models.DecimalField(max_digits=8, decimal_places=2,editable=False,blank=True,null=True)

class Currency(models.Model):

    PAIRS = [
    ('EUR/USD', 'EUR/USD'),
    ('USD/JPY', 'USD/JPY'),
    ('GBP/USD', 'GBP/USD'),
    ('USD/CHF', 'USD/CHF'),
    ('EUR/CHF', 'EUR/CHF'),
    ('EUR/JPY', 'EUR/JPY'),
    ('GBP/EUR', 'GBP/EUR'),
    ('GBP/JPY', 'GBP/JPY'),
    ('GBP/CHF', 'GBP/CHF'),
    ('CHF/JPY', 'CHF/JPY'),
    ('USD/SEK', 'USD/SEK'),
    ('EUR/HUF', 'EUR/HUF'),
    ('AUD/USD', 'AUD/USD'),
    ('AUD/JPY', 'AUD/JPY'),
    ('AUD/NZD', 'AUD/NZD'),
    ('AUD/CAD', 'AUD/CAD'),
    ('USD/CAD', 'USD/CAD'),
    ('USD/NOK', 'USD/NOK'),
    ('USD/RUB', 'USD/RUB'),
    ('USD/ZAR', 'USD/ZAR'),
    ('EUR/NOK', 'EUR/NOK'),
    ('EUR/RUB', 'EUR/RUB'),
    ('GBP/ZAR', 'GBP/ZAR'),
]
    trader = models.ForeignKey(Trader, verbose_name=_("Trader"), on_delete=models.SET_NULL,null=True)
    pair = models.CharField(max_length=50,verbose_name=_("Pair Traded"),choices=PAIRS)
    lots_traded = models.DecimalField(max_digits=12, decimal_places=6)
    proit_n_loss =  models.DecimalField(max_digits=12, decimal_places=2)
    pips =  models.DecimalField(max_digits=12, decimal_places=6)
    traded_date = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = _("Currency")
        verbose_name_plural = _("Currencies")
        ordering = ['-traded_date']

class Stock(models.Model):

    PAIRS = [
    ('Dow Jones', 'Dow Jones'),
    ('S&P 500', 'S&P 500'),
    ('Nasdaq', 'Nasdaq'),
    ('Small Cap 2000', 'Small Cap 2000'),
    ('S&P 500 VIX', 'S&P 500 VIX'),
    ('DAX', 'DAX'),
    ('FTSE 100', 'FTSE 100'),
    ('CAC 40', 'CAC 40'),
    ('S&P/BMV IPC', 'S&P/BMV IPC'),
    ('Euro Stoxx 50', 'Euro Stoxx 50'),
    ]

    trader = models.ForeignKey(Trader, verbose_name=_("Trader"), on_delete=models.SET_NULL,null=True)
    pair = models.CharField(max_length=50,verbose_name=_("Pair Traded"),choices=PAIRS)
    lots_traded = models.DecimalField(max_digits=12, decimal_places=6)
    proit_n_loss =  models.DecimalField(max_digits=12, decimal_places=2)
    pips =  models.DecimalField(max_digits=12, decimal_places=6)
    traded_date = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = _("Stock")
        verbose_name_plural = _("Stocks")
        ordering = ['-traded_date']


class FuturesSubcription(models.Model):

    PAIRS = [
    ('6B', 'BRITISH POUND FUTURES'),
    ('6E ', 'EURO FX FUTURES'),
    ('6A', 'AUSRALIAN DOLLAR FUTURES'),
    ('6J', 'JAPANESE YEN FUTURES'),
    ('6C', 'CANADIAN DOLLAR FUTURES'),
    ('6S', 'SWISS FRANC FUTURES'),
    ('GC', 'GOLD FUTURES'),
    ('CL', 'CRUDE OIL FUTURES'),
    ('RI', 'RTS INDEX FUTURES'),
    ('YM', 'E- MINI DOW ($5) FUTURES'),
    ]

    trader = models.ForeignKey(Trader, verbose_name=_("Trader"), on_delete=models.SET_NULL,null=True)
    instrument = models.CharField(max_length=50,verbose_name=_("Instrument Traded"),choices=PAIRS)
    proit_n_loss =  models.DecimalField(max_digits=12, decimal_places=2)
    pips =  models.DecimalField(max_digits=12, decimal_places=6)
    traded_date = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = _("Future")
        verbose_name_plural = _("Futures")
        ordering = ['-traded_date']

class Crypto(models.Model):
    PAIRS = [
    ('BTC', 'BITCOIN'),
    ('ETH ', 'ETHEREUM'),
    ('USDT', 'TETHER'),
    ('ADA', 'CARDANO'),
    ('BNB', 'BINANCE COIN'),
    ('XRP', 'XRP'),
    ('SOL', 'SOLANA'),
    ('USDC', 'USD COIN'),
    ('DOT', 'POLKADOT'),
    ('DOGE', 'DOGECOIN'),
    ]
    trader = models.ForeignKey(Trader, verbose_name=_("Trader"), on_delete=models.SET_NULL,null=True)
    crypo_name = models.CharField(max_length=50,verbose_name=_("Crypto name"),choices=PAIRS)
    daily_change = models.DecimalField(max_digits=12, decimal_places=6,verbose_name=_("Daily change in %"))
    traded_date = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = _("Crypto currency")
        verbose_name_plural = _("Crypto currencies")
        ordering = ['-traded_date']
