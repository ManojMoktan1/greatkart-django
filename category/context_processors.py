from category.models import Category

#for drop down menu
def menu_links(request):
    links = Category.objects.all()
    return dict(links=links)