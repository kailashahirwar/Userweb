import django_tables2 as tables

from app.models import Interest, Content


class InterestTable(tables.Table):
    class Meta:
        model = Interest
        template_name = 'django_tables2/bootstrap.html'


class ContentTable(tables.Table):
    class Meta:
        model = Content
        template_name = 'django_tables2/bootstrap.html'
