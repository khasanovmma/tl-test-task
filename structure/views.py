from django.views.generic import ListView

from .models import Employee

class EmployeeListView(ListView):
    
    template_name = 'structure/index.html'
    queryset = Employee.objects.filter(parent=None)
    context_object_name = "employees"
    paginate_by = 5

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(EmployeeListView, self).get_context_data(**kwargs)
        context['employees_count'] = Employee.objects.all().count()
        return context
