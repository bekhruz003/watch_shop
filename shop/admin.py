from django.contrib import admin
from .models import ProductModel
from modeltranslation.admin import TranslationAdmin


@admin.register(ProductModel)
class ProductModelAdmin(TranslationAdmin):
    list_display = ['title', 'price', 'real_price', 'discount', 'created_at']
    list_display_links = ['title', 'price', 'created_at']
    list_filter = ['created_at']
    search_fields = ['title', 'price']
    readonly_fields = ['real_price']

    class Media:
        js = (
            'http://ajax.googleapis.com/ajax/libs/jquery/1.9.1/jquery.min.js',
            'http://ajax.googleapis.com/ajax/libs/jqueryui/1.10.2/jquery-ui.min.js',
            'modeltranslation/js/tabbed_translation_fields.js',
        )
        css = {
            'screen': ('modeltranslation/css/tabbed_translation_fields.css',),
        }
