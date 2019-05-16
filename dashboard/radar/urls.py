from django.urls import path

from dashboard.radar.views import (
    radar_list_view,
    radar_redirect_view,
    radar_update_view,
    radar_detail_view,
)

app_name = "radar"
urlpatterns = [
    path("", view=radar_list_view, name="list"),
    path("~redirect/", view=radar_redirect_view, name="redirect"),
    path("~update/", view=radar_update_view, name="update"),
    path("<str:name>/", view=radar_detail_view, name="detail"),
]
