import pytest
from scraper import fetch_clean_text


def test_fetch_clean_text_valid_url():
    url = "https://www.novinky.cz/clanek/kultura-filmy-serialy-dabel-nosi-pradu-po-dvaceti-letech-v-pokracovani-modni-klasiky-se-objevi-i-ceska-topmodelka-40532934#dop_ab_variant=0&dop_source_zone_name=novinky.sznhp.box&source=hp&seq_no=2&utm_campaign=&utm_medium=z-boxiku&utm_source=www.seznam.cz"
    result = fetch_clean_text(url)
    assert isinstance(result, str)
    assert len(result)>0

def test_fetch_clean_text_invalid_url():
    url = "_invalid.com"
    result = fetch_clean_text(url)
    assert result is None


