from django import template
from shop.models import WishlistModel, ProductModel

register = template.Library()


@register.simple_tag()
def cart_info(request):
    return ProductModel.get_cart_info(request)


@register.filter()
def is_wishlist(product, request):
    return WishlistModel.objects.filter(user=request.user, product=product).exists()


@register.filter()
def is_cart(product, request):
    return product.id in request.session.get('cart', [])
