from megascrapper import MegaScraper

scraper = MegaScraper()

login_success = scraper.handle_login(
    login_url="https://github.com/login",
    credentials={"username": "ahammadnafiz", "password": "password"},
    username_field={"type": "id", "value": "login_field"},
    password_field={"type": "name", "value": "password"},
    submit_button={"type": "xpath", "value": "//input[@name='commit']"}
)

if not login_success:
    print("Login failed!")
    exit()