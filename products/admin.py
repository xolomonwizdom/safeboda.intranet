from django.contrib import admin

from products.models import ProductType, Scenario, Question, Notification, Tool

admin.site.register(ProductType)
admin.site.register(Scenario)
admin.site.register(Question)

@admin.register(Notification)
class NotificationAdmin(admin.ModelAdmin):
    list_display = ['title', 'resolved', 'updated_at']


@admin.register(Tool)
class ToolAdmin(admin.ModelAdmin):
    list_display = ['name', 'link']
