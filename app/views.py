from django.contrib import messages
from django.http import HttpResponseRedirect, JsonResponse
from django.shortcuts import render
from django_tables2 import RequestConfig

from app.forms import InterestForm, ContentForm
from app.models import Interest, Content, ContentType
from app.tables import InterestTable, ContentTable


def index(request):
    if request.method == 'POST':
        form = ContentForm(request.POST)
        # Check the validity of the form
        if form.is_valid():
            content = form.cleaned_data['content']
            if not Content.objects.filter(content=content).exists():
                content = form.save(commit=False)
                content.save()
                messages.success(request, 'Content submitted successfully.')
                return HttpResponseRedirect('/user/')
            else:
                form.add_error(field='content', error="Duplicated value")

        interests = Interest.objects.all()
        return render(request, 'interest.html', {'form': form, 'interests': interests})
    else:
        interests = Interest.objects.all()
        form = ContentForm()
        return render(request, "index.html", {"interests": interests, "form": form})


def home(request):
    contents = ContentTable(Content.objects.all())
    RequestConfig(request, paginate={'per_page': 25}).configure(contents)
    return render(request, "home.html", {"contents": contents})


def get_interests(request):
    # Process data
    if request.method == 'POST':
        form = InterestForm(request.POST)
        # Check the validity of the form
        if form.is_valid():
            name = form.cleaned_data['name']
            if not Interest.objects.filter(name=name).exists():
                interest = form.save(commit=False)
                interest['type'] = ContentType.objects.get(name="text")
                interest.save()
                messages.success(request, 'Interest submitted successfully.')
                return HttpResponseRedirect('/user/interests')
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
