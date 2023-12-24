from django.views import generic


class IndexView(generic.ListView):
    template_name = "home/index.html"

    def get_queryset(self):
        pass


class AddItemView(generic.FormView):
    template_name = "item/add_item.html"

    def get_queryset(self):
        pass
