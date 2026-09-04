# pyrefly: ignore [missing-import]
from django.contrib import admin
# pyrefly: ignore [missing-import]
from .models import Product, ProductImage, ProductReview, Price, offers, cart, order

admin.site.register(Product)
admin.site.register(ProductImage)
admin.site.register(Price)
admin.site.register(ProductReview)
admin.site.register(offers)
admin.site.register(cart)
admin.site.register(order)