from django.contrib.postgres.aggregates import ArrayAgg
from django.db.models import Count, Max

from traffic_director_system_app.dao.base_dao import BaseDAO
from traffic_director_system_app.models import Click


class ClickDao(BaseDAO):
    MODEL_CLASS = Click

    def create_click(self, **kwargs):
        click = self.MODEL_CLASS(**kwargs)
        return self.save(click)

    def get_click_count(self, redirect_link_id):
        clicks = self.MODEL_CLASS.objects.filter(redirect_link=redirect_link_id)\
            .values('redirect_link_id', 'redirect_link__short_url_identifier', 'redirect_link__click__ip_address')\
            .order_by('-redirect_link__click__created_at')\
            .annotate(clicks=Count('id'))\
            .annotate(country_count=Count('country', distinct=True))\
            .annotate(unique_clicks=Count('ip_address', distinct=True))

        return clicks.first()

    def get_clicks_over_time(self, redirect_link_id):
        clicks = self.MODEL_CLASS.objects.extra({'hour': "date_trunc('hour', created_at)"})\
            .filter(redirect_link_id=redirect_link_id)\
            .order_by()\
            .values('hour')\
            .annotate(count=Count('id'))

        return clicks

    def get_user_clicks(self, ip_address):
        return self.MODEL_CLASS.objects.filter(ip_address=ip_address)\
            .values('redirect_link__short_url_identifier', 'ip_address', 'created_at')\

