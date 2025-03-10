# 2022 농업용 로봇 경진대회

<img src="https://user-images.githubusercontent.com/89721794/209078494-b63b9448-6a2b-4558-afd9-8760186de155.png" width="450px" height="600px" title="px(300)" alt="Title"></img><br/>


## 프로젝트

### 프로젝트 목차
#### 프로젝트 소개 & 미션
#### 프로젝트 계획표
#### 환경 구성(설치)
#### 실행
#### 다이어그램
#### 추가자료
---

>### 프로젝트 소개 & 미션
*▷ 대회 미션 소개*   
※ 제작한 로봇을 이용하여 과수원 모사 경기장 내의 출발점부터 과수(과수번호 16번)까지 주행하면서 과수 모형에 달린 과일을 검출, 분류, 계수   

   *<주행 부분> (로봇 임무 제한 시간 5분 이내)*   
     * 과수 열을 인식하여 열 사이로 충돌 없이 주행해야 함   
     * 주행 시간은 로봇의 출발점부터 주행하면서 각 과수의 과일 검출을 끝내고 마지막 과수(과수 번호 16번)까지 통과한 시간으로 측정   
![image](https://user-images.githubusercontent.com/89721794/209081987-ad0c63ed-7af1-4269-9a8f-106bc8340564.png)   


   *<회피 부분>*   
     * 주행 동안 주어진 장애물 모형 3종을 충돌 없이 회피하여야 함   
     * 장애물은 본선대회 당일 임의 재배치   
     * 장애물에 의해 로봇 주행경로의 폭 넓이를 제한할 예정   
     * 로봇에 빨강, 파랑, 노랑 LED를 설치하고 장애물 인지시 노랑 LED가 켜지도록    
![image](https://user-images.githubusercontent.com/89721794/209085652-ace97e0d-496e-42e1-a56e-9136e5b51373.png)   


   *<검출 부분>*   
    * 과수 모형에 달린 과일을 정상과와 질병과로 분류하고 계수하여야 함   
    * 로봇이 과수를 스스로 인식하여야 함   
    * 과수 번호별로 정상과와 질병과를 분류 및 계수하여야 함   
    * 과일 정상과와 질병과는 반점으로 구분함   
    * 과일의 설치 위치와 높이는 일정하지 않으며 본선대회 당일 임의배치   
    * 한 과수에 정상과와 질병과는 여러개 좌우 상하 배치되며, 서로 겹쳐서 설치   
    * 정상과 인지시 빨강, 질병과 인지시 파랑 LED가 깜빡거리도록 함   
![image](https://user-images.githubusercontent.com/89721794/209085661-da5fc18c-1e6f-4264-8c58-0f9edaaf3d52.png)   

   *<맵핑 부분>*   
    * 과수별로 계수된 과일 검출 결과는 USB에 저장되어 사무국에 전달하여야 함   
    * 각 팀별 임무 시작전에 사무국에서 로봇 USB 포트에 USB를 삽입할 예정이며, 임무 수행전에 과일 검출 결과는 USB에 아래와 같은 형태로 자동 저장 되어야 함.   
![image](https://user-images.githubusercontent.com/89721794/209085699-ecf5f1e2-a1c5-4b07-8f05-0bc1b0348c72.png)   

<br></br> 
>### 프로젝트 계획표
* 본선 준비기간 : 2022.07.25. ~ 2022.09.01.   
![image](https://user-images.githubusercontent.com/89721794/209088416-4fbfd9d8-2b6e-491d-98e4-5ddc0df8355b.png)

<br></br>   
>### 환경 구성(설치)

   ▷ 사용 OS   
  - Remote PC : Ubuntu 20.04 Desktop   
  - RaspberryPi4 8GB : Ubuntu 20.04 Server
  - ROS noetic Version 사용     
   
   ▷ 최종 하드웨어(터틀봇 사용)   
   ![image](https://user-images.githubusercontent.com/89721794/209090541-add76396-8749-4029-8633-258c96fe4e81.png)
   
<br></br>       
>### 실행   
   
   * 주행 부분: <https://github.com/MinGi-SUNG/ROS-Agricultural/tree/main/contest>
   * 데이터 학습 부분: <https://github.com/MinGi-SUNG/ROS-Agricultural/tree/main/Fruit_Dataset>
   * 영상처리 부분 : <https://github.com/MinGi-SUNG/ROS-Agricultural/tree/main/contest>
   
<br></br>       
>### 다이어그램 (블록다이어그램)

   * 데이터 흐름도   
![image](https://user-images.githubusercontent.com/89721794/209091895-be11d89c-bbf4-46cb-8b79-cf92f675c329.png)   
   
   * 소프트웨어 블록다이어그램   
![image](https://user-images.githubusercontent.com/89721794/209092006-82851ea5-0780-4208-b1d4-78654d8d2675.png)   
   
<br></br>      
>### 추가자료 (수상)   
<img src="https://user-images.githubusercontent.com/89721794/209164274-0542bf30-f301-4c13-9ca9-41ac6a0c88d7.png" width="450px" height="600px" title="px(300)" alt="Title"></img><br/>   

   * 수상 기사 : <https://www.jbnu.ac.kr/web/Board/98354/detailView.do?pageIndex=1&menu=2382>

