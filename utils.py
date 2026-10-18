import json
import os
import requests
from deep_translator import LingueeTranslator
from deep_translator.exceptions import BaseError
import pymorphy3

ASSOCI_API = "https://associ.ru/api/v1/play"
GOOGLE_TRANSLATE_API = "https://translate.googleapis.com/translate_a/single"
USERS_FILE = '/app/data/users.json'

linguee = LingueeTranslator(source="russian", target="english")
morph = pymorphy3.MorphAnalyzer()

def get_random_russian_word() -> str:
    try:
        response = requests.post(
            ASSOCI_API,
            json={"lang_code": "ru"},
            timeout=5
        )
        response.raise_for_status()
        data = response.json()
        ru_word = data.get("new", {}).get("word")
        if not isinstance(ru_word, str):
            print(f"Unexpected API response: {data}")
        return ru_word
    except requests.RequestException as e:
        print("Random word service unavailable")


def translate_with_google(word: str) -> str:
    response = requests.get(
        GOOGLE_TRANSLATE_API,
        params={"client": "gtx", "sl": "ru", "tl": "en", "dt": "t", "q": word},
        timeout=5
    )
    response.raise_for_status()
    return "".join(part[0] for part in response.json()[0])


def translate_with_linguee(word: str) -> str:
    return linguee.translate(word)


def translate_ru_to_en(word: str) -> str:
    for translate in (translate_with_google, translate_with_linguee):
        try:
            return translate(word)
        except (requests.RequestException, BaseError, ValueError, LookupError, TypeError) as e:
            print(f"{translate.__name__} failed: {e}")
    return None


def get_word_message() -> str:
    ru_word = get_random_russian_word()

    # normalize word form (important!)
    ru_normalized = morph.parse(ru_word)[0].normal_form

    en_translation = translate_ru_to_en(ru_normalized)

    return (
        f"📖 {ru_normalized}\n"
        f"🇬🇧 {en_translation or 'translation unavailable'}"
    )

def load_users():
    if not os.path.exists(USERS_FILE):
        return []
    try:
        with open(USERS_FILE, 'r') as f:
            content = f.read().strip()
            return json.loads(content) if content else []
    except json.JSONDecodeError:
        return []

