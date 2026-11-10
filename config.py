"""VELOCITY SLOVAK - language pack, brand and motion design constants."""

import os
from pathlib import Path

from dotenv import load_dotenv

BASE_DIR = Path(__file__).resolve().parent
load_dotenv(BASE_DIR / ".env")

OUTPUT_DIR = BASE_DIR / "output"
LESSONS_DIR = OUTPUT_DIR / "lessons"
HISTORY_DIR = OUTPUT_DIR / "history"
SCENE_DIR = BASE_DIR / "scene"

VIDEO_WIDTH = 1080
VIDEO_HEIGHT = 1920
FPS = 30

# ---------------------------------------------------------------- brand

BRAND = "VELOCITY SLOVAK"
BRAND_LOCKUP_TOP = "VELOCITY"
BRAND_LOCKUP_BOTTOM = "SLOVAK"
HANDLE = "@velocityslovak"
MASCOT_NAME = "Velo"

# ==== LANGUAGE PACK START ====
LANGUAGE = {
    "code": "sk",
    "name": "Slovak",
    "native_name": "Slovenčina",
    "history_key": "slovak",
    "english_voice": "en-US-AvaNeural",
    "english_fallback_voice": "en-US-GuyNeural",
    "native_voice": "sk-SK-LukasNeural",
    "native_fallback_voice": "sk-SK-ViktoriaNeural",
    "native_engine": "edge",
    "native_lang_code": "sk",
    "english_rate": "-2%",
    "native_rate": "-6%",
    "english_pitch": "+0Hz",
    "native_pitch": "+0Hz",
    "native_label": "SLOVENČINA",
    "translit_label": "SAY IT LIKE",
    "greeting": "Ahoj!",
    "encouragement": "Výborne!",
    "rtl": False,
    "char_tiles": False,
    "script_font": "",
}
# ==== LANGUAGE PACK END ====

AI_MODEL = os.getenv("AI_MODEL", "gemini-fast")
POLLINATIONS_API_KEY = os.getenv("POLLINATIONS_API_KEY", "")

# ---------------------------------------------------------------- timing (seconds)

INTRO_DURATION = 4.0
OUTRO_DURATION = 5.2
EN_CARD_IN = 0.55
GAP_EN_NATIVE = 0.5
NATIVE_CARD_LEAD = 0.35
GAP_BEFORE_REPEAT = 0.8
TAIL_HOLD = 1.4
MAX_REEL_DURATION = 88.0

# ---------------------------------------------------------------- palette

INK = "#3C3C3C"
MUTED = "#8A8A8A"
CREAM = "#FFF8E7"
GREEN = "#58CC02"
GREEN_DARK = "#46A302"
GREEN_DEEP = "#3D8F00"
BLUE = "#1CB0F6"
PURPLE = "#A560E8"
ORANGE = "#FF7A00"
RED = "#FF4B4B"
YELLOW = "#F5A700"
TEAL = "#00A889"
PINK = "#E056A0"

PALETTE = [GREEN, BLUE, PURPLE, ORANGE, RED, YELLOW, TEAL, PINK]

# ---------------------------------------------------------------- categories
# (english, native, icon, accent)

