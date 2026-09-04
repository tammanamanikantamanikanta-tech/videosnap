# pyrefly: ignore [missing-import]
from django.urls import path
# pyrefly: ignore [missing-import]
from . import views

urlpatterns = [
    path("allproducts/", views.products_view, name="allproducts"),
    path("create_product/", views.create_product_view, name="create_product"),
    path("update_product/<int:product_id>/", views.update_product_view, name="update_product"),
    path("delete_product/<int:product_id>/", views.delete_product_view, name="delete_product"),
    path("checkout/", views.checkout_view, name="checkout"),
    # Cart URLs
    path("cart/", views.view_cart_view, name="view_cart"),
    path("cart/add/<int:product_id>/", views.add_to_cart_view, name="add_to_cart"),
    path("cart/remove/<int:cart_id>/", views.delete_cart_view, name="delete_cart"),
    path("cart/update/<int:cart_id>/", views.update_cart_quantity_view, name="update_cart_quantity"),
]