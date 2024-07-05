from .models import Category


def menu_links(request):
    links = Category.objects.all().filter(is_popular = True)[:3]
    return dict(links = links)