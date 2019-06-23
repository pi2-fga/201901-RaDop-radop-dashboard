from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse
from django.views.generic import DetailView, ListView, RedirectView, UpdateView
from dashboard.radar.models.models_radar import Radar
from dashboard.radar.utils import get_websocket_data
import json


class RadarDetailView(LoginRequiredMixin, DetailView):

    model = Radar
    slug_field = "name"
    slug_url_kwarg = "name"
    fields = ["identificacao"]


radar_detail_view = RadarDetailView.as_view()


class RadarListView(LoginRequiredMixin, ListView):

    model = Radar
    slug_field = "name"
    slug_url_kwarg = "name"


radar_list_view = RadarListView.as_view()


class RadarUpdateView(LoginRequiredMixin, UpdateView):

    model = Radar
    fields = ["name"]

    def get_success_url(self):
        return reverse("radar:detail", kwargs={"name": self.request.radar.name})

    def get_object(self):
        return Radar.objects.get(name=self.request.radar.name)


radar_update_view = RadarUpdateView.as_view()


class RadarRedirectView(LoginRequiredMixin, RedirectView):

    permanent = False

    def get_redirect_url(self):
        return reverse("radar:detail", kwargs={"name": self.request.radar.name})


radar_redirect_view = RadarRedirectView.as_view()
