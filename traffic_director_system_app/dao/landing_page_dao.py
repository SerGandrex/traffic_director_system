from django.db.models import Q

from traffic_director_system_app.dao.base_dao import BaseDAO
from traffic_director_system_app.models import LandingPage


class LandingPageDao(BaseDAO):
    MODEL_CLASS = LandingPage

    def get_landing_page(self, key):
        return self.get(key)

    def delete_landing_page(self, key):
        landing_page = self.get(key)
        return self.delete(landing_page)

    def filter_landing_page(self, **kwargs):
        return self.filter_by_kwargs(**kwargs)

    @staticmethod
    def get_landing_pages_existence(**kwargs):
        return LandingPage.objects.filter(**kwargs).exists()


