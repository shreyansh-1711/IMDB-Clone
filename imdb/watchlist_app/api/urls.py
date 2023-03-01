from django.urls import path, include
# from watchlist_app.api.views import movie_list, movie_detail
from watchlist_app.api.views import (WatchListAV, WatchListDetailAV,StreamPlatformAV
                                     ,StreamPlatformDetailAV,ReviewCreate, ReviewList,ReviewDetail)

urlpatterns = [
    path('list/', WatchListAV.as_view(), name='movie_list'),
    path('<int:pk>', WatchListDetailAV.as_view(), name='movie-detail'),
    path('stream/', StreamPlatformAV.as_view(), name='stream'),
    path('stream/<int:pk>', StreamPlatformDetailAV.as_view(), name='stream-detail'),
    
    # path('review/', ReviewList.as_view(), name='review'),
    # path('review/<int:pk>', ReviewDetail.as_view(), name='review-detail')
    
    path('stream/<int:pk>/review-create',  ReviewCreate.as_view(), name='review-create'),
    path('stream/<int:pk>/review',  ReviewList.as_view(), name='review'),
    path('stream/review/<int:pk>', ReviewDetail.as_view(), name='review-detail'),
]
