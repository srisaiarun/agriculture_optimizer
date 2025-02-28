from django.shortcuts import render
from .forms import FarmDataForm
from .utils import optimize_costs

def home(request):
    result = None
    if request.method == 'POST':
        form = FarmDataForm(request.POST)
        if form.is_valid():
            transport_costs = form.cleaned_data['transport_costs']
            constraints = form.cleaned_data['constraints']
            result = optimize_costs(transport_costs, constraints)
    else:
        form = FarmDataForm()

    return render(request, 'optimizer/home.html', {'form': form, 'result': result})

def result_view(request):
    return render(request, 'optimizer/result.html')
