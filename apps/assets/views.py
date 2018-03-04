from django.views.generic import TemplateView


class AssetListView(TemplateView):
    template_name = "assets/assets.html"


class AssetDetailView(TemplateView):
    template_name = "assets/asset.html"
