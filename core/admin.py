from django.contrib import admin
from .models import URLForProcessing, ResultFromParsing


@admin.register(URLForProcessing)
class URLForProcessingAdmin(admin.ModelAdmin):
    list_display = ('url', 'status', 'start_processing')
    list_filter = ('status', 'start_processing')
    fields = ('url', 'timeshift', 'status', 'start_processing')
    readonly_fields = ('status', 'start_processing')
    search_fields = ('url',)


@admin.register(ResultFromParsing)
class ResultFromParsingAdmin(admin.ModelAdmin):
    list_display = ('url', 'created_at')
    list_filter = ('created_at',)
    fields = ('url', 'title', 'charset', 'h1', 'created_at')
    readonly_fields = ('url', 'title', 'charset', 'h1', 'created_at')
    search_fields = ('url__url',)
