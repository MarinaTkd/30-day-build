import unittest
from fetch_page import fetch_clean_text

class TestFetchPage(unittest.TestCase):
    def test_fetch_clean_text_return_text(self):
        url = "https://www.novinky.cz/clanek/domaci-vojaci-dostanou-nove-prilby-za-14-600-kusu-zaplati-skoro-dve-miliardy-korun-40531564#dop_ab_variant=0&dop_source_zone_name=novinky.sznhp.box&source=hp&seq_no=1&utm_campaign=&utm_medium=z-boxiku&utm_source=www.seznam.cz"
        result = fetch_clean_text(url)

        #check if something is returned
        self.assertIsInstance(result, str)
        self.assertTrue(len(result)>0)

if __name__ == "__main__":
    unittest.main()