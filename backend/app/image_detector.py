
from pathlib import Path
from functools import lru_cache

from PIL import Image
from ultralytics import YOLO


MODEL_PATH = (
    Path(__file__).resolve().parent.parent
    / "models"
    / "best.pt"
)


@lru_cache(maxsize=1)
def load_model():
    if not MODEL_PATH.exists():
        raise FileNotFoundError(
            f"Trained YOLO model not found: {MODEL_PATH}"
        )

    return YOLO(str(MODEL_PATH))


def analyze_image(image: Image.Image, confidence: float = 0.25):
    model = load_model()

    results = model.predict(
        source=image.convert("RGB"),
        conf=confidence,
        verbose=False
    )

    result = results[0]
    detections = []

    for box in result.boxes:
        class_id = int(box.cls[0])
        score = float(box.conf[0])
        x1, y1, x2, y2 = map(
            float, box.xyxy[0].tolist()
        )

        detections.append({
            "class_name": model.names[class_id],
            "confidence": round(score, 4),
            "box": {
                "x1": round(x1, 2),
                "y1": round(y1, 2),
                "x2": round(x2, 2),
                "y2": round(y2, 2)
            }
        })

    annotated = result.plot()[:, :, ::-1]
    annotated_image = Image.fromarray(annotated)

    return {
        "detection_count": len(detections),
        "detections": detections,
        "annotated_image": annotated_image
    }
