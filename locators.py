from selenium.webdriver.common.by import By

class HomePageLocators:
    LOGIN_REGISTER_BUTTON = (By.XPATH, "//button[contains(.,'Вход') and contains(.,'регистра')] | //button[contains(.,'Вход')]")
    POST_AD_BUTTON = (By.XPATH, "//button[contains(.,'Разместить') and contains(.,'объявл')]")
    USER_AVATAR = (By.XPATH, "//header//*[self::img or self::*[@role='img']][contains(@alt,'avatar') or contains(@class,'avatar')]")
    USER_NAME_NEAR_POST = (By.XPATH, "//header//*[contains(normalize-space(),'User') or contains(@class,'user-name')]")

class AuthModalLocators:
    MODAL = (By.XPATH, "//div[contains(@role,'dialog') or contains(@class,'modal') or contains(@class,'Dialog')]")
    TITLE = (By.XPATH, "//div[contains(@role,'dialog') or contains(@class,'modal')]//h1|//h2|//h3")
    NO_ACCOUNT_BUTTON = (By.XPATH, "//button[contains(.,'Нет аккаунта') or contains(.,'Зарегистрироваться') or contains(.,'Регистрация')]")
    HAVE_ACCOUNT_BUTTON = (By.XPATH, "//button[contains(.,'Есть аккаунт') or contains(.,'У меня уже есть') or contains(.,'Войти')]")

class RegisterFormLocators:
    FORM = (By.XPATH, "//form[.//button[contains(.,'Создать аккаунт') or contains(.,'Зарегистр')]] | //form[contains(@id,'register')]")
    NAME_INPUT = (By.XPATH, "//input[@name='name' or @id='name' or @placeholder='Имя']")
    EMAIL_INPUT = (By.XPATH, "//input[@type='email' or @name='email' or @id='email' or @placeholder='Email' or @inputmode='email']")
    PASSWORD_INPUT = (By.XPATH, "(//input[@type='password' or contains(@name,'password')])[1]")
    PASSWORD_REPEAT_INPUT = (By.XPATH, "(//input[@type='password' or contains(@name,'password')])[2]")
    CREATE_ACCOUNT_BUTTON = (By.XPATH, "//button[contains(.,'Создать аккаунт') or contains(.,'Зарегистр')]")
    ANY_ERROR_TEXT = (By.XPATH, "//div[contains(@role,'dialog') or contains(@class,'modal')]//*[contains(.,'Ошибка') or contains(.,'ошибка')]")

class LoginFormLocators:
    FORM = (By.XPATH, "//form[.//button[contains(.,'Войти')]] | //form[contains(@id,'login')]")
    EMAIL_INPUT = (By.XPATH, "//input[@type='email' or contains(@name,'email') or @id='email']")
    PASSWORD_INPUT = (By.XPATH, "//input[@type='password' or contains(@name,'password') or @id='password']")
    SUBMIT_BUTTON = (By.XPATH, "//button[contains(.,'Войти')]")

class HeaderLocators:
    LOGOUT_BUTTON = (By.XPATH, "//button[contains(.,'Выйти')] | //a[contains(.,'Выйти')]")
    PROFILE_LINK = (By.XPATH, "//a[contains(@href,'profile') or contains(@href,'account') or contains(.,'Профиль')]")

class CreateAdLocators:
    TITLE_INPUT = (By.XPATH, "//input[@name='title' or @id='title' or contains(@placeholder,'Назв')]")
    DESCRIPTION_TEXTAREA = (By.XPATH, "//textarea[@name='description' or @id='description' or contains(@placeholder,'Описание')]")
    PRICE_INPUT = (By.XPATH, "//input[@name='price' or @id='price' or @inputmode='numeric' or @type='number' or contains(@placeholder,'Стоим')]")
    CATEGORY_DROPDOWN = (By.XPATH, "//select[@name='category'] | //div[contains(@class,'select')][.//label[contains(.,'Категор')]]")
    CITY_DROPDOWN = (By.XPATH, "//select[@name='city'] | //div[contains(@class,'select')][.//label[contains(.,'Город')]]")
    CONDITION_NEW = (By.XPATH, "//label[.//input[@type='radio']][contains(.,'Новый')]//input | //input[@type='radio' and @value='new']")
    CONDITION_USED = (By.XPATH, "//label[.//input[@type='radio']][contains(.,'Б/У')]//input | //input[@type='radio' and @value='used']")
    PUBLISH_BUTTON = (By.XPATH, "//button[contains(.,'Опубликовать')] | //button[contains(.,'Создать') and contains(.,'объяв')]")

class ProfilePageLocators:
    MY_ADS_BLOCK = (By.XPATH, "//*[contains(@class,'my-ads') or .//h2[contains(.,'Мои объявления')] or .//h1[contains(.,'Мои объявления')]]")
    MY_AD_CARD_BY_TITLE = lambda title: (By.XPATH, f"//*[contains(@class,'ad-card') or contains(@class,'card')][.//*[normalize-space()='{title}']]")
