from django.views.generic import TemplateView
from dashboard.radar.utils import get_websocket_data
from dashboard.radar.models.models_radar import Radar
import datetime


class DashboardView(TemplateView):
    template_name = 'pages/home.html'

    def get_last_date(self, notifications):
        notifications.sort(key=lambda x: datetime.datetime.strptime(x['date'], '%d/%m/%Y'))
        return notifications[0]['date']

    def get_last_infractions(self, notifcations):
        notifcations.sort(
            key=lambda x: datetime.datetime.strptime(
                x['date'] + ' ' + x['time'], '%d/%m/%Y %H:%M:%S'
            ),
            reverse=True
        )

        return notifcations[:5]

    def get_context_data(self, **kwargs):
        context = super(DashboardView, self).get_context_data(**kwargs)
        infractions, statuses, notify_infraction, notify_feasible = get_websocket_data()
        radars = Radar.objects.all()
        context['radars'] = radars
        context['infractions'] = infractions
        context['notify_feasible'] = notify_feasible
        context['notify_infraction'] = notify_infraction
        context['total_notifications'] = len(notify_feasible) + len(notify_infraction)
        context['statuses'] = statuses['response_message']
        context['last_updated'] = self.get_last_date(notify_infraction)
        context['last_infractions'] = self.get_last_infractions(notify_infraction)
        return context
