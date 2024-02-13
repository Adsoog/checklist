from django.urls import path
from .views import persona_crud, desempeno_crud, persona_desempeno_crud

urlpatterns = [
    path('', persona_crud, name='persona_crud'),
    path('desempeno_crud/', desempeno_crud, name='desempeno_crud'),
    path('persona_desempeno_crud/', persona_desempeno_crud, name='persona_desempeno_crud'),

]
