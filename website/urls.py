from django.urls import path
from . import views

urlpatterns = [
    path('login/', views.log, name='log'),
    path('signup/', views.signup, name='signup'),
    path('for_candidates/', views.for_candidates, name='for_candidates'),
    path('for_employers/', views.for_employers, name='for_employers'),
    path('candidate_profile/', views.candidate_profile, name='candidate_profile'),
    path('post_job/', views.post_job, name='post_job'),
    path('candidates/', views.candidates, name='candidates'),
    path('employers_profile/', views.employers_profile, name='employers_profile'),
    path('search/', views.search, name='search'),
]
