from django.contrib import admin
from .models import ChaiVariety, ChaiOrder, chaiStore, ChaiReview

# Register your models here.
class ChaiReviewInline(admin.TabularInline):
    model = ChaiReview
    extra = 2

class ChaiVarietyAdmin(admin.ModelAdmin):
    list_display = ('name', 'type', 'date_added')
    inlines = [ChaiReviewInline]

class ChaiStoreAdmin(admin.ModelAdmin):
    list_display = ('name', 'location')
    filter_horizontal = ('chai_varieties',)

class ChaiOrderDetail(admin.ModelAdmin):
    list_display = ('chai', 'order_number')

admin.site.register(ChaiVariety, ChaiVarietyAdmin)
admin.site.register(chaiStore, ChaiStoreAdmin)
admin.site.register(ChaiOrder, ChaiOrderDetail)