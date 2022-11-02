from modeltranslation.translator import register, TranslationOptions
from .models import ProductModel


@register(ProductModel)
class ProductModelTranslator(TranslationOptions):
    fields = ['title', 'description']
