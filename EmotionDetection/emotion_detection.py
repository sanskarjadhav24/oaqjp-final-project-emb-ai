
import requests

def emotion_detector(text_to_analyze):
    if not isinstance(text_to_analyze, str) or not text_to_analyze.strip():
        return None

    url = (
        "https://sn-watson-emotion.labs.skills.network/"
        "v1/watson.runtime.nlp.v1/NlpService/EmotionPredict"
    )

    headers = {
        "grpc-metadata-mm-model-id":
        "emotion_aggregated-workflow_lang_en_stock"
    }

    try:
        response = requests.post(
            url,
            headers=headers,
            json={"raw_document": {"text": text_to_analyze}},
            timeout=20
        )

        if response.status_code != 200:
            return None

        emotions = response.json()["emotionPredictions"][0]["emotion"]
        dominant = max(emotions, key=emotions.get)

        return {
            **emotions,
            "dominant_emotion": dominant
        }

    except (requests.RequestException, ValueError, KeyError, IndexError):
        return None
