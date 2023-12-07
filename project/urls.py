from django.contrib import admin
from django.urls import path, include
from tickets import views
from rest_framework.routers import DefaultRouter
from rest_framework.authtoken.views import obtain_auth_token

router = DefaultRouter()
router.register('guests', views.viewsets_guest)
router.register('movies', views.viewsets_movie)
router.register('reservations', views.viewsets_reservation)

urlpatterns = [
    # grappelli admin panel theme

    path('grappelli/', include('grappelli.urls')),
    path('admin/', admin.site.urls),

    # 1
    path('django/jsonresponsenomodel/', views.no_rest_no_model),

    # 2
    path('django/jsonresponsefrommodel/', views.no_rest_from_model),

    # 3.1 GET POST from rest framkework function based view @api_view
    path('rest/fbv/', views.FBV_List),

    # 3.2 GET PUT DELETE from rest framkework function based view @api_view
    path('rest/fbv/<int:pk>', views.FBV_pk),

    # 4.1 GET POST from rest framkework Class based view APIView
    path('rest/cbv/', views.CBV_List.as_view()),

    # 4.1 GET PUT DELETE from rest framkework Class based view APIView
    path('rest/cbv/<int:pk>', views.CBV_pk.as_view()),

    # 5.1 GET POST from rest framkework Class based view mixins
    path('rest/mixins/', views.mixins_list.as_view()),

    # 5.2 GET PUT DELETE from rest framkework Class based view mixins
    path('rest/mixins/<int:pk>', views.mixins_pk.as_view()),

    # 6.1 GET POST from rest framkework Class based view mixins
    path('rest/generics/', views.generics_list.as_view()),

    # 6.2 GET PUT DELETE from rest framkework Class based view mixins
    path('rest/generics/<int:pk>', views.generics_pk.as_view()),

    # 7 ViewSets
    path('rest/viewsets/', include(router.urls)),

    # 8 Find Movie
    path('fbv/findmovie', views.find_movie),

    # 9 New Reservation
    path('fbv/newreservation', views.new_reservation),

    # 10 rest auth url >>>> allowing you to logout from ur user 3ala el URL
    path('api-auth', include('rest_framework.urls')),

    # 11 Token Authentication
    path('api-token-auth', obtain_auth_token),

    # 12 Post pk generics Post_pk
    path('post/generics/<int:pk>', views.post_pk.as_view()),

]
