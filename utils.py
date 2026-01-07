import json
import os
import requests
from deep_translator import GoogleTranslator
import pymorphy3

ASSOCI_API = "https://associ.ru/api/v1/play"
USERS_FILE = '/app/data/users.json'

translator = GoogleTranslator(source="ru", target="en")
morph = pymorphy3.MorphAnalyzer()

def get_random_russian_word() -> str:
    response = requests.get(ASSOCI_API, timeout=5)
    response.raise_for_status()
    return response.json()["new"]


def translate_ru_to_en(word: str) -> str:
    try:
        return translator.translate(word)
    except Exception:
        return "Translation unavailable"


def get_word_message() -> str:
    ru_word = get_random_russian_word()

    # normalize word form (important!)
    ru_normalized = morph.parse(ru_word)[0].normal_form

    en_translation = translate_ru_to_en(ru_normalized)

    return (
        f"📖 {ru_normalized}\n"
        f"🇬🇧 {en_translation}"
    )

def save_user(chat_id):
    users = load_users()
    if chat_id not in users:
        users.append(chat_id)
        with open(USERS_FILE, 'w') as f:
            json.dump(users, f)

def load_users():
    if not os.path.exists(USERS_FILE):
        return []
    try:
        with open(USERS_FILE, 'r') as f:
            content = f.read().strip()
            return json.loads(content) if content else []
    except json.JSONDecodeError:
        return []

