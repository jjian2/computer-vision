import os
import uuid
from flask import Flask, request, render_template, redirect, url_for, send_from_directory
import cv2
import torch
from PIL import Image

# Flask 애플리케이션 초기화
app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = './static/uploads'  # 업로드 경로
app.config['DETECTION_FOLDER'] = './static/detections'  # 감지 결과 경로
os.makedirs(app.config['UPLOAD_FOLDER'], exist_ok=True)
os.makedirs(app.config['DETECTION_FOLDER'], exist_ok=True)

# YOLOv11 모델 로드 (YOLOv5n 사용으로 대체)
def load_model():
    model = torch.hub.load('ultralytics/yolov5', 'yolov5n', pretrained=True)  # YOLOv5n 로드
    model.eval()  # 평가 모드 설정
    return model

# 객체 감지 수행 및 결과 저장
def detect_objects(model, input_path, output_path):
    # 이미지 로드
    img = Image.open(input_path).convert('RGB')

    # 객체 감지 수행
    results = model(img)

    # 결과 이미지에 바운딩 박스 그리기
    results.render()  # results.ims에 바운딩 박스가 그려진 이미지 저장

    # 결과 이미지를 저장
    result_img = Image.fromarray(results.ims[0])
    result_img.save(output_path)

    # 감지된 객체 정보 반환
    return results.pandas().xyxy[0]  # 감지된 객체 정보 (Bounding Box, 클래스, 신뢰도 등)

# Flask 라우트
@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        if 'file' not in request.files:
            return redirect(request.url)
        file = request.files['file']
        if file.filename == '':
            return redirect(request.url)

        # UUID로 파일 이름 생성
        extension = os.path.splitext(file.filename)[1].lower()
        filename = f"{uuid.uuid4().hex}{extension}"
        input_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
        output_path = os.path.join(app.config['DETECTION_FOLDER'], filename)
        file.save(input_path)

        # 객체 감지 수행
        try:
            detections = detect_objects(model, input_path, output_path)
            detection_info = detections.to_dict(orient='records')  # 객체 정보를 리스트로 변환
            return render_template('result.html', filename=filename, detections=detection_info)
        except Exception as e:
            return f"오류 발생: {str(e)}"

    return render_template('index.html')

@app.route('/uploads/<filename>')
def uploaded_file(filename):
    return send_from_directory(app.config['UPLOAD_FOLDER'], filename)

@app.route('/detections/<filename>')
def detection_file(filename):
    return send_from_directory(app.config['DETECTION_FOLDER'], filename)

# 메인 실행
if __name__ == '__main__':
    print("YOLOv11 모델 로드 중...")
    model = load_model()
    app.run(debug=True)
