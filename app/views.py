from django.http import HttpResponseRedirect, JsonResponse
from django.shortcuts import render
from django_tables2 import RequestConfig

from app.forms import InterestForm
from app.models import Interest
from app.tables import InterestTable


def index(request):
    return render(request, "index.html")


def home(request):
    return render(request, "home.html")


def get_interests(request):
    # Process data
    if request.method == 'POST':
        form = InterestForm(request.POST)
        # Check the validity of the form
        if form.is_valid():
            name = form.cleaned_data['name']
            if not Interest.objects.filter(name=name).exists():
                interest = form.save(commit=False)
                interest.save()
                return HttpResponseRedirect('/user/interests/')
            else:
                form.add_error(field='name', error="Duplicated value")

        interests = InterestTable(Interest.objects.all())
        RequestConfig(request, paginate={'per_page': 25}).configure(interests)
        return render(request, 'interest.html', {'form': form, 'interests': interests})
    else:
        interests = InterestTable(Interest.objects.all())
        RequestConfig(request, paginate={'per_page': 25}).configure(interests)
        form = InterestForm()
        return render(request, 'interest.html', {'form': form, 'interests': interests})
