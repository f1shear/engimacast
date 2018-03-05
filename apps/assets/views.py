from django.views.generic import TemplateView


class AssetListView(TemplateView):
    template_name = "assets/assets.html"


class AssetDetailView(TemplateView):
    template_name = "assets/asset.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['asset_id'] = self.kwargs['pk']
        return context