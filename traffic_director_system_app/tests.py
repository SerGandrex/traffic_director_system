from unittest.mock import patch, Mock

from django.test import TestCase

from traffic_director_system_app.services.landing_page_service import LandingPageService
from traffic_director_system_app.services.redirect_link_service import RedirectLinkService


class RedirectLinkServiceTestCase(TestCase):

    @patch('traffic_director_system_app.services.redirect_link_service.RedirectLinkDao.get_all_redirect_links',
           Mock(return_value=['redirect_link_1', 'redirect_link_2']))
    def test_get_redirect_links(self):
        result = RedirectLinkService.get_redirect_links()

        self.assertEqual(['redirect_link_1', 'redirect_link_2'], result)

    @patch('traffic_director_system_app.services.redirect_link_service.RedirectLinkDao.get_redirect_link',
           Mock(return_value='redirect_link_1'))
    def test_get_redirect_link(self):
        result = RedirectLinkService.get_redirect_link('id')

        self.assertEqual('redirect_link_1', result)


class LandingPageServiceTestCase(TestCase):

    @patch('traffic_director_system_app.services.landing_page_service.LandingPageDao.get_landing_page',
           Mock(return_value='landing_page'))
    def test_get_landing_page(self):
        result = LandingPageService.get_landing_page('key')

        self.assertEqual('landing_page', result)

    @patch('traffic_director_system_app.services.landing_page_service.LandingPageDao.delete_landing_page',
           Mock(return_value=True))
    def test_delete_landing_page(self):
        result = LandingPageService.delete_landing_page('key')

        self.assertTrue(result)

    @patch('traffic_director_system_app.services.landing_page_service.LandingPageDao.filter_landing_page',
           Mock(return_value=['landing_page_1', 'landing_page_2']))
    def test_filter_landing_page(self):
        result = LandingPageService.filter_landing_page(**{'key': 'value'})

        self.assertEqual(['landing_page_1', 'landing_page_2'], result)