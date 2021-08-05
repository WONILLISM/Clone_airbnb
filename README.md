# Clone Air bnb
## with nomad coder

프래임워크 : Django

## 2021.07.30

# python 버전 관리
python은 2.x버전과 3.x버전이 많이다르고, 요즘은 3.x버전을 많이 사용하지만 3.x버전들끼리도 조금씩 차이가 있다.
이를 해결하기 위한 방법으로 virtureenv라는 것이 있는데, 각 프로젝트마다 쓰일 가상환경을 생성하여 그 프로젝트에 해당되는 python 버전을 활성화 한 후에 실행시킨다.

# pyenv란?
pyenv란 여러 버전의 python을 쉽게 바꿔서 쓸 수 있게 해주는 도구이다.
pyenv를 사용함으로써 python 버전에 대한 의존성을 해결할 수 있다.

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

# virtualenv란?
로컬에는 단 하나의 파이썬을 설치할 수 있다.
예를들어 A에서는 3.5.x버전을 사용하고 B에서는 3.6.x버전 사용이 불가능하다.
이 문제를 해결하기 위해 virtualenv를 사용한다.

**가상환경 생성**
pyenv virtualenv [python-versions] [virtualenv-name]

**가상환경 확인**
pyenv virtualenvs

**가상환경 사용**
pyenv shell [virtualenv-name]

**가상환경 삭제**
pyenv uninstall [virtualenv-name]

**가상환경 설정/해제**
pyenv activate
pyenv deactivate



1. pipenv 설치.
2. pipenv shell을 이용해서 가상환경을 켠다.
3. pipenv install Django==2.2.5
4. django-admin으로 잘 설치되었는지 확인.
   1. 가상환경이 실행되지 않은 쉘에서는 장고를 찾을 수 없다.
5. exit로 가상환경을 종료할 수 있다.

### Creating a Django Project
장고 프로젝트 만들기
```zsh
$ django-admin startproject config
```
+ rename config -> Aconfig
+ 안에있는 config폴더를 꺼낸 후 Aconfig를 삭제


## 2021.08.02
python manage.py runserver -> 서버 구동
python mamage.py createsuperuser -> 관리자 계정 만들기
python manage.py migrate -> 데이터베이스 업데이트

django-admin startapp 앱이름

**파일 이름은 절대로 변경해서는 안된다.**

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
