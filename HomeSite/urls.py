
from django.contrib import admin
from django.urls import path, include, re_path
from django.views.generic import TemplateView
from Account import views
urlpatterns = [

    path('', TemplateView.as_view(template_name='index.html'), name='home'),
    path('register/',views.register_request, name='register'),
    path('login/', views.login_request, name='login'),
    path('logout/', views.logout_request, name='logout'),
    path('blog/', views.NewsList, name='blog'),
    path('pc_news_details/', TemplateView.as_view(template_name='pc_news_details.html'), name='pc_news_details'),

    path('elements/', TemplateView.as_view(template_name='elements.html'), name='elements'),
    path('pc_news/', TemplateView.as_view(template_name='pc_news.html'), name='pc_news'),
    path('fix/', TemplateView.as_view(template_name='fix.html'), name='fix'),
    path('fix_details/', TemplateView.as_view(template_name='fix_details.html'), name='fix_details'),

    path('pc_download/', TemplateView.as_view(template_name='pc_download.html'), name='pc_download'),
    #path('account/', include('django.contrib.auth.urls')),
    path('contact/', TemplateView.as_view(template_name='Contact.html'), name='contact'),
    path('about/', TemplateView.as_view(template_name='About.html'), name='about'),
    path('blog/<int:id>/', views.NewsDetail, name='NewsDetails'),
    path('android_download/<int:id>/', views.GameDetail, name='NewsDetails'),
    path('android_download/', views.GameList, name='mobdown'),  #mobile download
]
