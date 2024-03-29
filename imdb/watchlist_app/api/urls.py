from django.urls import path, include
from rest_framework.routers import DefaultRouter
# from watchlist_app.api.views import movie_list, movie_detail
from watchlist_app.api.views import (WatchListAV, WatchListDetailAV,StreamPlatformAV,StreamPlatformVS
                                     ,StreamPlatformDetailAV, WatchListGV,ReviewCreate,UserReview, ReviewList,ReviewDetail)


router = DefaultRouter()
router.register("stream", StreamPlatformVS, basename='streamplatform')


urlpatterns = [
    path('list/', WatchListAV.as_view(), name='movie-list'),
    path('<int:pk>', WatchListDetailAV.as_view(), name='movie-detail'),
    
    # search
    path('list2/', WatchListGV.as_view(), name='watch-list'),
    
    path('', include(router.urls)),
    
    # path('stream/', StreamPlatformAV.as_view(), name='stream'),
    # path('stream/<int:pk>', StreamPlatformDetailAV.as_view(), name='stream-detail'),
    
    # path('review/', ReviewList.as_view(), name='review'),
    # path('review/<int:pk>', ReviewDetail.as_view(), name='review-detail')
    
    path('<int:pk>/review-create',  ReviewCreate.as_view(), name='review-create'),
    path('<int:pk>/reviews',  ReviewList.as_view(), name='review'),
    path('review/<int:pk>', ReviewDetail.as_view(), name='review-detail'),
    path('review/', UserReview.as_view(), name='user-review-detail'),
    
]
