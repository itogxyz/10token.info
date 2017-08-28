from django.core.urlresolvers import reverse
from django.views.generic import DetailView, CreateView, ListView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Startup
from django.utils import timezone

from .forms import StartupSearchForm
from search_views.search import SearchListView
from search_views.filters import BaseFilter

from django.core.urlresolvers import reverse_lazy

class StartupCreate(CreateView):
    model = Startup
    fields = [
    'name',
    'description',
    'logo',
    'goal',
    'wallet',
    'website',
    'launch_date'
    ]

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super(StartupCreate, self).form_valid(form)

class StartupUpdate(LoginRequiredMixin, UpdateView):
    model = Startup
    fields = ['name']

class StartupDelete(LoginRequiredMixin, DeleteView):
    model = Startup
    success_url = reverse_lazy('startup-list')





class StartupFilter(BaseFilter):
    search_fields = {
        'search_text' : ['name'],
        # 'token_id_exact' : { 'token_id' },
    }

class StartupSearchList(SearchListView):
    model = Startup
    paginate_by = 30
    template_name = "startup/startup_list.html"
    form_class = StartupSearchForm
    filter_class = StartupFilter


class StartupSelected(ListView):
    model = Startup
    context_object_name = 'startup'
    # slug_field = 'name'
    # slug_url_kwarg = 'name'
    # queryset = Startup.objects.filter(selected=True)
    template_name = 'startup/startup_list.html'
    paginate_by = 10

    # def get_queryset(self):
    #     """
    #     Список наших объектов будет состоять лишь из отмеченных модераторами токенов
    #     """
    #     return Startup.objects.filter(selected=True)

class StartupDetail(DetailView):
    model = Startup
    # These next two lines tell the view to index lookups by username
    slug_field = 'token_id'
    slug_url_kwarg = 'token_id'
