from django_distill import distill_path

# from .views import StatusView

from django.views.generic import TemplateView


def get_status():
    return None


urlpatterns = [

    # note: GitLab Pages works without the trailing slash,
    # but GitHub Pages does not
    distill_path('status/',
                 TemplateView.as_view(
                    template_name='foundation/status.html'
                 ),
                 name='status',
                 distill_func=get_status),

]
