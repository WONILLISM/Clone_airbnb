# 에어비엔비 클론 코딩
> 개발 환경 :  visual studio code  
  기술 스택 : python(3.6.9), django, javascript, html, css  
  개발 기간 : 2020-07-11 ~  
  


## 1. Environment setup
pipenv (npm + package.json과 같은 역할)  

### 왜 pipenv 인가?  
+ pip은 python을 이용하면서 사용하게 되는 패키지 관리 툴이다. 다양한 패키지 설치를 위하여 사용한다.
+ virtualenv - python으로 개발을하게되면 복수의 패키지를 설치하여 사용하게되는 일이 많다. 하지만 각각 프로젝트가 요구하는 패키지들의 상세 내용이 다를 수 있다. 이를 위해 프로젝트 내 개발환경을 구축할 수 있게 지원해주는 것이 virtuerenv이다.

pip은 패키지들을 설치하는데 있어서 귀찮은 일이 많다. pip을 하나씩 설치하면 많은 시간이 소요된다.  
requirements.txt라는 파일을 통해 통으로 패키지들을 관리할 수 있지만, 항상 버전을 명시해야한다는 귀찮음이 발생한다.  
  
이러한 이유들로 인해 사용하는 것이 pipenv이다.  
+ pip과 virtualenv를 따로 쓸 필요가 없다. 동시 사용 가능  
+ pipenv는 pipfile과 pipfile.lock을 requirements.txt를 대신하여 사용한다.  
+ 해쉬가 자동생성된다.(보안)  
+ 의존성 그래프를 제공함으로서 insight를 제공한다(e.g. `$ pipenv graph`)  
+ .env 파일들을 사용한 스트림라인 개발 워크플로우  
  
특징  
+ 필요한 것만 정의하면서, 결정론적인(deterministic, 파일에 정의된대로) 빌드가 가능하다.  
+ 락이 걸린 의존성에 대해 해쉬 파일을 생성하고 확인한다.  
+ pyenv가 사용 가능하다면, 필요한 python도 자동으로 설치한다.  
+ Pipfile을 찾으면서자동으로 프로젝트 홈을 찾아준다.  
+ Pipfile이 없다면 자동으로 생성해준다.  
+ 자동으로 virtualenv 환경을 생성한다.  
+ 패키지를 설치/삭제하면, 자동으로 Pipfile에서 추가/삭제한다.  
+ 자동으로 .env 파일을 인식한다.  

> 참조 :  
  https://docs.python-guide.org/dev/virtualenvs/  
  https://medium.com/@erish/python-pipenv-%EB%9E%80-%EB%AC%B4%EC%97%87%EC%9D%B8%EA%B0%80-961b00d4f42f  

### pipenv 설치  
  
`sudo pip install pipenv`  

## 프로젝트 생성  
  
`pipenv --three`  (python3의 pipenv 프로젝트 생성)  
  
`pipenv shell` (가상환경 실행)  
  
## Django 2.2.5 설치  
  
`pipenv install Django==2.2.5`  
  



  
