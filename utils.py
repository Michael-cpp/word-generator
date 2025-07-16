import csv
import json
import random
import os

CSV_PATH = '/app/data/words.csv'
USERS_FILE = '/app/data/users.json'

def pop_random_word():
    if not os.path.exists(CSV_PATH):
        return None
    with open(CSV_PATH, newline='', encoding='utf-8') as csvfile:
        words = list(csv.DictReader(csvfile))
    if not words:
        return None

    selected = random.choice(words)
    remaining = [w for w in words if w != selected]

    with open(CSV_PATH, 'w', newline='', encoding='utf-8') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=['word', 'description'])
        writer.writeheader()
        writer.writerows(remaining)

    return f"📖 {selected['word']}\n{selected['description']}"

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