# ==== CATEGORY TABLE START ====
CATEGORY_TABLE = [
    ("Greetings", "Pozdravy", "hand", "#1CB0F6"),
    ("Basic Phrases", "Základné Frázy", "chat", "#58CC02"),
    ("Common Expressions", "Bežné Výrazy", "chat", "#1CB0F6"),
    ("Travel", "Cestovanie", "plane", "#1CB0F6"),
    ("Restaurant", "Reštaurácia", "fork", "#FF7A00"),
    ("Shopping", "Nakupovanie", "bag", "#E056A0"),
    ("Emergency", "Núdzové Situácie", "siren", "#FF4B4B"),
    ("Family Terms", "Rodinné Výrazy", "heart", "#E056A0"),
    ("Numbers", "Čísla", "hash", "#A560E8"),
    ("Time", "Čas", "clock", "#00A889"),
    ("Motivation", "Motivácia", "rocket", "#A560E8"),
    ("Love", "Láska", "heart", "#FF4B4B"),
    ("Success", "Úspech", "trophy", "#F5A700"),
    ("Wisdom", "Múdrosť", "book", "#A560E8"),
    ("Happiness", "Šťastie", "smile", "#F5A700"),
    ("Self Improvement", "Sebazdokonaľovanie", "leaf", "#58CC02"),
    ("Gratitude", "Vďačnosť", "heart", "#FF7A00"),
    ("Friendship", "Priateľstvo", "users", "#00A889"),
    ("Hope", "Nádej", "sun", "#FF7A00"),
    ("Creativity", "Kreativita", "palette", "#E056A0"),
    ("Inner Peace", "Vnútorný Pokoj", "lotus", "#00A889"),
    ("Confidence", "Sebadôvera", "shield", "#1CB0F6"),
    ("Perseverance", "Vytrvalosť", "mountain", "#FF7A00"),
    ("Inspiration", "Inšpirácia", "sparkles", "#A560E8"),
    ("Positive Life", "Pozitívny Život", "sun", "#58CC02"),
    ("Courage", "Odvaha", "shield", "#FF4B4B"),
    ("Kindness", "Láskavosť", "heart", "#E056A0"),
    ("Patience", "Trpezlivosť", "hourglass", "#00A889"),
    ("Forgiveness", "Odpustenie", "hands", "#FF7A00"),
    ("Strength", "Sila", "dumbbell", "#FF4B4B"),
    ("Joy", "Radosť", "smile", "#F5A700"),
    ("Balance", "Rovnováha", "scale", "#00A889"),
    ("Growth", "Rast", "sprout", "#58CC02"),
    ("Purpose", "Účel", "target", "#A560E8"),
    ("Mindfulness", "Všímavosť", "lotus", "#00A889"),
    ("Daily Routine", "Denná rutina", "calendar", "#1CB0F6"),
    ("Weather", "Počasie", "cloud", "#1CB0F6"),
    ("Feelings", "Pocity", "smile", "#E056A0"),
    ("Food", "Jedlo", "fork", "#FF7A00"),
    ("Health", "Zdravie", "heart", "#58CC02"),
    ("Work", "Práca", "briefcase", "#1CB0F6"),
    ("Technology", "Technológia", "chip", "#A560E8"),
    ("Nature", "Príroda", "leaf", "#58CC02"),
    ("Animals", "Zvieratá", "paw", "#FF7A00"),
    ("Colors", "Farby", "palette", "#E056A0"),
    ("Directions", "Smery", "compass", "#1CB0F6"),
    ("Body Parts", "Časti tela", "hand", "#00A889"),
    ("Clothes", "Oblečenie", "shirt", "#E056A0"),
    ("Music", "Hudba", "music", "#A560E8"),
    ("Sports", "Šport", "ball", "#FF7A00"),
    ("Holidays", "Sviatky", "gift", "#FF4B4B"),
    ("Education", "Vzdelávanie", "book", "#1CB0F6"),
    ("Culture", "Kultúra", "globe", "#00A889"),
    ("Finance", "Financie", "coin", "#58CC02"),
    ("Relationships", "Vzťahy", "users", "#E056A0"),
]
# ==== CATEGORY TABLE END ====

CATEGORIES = [c[0] for c in CATEGORY_TABLE]
CATEGORIES_NATIVE = {c[0]: c[1] for c in CATEGORY_TABLE}
CATEGORY_META = {c[0]: {"native": c[1], "icon": c[2], "accent": c[3]} for c in CATEGORY_TABLE}
MAX_RECENT_CATEGORIES = 25

# ==== HASHTAGS START ====
HASHTAGS = [
    "#learnslovak",
    "#slovaklessons",
    "#slovakforbeginners",
    "#languagelearning",
    "#slovakvocabulary",
    "#velocityslovak",
    "#dailyslovak",
    "#slovak",
    "#learnlanguages",
    "#speakslovak",
    "#bilingual",
    "#languagetips",
]
# ==== HASHTAGS END ====
