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
pyenv shell [python-version]

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
  
+ django 모델
  + django에서 model은 데이터 서비스를 제공하는 Layer이다. django의 model은 각 django app안에 기본적으로 생성되는 models.py 모듈 안에 정의하게 된다. models.py 모듈 안에 하나 이상의 모델 클래스를 정의할 수 있으며, 하나의 모델 클래스는 데이터베이스에서 하나의 테이블에 해당된다.
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

application == function들의 그룹

객체 상속 알아보기
+ USER 확장하기
+ config/settings.py 에 AUTH_USER_MODEL 추가 (costomizing auth 알아보기)
+ 장고에 있는 기본 user를 상속받아서 모든 앱에 적용시킬 예정
+ Abstract user 알아보기
+ dependency 에러?
+ pillow를 설치해야 imagefield를 사용할 수 있다
+ m1 pillow 설치 에러 이슈
+ 데코레이터란?
+ list_display()
+ list_filter()
+ fieldset
+ 장고 ORM 이란?
+ admin.py에서 admin 패널을 수정 확장 할 수 있다.


## 2021.08.04
## 4. ROOMS APP
+ 만든날짜 수정날짜가 여러군데에서 나올 것이다.
  + 이를 위해 core라는 앱을 만듬.
  + django-admin startapp core
  + core 모델은 디비에 추가하지 않는다.
  + abstract=true?
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
