import datetime as dt

from traffic_director_system_app.dao.click_dao import ClickDao


class ClickService:

    @staticmethod
    def create_click(redirect_link, ip_address):
        return ClickDao().create_click(redirect_link=redirect_link, ip_address=ip_address)

    @staticmethod
    def get_redirect_link_clicks(redirect_link_id):
        clicks = ClickDao().get_click_count(redirect_link_id)
        return clicks

    @staticmethod
    def get_clicks_over_time(redirect_link_id):
        clicks = ClickDao().get_clicks_over_time(redirect_link_id)
        click_hours = []
        click_count = []
        for item in clicks:
            click_hours.append(item['hour'])
            click_count.append(item['count'])
        click_count.append(0)
        return click_hours, click_count

    @staticmethod
    def get_user_clicks(ip_address):
        return ClickDao().get_user_clicks(ip_address)
