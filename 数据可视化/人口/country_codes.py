from pygal_maps_world.i18n import COUNTRIES


def get_country_code(country_name):
    """通过国家名称寻找国别码"""
    for code, name in COUNTRIES.items():
        if name == country_name:
            return code
    return None
