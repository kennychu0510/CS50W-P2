from django.contrib import admin
from .models import User, AuctionList, BidList, CommentList, WatchList


class UserAdmin(admin.ModelAdmin):
    list_display = ("id", "username", "password", "email")


class AuctionListAdmin(admin.ModelAdmin):
    list_display = ("id", "auctioner", "title",
                    "startingPrice", "currentPrice", "photoURL", "date_created", "winner")


class WatchListAdmin(admin.ModelAdmin):
    list_display = ("id", "user", "item", "date_created")


class BidListAdmin(admin.ModelAdmin):
    list_display = ("bidder", "item", "bidPrice", "date_created")


class BidListAdmin(admin.ModelAdmin):
    list_display = ("bidder", "item", "bidPrice", "date_created")


class CommentListAdmin(admin.ModelAdmin):
    list_display = ("commenter", "comment", "item", "date_created")


# Register your models here.
admin.site.register(User, UserAdmin)
admin.site.register(AuctionList, AuctionListAdmin)
admin.site.register(BidList, BidListAdmin)
admin.site.register(CommentList, CommentListAdmin)
admin.site.register(WatchList, WatchListAdmin)
