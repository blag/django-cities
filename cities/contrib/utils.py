import swapper

from cities.models import (  # noqa F401
    Continent, Country, Region, Subregion, City, District, PostalCode,
    AlternativeName)


def get_cities_models():
    return (
        swapper.load_model('cities', 'Continent'),
        swapper.load_model('cities', 'Country'),
        Region,
        Subregion,
        swapper.load_model('cities', 'City'),
        District,
        PostalCode,
        AlternativeName,
    )
