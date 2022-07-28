from django.views.generic.edit import CreateView
from django.urls import reverse, reverse_lazy

from .models import Crm
from .forms import CrmForm
# Create your views here.
class CrmCreateView(CreateView):
    model = Crm
    template_name = 'crm.html'
    form_class = CrmForm
    success_url = reverse_lazy('crm_form')


