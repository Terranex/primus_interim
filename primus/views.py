from django.views.generic import TemplateView


class HomeView(TemplateView):
    template_name = "index.jade"

    def get_context_data(self, **kwargs):
        print(kwargs)

