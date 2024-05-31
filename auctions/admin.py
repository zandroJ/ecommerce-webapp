from django.contrib import admin
from .models import User, Listing, Bid, Comment, Category, Watchlist

admin.site.register(User)
admin.site.register(Listing)
admin.site.register(Bid)
admin.site.register(Comment)
admin.site.register(Category)
admin.site.register(Watchlist)
