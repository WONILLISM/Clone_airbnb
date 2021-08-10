# Clone Air bnb
## with nomad coder

프래임워크 : Django

## 2021.07.30
## 1. ENVIRONMENT SETUP
## m1 맥 brew 설치  
  
```
# We'll be installing Homebrew in the /opt directory.
 cd /opt

 # Create a directory for Homebrew. This requires root permissions.
 sudo mkdir homebrew

 # Make us the owner of the directory so that we no longer require root permissions.
 sudo chown -R $(whoami) /opt/homebrew

 # Download and unzip Homebrew. This command can be found at https://docs.brew.sh/Installation.
 curl -L https://github.com/Homebrew/brew/tarball/master | tar xz --strip 1 -C homebrew

 # Add the Homebrew bin directory to the PATH. If you don't use zsh, you'll need to do this yourself.
 echo "export PATH=/opt/homebrew/bin:$PATH" >> ~/.zshrc
```  
  
+ 터미널 재실행
+ `brew update`

## python 버전 관리
python은 2.x버전과 3.x버전이 많이다르고, 요즘은 3.x버전을 많이 사용하지만 3.x버전들끼리도 조금씩 차이가 있다.
이를 해결하기 위한 방법으로 virtureenv라는 것이 있는데, 각 프로젝트마다 쓰일 가상환경을 생성하여 그 프로젝트에 해당되는 python 버전을 활성화 한 후에 실행시킨다.

## pyenv란?
pyenv란 여러 버전의 python을 쉽게 바꿔서 쓸 수 있게 해주는 도구이다.
pyenv를 사용함으로써 python 버전에 대한 의존성을 해결할 수 있다.
  
`brew install pyenv`  

**설치 가능한 버전 리스트**
pyenv install -list

**파이썬 버전 설치**
pyenv install [python-version]

**파이썬 버전 삭제**
pyenv uninstall [python-version]

**파이썬 버전 사용(일시적)**
pyenv local [python-version]

**파이썬 버전 사용(전역적)**
pyenv global [python-version]

**로컬에 설치된 파이썬으로 되돌리기**
pyenv global system

**현재 파이썬 버전 확인**
pyenv version

**pyenv로 설치된 파이썬 버전 목록**
pyenv versions  
  
+ zsh 사용시 설정
  + echo 'eval "$(pyenv init --path)"' >> ~/.zprofile
  + echo 'export PYENV_ROOT="$HOME/.pyenv"' >> ~/.zprofile
  + echo 'export PATH="$PYENV_ROOT/bin:$PATH"' >> ~/.zprofile
  + echo 'eval "$(pyenv init --path)"' >> ~/.zprofile
  + echo 'eval "$(pyenv init -)"' >> ~/.zshrc
  
1. python version 3.7.11사용  
2. pipenv 설치.
   1. sudo python3 -m pip install --upgrade pip
   2. pip install pipenv
3. pipenv shell을 이용해서 가상환경을 켠다.
4. pipenv install Django==2.2.5
5. django-admin으로 잘 설치되었는지 확인.
   1. 가상환경이 실행되지 않은 쉘에서는 장고를 찾을 수 없다.
6. exit로 가상환경을 종료할 수 있다.

## 2021.08.02
## 2.INTRODUCTION TO DJANGO

장고 프로젝트 만들기
```zsh
$ django-admin startproject config
```
+ rename config -> Aconfig
+ 안에있는 config폴더를 꺼낸 후 Aconfig를 삭제

+ 이 때 settings.py에 있는 secret_key를 그냥 올리게 되면 깃에서 보안 경고 메일이 온다.
+ 이를 처리하기 위한 방법
  + secrets.json 파일 생성
```json
{
  "SECRET_KEY": "(1djli9wygoor+6^5g36bcn^ca+!+@8uc-=bw-3bk)z2pwrdq8"
}
```
+ gitignore에 secrets.json 추가
+ setting.py 아래와 같이 수정
```python3
import os, json
from django.core.exceptions import ImproperlyConfigured

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/2.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
secret_file = os.path.join(BASE_DIR, "secrets.json")

with open(secret_file) as f:
    secrets = json.loads(f.read())

def get_secret(setting, secrets=secrets):
    try:
        return secrets(setting)
    execept KeyError:
        error_msg = "Set the {} environment variable".format(setting)
        raise ImproperlyConfigured(error_msg)

SECRET_KEY = get_secret("SECRET_KEY")

...
```

