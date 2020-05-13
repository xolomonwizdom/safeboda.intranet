from django.contrib import admin

from .models import Document

@admin.register(Document)
class DocumentAdmin(admin.ModelAdmin):
    list_display = ['file', 'created_at', 'updated_at']