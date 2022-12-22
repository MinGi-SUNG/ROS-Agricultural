영상처리
=====



### [Yolo v5 사용] 정상과, 질병과 학습
![YOlo v5 이미지](https://user-images.githubusercontent.com/89784307/209088907-ae06ef8d-8393-4391-8930-5d88ae4748de.png)


- 데이터 수집

| Disease fruit | Normal fruit | Obstacle |
|--|--|--|
|![Disease fruit](https://user-images.githubusercontent.com/89784307/209089720-6ece6c6b-e040-465e-a1ec-51ae1b7d9419.png)|![Normal fruit](https://user-images.githubusercontent.com/89784307/209089964-6ece60d6-cfe9-4181-be2b-1b8980d367ea.png)|![Obstacle](https://user-images.githubusercontent.com/89784307/209090017-0ef5830c-5ba8-41f7-8b2f-01be5cb9ce53.png)|

&nbsp;&nbsp; YOLOv5를 통한 정상과, 질병과, 장애물을 학습시킴</br>
  
- 학습 이미지 데이터</br>
  테스트에 필요한 이미지를 직접촬영하여 사용</br>
  Roboflow를 이용하여 클래스 라벨링 및 회전, 잡음 등의 효과를 적용</br>
  →  최종 데이터셋 생성
    
| 이미지 파일 생성 | 데이터 전처리를 통한 데이터셋 생성 |
|--|--|
|![image](https://user-images.githubusercontent.com/89721794/209165289-75309987-6728-46f4-b9ee-c30422f9f74b.png)|![image](https://user-images.githubusercontent.com/89721794/209165296-6c257319-ac6b-47a3-9c23-df41917a6da7.png)|

* 학습
  - 각 클래스별 데이터 약 500개
  - ‘batch size = 4 / epochs = 100’으로 진행
  - 앞선 학습에서 나타난 문제를 해결하기 위해 데이터를 추가
        * 검출할 객체와 비슷한 색을 배경으로한 데이터 추가
        * 다양한 각도에서 촬영한 데이터를 추가
