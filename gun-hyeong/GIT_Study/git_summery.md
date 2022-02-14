# git 써보기


1. git init : git 레포지토리 생성 명령어 

```bash
git init
```

2. git add : 깃에 의해 추적되지 않은 파일을 추가하는명령어

Untracked -> Tracked 파일로 전환 

git add .  : 현재 디렉토리에 존재하는 모든 파일을 git 으로 추적 

```bash
git add . 
```

root-commit : 이 레파지토리의 첫번째 커밋 


## 주의사항

1. 누가 했는지 사용자의 이름과 이메일 주소 설정 git config user.name [ ]
2. 커밋 메시지 남겨야 한다 -m 옵션
3. 커밋할 파일을 git add로 지정해 줘야힘 


## 작업영역의 종류 

<img width="433" alt="깃" src="https://user-images.githubusercontent.com/27615279/153789422-614d9d73-42b5-4f9d-96ed-4f2cc22c230c.PNG">


* working directory : 작업을 하는 프로젝트 디렉토리를 말함
* staging area : git add를 한 파일들이 존재하는 영역
* repository :  working directory의 변경 이력들이 저장되어 있는 영역
working directory는 working tree라고 하기도 하고, staging area는 index라고 할 때도 있음

git status : 깃이 인식하고 있는 프로젝트 디렉토리의 현재상태를 보여줌 




## status 관련

### 일단 Git에서 파일들은 크게 다음 2가지 상태를 가짐

<img width="488" alt="git_Status" src="https://user-images.githubusercontent.com/27615279/153789488-25991dec-71aa-428a-9e6e-d8d72e1b446d.PNG">


* Untracked 상태
* Tracked 상태 

그리고 Tracked 상태는 다시 아래와 같은 3가지 상태로 나눌 수 있음

<img width="425" alt="git_status2" src="https://user-images.githubusercontent.com/27615279/153789531-5c18e213-1d13-4a36-a8d9-5c1dd2486b15.PNG">



* Staged 상태
* Unmodified 상태
* Modified 상태


## git add 취소하기

git reset [file] : staging area에서 파일 제거  그러나, 변경된 새 모습은 그대로 workging directory에 남아있기 때문에 따로 지워줘야함 

```bash
git reset [file]
```


### 정리
```
이번 챕터에서 배운 커멘드 정리 

git init : 현재 디렉토리를 Git이 관리하는 프로젝트 디렉토리(=working directory)로 설정하고 그 안에 레포지토리(.git 디렉토리) 생성
git config user.name 'codeit' : 현재 사용자의 아이디를 'codeit'으로 설정(커밋할 때 필요한 정보)
git config user.email 'teacher@codeit.kr' : 현재 사용자의 이메일 주소를 'teacher@codeit.kr'로 설정(커밋할 때 필요한 정보)
git add [파일 이름] : 수정사항이 있는 특정 파일을 staging area에 올리기
git add [디렉토리명] : 해당 디렉토리 내에서 수정사항이 있는 모든 파일들을 staging area에 올리기 
git add . : working directory 내의 수정사항이 있는 모든 파일들을 staging area에 올리기
git reset [파일 이름] : staging area에 올렸던 파일 다시 내리기
git status : Git이 현재 인식하고 있는 프로젝트 관련 내용들 출력(문제 상황이 발생했을 때 현재 상태를 파악하기 위해 활용하면 좋음) 
git commit -m "커밋 메시지" : 현재 staging area에 있는 것들 커밋으로 남기기
git help [커맨드 이름] : 사용법이 궁금한 Git 커맨드의 공식 메뉴얼 내용 출력
```


# 커밋 다루기

## 최신커밋 수정하기 

파일 수정수 git add . , git commit --amend 명령어 수행

```
git add .

git commit --amend
```
commit 아이디는 변경됨 


## 커밋 메시지 작성 가이드 라인

1. 커밋 메세지의 제목과 상세 설명 사이에는 한줄을 비우기
2. 커밋 메시지의 제목 뒤에 온점(.)을 붙이지 말기
3. 커밋 메시지의 제목의 첫 번째 알파벳은 대문자로 작성하기
4. 커밋 메시지의 제목은 명령조로 작성하기(Fix it / Fixed it / Fixes it)
5. 커밋의 상세 내용에는 이런 걸 적으면 좋음
* 왜 커밋을 했는지
* 어떤 문제가 있었고
* 적용한 해결책이 어떤 효과를 가지는지

6.  현재 프로젝트 디렉토리의 상태가 그 내부의 전체 코드를 실행했을 때 에러가 발생하지 않는 상태인 경우에만 커밋을 하도록 함. 나중에 동료 개발자가 특정 커밋의 코드로 실행했을 때 에러가 발생한다면 혼란을 줄 수 있음

깃 alias 등록하기 

```
git config alias.history 'log --pretty=oneline'
```

git diff [commit id] [commit id] 

## 이전 커밋으로 git reset 하기

```
git reset --hard  [commit id]
```


## soft mixed hard 차이

![image](https://user-images.githubusercontent.com/27615279/153792106-60ea1fea-199b-40f4-9e97-f74d7b143860.png)



```
git reset HEAD^ #HEAD 바로 이전 커밋을 나타냄
git reset HEAD~2 #HEAD보다 2단계 아래의 커밋을 나타냄 
```


#### 커멘드 정리

```
git log : 커밋 히스토리를 출력
git log --pretty=oneline : --pretty 옵션을 사용하면 커밋 히스토리를 다양한 방식으로 출력할 수 있습니다. --pretty 옵션에 oneline이라는 값을 주면 커밋 하나당 한 줄씩 출력해줍니다. --pretty 옵션에 대해 더 자세히 알고싶으면 이 링크를 참고하세요. 
git show [커밋 아이디] : 특정 커밋에서 어떤 변경사항이 있었는지 확인
git commit --amend : 최신 커밋을 다시 수정해서 새로운 커밋으로 만듦
git config alias.[별명] [커맨드] : 길이가 긴 커맨드에 별명을 붙여서 이후로 별명으로 해당 커맨드를 실행할 수 있도록 설정
git diff [커밋 A의 아이디] [커밋 B의 아이디] : 두 커밋 간의 차이 비교
git reset [옵션] [커밋 아이디] : 옵션에 따라 하는 작업이 달라짐(옵션을 생략하면 --mixed 옵션이 적용됨) 
		(1) HEAD가 특정 커밋을 가리키도록 이동시킴(--soft는 여기까지 수행)

		(2) staging area도 특정 커밋처럼 리셋(--mixed는 여기까지 수행)

		(3) working directory도 특정 커밋처럼 리셋(--hard는 여기까지 수행)

		그리고 이때 커밋 아이디 대신 HEAD의 위치를 기준으로 한 표기법(예 : HEAD^, HEAD~3)을 사용해도 됨

git tag [태그 이름] [커밋 아이디] : 특정 커밋에 태그를 붙임
```


# git branch

브랜치 생성되 동시에 이동 
```
git checkout -b test
```

## conflic 해결

1. confilct가 발생한 파일을 연다
2. 머지의 결과가 되었으면 하는 모습대로 코드를 수정
3.  커밋 

혹은, 머지 자체를 취소 하는것도 방법

```
git merge --abort
```

### 여러개 파일 충돌

파일 하나씩 conflict를 해결하고 git add [파일 이름] 커맨드로 하나씩 staging area에 올리거나(중간중간에 git status 커맨드로 현재 상태 확인하면서) 모든 파일들의 conflict를 다 해결하고, git add . 커맨드로 한번에 staging area에 올리고

