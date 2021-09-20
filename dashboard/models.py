from django.db import models
from django.conf import settings
from django.utils.translation import ugettext_lazy as _
from django.utils.text import slugify
from django.urls import reverse


# Create your models here.
class TradersCategorty(models.Model):
    name  = models.CharField(max_length=50,verbose_name=_("Traders Category name"),help_text=_("Example currency,crypo,futures"))
    slug = models.SlugField(_("slug"),unique=True,editable=False)
    
    def __str__(self):
        return self.name
    
    def save(self,*args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        return super().save(*args, **kwargs)

class Trader(models.Model):
    trader = models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.SET_NULL,verbose_name=_("Traders Name"))
    category = models.ManyToManyField(TradersCategorty)
    register_date = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = _("Trader")
        verbose_name_plural = _("Traders")

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("Trader_detail", kwargs={"pk": self.pk})


class Currency(models.Model):
    trader = models.ForeignKey(Trader, verbose_name=_("Trader"), on_delete=models.CASCADE)
    pair = models.CharField(max_length=50,verbose_name=_("Pair Traded"),help_text="add / in pairs such USD/GBP")
    lots_traded = models.DecimalField(max_digits=12, decimal_places=6)
    proit_n_loss =  models.DecimalField(max_digits=12, decimal_places=6)
    pips =  models.DecimalField(max_digits=12, decimal_places=6)

class Stock(models.Model):
    trader = models.ForeignKey(Trader, verbose_name=_("Trader"), on_delete=models.CASCADE)
    pair = models.CharField(max_length=50,verbose_name=_("Pair Traded"),help_text="add / in pairs such USD/GBP")
    lots_traded = models.DecimalField(max_digits=12, decimal_places=6)
    proit_n_loss =  models.DecimalField(max_digits=12, decimal_places=6)
    pips =  models.DecimalField(max_digits=12, decimal_places=6)

class FuturesSubcription(models.Model):
    trader = models.ForeignKey(Trader, verbose_name=_("Trader"), on_delete=models.CASCADE)
    instrument = models.CharField(max_length=50,verbose_name=_("Instrument Traded"),help_text="add / in pairs such USD/GBP")
    proit_n_loss =  models.DecimalField(max_digits=12, decimal_places=6)
    pips =  models.DecimalField(max_digits=12, decimal_places=6)

class Crypto(models.Model):
    trader = models.ForeignKey(Trader, verbose_name=_("Trader"), on_delete=models.CASCADE)
    crypo_name = models.CharField(max_length=50,verbose_name=_("Crypto name"),help_text="Invested crypto")
    daily_change = models.DecimalField(max_digits=12, decimal_places=6,verbose_name=_("Daily change in %"))
