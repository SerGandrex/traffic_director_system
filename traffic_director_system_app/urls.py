"""traffic_director_system URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path

from .views import RedirectLinkView, LandingPageView, UserStatistics

urlpatterns = [
    path("", RedirectLinkView.home, name="home"),
    path("redirect-link/", RedirectLinkView.get_redirect_links, name="get_redirect_links"),
    path("redirect-link/create", RedirectLinkView.create_redirect_link, name="create_redirect_link"),
    path("redirect-link/<int:redirect_link_id>/clicks/", RedirectLinkView.get_redirect_link_clicks,
         name="get_redirect_link_clicks"),
    path("landing-page/<int:redirect_link_id>/get", LandingPageView.get_landing_pages, name="get_landing_pages"),
    path("landing-page/<int:redirect_link_id>/create/", LandingPageView.create_landing_page,
         name="create_landing_page"),
    path("landing-page/delete/<int:landing_page_id>/<int:redirect_link_id>", LandingPageView.delete_landing_page,
         name="delete_landing_page"),
    path("landing-page/update/<int:landing_page_id>/<int:redirect_link_id>", LandingPageView.update_landing_page,
         name="update_landing_page"),
    path("landing-page/traffic-redirect/<int:redirect_link_id>", LandingPageView.traffic_redirect,
         name="traffic_redirect"),
    path('clicks-chart/<int:redirect_link_id>', RedirectLinkView.clicks_chart, name='clicks_chart'),
    path('user-statistics/', UserStatistics.get_user_statistics, name='user_statistics'),
]