from django.contrib import admin
from .models import TradersCategory, Trader,Currency,Stock,FuturesSubcription,Crypto,TraderBalance



admin.site.register(TradersCategory)
admin.site.register(Trader)
admin.site.register(Currency)
admin.site.register(Stock)
admin.site.register(FuturesSubcription)
admin.site.register(Crypto)
admin.site.register(TraderBalance)
