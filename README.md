# 에어비엔비 클론 코딩

> 개발 환경 : visual studio code  
>  기술 스택 : Python(3.6.9), Django(2.2.5), Tailwind, html, javascript
> 개발 기간 : 2020-07-11 ~

## 1. Environment setup

pipenv (npm + package.json과 같은 역할)

### 왜 pipenv 인가?

- pip은 python을 이용하면서 사용하게 되는 패키지 관리 툴이다. 다양한 패키지 설치를 위하여 사용한다.
- virtualenv - python으로 개발을하게되면 복수의 패키지를 설치하여 사용하게되는 일이 많다. 하지만 각각 프로젝트가 요구하는 패키지들의 상세 내용이 다를 수 있다. 이를 위해 프로젝트 내 개발환경을 구축할 수 있게 지원해주는 것이 virtuerenv이다.

pip은 패키지들을 설치하는데 있어서 귀찮은 일이 많다. pip을 하나씩 설치하면 많은 시간이 소요된다.  
requirements.txt라는 파일을 통해 통으로 패키지들을 관리할 수 있지만, 항상 버전을 명시해야한다는 귀찮음이 발생한다.

이러한 이유들로 인해 사용하는 것이 pipenv이다.

- pip과 virtualenv를 따로 쓸 필요가 없다. 동시 사용 가능
- pipenv는 pipfile과 pipfile.lock을 requirements.txt를 대신하여 사용한다.
- 해쉬가 자동생성된다.(보안)
- 의존성 그래프를 제공함으로서 insight를 제공한다(e.g. `$ pipenv graph`)
- .env 파일들을 사용한 스트림라인 개발 워크플로우

특징

- 필요한 것만 정의하면서, 결정론적인(deterministic, 파일에 정의된대로) 빌드가 가능하다.
- 락이 걸린 의존성에 대해 해쉬 파일을 생성하고 확인한다.
- pyenv가 사용 가능하다면, 필요한 python도 자동으로 설치한다.
- Pipfile을 찾으면서자동으로 프로젝트 홈을 찾아준다.
- Pipfile이 없다면 자동으로 생성해준다.
- 자동으로 virtualenv 환경을 생성한다.
- 패키지를 설치/삭제하면, 자동으로 Pipfile에서 추가/삭제한다.
- 자동으로 .env 파일을 인식한다.

> 참조 :  
>  https://docs.python-guide.org/dev/virtualenvs/  
>  https://medium.com/@erish/python-pipenv-%EB%9E%80-%EB%AC%B4%EC%97%87%EC%9D%B8%EA%B0%80-961b00d4f42f

### pipenv 설치

`sudo pip install pipenv`

### 가상환경 생성

`pipenv --three` (python3의 pipenv 가상환경 생성)

`pipenv shell` (가상환경 실행)

### Django 2.2.5 설치

`pipenv install Django==2.2.5`

## setting

`dango-admin startproject config`

만약 wsl 환경이라면 vscode를 종료하고 linux 명령어로 실행해야함.

`./config` rename `./Aconfig`

`./Aconfig/config/` and `./Aconfig/manage.py` move `./`

delete `./Aconfig`

### vscode

**하단부 python 설정을 pipenv가 적용된 python으로 바꿔주어야함**

**linter 확장 설치**

파이썬은 compiled 언어가 아니라 runtime 언어이다. 컴파일 언어는 컴파일러가 있어서 프로그램이 시작되기 전에 에러를 잡아준다.

이를 해결하기 위한게 linter이다.

python 확장이 설치되었으면 자동으로 pylint 경고창이 뜰텐데, 만약 뜨지않거나 다른 linter를 사용하고싶다면 setting.json를 아래와 같이 수정한다.

```json
{
  "python.pythonPath": "/home/wonillism/.local/share/virtualenvs/clone_airbnb-l_EnjvOx/bin/python",
  "python.linting.flake8Enabled": true,
  "python.linting.enabled": true
}
```

formater도 설치해준다.

`pipenv install black --dev --pre`

## 2. Django

### ./config/**init**.py

이 파일은 django에 필요하다기보단 python에 필요한 파일이다. 새로운 폴더를 만들어 그 폴더의 파일을 사용할 때 항상 있어야하는 파일이다. 폴더를 패키지처럼 import 시켜서 사용할 수 있게 하는 역할을 한다.

### Django app 생성

`django-admin startapp rooms`

`django-admin startapp users`

`django-admin startapp reviews`

`django-admin startapp lists`

`django-admin startapp reservations`

## User app

장고에서 기존에 주어진 user를 커스텀 해서 이용

[Django Docs](https://docs.djangoproject.com/en/3.0/topics/auth/customizing/)

`./config/settings.py`

```python

...

# Application definition

## Default django apps
DJANGO_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
]

## Customized apps
PROJECT_APPS = [
    "users.apps.UsersConfig",
]
INSTALLED_APPS = DJANGO_APPS + PROJECT_APPS

...

AUTH_USER_MODEL = 'users.User"

```

`./users/models.py`

```python
from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    pass
```

`./users/admin.py`

```python
from django.contrib import admin
from . import models


@admin.register(models.User)
class CustomUserAdmin(admin.ModelAdmin):
    pass

```

`python manage.py createsuperuser`

`python manage.py makemigrations`

`python manage.py migrate`

### Set users model

ImageField를 사용하기 위해 Pillow 설치

`pipenv install Pillow`

`models.py`

```python
from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):

    """ Custom User Model """

    GENDER_MALE = "male"
    GENDER_FEMALE = "female"
    GENDER_OTHER = "other"

    GENDER_CHOICES = (
        (GENDER_MALE, "Male"),
        (GENDER_FEMALE, "Female"),
        (GENDER_OTHER, "Other"),
    )

    LANGUAGE_ENGLISH = "en"
    LANGUAGE_KOREAN = "kr"

    LANGUAGE_CHOICES = (
        (LANGUAGE_ENGLISH, "English"),
        (LANGUAGE_KOREAN, "Korean"),
    )

    CURRENCY_USD = "usd"
    CURRENCY_KRW = "krw"

    CURRENCY_CHOICES = (
        (CURRENCY_USD, "USD"),
        (CURRENCY_KRW, "KRW"),
    )

    avatar = models.ImageField(null=True, blank=True)
    gender = models.CharField(
        choices=GENDER_CHOICES, max_length=10, null=True, blank=True
    )
    bio = models.TextField(default="")
    birthdate = models.DateField(null=True)
    language = models.CharField(
        choices=LANGUAGE_CHOICES, max_length=2, null=True, blank=True,
    )
    currency = models.CharField(
        choices=CURRENCY_CHOICES, max_length=3, null=True, blank=True,
    )
    superhost = models.BooleanField(default=False)

```

`python manage.py makemigration`  
`python manage.py migrate`

### user 정보를 list로 보여주기, filter 사용하기

```python
from django.contrib import admin
from . import models

# decorator 방식
# admin 패널에서 User를 보고싶다, User를 컨트롤할 클래스가 아래의 클래스다.
@admin.register(models.User)
class CustomUserAdmin(admin.ModelAdmin):

    """ Custom User Adimin """

    list_display = (
        "username",
        "gender",
        "currency",
        "language",
        "superhost",
    )
    list_filter = (
        "language",
        "superhost",
        "currency",
    )


```
