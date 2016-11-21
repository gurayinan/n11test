from modules import *


class N11BasePage(object):

    def __init__(self):
        self.settings_location = os.path.join(os.getcwd(), 'n11', 'settings.ini')
        self.settings = {}
        self.parse_settings()
        self.driver = None
        self.select_browser()
        self.wait = WebDriverWait(self.driver, 30)

    def parse_settings(self):
        try:
            config = ConfigParser.ConfigParser()
            config.read(self.settings_location)
            for section in config.sections():
                for option in config.options(section):
                    self.settings[option] = config.get(section, option)
        except StandardError:
            raise

    def init_chrome(self):
        try:
            if self.settings is not None:
                self.driver = webdriver.Chrome(self.settings.get('chromedriver_path'))
                width = self.driver.execute_script("return window.screen.availWidth")
                height = self.driver.execute_script("return window.screen.availHeight")
                self.driver.set_window_position(0, 0)
                self.driver.set_window_size(width, height)
        except StandardError:
            raise

    def init_firefox(self):
        try:
            if self.settings is not None:
                self.driver = webdriver.Firefox(self.settings.get('geckodriver_path'))
                self.driver.maximize_window()
        except StandardError:
            raise

    def select_browser(self):
        try:
            if self.settings is not None:
                desired_browser = self.settings.get('desired_browser')
                if desired_browser == "chrome":
                    self.init_chrome()
                elif desired_browser == "firefox":
                    self.init_firefox()
                else:
                    raise StandardError("Selected browser not valid.")
        except StandardError:
            raise


class N11MainPage(N11BasePage):

    def redirect_to_login(self):
        try:
            self.wait.until(ec.element_to_be_clickable(N11MainPageLocators.LOGIN_LINK)).click()
        except StandardError:
            raise

    def search_products(self, search_for):
        try:
            self.wait.until(ec.element_to_be_clickable(N11MainPageLocators.SEARCH_FIELD)).send_keys(search_for)
            self.wait.until(ec.element_to_be_clickable(N11MainPageLocators.SEARCH_BUTTON)).click()
        except StandardError:
            raise


class N11LoginPage(N11BasePage):

    def login_user(self):
        try:
            if self.settings is not None:
                email = self.settings.get('user_mail')
                password = self.settings.get('user_password')
                self.wait.until(ec.element_to_be_clickable(N11LoginPageLocators.EMAIL_FIELD)).send_keys(email)
                self.wait.until(ec.element_to_be_clickable(N11LoginPageLocators.PASSWORD_FIELD)).send_keys(password)
                self.wait.until(ec.element_to_be_clickable(N11LoginPageLocators.LOGIN_SUBMIT)).click()
        except StandardError:
            raise


class N11SearchResultsPage(N11BasePage):

    def search_check(self):
        try:
            search_detail = self.wait.until(ec.presence_of_element_located(N11SearchResultPageLocators.SEARCH_RESULT_TEXT))
            return search_detail.text
        except StandardError:
            raise

    def change_page(self):
        try:
            self.driver.execute_script('window.scrollTo(0,document.body.scrollHeight);') #to be able to see pagination
            self.driver.execute_script('$.fancybox.close()') #for closing campaign shows on search page
            pagination = self.driver.find_element_by_link_text('2')
            pagination.click()
            return self.driver.current_url
        except StandardError:
            raise

    def add_favorite_product(self):
        try:
            self.driver.execute_script('window.scrollTo(0, 500);')
            third_prod = self.driver.find_element_by_css_selector('.followBtn:nth-child(3)')
            third_prod.click()
        except StandardError:
            raise

    def navigate_to_favorites(self):
        try:
            self.driver.execute_script('window.scrollTo(0, 0)')
            hover_to_menu = self.driver.find_element_by_class_name('myAccount')
            hover = ActionChains(self.driver).move_to_element(hover_to_menu)
            hover.perform()
            favorites_list = self.driver.find_element_by_link_text('Favorilerim')
            favorites_list.click()
        except StandardError:
            raise


class N11FavoritesPage(N11BasePage):

    def check_list(self):
        try:
            self.wait.until(ec.presence_of_element_located(N11FavoriteProductsPageLocators.EMPTY_WATCHLIST))
        except StandardError:
            raise

    def delete_item(self):
        try:
            self.wait.until(ec.element_to_be_clickable(N11FavoriteProductsPageLocators.DELETE_PRODUCT)).click()
        except StandardError:
            raise



