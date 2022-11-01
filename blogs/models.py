from django.db import models
from django.utils.translation import gettext_lazy as _
from ckeditor_uploader.fields import RichTextUploadingField


class CategoryModel(models.Model):
    name = models.CharField(max_length=50, verbose_name=_('name'))
    created_at = models.DateTimeField(auto_now_add=True, verbose_name=_('created at'))

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'category'
        verbose_name_plural = 'categories'


class CommentModel(models.Model):
    comment = models.TextField(verbose_name=_('comment'))
    name = models.CharField(max_length=255, verbose_name=_('name'))
    email = models.EmailField(verbose_name=_('email'))
    site = models.CharField(max_length=255, verbose_name=_('site'))
    created_at = models.DateTimeField(auto_now_add=True, verbose_name=_('created at'))

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = _('comment')
        verbose_name_plural = _('comments')


class AutherModel(models.Model):
    full_name = models.CharField(max_length=100, verbose_name=_('full name'))
    image = models.ImageField(upload_to='auther_images/', verbose_name=_('image'))

    def __str__(self):
        return self.full_name

    class Meta:
        verbose_name = _('auther')
        verbose_name_plural = _('authers')


class PostTagModel(models.Model):
    name = models.CharField(max_length=30, verbose_name=_('name'))
    created_at = models.DateTimeField(auto_now_add=True, verbose_name=_('created at'))

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = _('tag')
        verbose_name_plural = _('tags')


class PostModel(models.Model):
    title = models.CharField(max_length=255, verbose_name=_('title'))
    body = RichTextUploadingField(verbose_name=_('body'))
    main_image = models.ImageField(upload_to='main_images/', verbose_name=_('main image'))
    banner = models.ImageField(upload_to='post_banners/', verbose_name=_('banner'))
    auther = models.ForeignKey(AutherModel, related_name='posts', on_delete=models.RESTRICT)
    tag = models.ManyToManyField(PostTagModel, related_name='posts', verbose_name=_('tag'))
    category = models.ForeignKey(CategoryModel, null=True, on_delete=models.RESTRICT, related_name='posts',
                                 verbose_name=_('category'))
    created_at = models.DateTimeField(auto_now_add=True, verbose_name=_('created at'))

    def __str__(self):
        return f"{self.title[:100]} ...."

    class Meta:
        verbose_name = _('post')
        verbose_name_plural = _('posts')


class CommentModel(models.Model):
    comment = models.TextField(verbose_name=_('comment'))
    name = models.CharField(max_length=255, verbose_name=_('name'))
    email = models.EmailField(verbose_name=_('email'))
    site = models.CharField(max_length=255, verbose_name=_('site'))
    post = models.ForeignKey(PostModel, on_delete=models.CASCADE, related_name='comments', verbose_name=_('post'))
    created_at = models.DateTimeField(auto_now_add=True, verbose_name=_('created at'))

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = _('comment')
        verbose_name_plural = _('comments')
