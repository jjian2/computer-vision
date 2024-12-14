# Object recognition services for the visually impaired
![1111](https://github.com/user-attachments/assets/8af4e06d-d85c-4727-bbbf-b8b41233154f)
![3333333](https://github.com/user-attachments/assets/1d655a2d-c12c-4bc9-9685-a017b3b1a3af)
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
