from traffic_director_system_app.dao.base_dao import BaseDAO
from traffic_director_system_app.models import RedirectLink


class RedirectLinkDao(BaseDAO):
    MODEL_CLASS = RedirectLink

    def get_all_redirect_links(self):
        return self.get_all()

    def get_redirect_link(self, key):
        return self.get(key)

