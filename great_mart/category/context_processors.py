from .models import Category


def menu_link(request):
    all_categories = Category.objects.all()
    return dict(all_categories=all_categories)
