# Object recognition services for the visually impaired
![1111](https://github.com/user-attachments/assets/8af4e06d-d85c-4727-bbbf-b8b41233154f) ![3333333](https://github.com/user-attachments/assets/1d655a2d-c12c-4bc9-9685-a017b3b1a3af)
![2222222](https://github.com/user-attachments/assets/10c1a171-d754-4393-bab6-1a0f6deb4598)
![444444](https://github.com/user-attachments/assets/2cdf18df-c7e4-49d6-9d8e-13ff7335df28)

# 객체 인식 기술을 이용하여 장애인 보조 시스템을 서비스 기획 및 구현

- 주제: 시각 장애인을 위한 객체 인식 기반 안내 시스템.
- 구현 아이디어 : 카메라로 주변 객체(사람, 장애물, 신호등 등)를 감지.
                 음성으로 정보를 제공하여 안전한 이동 지원.
- 활용 분야: 장애인 지원, 접근성 향상.

# 요구 사항들

- 파이썬 3.6.10
- GPU 및 CUDA 9.0 설치

# 짧은 개요
- 이 시스템은 YOLOv11 모델을 사용하여 시각 장애인분들이 여러 객체를 인식 할 때 이 기술이 사진을 보고 어떤 객체인지 인식을 해주는 시스템 또한,  머신 러닝 및 컴퓨터 비전 프로젝트로 개발했으며, 동물, 자동차, 사람등을 구분할 수 있도록 설계하였습니다.

# 코드 요약

- 파일 업로드: 사용자가 이미지를 업로드.
- YOLO 모델 로드 및 감지: 업로드된 이미지에서 객체를 감지.
- 결과 저장 및 반환: 감지된 이미지를 저장하고, 객체 정보를 템플릿에 전달.
- 웹 프론트엔드 연결: 결과를 HTML 템플릿을 통해 사용자에게 표시.

 # 영상 파일을 처리할 경우
 
 영상 파일 업로드:
 
- 사용자가 동영상을 업로드하도록 <form>에서 accept="video/*"를 추가.
- 업로드된 동영상을 Flask에서 처리하여 저장.
  
OpenCV로 영상 처리:

- cv2.VideoCapture로 동영상을 읽어 프레임 단위로 처리.
- YOLO 모델로 각 프레임을 처리하여 객체 감지 수행.
- 감지 결과를 새 비디오 파일로 저장.
  
영상 파일 출력:

- 감지 결과 비디오를 사용자가 다운로드하거나 시청할 수 있도록 반환.

영상 처리 코드: 

- 영상 처리 루프

![12](https://github.com/user-attachments/assets/d0cdffc2-cc11-4447-87d7-8c46d9b25594)

- flask 라우트

![13](https://github.com/user-attachments/assets/06064332-c837-4148-a86d-edcfbb10c0e9)

# 웹캠으로 실시간 감지를 처리할 경우

OpenCV로 웹캠 연결:

- cv2.VideoCapture(0)을 사용하여 웹캠 스트림을 연결.
  
실시간 감지:

- 각 프레임에서 YOLO 모델로 객체 감지를 수행하고 화면에 표시.
  
종료 처리:

- 키 입력(q)으로 스트리밍을 종료.

웹캠 처리 코드

- 실시간 웹캠 감지 루프:

![12](https://github.com/user-attachments/assets/7dae2648-53fa-4866-9aea-b28dbc5dfc5d)

- Flask와 연동:
  
- 실시간 웹캠 스트리밍은 Flask-SocketIO 또는 Flask Video Streaming을 활용하여 웹에서 제공 가능.
- OpenCV로 캡처한 프레임을 HTTP 응답으로 전송.

# 주요 차이점

![1313](https://github.com/user-attachments/assets/144d87e0-1d00-4ecd-a7f5-5aac67828f25)
