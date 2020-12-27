from traffic_director_system_app.dao.redirect_link_dao import RedirectLinkDao


class RedirectLinkService:

    @staticmethod
    def get_redirect_links():
        queryset = RedirectLinkDao().get_all_redirect_links()
        return queryset

    @staticmethod
    def get_redirect_link(key):
        queryset = RedirectLinkDao().get_redirect_link(key)
        return queryset





