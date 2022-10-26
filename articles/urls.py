from django.urls import path,include
from articles import views

urlpatterns = [
    path("",views.articleslist.as_view(), name="index"),
    path("<int:article_id>/",views.articlestDetail.as_view(), name="articles_view")
]
