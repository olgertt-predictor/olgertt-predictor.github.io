import json
from datetime import datetime

def generate_predictions():
    predictions = {
        "date": datetime.now().strftime("%Y-%m-%d %H:%M"),
        "predictions": [
            {
                "match": "Реал Мадрид vs Манчестер Сити",
                "prediction": "Победа Реал Мадрид или ничья (1X), тотал больше 2.5"
            },
            {
                "match": "Бавария vs Боруссия Дортмунд",
                "prediction": "Обе забьют — да"
            },
            {
                "match": "Ювентус vs Милан",
                "prediction": "Меньше 2.5 голов"
            }
        ]
    }
    with open("predictions.json", "w", encoding="utf-8") as f:
        json.dump(predictions, f, ensure_ascii=False, indent=2)

if __name__ == "__main__":
    generate_predictions()