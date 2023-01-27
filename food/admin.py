from django.contrib import admin
from .models import Category, Client, Product, Sale, SoldProduct
from django import forms

# Register your models here.


class ProductForm(forms.ModelForm):

    class Meta:
        exclude = ['user']
        model = Product


class ProductAdmin(admin.ModelAdmin):

    readonly_fields = ('user',)

    form = ProductForm

    def has_change_permission(self, request, obj=None) -> bool:
        if obj is None:
            return False
        return obj.user == request.user

    def save_model(self, request, obj, form, change) -> None:
        if not obj.pk:
            obj.user = request.user
        obj.save()





class ClientAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name')


class CategoryProductsAdmin(admin.StackedInline):
    model = Product
    extra = 0


class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name']
    inlines = [CategoryProductsAdmin]


admin.site.register(Client, ClientAdmin)
admin.site.register(Sale)
admin.site.register(SoldProduct)
admin.site.register(Product, ProductAdmin)
admin.site.register(Category, CategoryAdmin)
