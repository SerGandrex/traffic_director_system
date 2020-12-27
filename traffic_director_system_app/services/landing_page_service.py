import numpy as np
from django.forms import model_to_dict
from numpy.random.mtrand import choice

from traffic_director_system_app.dao.landing_page_dao import LandingPageDao


class LandingPageService:

    @staticmethod
    def get_landing_page(key):
        return LandingPageDao().get_landing_page(key)

    @staticmethod
    def delete_landing_page(key):
        return LandingPageDao().delete_landing_page(key)

    @staticmethod
    def filter_landing_page(**kwargs):
        return LandingPageDao().filter_landing_page(**kwargs)

    @staticmethod
    def traffic_redirect(redirect_link_id, country):
        landing_page_url = 'https://www.google.com/'

        if LandingPageDao.get_landing_pages_existence(redirect_link=redirect_link_id, country=country):
            landing_pages = LandingPageDao().filter_landing_page(redirect_link=redirect_link_id, country=country)
        else:
            landing_pages = LandingPageDao().filter_landing_page(redirect_link=redirect_link_id, country='default')

        if landing_pages:
            weights = []
            urls = []
            for item in landing_pages:
                if item.weight:
                    urls.append(item.url)
                    weights.append(item.weight)

            if weights:
                p = np.array(weights)
                p /= p.sum()
                landing_page_url = choice(urls, 1, p=p, replace=False)[0]
            else:
                landing_page_url = choice(landing_pages, 1)[0].url

        return landing_page_url



