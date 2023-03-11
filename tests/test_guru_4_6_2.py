from datetime import time


def test_dark_theme():
    """
    Протестируйте правильность переключения темной темы на сайте
    """
    is_dark_theme = None
    current_time = time(hour=23)
    """ # реализация со списком
    current_time = current_time.hour
    dark_theme_hours = [22, 23, 0, 1, 2, 3, 4, 5]
    if current_time in dark_theme_hours:
        is_dark_theme = True
    else:
        is_dark_theme = False
    """
    if current_time >= time(22) or current_time < time(6):
        is_dark_theme = True
    else:
        is_dark_theme = False

    # TODO переключите темную тему в зависимости от времени суток (с 22 до 6 часов утра - ночь)

    assert is_dark_theme is True

    is_dark_theme = None
    current_time = time(hour=16)
    dark_theme_enabled = True
    if current_time >= time(22) or current_time < time(6) or dark_theme_enabled == True:
        is_dark_theme = True
    else:
        is_dark_theme = False

    """ # реализация со списком
    current_time = current_time.hour
    if current_time in dark_theme_hours or dark_theme_enabled == True:
        is_dark_theme = True
    else:
        is_dark_theme = False
     """
    # TODO переключите темную тему в зависимости от времени суток,
    #  но учтите что темная тема может быть включена вручную

    assert is_dark_theme is True


def test_find_suitable_user():
    """
    Найдите нужного пользователя по условиям в списке пользователей
    """
    users = [
        {"name": "Oleg", "age": 32},
        {"name": "Sergey", "age": 24},
        {"name": "Stanislav", "age": 15},
        {"name": "Olga", "age": 45},
        {"name": "Maria", "age": 18},
    ]
    # TODO найдите пользователя с именем "Olga"
    suiable_user = None
    """ # реализация c циклом

    def get_user_name(users):
        return users["name"]
    for i in range(len(users)):
        if get_user_name(users[i]) == "Olga":
            suiable_user = users[i]
    """
    suiable_user = [i for i in users if i['name'] == 'Olga'][0]

    assert suiable_user == {"name": "Olga", "age": 45}

    # TODO найдите всех пользователей младше 20 лет
    suiable_users = None
    """ # реализация c циклом
    suiable_users = []
    def get_user_age(users):
        return users["age"]
    for i in range(len(users)):
        if get_user_age(users[i]) < 20:
            suiable_users.append(users[i])
    """
    suiable_users = [i for i in users if i['age'] < 20]

    assert suiable_users == [
        {"name": "Stanislav", "age": 15},
        {"name": "Maria", "age": 18},
    ]


# Сделайте функцию, которая будет печатать
# читаемое имя переданной ей функции и значений аргументов.
# Вызовите ее внутри функций, описанных ниже
# Подсказка: Имя функции можно получить с помощью func.__name__
# Например, вызов следующей функции должен преобразовать имя функции
# в более читаемый вариант (заменить символ подчеркивания на пробел,
# сделать буквы заглавными (или первую букву), затем вывести значения всех аргументов этой функции:
# >>> open_browser(browser_name="Chrome")
# "Open Browser [Chrome]"

def function_name(f_name, **kwargs):
    return f'''{f_name.__name__.replace('_', ' ').title()} {str(list(kwargs.values())).replace("'", "")}'''


def test_readable_function():
    open_browser(browser_name="Chrome")
    go_to_companyname_homepage(page_url="https://companyname.com")
    find_registration_button_on_login_page(page_url="https://companyname.com/login", button_text="Register")


def open_browser(browser_name):
    actual_result = None
    actual_result = function_name(open_browser, browser=browser_name)
    assert actual_result == "Open Browser [Chrome]"


def go_to_companyname_homepage(page_url):
    actual_result = None
    actual_result = function_name(go_to_companyname_homepage, page=page_url)
    assert actual_result == "Go To Companyname Homepage [https://companyname.com]"


def find_registration_button_on_login_page(page_url, button_text):
    actual_result = None
    actual_result = function_name(find_registration_button_on_login_page, page=page_url, button=button_text)
    assert actual_result == "Find Registration Button On Login Page [https://companyname.com/login, Register]"