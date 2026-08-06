from django.shortcuts import get_object_or_404, render
from .models import Category, Product


def product_catalog(request, category_slug=None):
  category = None
  categories = Category.objects.all()
  products = Product.objects.filter(is_active=True)

  if category_slug:
    category = get_object_or_404(Category, slug=category_slug)
    products = products.filter(category=category)

  context = {
      'category': category,
      'categories': categories,
      'products': products,
  }
  return render(request, 'nutrition/catalog.html', context)


def about_view(request):
  return render(request, 'nutrition/about.html')