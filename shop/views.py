from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import ListView, DetailView
from .models import ProductModel, WishlistModel


class ShoppingCart(ListView):
    template_name = 'cart.html'

    def get_queryset(self):
        products = ProductModel.get_cart_objects(self.request)
        return products


class ShopView(ListView):
    template_name = 'shop.html'
    paginate_by = 3

    def get_queryset(self, **kwargs):
        qs = ProductModel.objects.all()
        sort = self.request.GET.get('sort')
        if sort == 'price':
            qs = qs.order_by('price')
        elif sort == '-price':
            qs = qs.order_by('-price')

        return qs


class ProductDetailView(DetailView):
    model = ProductModel
    template_name = 'product_detail.html'


@login_required
def wishlist_view(request, pk):
    product = get_object_or_404(ProductModel, pk=pk)
    WishlistModel.create_or_delete(request.user, product)
    return redirect(request.GET.get('next', '/'))


class WishListView(LoginRequiredMixin, ListView):
    template_name = 'wishlist.html'

    def get_queryset(self):
        return ProductModel.objects.filter(wishlistmodel__user_id=self.request.user)


def update_cart_view(request, id):
    cart = request.session.get('cart', [])

    if id in cart:
        cart.remove(id)
    else:
        cart.append(id)

    request.session['cart'] = cart
    return redirect(request.GET.get('next', '/'))