python manage.py runserver -> 서버 구동  
python mamage.py createsuperuser -> 관리자 계정 만들기  
python manage.py migrate -> 데이터베이스 업데이트  
  
### INSTALLED_APPS
+ django와 함께 딸려오는 기본 앱들은 다음과 같다.
  + django.contrib.admin
    + django의 가장 강력한 부분 중 하나인 자동 관리 인터페이스이다.
    + 모델에서 메타데이터를 읽어 신뢰할 수 있는 사용자가 사이트의 콘텐츠를 관리할 수 있는 빠른 모델 중심 인터페이스를 제공한다.
    + `(연결한 url/admin/)`을 통해서 사용할 수 있다.
  + django.contrib.auth
    + 사용자 인증 시스템을 지원한다.
    + 사용자 계정, 그룹, 권한과 쿠키 기반의 사용자, 세션을 다룬다.
  + django.contrib.contenttypes
    + django 기반 프로젝트에 설치된 모든 모델을 추적할 수 있는 contenttypes 앱이 포함되어 있어 모델 작업을 위한 고급, 일반 인터페이스를 제공한다.
  + django.contrib.sessions
    + 세션 프레임워크를 사용하면 사이트 방문자별로 임의의 데이터를 저장하고 검색할 수 있다. 서버에 데이터를 저장하고 쿠키의 송수신을 추상화한다.
  + django.contrib.messages
    + 익명 및 인증된 사용자 모두에게 쿠키 및 세션 기반 메시징을 완벽하게 지원한다.
  + django.contrib.staticfiles
    + 정적파일을 관리하는 프레임워크
+ 

django-admin startapp 앱이름
  
+ makemigrations 
  + 생성 / 수정된 모델들의 변경사항을 migrations로 저장하고자 Django에게 알려준다.
+ migrate
  + makemigrations 또는 기본적으로 생성된 migrations들을 실행시켜주고 자동으로 데이터베이스 스키마를 관리해준다.
+ createsuperuser
  + 모든 권한을 가지는 superuser를 생성한다.
  
+ django-admin startapp `app 이름`
  + conversations
  + lists
  + reservations
  + reviews
  + rooms
  + users
    + django에는 기본적으로 user가 존재하지만, 이 user는 데이터베이스에 접근 할 수 있는 user를 뜻한다. 하지만 우리가 필요한 user는 홈페이지를 사용할 고객이기 때문에 데이터베이스에 접근하지 못하는 새로운 users를 생성해서 사용한다.
    + app을 생성했을때 만들어지는 기본적인 파일 및 폴더들은 django에게 필요한 것이기 때문에 삭제하거나 이름을 바꾸어서는 안된다.
  
### 생성한 app안의 파일들
+ `__init__.py`
+ `admin.py`
  + app의 내용들을 admin 패널에 보여주기위한 파일
+ `veiw.py`
  + 페이지에서 보여질 부분들을 작성하는 파일 -> html렌더
+ `urls.py`
  + url들을 관리하는 파일
  + config/urls.py 에 모든 앱들의 url을 관리하지않고 각 앱에 있는 urls.py만들어서 연동시켜준다.
+ `apps.py`
  + 앱의 구성을 관리하는 파일
+ `models.py`
  + 앱의 모델을 관리하는 파일(데이터베이스) -> 앱의 데이터 변경
+ `tests.py`

## 2021.08.03
## 3. USER APP
## class
https://wikidocs.net/16071  
  
+ 클래스는 객체의 구조와 행동을 정의한다.
+ 객체의 클래스는 초기화를 통해 제어한다.

**클래스 정의**  
```python3
class 클래스 이름:
  def __init__(self, 파라미터들...):
    ...
```
  
### `constructor(생성자)`, `__init__`
```python3
c = 클래스이름() # 생성자
```
+ 생성자로 객체생성을 호출받으면 `__new__`를 호출하여 객체를 생성/할당하고, `__new__`메소드가 `__init__`메소드를 호출하여 객체에서 사용할 초기값들을 초기화하게된다.
+ 다른 언어(c++ 등)들의 생성자와 `__init__`메소드 생성자처럼 생각할 수 있지만 그렇지 않다.
  + https://stackoverflow.com/questions/6578487/init-as-a-constructor
  + `__init__`메소드는 생성자처럼 보이고 작동하기때문에 생성자로 착각할 수 있지만, 관례상 `__init__`메소드는 클래스에 대해 정의된 첫 번째 메소드이고, 이 메소드가 호출될 때에는 이미 객체가 생성되었고 클래스의 새 인스턴스에 대한 유효한 참조가 있기 때문이다.
  
