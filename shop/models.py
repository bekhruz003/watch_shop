from django.db import IntegrityError
from django.contrib.auth import get_user_model
from django.db.models import Sum
from django.db import models
from django.utils.translation import gettext_lazy as _
from ckeditor_uploader.fields import RichTextUploadingField
from django.utils import timezone

UserModel = get_user_model()


class ProductModel(models.Model):
    title = models.CharField(max_length=60, verbose_name=_('title'))
    description = RichTextUploadingField(verbose_name=_('description'))
    price = models.FloatField(verbose_name=_('price'))
    real_price = models.FloatField(verbose_name=_('real price'), default=0)
    discount = models.PositiveSmallIntegerField(default=0, verbose_name=_('discount'))
    main_image = models.ImageField(upload_to='products/', verbose_name=_('main image'))
    banner_image = models.ImageField(upload_to='probanner/', verbose_name=_('banner image'))
    created_at = models.DateTimeField(auto_now_add=True, verbose_name=_('created at'))

    def get_price(self):
        if self.discount:
            return ((100 - self.discount) / 100) * self.price
        return self.price

    def is_discount(self):
        return bool(self.discount)

    @staticmethod
    def get_cart_info(request):
        cart = request.session.get('cart', [])
        if not cart:
            return 0, 0.0
        return len(cart), ProductModel.objects.filter(id__in=cart).aggregate(Sum('real_price'))['real_price__sum']

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'product'
        verbose_name_plural = 'products'


class WishlistModel(models.Model):
    user = models.ForeignKey(
        UserModel, on_delete=models.CASCADE,
        related_name='wishlists',
        verbose_name=_('user')
    )
    product = models.ForeignKey(
        ProductModel, on_delete=models.CASCADE,
        verbose_name=_('product')
    )

    @staticmethod
    def create_or_delete(user, product):
        try:
            return WishlistModel.objects.create(user=user, product=product)
        except IntegrityError:
            return WishlistModel.objects.get(user=user, product=product).delete()

    def __str__(self):
        return f"{self.user.get_full_name()} | {self.product.title}"

    class Meta:
        verbose_name = 'wishlist'
        verbose_name_plural = 'wishlists'
        unique_together = 'user', 'product',
