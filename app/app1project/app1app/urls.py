from. import views
from django.urls import path
app_name='songapp'
urlpatterns = [
    path('', views.index, name='index'),
    path('song/<int:song_id>/',views.detail,name="detail"),
    path('add/',views.add_song,name='add_song'),
    path('update/<int:id>/',views.update,name='update'),
    path('delete/<int:id>/',views.delete,name='delete')

]