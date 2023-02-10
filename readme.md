# پروژه سلنیوم آزمون نرم افزار
## _پاییز 1401_

## شرح پروژه
با استفاده از ابزار سلنیوم، یک مجموعه تست برای روال لاگین یک پروژه تبدیل واحد پولی انجام داده ایم. 


### unittest
این کتابخانه در پایتون، وظیفه تست کردن مواردی که ما برای آن تعیین می کنیم را دارد. پروژه ما یک کلاس دارد که از کلاس TestCase این کتابخانه ارث بری می کند.
این کلاس، متدهای مختلفی دارد که به تفصیل در زیر آنها را معرفی خواهیم کرد:


| تابع | توضیحات |
| ------ | ------ |
| setUp | وظیفه این متد، انجام کارهایی است که نیاز است قبل از هر تست انجام پذیرد. در پروژه ما، وظیفه این متد راه اندازی درایور سلنیوم و رفتن به آدرس پروژه ری اکت اجرا شده است (http://localhost:3000) |
| tearDown | وظیفه این متد، انجام کارهایی است که پس از هر تست باید انجام شود. در پروژه ما، وظیفه این متد بستن درایور است.|

هنگامی که ما یک کلاس بسازیم که از TestCase ارث بری کند، هر تابع به جز توابع بالا را که بنویسیم، یک تست کیس محسوب می شود.

### نصب و اجرا

برای اجرای پروژه باید کارهای زیر را انجام دهیم: 
ابتدا باید یک محیط مجازی (virtual environment)ایجاد کنیم. برای این کار، دستور زیر را در ترمینال وارد می کنیم:

```sh
virtualenv env
```

> اگر virtualenv روی سیستم شما نصب نبود باید با دستور`pip install virtualenv`آن را نصب کنید.

پس از ساخته شدن محیط مجازی، آن را فعال می کنیم:

```sh
.\env\Scripts\activate
```

بعد از فعال سازی، پکیج سلنیوم را به وسیله دستور زیر نصب می کنیم:

```python
pip install selenium
```

حال هر زمان که بخواهیم پروژه را اجرا کنیم، با دستور `python .\Demo\sample1.py` آن را اجرا می کنیم.

### شرح تست های پروژه:

_test_signup_click_

هنگام اجرای پروژه ری اکتی، یک لینک signin در صفحه دیده می شود. به کمک inspect گرفتن، مقدار xpath آن لینک را گرفته و به وسیله درایور سلنیوم روی آن کلیک می کنیم. اگر url صفحه به `http://localhost:3000/auth` تغییر یافت، تست به درستی کار می کند.

```python
def test_signup_click(self):
        signup_link = self.driver.find_element(By.XPATH, '//*[@id="root"]/div/p[1]/a')
        signup_link.click()
        self.assertEqual(self.driver.current_url, 'http://localhost:3000/auth')
```

_test_email_field_

پس از بازشدن صفحه لاگین، یک فیلد ایمیل در آن موجود است. مقدار xpath آن اینپوت را به دست آورده و به وسیله متد send_keys سلنیوم، یک ایمیل معتبر را در آن وارد می کنیم. پس از وارد کردن مقدار ایمیل، اگر attribute value آن اینپوت برابر با همان مقدار ایمیل بود، تست صحیح می باشد.

```python
def test_email_field(self):
        signup_link = self.driver.find_element(By.XPATH, '//*[@id="root"]/div/p[1]/a')
        signup_link.click()
        emailField = self.driver.find_element(By.XPATH, '//*[@id="root"]/div/form/div/div/input')
        emailField.send_keys('toobaahrabi@gmail.com')
        self.assertEqual(emailField.get_attribute('value'), 'toobaahrabi@gmail.com')
```

_test_btn_click_

هنگامی که روی دکمه سابمیت کلیک می شود، اینپوت حالت غیرفعال دارد. پس ما ابتدا روی دکمه کلیک می کنیم و اگر attribute disabled اینپوت فعال باشد، تست درست کار می کند. برای این کار از متد is_enabled() سلنیوم استفاده کرده ایم.

```python
def test_btn_click(self):
        signup_link = self.driver.find_element(By.XPATH, '//*[@id="root"]/div/p[1]/a')
        signup_link.click()
        emailField = self.driver.find_element(By.XPATH, '//*[@id="root"]/div/form/div/div/input')
        emailField.send_keys('toobaahrabi@gmail.com')
        submit_button = self.driver.find_element(By.XPATH, '//*[@id="root"]/div/form/div/div/button')
        submit_button.click()
        self.assertEqual(emailField.is_enabled(), False)
```

_test_btn_loading_class_

هنگامی که روی دکمه سابمیت کلیک می شود، یک کلاس loading به کلاس هایش اضافه می شود و انیمیشن لودینگ روی دکمه قرار میگیرد. به وسیله get_attribute('class')این تست را بررسی می کنیم.

```python
def test_btn_loading_class(self):
        signup_link = self.driver.find_element(By.XPATH, '//*[@id="root"]/div/p[1]/a')
        signup_link.click()
        emailField = self.driver.find_element(By.XPATH, '//*[@id="root"]/div/form/div/div/input')
        emailField.send_keys('toobaahrabi@gmail.com')
        submit_button = self.driver.find_element(By.XPATH, '//*[@id="root"]/div/form/div/div/button')
        submit_button.click()
        self.assertEqual('loading' in submit_button.get_attribute('class'), True)
```

_test_empty_field_

اگر هیچ مقداری در فیلد ایمیل قرار ندهیم، نباید عملیات اجرا شده و دکمه حالت لودینگ داشته باشد. در نتیجه کلاس لودینگ نباید در لیست کلاس های دکمه باشد.

```python
def test_empty_field(self):
        signup_link = self.driver.find_element(By.XPATH, '//*[@id="root"]/div/p[1]/a')
        signup_link.click()
        submit_button = self.driver.find_element(By.XPATH, '//*[@id="root"]/div/form/div/div/button')
        submit_button.click()
        self.assertEqual('loading' in submit_button.get_attribute('class'), False)
```

[پروژه ری اکت](https://github.com/ayastreb/money-tracker)
