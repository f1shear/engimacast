from django.views.generic import TemplateView


class ChatRoomListView(TemplateView):
    template_name = "chat/list.hml"


class ChatRoomDetailView(TemplateView):
    template_name = "chat/room.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['room'] = 'Dummy'
        return context


class ChatRoomGlobalView(TemplateView):
    template_name = "chat/global.html"
