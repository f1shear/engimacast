from django.views.generic import TemplateView


class CompanyListView(TemplateView):
    template_name = "company/companies.html"


class CompanyDetailView(TemplateView):
    template_name = "company/company.html"
