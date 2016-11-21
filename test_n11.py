from n11.n11 import *


class N11TestCases(unittest.TestCase, N11LoginPage, N11MainPage, N11SearchResultsPage, N11FavoritesPage):

    def setUp(self):
        N11MainPage.__init__(self)
        self.driver.get("http://www.n11.com")

    def test_main(self):
        self.redirect_to_login()
        self.login_user()
        self.search_products('samsung')
        search_text = self.search_check()
        self.assertIn('Samsung', search_text, 'Search result assertion failed.')
        current_page_url = self.change_page()
        self.assertIn('pg=2',current_page_url, 'Page change failed.')
        self.add_favorite_product()
        self.navigate_to_favorites()
        self.delete_item()
        self.check_list()

    def tearDown(self):
        self.driver.close()
