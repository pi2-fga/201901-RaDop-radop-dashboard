from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse
from django.views.generic import DetailView, ListView, RedirectView, UpdateView
from dashboard.notification.models import Notification, Penalty
from dashboard.radar.utils import get_websocket_data
import json


class NotificationDetailView(LoginRequiredMixin, DetailView):

    model = Notification
    slug_field = "identifier"
    slug_url_kwarg = "identifier"
    fields = ["vehicle_plate"]


notification_detail_view = NotificationDetailView.as_view()


class NotificationListView(LoginRequiredMixin, ListView):

    model = Notification
    slug_field = "notification_type"
    slug_url_kwarg = "notification_type"


notification_list_view = NotificationListView.as_view()


class NotificationUpdateView(LoginRequiredMixin, UpdateView):

    model = Notification
    fields = ["notification_type"]

    def get_success_url(self):
        return reverse("notification:detail", kwargs={"notification_type": self.request.notification.notification_type})

    def get_object(self):
        return notification.objects.get(notification_type=self.request.notification.notification_type)


notification_update_view = NotificationUpdateView.as_view()


class NotificationRedirectView(LoginRequiredMixin, RedirectView):

    permanent = False

    def get_redirect_url(self):
        return reverse("notification:detail", kwargs={"notification_type": self.request.notification.notification_type})


notification_redirect_view = NotificationRedirectView.as_view()
