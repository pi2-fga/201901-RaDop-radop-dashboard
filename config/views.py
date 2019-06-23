from django.views.generic import TemplateView
from dashboard.radar.utils import get_websocket_data
from dashboard.radar.models.models_radar import Radar

class DashboardView(TemplateView):
    template_name = 'pages/home.html'

    def get_context_data(self, **kwargs):
        context = super(DashboardView, self).get_context_data(**kwargs)
        infractions, statuses, notifications = get_websocket_data()
        radars = Radar.objects.all()
        context['radars'] = radars
        context['infractions'] = infractions
        context['notifications'] = notifications
        context['statuses'] = statuses['response_message']
        return context
