# git 사용법 알려주세요..집단지성 

## 1 Git에서 프로젝트가 저장되는 과정
- 1 ) 작업공간 : local로 개발하고 있는 공간
- 2 ) Staging area : Repository로 가기 전에 거쳐가는 확인공간
- 3 ) Repository : 저장소
#### 여기서 1 -> 2 -> 3 순으로 파일이 이동하는데 1 -> 2 는 Add / 2 -> 3은 commit & push 한다고 함
#### commit은 저장소의 Check point로 어떤 변경사항들이 저장되있는지를 기록하는거라함
#### commit 예제 : "[Mainpage css fix] 메인페이지 interface 수정" 
#### -> [이번 커밋의 간단한 내역] 이번 커밋의 자세한 내역 
<br/>

## 2 git 사용법
### 1 Repository에서 내 editor로 파일 가져오기
- 1 ) `git clone https://github.com/whenilikeahorse/web.git <클론할 폴더 이름>`
- 2 ) 클론한 폴더에서 editor키면 repo에 있는 자료들 가져와짐
- 3 ) 누군가 origin master branch를 업데이트 한 경우 `git pull origin master` 명령어로 local 데이터 업데이트 할 수 있음 <push 하기 전에 꼭!! 해주어야함>
### 2 내 local에서 Repository로 옮기기 
#### 명령어 순서
- 1 ) `git init` : git 저장소 초기화 (프로젝트 초기에 한번)
- 2 ) `git status` : 저장소 상태 체크, 현재 프로젝트 변경사항 확인
- 3 ) `git add .` : 모든 파일을 staging area로 올리기
- 4 ) `git commit -m <설명>` : 어떤거를 commit했는지 설명에 간략하게 작성
#### 추후에 변경사항이 있을 시에 3,4번 항목(add & commit)을 실행해준다
- 5 ) `git remote add origin https://github.com/whenilikeahorse/web.git`
- 6 ) `git push origin master`

### 근데 여기서 에러뜰꺼임
![image](file:///C:/Users/%EA%B4%91%EC%9D%BC/Desktop/%EC%BA%A1%EC%B2%98.JPG)
그 이유는 여기에 가서 확인 (규리쓰가 알려줌)https://lhy.kr/git-workflow<br/>

### 이후에
`git fetch origin`<br/>
`git rebase origin/master`<br/>
하고 다시 push하면 될거임 // commit 상태 확인하고 싶으면 `git log`
