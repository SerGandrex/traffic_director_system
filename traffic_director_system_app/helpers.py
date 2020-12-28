from django.contrib.gis.geoip2 import GeoIP2


class RequestIp:

    @staticmethod
    def get_client_ip(request):
        x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
        if x_forwarded_for:
            ip = x_forwarded_for.split(',')[-1].strip()
        elif request.META.get('HTTP_X_REAL_IP'):
            ip = request.META.get('HTTP_X_REAL_IP')
        else:
            ip = request.META.get('REMOTE_ADDR')
        return ip


class CountryLimitation:

    @staticmethod
    def get_country_by_ip(ip):
        try:
            g = GeoIP2()
            return g.country(ip)
        except Exception:
            return False

