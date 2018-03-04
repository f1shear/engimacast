from django.views.generic import TemplateView


class AssistantView(TemplateView):
    template_name = "trade/assistant.html"


class MediaView(TemplateView):
    template_name = "trade/media.html"


class ToolsView(TemplateView):
    template_name = "trade/tools.html"
