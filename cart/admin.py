from django.contrib import admin
from .models import Cart, CartItem

# Inline display of CartItems inside Cart
class CartItemInline(admin.TabularInline):
    model = CartItem
    extra = 0  # Don't show empty extra rows

# Customize Cart admin
@admin.register(Cart)
class CartAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'created_at')  # Show user and timestamp
    inlines = [CartItemInline]  # Show related items inline
    search_fields = ('user__username', 'user__email')  # Optional: search by user

# Customize CartItem admin to show user too
@admin.register(CartItem)
class CartItemAdmin(admin.ModelAdmin):
    list_display = ('id', 'product', 'quantity', 'get_user', 'cart')
    search_fields = ('cart__user__username', 'product__name')

    # Method to show the user in CartItem admin
    def get_user(self, obj):
        return obj.cart.user
    get_user.short_description = 'User'
