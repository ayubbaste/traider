from django.contrib import admin
from traider.models import *


@admin.register(Balance)
class BalanceAdmin(admin.ModelAdmin):
    list_display = ('date', 'amount', 'currency')

@admin.register(Coin)
class CoinAdmin(admin.ModelAdmin):
    list_display = ('name',)

@admin.register(Operation)
class OperationAdmin(admin.ModelAdmin):
    list_display = ('coin', 'binance_id', 'operation_type',
                    'operation_date', 'operation_time', 'qty', 'price',
                    'quoteQty', 'commission', 'commissionAsset')
    search_fields = ['coin__name']
    #list_filter = ('deal_type',)

@admin.register(Reason)
class ReasonAdmin(admin.ModelAdmin):
    list_display = ('name',)

class EntryReasonInlineAdmin(admin.TabularInline):
    model = EntryReason
    extra = 1

@admin.register(Indicator)
class IndicatorAdmin(admin.ModelAdmin):
    list_display = ('name',)

class EntryIndicatorInlineAdmin(admin.TabularInline):
    model = EntryIndicator
    extra = 0

@admin.register(Screenshot)
class ReasonAdmin(admin.ModelAdmin):
    list_display = ('id', 'filename',)

class ScreenshotInlineAdmin(admin.TabularInline):
    model = Screenshot
    extra = 0

@admin.register(Traid)
class TraidAdmin(admin.ModelAdmin):
    list_display = ('coin', 'date', 'time', 'result', 'result_percent',)

    inlines = [
        EntryReasonInlineAdmin,
        ScreenshotInlineAdmin,
        EntryIndicatorInlineAdmin
    ]

@admin.register(Candidate)
class CandidateAdmin(admin.ModelAdmin):
    list_display = ('symbol', 'timeframe', 'status',)
