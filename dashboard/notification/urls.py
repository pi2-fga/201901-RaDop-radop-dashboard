from django.urls import path

from dashboard.notification.views import (
    notification_list_view,
    notification_redirect_view,
    notification_update_view,
    notification_detail_view,
)

app_name = "notification"
urlpatterns = [
    path("", view=notification_list_view, name="list"),
    path("~redirect/", view=notification_redirect_view, name="redirect"),
    path("~update/", view=notification_update_view, name="update"),
    path("<str:identifier>/", view=notification_detail_view, name="detail"),
]
