from django.contrib import admin
from django.urls import path
from firstAPPE1.views import index, renderTripulacion1, renderTripulacion2, renderTripulacion3, renderPagina1, renderPagina2, renderPagina3

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index),
    path('Tripulacion1/', renderTripulacion1),
    path('Tripulacion2/', renderTripulacion2),
    path('Tripulacion3/', renderTripulacion3),
    path('pagina1/',renderPagina1),
    path('pagina2/',renderPagina2),
    path('pagina3/',renderPagina3),



]