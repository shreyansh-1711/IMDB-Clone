
# from django.shortcuts import render
# from watchlist_app.models import Movie
# from django.http import JsonResponse


# def movie_list(request):
#     movies = Movie.objects.all()
#     data = {
#         'movies' : list(movies.values())
#     }
#     # print(movies.values())
#     return JsonResponse(data)


# def movie_detail(request, pk):
#     # pk = primary key 
    
#     movie = Movie.objects.get(pk=pk)
#     data = {
#         'name' : movie.name,
#         'description' : movie.description,
#         'active' : movie.active
#     }
#     print(movie)
#     return JsonResponse(data)
    
    