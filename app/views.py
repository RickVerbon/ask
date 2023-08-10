from django.views.generic import TemplateView


# Create your views here.
class HomeView(TemplateView):
    template_name = 'app/home.html'

    def get(self, request, *args, **kwargs):
        print("HomeView get method called")
        return super().get(request, *args, **kwargs)
