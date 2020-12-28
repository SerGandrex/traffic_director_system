import urllib.request
from django.http import JsonResponse
from django.shortcuts import render, redirect
from .forms import RedirectLinkCreateForm, LandingPageCreateUpdateForm
from .helpers import RequestIp, CountryLimitation
from .services.click_service import ClickService
from .services.redirect_link_service import RedirectLinkService
from .services.landing_page_service import LandingPageService

# Create your views here.


class RedirectLinkView:

    @staticmethod
    def home(request):
        return render(request, 'index.html')

    @staticmethod
    def get_redirect_links(request):
        redirect_links = RedirectLinkService.get_redirect_links()
        return render(request, 'redirect-links.html', {'redirect_links': redirect_links})

    @staticmethod
    def create_redirect_link(request):
        form = RedirectLinkCreateForm()
        if request.method == 'POST':
            form = RedirectLinkCreateForm(request.POST)
            if form.is_valid():
                form.save()
                return redirect(RedirectLinkView.get_redirect_links)
            else:
                return redirect(RedirectLinkView.get_redirect_links)
        else:
            return render(request, 'create-redirect-link.html', {'form': form})

    @staticmethod
    def get_redirect_link_clicks(request, redirect_link_id):
        click = ClickService.get_redirect_link_clicks(redirect_link_id)
        return render(request, 'statistics.html', {'redirect_link_id': redirect_link_id, 'click': click})

    @staticmethod
    def clicks_chart(request, redirect_link_id):
        click_hours, count_click = ClickService.get_clicks_over_time(redirect_link_id)
        return JsonResponse(data={
            'count_click': count_click,
            'click_hours': click_hours
        })


class LandingPageView:

    @staticmethod
    def get_landing_pages(request, redirect_link_id):
        landing_pages = LandingPageService.filter_landing_page(redirect_link=redirect_link_id)
        return render(request, 'landing-pages.html', {'landing_pages': landing_pages})

    @staticmethod
    def create_landing_page(request, redirect_link_id=None):
        redirect_link = RedirectLinkService.get_redirect_link(redirect_link_id)
        form = LandingPageCreateUpdateForm()
        if request.method == 'POST':
            form = LandingPageCreateUpdateForm(request.POST)
            if form.is_valid():
                form = form.save(commit=False)
                form.redirect_link = redirect_link
                form.save()
                return redirect(LandingPageView.get_landing_pages, redirect_link_id)
            else:
                return redirect(LandingPageView.get_landing_pages, redirect_link_id)
        else:
            return render(request, 'create-update-landing-page.html', {'form': form})

    @staticmethod
    def delete_landing_page(request, redirect_link_id, landing_page_id):
        LandingPageService.delete_landing_page(landing_page_id)
        return redirect(LandingPageView.get_landing_pages, redirect_link_id)

    @staticmethod
    def update_landing_page(request, landing_page_id, redirect_link_id):
        redirect_link = RedirectLinkService.get_redirect_link(redirect_link_id)
        landing_page = LandingPageService.get_landing_page(landing_page_id)
        if request.method == 'POST':
            form = LandingPageCreateUpdateForm(request.POST, instance=landing_page)
            if form.is_valid():
                form = form.save(commit=False)
                form.redirect_link = redirect_link
                form.save()
                return redirect(LandingPageView.get_landing_pages, redirect_link_id)
        else:
            data = {"url": landing_page.url, "country": landing_page.country, "weight": landing_page.weight}
            form = LandingPageCreateUpdateForm(initial=data)
        return render(request, 'create-update-landing-page.html', {'form': form})

    @staticmethod
    def traffic_redirect(request, redirect_link_id):
        ip_address = RequestIp.get_client_ip(request)
        if ip_address == '127.0.0.1':
            ip_address = urllib.request.urlopen('https://api.ipify.org').read().decode()
        country = CountryLimitation.get_country_by_ip(ip_address)
        landing_page_url = LandingPageService.traffic_redirect(redirect_link_id, country['country_code'])
        ClickService.create_click(RedirectLinkService
                                  .get_redirect_link(redirect_link_id), ip_address, country['country_code'])
        return redirect(landing_page_url)


class UserStatistics:

    @staticmethod
    def get_user_statistics(request):
        ip_address = RequestIp.get_client_ip(request)
        if ip_address == '127.0.0.1':
            ip_address = urllib.request.urlopen('https://api.ipify.org').read().decode()

        user_clicks = ClickService.get_user_clicks(ip_address)
        return render(request, 'user-statistics.html', {'user_clicks': user_clicks})