### 클래스 속성과 인스턴스 속성의 차이
+ 클래스 속성은 `self.속성`에 할당하는 것이 아니라 class안에서 바로 할당한다.  
```python3
class 클래스이름:
  클래스속성명 = 값

  def __init__(self):
    self.인스턴스속성명 = 값
```
+ 만약 인스턴스와 클래스에 같은 속성이 있으면 인스턴스 속성을 먼저 찾는다.
+ 속성/메소드 이름 찾는 순
  + 인스턴스 > 클래스
  

### 상속(inheritance) 이란?
+ 클래스에서 상속이란, 물려주는 클래스(Parent Class, Super class)의 내용(속성과 메소드)을 물려받는 클래스(Child class, Sub class)가 가지게 되는 것이다.
+ examples
  + 국가라는 클래스가 있으면 그것을 상속받은 한국, 미국, 일본, 중국 등의 클래스를 만들 수 있다
  + 상속 받은 클래스들은 부모 클래스의 속성과 메소드를 사용할 수 있다.
  
```python3
class 부모클래스:
    ...내용...

class 자식클래스(부모클래스):
    ...내용...
```  
  
**메소드 오버라이딩(Method overriding**  
+ 메소드 오버라이딩은 부모클래스의 메소드를 자식 클래스에서 재정의 하는 것이다.
+ 부모 클래스의 메소드 호출하기
  + `super()` 키워드를 사용하여 호출가능하다.

**다중 상속**  
+ C# 또는 Java는 다중상속이 불가능한 언어이다. 파이썬은 C++과 같이 다중상속이 가능하다.

```python3
    class 부모클래스1:
        ...내용...

    class 부모클래스2:
        ...내용...

    class 자식클래스(부모클래스1, 부모클래스2):
        ...내용...
```
+ `클래스이름.mro()`를 이용하면 상속관계를 확인할 수 있다.
  
### django model
http://pythonstudy.xyz/python/article/308-Django-%EB%AA%A8%EB%8D%B8-Model  
  
+ django에서 model은 데이터 서비스를 제공하는 Layer이다. django의 model은 각 django app안에 기본적으로 생성되는 models.py 모듈 안에 정의하게 된다. models.py 모듈 안에 하나 이상의 모델 클래스를 정의할 수 있으며, 하나의 모델 클래스는 데이터베이스에서 하나의 테이블에 해당된다.
+ django 모델은 `django.db.models.Model`의 파생 클래스이며, 모델의 필드는 클래스의 Attribute(속성)로 표현되며 테이블의 column(컬럼)에 해당한다. 
+ 만약 Primary key가 지정되지 않으면, 모델에 Primary key역할을 하는 id필드가 자동으로 추가되며 DB테이블 생성시 자동으로 id컬럼이 생성된다.
+ 모델 클래스는 필드를 정의하기 위해 인스턴스 변수가 아닌 클래스 변수를 사용하는데, 이는 그 변수가 테이블 컬럼의 내용을 갖는 것이 아니라, 테이블의 컬럼 메타 데이터를 정의하는 것이기 때문이다.

### django model 필드 타입
모델의 필드에는 다양한 타입들이 있다.  
https://docs.djangoproject.com/en/1.11/ref/models/fields/#field-types 
|Feild Type| 설명 | 
|:--------:|:---|
|AutoField |사용 가능한 ID에 따라 자동으로 증가하는 IntegerField. 직접적으로 사용할 필요 없이 자동으로 모델에 추가된다.|
|BigAutoField|64비트 크기의 AutoField이다.</br>1 ~ 9223372036854775807|
|IntegerField|정수 필드이다.</br>-2147483648 ~ 2147483647</br>localize가 False이면 NumberInput True이면 TextInput이다.|
|BigIntegerField|-9223372036854775808 to 9223372036854775807인 정수 필드이다.|
|SmallIntegerField|-32768 to 32767인 정수 필드이다.|
|BinaryField|class BinaryField(**options)</br> 원시 이진 데이터 필드.</br>BinaryField 값에 대한 쿼리 집합을 필터링할 수 없다.</br>ModelForm에 BinaryField를 포함하는것도 불가능하다.|
|BooleanField|class BooleanField(**options)</br>기본 양식은 CheckboxInput이다.</br>default가 정의되지 않은 경우 None이 기본값이다.</br>null을 허용하기 위해서는 NullBooleanField를 사용|
|CharField |제한된 문자열 필드타입. </br>max_length를 이용하여 최대 길이를 필수로 지정해야한다.</br>CharField 파생클래스</br>EmailField : 이메일 주소 체크 필드</br>GenericIPAddressField : IP 주소를 체크하는 필드</br>CommaSeparatedIntegerField : 콤마로 정수를 분리한 필드</br>FilePathField : 특정 폴더의 파일 경로를 표현하는 필드</br>URLField : URL을 표현하는 필드|
|TextField|대용량 문자열을 갖는 필드|
|DateTimeField|날짜와 시간을 갖는 필드</br>DateField : 날짜만 갖는 필드</br>TimeField : 시간만 갖는 필드|
|DecimalField| 소숫점을 갖는 필드|
|FileField| 파일 업로드 필드|
|ImageField|FileField의 파생 클래스, 이미지 파일인지 체크한다.|
  
### 테이블 혹은 필드 간 관계(Relationships) 표현 필드
**Relationships**  
관계형 데이터베이스의 장점은 테이블을 서로 연관시키는데에 있다. 속도면에서는 key-value형 데이터베이스가 빠르지만, 관계형 데이터베이스는 저장용량을 아끼는데에 최적화 되어있다.  
https://himanmengit.github.io/django/2018/02/05/DjangoModels-04-ManyToMany.html
|Feild Type| 설명 | 
|:--------:|:---|
|ForeignKey|One to Many 혹은 Many to One을 표현하기 위해 흔히 사용된다.|
|ManyToManyField|서로 여러개의 관계를 가지는 형태</br>example</br>어떤 글의 좋아요를 누르면 해당 글에 어떤 사람이 좋아요를 눌렀는지 가지고 그 사람은 여러 글에 좋아요를 누를 수 있다|
|OneToOneField|기존의 데이터는 그대로 두고 확장할 때 사용할 수 있다.|  
  
### Field Option
모델의 필드는 필드 타입에 따라 여러 옵션(Argument)를 가질 수 있다.  
|Field Option|설명|
|:----------:|:--|
|null (Field.null)|	null=True 이면, Empty 값을 DB에 NULL로 저장한다. DB에서 Null이 허용된다. 예: models.IntegerField(null=True)|
|blank (Field.blank)|	blank=False 이면, 필드가 Required 필드이다. blank=True 이면, Optional 필드이다. 예: models.DateTimeField(blank=True)|
|primary_key (Field.primary_key)|	해당 필드가 Primary Key임을 표시한다. 예: models.CharField(max_length=10, primary_key=True)|
|unique (Field.unique)|	해당 필드가 테이블에서 Unique함을 표시한다. 해당 컬럼에 대해 Unique Index를 생성한다. 예: models.IntegerField(unique=True)|
|default (Field.default)|	필드의 디폴트값을 지정한다. 예: models.CharField(max_length=2, default="WA")|
|db_column (Field.db_column)|	컬럼명은 디폴트로 필드명을 사용하는데, 만약 다르게 쓸 경우 지정한다.|


+ USER 확장하기
+ config/settings.py에 있는 INSTALLED_APPS를 좀 세분화 하기 위해 장고에 기본으로 설치된 앱들을 DJANGO_APPS로 옮기고 PROJECT_APPS에 앞으로 설치할 앱들을 적고 INSTALLED_APPS = DJANGO_APPS + PROJECT_APPS로 합쳐준다.
+ config/settings.py 에 AUTH_USER_MODEL='users.User' 추가 

### Customizing authentication in Django
https://docs.djangoproject.com/en/3.2/topics/auth/customizing/  
django는 기본적으로 authentication을 내장하고 있고, UserModel을 가지고있다.  
제공되는 UserModel이 항상 적절하지 않을 수 있기 때문에, 커스텀 UserModel을 대체할 수 있다.  
+ `AUTH_USER_MODEL = 'myapp.MyUser'`를 config/setting.py에 추가
+ 커스텀할 유저 앱의 `models.py`에 `from django.contrib.auth.models import AbstractUser`를 추가한다.

+ pillow를 설치해야 imagefield를 사용할 수 있다
+ m1 pillow 설치 에러 이슈
  + 파이썬 3.9 버전부터 pillow를 지원해서 파이썬 버전을 3.9로 바꿈

### Decorator(데코레이터)
https://m.blog.naver.com/b2bhjlee/222094004738  
https://docs.djangoproject.com/ko/1.11/_modules/django/contrib/admin/  
데코레이터는 사용자가 객체의 구조를 수정하지 않고, 기존 객체에 새로운 함수 기능을 추가할 수 있도록하는 Python의 디자인 패턴이다.  
  
데코레이터는 일반적으로 데코레이트하려는 함수의 정의 이전에 호출된다.  
  
함수는 인수로 전달되고, 함수에서 return 되고, 수정되고, 변수에 할당되는 것과 같은 작업을 지원한다.
  
우리는 admin.py를 통해서 관리자 페이지에 모델을 추가할때 `from django.contrib import admin`로 패키지를 통해서 추가한다.  
`django/contrib/admin/decorators.py` 코드를 확인해보자.  
  
```python3
def register(*models, site=None):
    """
    Register the given model(s) classes and wrapped ModelAdmin class with
    admin site:

    @register(Author)
    class AuthorAdmin(admin.ModelAdmin):
        pass

    The `site` kwarg is an admin site to use instead of the default admin site.
    """
    from django.contrib.admin import ModelAdmin
    from django.contrib.admin.sites import site as default_site, AdminSite

    def _model_admin_wrapper(admin_class):
        if not models:
            raise ValueError('At least one model must be passed to register.')

        admin_site = site or default_site

        if not isinstance(admin_site, AdminSite):
            raise ValueError('site must subclass AdminSite')

        if not issubclass(admin_class, ModelAdmin):
            raise ValueError('Wrapped class must subclass ModelAdmin.')

        admin_site.register(models, admin_class=admin_class)

        return admin_class
    return _model_admin_wrapper

```
  
주석에 나와있는 것처럼  
```python3
@register(Author)
    class AuthorAdmin(admin.ModelAdmin):
        pass
```
위와 같이 adminsite에 모델을 추가할 수 있다.  
+ 만들어진 app의 `admin.py`에 `django/contrib/admin`패키지를 추가
+ 우리는 `from django.contrib import admin`으로 패키지를 추가했으므로
+ `@admin.register(모델명)` 데코레이터를 통해서 모델을 admin site에 추가한다.
+ 이를 통해 admin.py에서 admin 패널을 수정 확장 할 수 있다.

### 장고 ORM 이란?
Object-Relational Mapping의 약자
+ 객체와 관계형 데이터베이스의 데이터를 매핑 해주는 것이다.
+ 객체 간의 관계를 바탕으로 SQL을 자동으로 생성해서 sql쿼리문 없이도 데이터베이스의 데이터들을 다룰 수 있다.
+ 개발자가 사소하게 신경쓰지 않아도 자동으로 처리해주어 빠른 개발이 가능하고, 생산성이 좋아진다.
+ 선언문, 할당, 종료와 같은 코드가 줄어들고, 객체에 대한 코드를 별도로 작성하기 때문에 코드 가독성이 좋아진다.
+ 코드의 재사용이 용이하여 유지보수도 편리하다.
+ 규모가 큰 프로젝트나 복잡한 프로젝트의 경우 sql을 이용하여 데이터베이스를 관리하는 것이 보통 더 좋다.
+ 정확한 원리를 이해하고 프로젝트를 진행해야하지만, 그렇지 않아도 사용 가능하므로 대처능력이 떨어질 가능성이 있다.


## 2021.08.08
## 4. ROOMS APP
+ 만든날짜 수정날짜가 여러군데에서 나올 것이다.
  + 이를 위해 core라는 앱을 만듬.
  + django-admin startapp core
  + core 모델은 디비에 추가하지 않는다.
  + abstract=true?
  + pipenv install django-countries (모든 국가 패키지)
  + from django_countries.fields import CountryField 모델에 추가
  + setting.py에 인스톨 앱 추가
+ import 순서
  1. 파이썬 관련
  2. 장고와 관련
  3. 외부 패키지
  4. 내가 만든 패키지
+ 모델과 모델을 연결하기위해 Foreignkey(many to one)를 이용
  + on_delete?
  + 장고에게 room으로 무엇을 할것인지 말하는 행동
  + CASCADE?
  + 폭포수와 같이 위에서 아래로 모두 영향을줌
  + django foreign key?
+ verbose name?
+ meta class?


## 2021.08.09
## 5. ALL OTHER APPS


## 2021.08.10
## 6. ROOM ADMIN

+ admin filter 알아보기
+ icontains
+ fieldsets 커스터마이징
+ ordering(정렬)

## 7. MODELS AND QUERYSETS

+ querysets
+ python manage.py shell
+ related_name
+ 
