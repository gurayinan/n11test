from selenium.webdriver.common.by import By


class N11MainPageLocators(object):
    LOGIN_LINK = (By.CLASS_NAME, "btnSignIn")
    SEARCH_FIELD = (By.ID, "searchData")
    SEARCH_BUTTON = (By.CLASS_NAME, "searchBtn")


class N11LoginPageLocators(object):
    EMAIL_FIELD = (By.ID, "email")
    PASSWORD_FIELD = (By.ID, "password")
    LOGIN_SUBMIT = (By.ID, "loginButton")


class N11SearchResultPageLocators(object):
    SEARCH_RESULT_TEXT = (By.CLASS_NAME, "resultText")
    RESULT_SECOND_PAGE = (By.CSS_SELECTOR, "//*[@id=\"contentListing\"]/div/div/div[2]/div[3]/a[2]")
    FAVORITES_BUTTON = (By.CSS_SELECTOR, "a[href*=\"hesabim/favorilerim\"]")


class N11FavoriteProductsPageLocators(object):
    DELETE_PRODUCT = (By.CLASS_NAME, "removeSelectedProduct")
    EMPTY_WATCHLIST = (By.CLASS_NAME, "emptyWatchList")

