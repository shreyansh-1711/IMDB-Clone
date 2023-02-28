from django.urls import path, include
# from watchlist_app.api.views import movie_list, movie_detail
from watchlist_app.api.views import WatchListAV, WatchListDetailAV,StreamPlatformAV

urlpatterns = [
    path('list/', WatchListAV.as_view(), name='movie_list'),
    path('<int:pk>', WatchListDetailAV.as_view(), name='movie_detail'),
    path('stream/', StreamPlatformAV.as_view(), name='stream')
]
