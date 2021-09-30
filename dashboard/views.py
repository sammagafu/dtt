# from django.forms.models import _Labelsss
from django.http import request
from django.shortcuts import render
from django.views.generic import TemplateView,CreateView,DetailView,ListView
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import TradersCategory, Trader,Currency,Stock,FuturesSubcription,Crypto,TraderBalance
from .forms import CurrencyForm,StockForm,FuturesForm,CryptoForm
from django.db.models import Sum, query
from django.urls import reverse_lazy
from django.http import JsonResponse




# Create your views here.
# currency views starts here



class DashboardView(LoginRequiredMixin,TemplateView):
    template_name = "dashboard/index.html"
    def get_context_data(self, **kwargs):
        context = super(DashboardView, self).get_context_data(**kwargs)
        context['assets_allocation'] = TradersCategory.objects.count()
        context["starting_balance"] = TraderBalance.objects.aggregate(Sum('startingbalance'))
        return context

# currency views starts here
class RegisterCurrencyCreateView(LoginRequiredMixin,CreateView):
    model = Currency
    form_class = CurrencyForm
    template_name = "dashboard/currency/register.html"
    success_url = reverse_lazy('dashboard:currency-list')

    def form_valid(self, form):
        form.instance.trader = Trader.objects.get(trader=self.request.user)
        # print()
        return super().form_valid(form)

class CurrencyListView(ListView):
    model = Currency
    context_object_name = "currency"
    template_name = "dashboard/currency/list.html"
# currency views ends here

# stocks starts here
class RegisterStockCreateView(LoginRequiredMixin,CreateView):
    model = Stock
    form_class = StockForm
    template_name = "dashboard/stock/register.html"
    success_url = reverse_lazy('dashboard:stock-list')

    def form_valid(self, form):
        form.instance.trader = Trader.objects.get(trader=self.request.user)
        return super().form_valid(form)

class StockListView(ListView):
    model = Stock
    context_object_name = "stock"
    template_name = "dashboard/stock/list.html"
# stocks ends here

# futures starts here
class RegisterFutureCreateView(LoginRequiredMixin,CreateView):
    model = FuturesSubcription
    form_class = FuturesForm
    template_name = "dashboard/future/register.html"
    success_url = reverse_lazy('dashboard:futures-list')

    def form_valid(self, form):
        form.instance.trader = Trader.objects.get(trader=self.request.user)
        return super().form_valid(form)

class FuturesListView(ListView):
    model = FuturesSubcription
    context_object_name = "futures"
    template_name = "dashboard/future/list.html"

# futures ends here

# futures starts here
class RegisterCryptoCreateView(LoginRequiredMixin,CreateView):
    model = Crypto
    form_class = CryptoForm
    template_name = "dashboard/crypto/register.html"
    success_url = reverse_lazy('dashboard:cryto-list')

    def form_valid(self, form):
        form.instance.trader = Trader.objects.get(trader=self.request.user)
        return super().form_valid(form)

class CryptoListView(ListView):
    model = Crypto
    context_object_name = "cryto"
    template_name = "dashboard/crypto/list.html"



def population_chart(request):
    labels = []
    data = []
    crypto = []

    currency = Currency.objects.all()
    crypo = Crypto.objects.all()

    for currency in currency:
        labels.append(currency.traded_date)
        data.append(currency.proit_n_loss)
    
    for cry in crypo:
        print(cry.daily_change)
        crypto.append(cry.daily_change)


    return JsonResponse(data={
        'labels': labels,
        'data': data,
    })