# 에어비엔비 클론 코딩

> 개발 환경 : visual studio code  
>  기술 스택 : Python(3.6.9), Django(2.2.5), Tailwind, html, javascript
> 개발 기간 : 2020-07-11 ~

# 1. Environment setup

<details>
<summary></summary>

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

</details>
  
# 2. Django

<details>  
<summary></summary>

### ./config/**init**.py

이 파일은 django에 필요하다기보단 python에 필요한 파일이다. 새로운 폴더를 만들어 그 폴더의 파일을 사용할 때 항상 있어야하는 파일이다. 폴더를 패키지처럼 import 시켜서 사용할 수 있게 하는 역할을 한다.

### Django app 생성

`django-admin startapp rooms`

`django-admin startapp users`

`django-admin startapp reviews`

`django-admin startapp lists`

`django-admin startapp reservations`

</details>  
  
# 3. User app

<details>
<summary></summary>

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

### UserAdimin + CustomAdmin

위에서는 CustomAdmin을 작성하는 법을 배웠다. 기존에 장고에서 주어지는 UserAdmin과 CustomAdmin을 합쳐보자.

`admin.py`에 기존에 있던 코드를 지우고 아래와 같이 변경

```python
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from . import models

# decorator 방식
# admin 패널에서 User를 보고싶다, User를 컨트롤할 클래스가 아래의 클래스다.
@admin.register(models.User)
class CustomUserAdmin(UserAdmin):

    """ Custom User Adimin """

    fieldsets = UserAdmin.fieldsets + (
        (
            "Custom Profile",
            {
                "fields": (
                    "avatar",
                    "gender",
                    "bio",
                    "birthdate",
                    "language",
                    "currency",
                    "superhost",
                )
            },
        ),
    )


```

**새로운 모델을 작성하기 전에 db.sqlite3, 생성된 migrations, `/__pycache`를 모두 지워주자. 그리고 다시 한번 makemigrations과 migrate를 실행해서 하나의 db만 남도록 하자.**

</details>
  
# 4. Room app

<details>
<summary></summary>
  
새 어플리케이션 `core` 추가  
`django-admin startapp core`  
  
여러 모델에 사용될 TimeStampedModel은 abstract 처리  
  
`./core/models.py`

```python
from django.db import models

class TimeStampedModel(models.Model):

    """ Time Stamped Model """

    created = models.DateTimeField()
    updated = models.DateTimeField()

    class Meta:
        abstract = True

```

국가 정보를 이용하기 위한 라이브러리 사용

[django-countries](https://github.com/SmileyChris/django-countries)
`pipenv install django-countries`

Tip.

1. python 관련 import
2. django와 관련된 것들을 모두 import
3. 외부 패키지 import
4. 내가 만든 패키지 import

DateTimeField의 `auto_now_add = True`는 Model을 저장할 때마다 자동으로 현제 날짜를 등록한다.

Foreignkey는 한 모델을 다른 모델과 연결시켜주는 역할을 함.
-> 데이터베이스의 Foreignkey와 동일

[Djaong docs](https://docs.djangoproject.com/en/3.0/topics/db/models/)

Model 클래스(table)이 반환값이 클래스 이름이 아닌 입력된 name값으로 반환하기

```python

class ClassName:
    name = # ...


def __str__(self):
      return self.name

```

### on delete = CASCADE

데이터베이스에서 쓰이는 내용이다.  
다른 테이블의 키를 FK로 갖고 있을 때 즉, 다른 테이블과 연결되어있을때 그 테이블이 삭제된다면 연결된 테이블도 같이 삭제된다. 참조무결성 유지.  
(폭포수 효과)

### on delete SET_NULL

부모테이블에서 primary 값이 삭제될 경우 하위테이블의 reference값은 존재할 수 없다. 옵션이 없을 경우는 에러가 발생하고 옵션 SET NULL 로 정의되면 하위테이블의 reference값이 NULL 값으로 변경되면서 참조무결성을 유지한다.

### verbose_name

장고는 작성한 모델의 이름에 s를 자동으로 붙여준다. 하지만 Facility같은경우는 Facilitys 가 아닌 Facilities가 되어야한다.  
이를 해결하기위해 meta 클래스를 불러와 직접 지정해주자.

### Foreign Key를 생성하는 방법

클래스 모델 명을 그대로 써도 되지만, ""를 이용해서 string으로 바꾸어 사용하면 장고가 그 클래스가 어딨는지 알아서 찾아준다. 클래스를 많이 정의해야할 때 유용하다.

</details>
  
# 5. ALL OTHER APPS

<details>
<summary></summary>  
  
## Review Model

[commit](https://github.com/WONILLISM/Clone_airbnb/commit/a30e004bde2d8e4094e95eadc57fa3132e7662a9)

[`./reviews/models.py`](./reviews/models.py)  
[`./reviews/admin.py`](./reviews/admin.py)

## Reservation Model

[commit](https://github.com/WONILLISM/Clone_airbnb/commit/ee8a8d0c31fcaeb2c5822b76f87763a60f477b44)

[`./reservations/models.py`](./reservations/models.py)  
[`./reservations/admin.py`](./reservations/admin.py)

## List Model

[commit](https://github.com/WONILLISM/Clone_airbnb/commit/889831e97a9f36ae0f4c93cd84e6c5cb31cd80e0)

[`./lists/models.py`](./lists/models.py)  
[`./lists/admin.py`](./lists/admin.py)

## Conversation Model

[commit](https://github.com/WONILLISM/Clone_airbnb/commit/9c29087b08fa1994861cf7d4d8bf8485ad44ce94)

[`./conversations/models.py`](./conversations/models.py)  
[`./conversations/admin.py`](./conversations/admin.py)

</details>
  
# 6. Room Admin

<details>
<summary></summary>

`fiter_horizontal`는 many to many 관계에서 작동한다.

`"classes":("collapse",),`은 `fieldsets`의 항목들을 접었다 폈다 할 수 있다.  
[commit](https://github.com/WONILLISM/Clone_airbnb/commit/cddb0a3aa7e1ec70749c8143b3e8aff338243808)

</details>
  
# 7. Models and Querysets

<details>
<summary></summary>

queryset을 이용하여 오브젝트의 수 카운트 하기

```python
def count_amenities(self, obj):
        return obj.amenities.count()
```

진행중인 프로젝트와 파이썬과 연결하기  
`python manage.py shell`

[Django queryset api reference](https://docs.djangoproject.com/en/3.0/ref/models/querysets/)

</details>
