# pyrefly: ignore [missing-import]
from django.shortcuts import render, redirect, get_object_or_404
# pyrefly: ignore [missing-import]
from django.contrib.auth.decorators import login_required
# pyrefly: ignore [missing-import]
from .models import Product, cart as Cart

# Display all products
def products_view(request):
    products = Product.objects.all()
    cart_count = 0
    if request.user.is_authenticated:
        cart_count = Cart.objects.filter(user=request.user).count()
    return render(request, "accounts/allproducts.html", {
        "allproducts": products,
        "cart_count": cart_count,
    })

# Create a new product
def create_product_view(request):
    if request.method == "POST":
        name = request.POST.get("name")
        description = request.POST.get("description")
        price = request.POST.get("price")
        stock = request.POST.get("stock")
        image = request.FILES.get("image")

        if name and price:
            Product.objects.create(
                name=name,
                description=description,
                price=price,
                stock=stock or 0,
                image=image
            )
            return redirect("allproducts")

    return render(request, "accounts/create_product.html")

def update_product_view(request, product_id=None):
    if product_id is None:
        return redirect("allproducts")
    product = get_object_or_404(Product, id=product_id)
    if request.method == "POST":
        product.name = request.POST.get("name")
        product.description = request.POST.get("description")
        product.price = request.POST.get("price")
        product.stock = request.POST.get("stock")
        new_image = request.FILES.get("image")
        if new_image:
            product.image = new_image
        product.save()
        return redirect("allproducts")
    return render(request, "accounts/update_product.html", {"product": product})

def delete_product_view(request, product_id=None):
    if product_id is None:
        return redirect("allproducts")
    product = get_object_or_404(Product, id=product_id)
    if request.method == "POST":
        product.delete()
        return redirect("allproducts")
    return render(request, "accounts/delete_product.html", {"product": product})

def checkout_view(request):
    return render(request, "accounts/checkout.html")

# ─── Cart Views ───────────────────────────────────────────────────────────────

@login_required(login_url="/accounts/login/")
def add_to_cart_view(request, product_id):
    """Add a product to the cart, or increment quantity if already present (capped at stock)."""
    product = get_object_or_404(Product, id=product_id)
    cart_item, created = Cart.objects.get_or_create(
        user=request.user,
        product=product,
        defaults={"quantity": 1}
    )
    if not created and cart_item.quantity < product.stock:
        cart_item.quantity += 1
        cart_item.save()
    return redirect("view_cart")

@login_required(login_url="/accounts/login/")
def view_cart_view(request):
    """Display all cart items for the current user with totals."""
    cart_items = Cart.objects.filter(user=request.user).select_related("product")
    total = sum(item.product.price * item.quantity for item in cart_items)
    cart_count = cart_items.count()
    return render(request, "accounts/view_cart.html", {
        "cart_items": cart_items,
        "total": total,
        "cart_count": cart_count,
    })

@login_required(login_url="/accounts/login/")
def delete_cart_view(request, cart_id):
    """Remove a specific item from the user's cart."""
    cart_item = get_object_or_404(Cart, id=cart_id, user=request.user)
    if request.method == "POST":
        cart_item.delete()
    return redirect("view_cart")

@login_required(login_url="/accounts/login/")
def update_cart_quantity_view(request, cart_id):
    """
    Increment or decrement the quantity of a cart item.
    - action=inc  → +1 (capped at product.stock)
    - action=dec  → -1 (removes item when reaching 0)
    """
    cart_item = get_object_or_404(Cart, id=cart_id, user=request.user)
    if request.method == "POST":
        action = request.POST.get("action")
        if action == "inc":
            if cart_item.quantity < cart_item.product.stock:
                cart_item.quantity += 1
                cart_item.save()
        elif action == "dec":
            if cart_item.quantity > 1:
                cart_item.quantity -= 1
                cart_item.save()
            else:
                # quantity would become 0 — remove from cart
                cart_item.delete()
    return redirect("view_cart")