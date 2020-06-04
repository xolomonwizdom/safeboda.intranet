from django.contrib import admin

from products.models import Product, Activity, Question, Notification

admin.site.register(Product)
admin.site.register(Activity)
admin.site.register(Question)

@admin.register(Notification)
class NotificationAdmin(admin.ModelAdmin):
    list_display = ['title', 'resolved', 'updated_at']
