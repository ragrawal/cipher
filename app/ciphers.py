from enum import Enum
from typing import Dict, Callable

class CipherAlgorithm(str, Enum):
    """Available cipher algorithms."""
    MORSE = "morse"
    SHADOW = "shadow"
    CAESAR = "caesar"
    EMOJI = "emoji"
    DINO = "dinosaur"
    SUPERHERO = "superhero"

# Morse code mapping
MORSE_CODE: Dict[str, str] = {
    'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.', 'F': '..-.',
    'G': '--.', 'H': '....', 'I': '..', 'J': '.---', 'K': '-.-', 'L': '.-..',
    'M': '--', 'N': '-.', 'O': '---', 'P': '.--.', 'Q': '--.-', 'R': '.-.',
    'S': '...', 'T': '-', 'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-',
    'Y': '-.--', 'Z': '--..', '1': '.----', '2': '..---', '3': '...--',
    '4': '....-', '5': '.....', '6': '-....', '7': '--...', '8': '---..',
    '9': '----.', '0': '-----', ' ': ' '
}

REVERSE_MORSE_CODE: Dict[str, str] = {v: k for k, v in MORSE_CODE.items()}

def morse_encrypt(text: str) -> str:
    """Convert text to Morse code."""
    return ' '.join(MORSE_CODE.get(char.upper(), char) for char in text)

def morse_decrypt(text: str) -> str:
    """Convert Morse code back to text."""
    return ''.join(REVERSE_MORSE_CODE.get(code, code) for code in text.split())

def shadow_encrypt(text: str) -> str:
    """Convert text to shadow cipher (each letter is followed by its shadow)."""
    shadow_map = {'a': 'α', 'b': 'β', 'c': 'ç', 'd': 'δ', 'e': 'ε', 'f': 'φ',
                 'g': 'γ', 'h': 'η', 'i': 'ι', 'j': 'ξ', 'k': 'κ', 'l': 'λ',
                 'm': 'μ', 'n': 'ν', 'o': 'ο', 'p': 'π', 'q': 'θ', 'r': 'ρ',
                 's': 'σ', 't': 'τ', 'u': 'υ', 'v': 'ω', 'w': 'ψ', 'x': 'χ',
                 'y': 'υ', 'z': 'ζ', ' ': ' '}
    return ''.join(shadow_map.get(char.lower(), char) for char in text)

def shadow_decrypt(text: str) -> str:
    """Convert shadow cipher back to text."""
    reverse_shadow_map = {'α': 'a', 'β': 'b', 'ç': 'c', 'δ': 'd', 'ε': 'e',
                         'φ': 'f', 'γ': 'g', 'η': 'h', 'ι': 'i', 'ξ': 'j',
                         'κ': 'k', 'λ': 'l', 'μ': 'm', 'ν': 'n', 'ο': 'o',
                         'π': 'p', 'θ': 'q', 'ρ': 'r', 'σ': 's', 'τ': 't',
                         'υ': 'u', 'ω': 'v', 'ψ': 'w', 'χ': 'x', 'υ': 'y',
                         'ζ': 'z', ' ': ' '}
    return ''.join(reverse_shadow_map.get(char, char) for char in text)

def caesar_encrypt(text: str, shift: int = 3) -> str:
    """Encrypt text using Caesar cipher with a default shift of 3."""
    result = ""
    for char in text:
        if char.isalpha():
            ascii_offset = ord('A') if char.isupper() else ord('a')
            shifted = (ord(char) - ascii_offset + shift) % 26
            result += chr(shifted + ascii_offset)
        else:
            result += char
    return result

def caesar_decrypt(text: str, shift: int = 3) -> str:
    """Decrypt text using Caesar cipher with a default shift of 3."""
    return caesar_encrypt(text, -shift)

# Fun Emoji mapping
EMOJI_CODE: Dict[str, str] = {
    'A': '🅰️', 'B': '🅱️', 'C': '©️', 'D': '🎯', 'E': '📧', 'F': '🏁',
    'G': '🎮', 'H': '🏠', 'I': '💡', 'J': '🎮', 'K': '🔑', 'L': '🎪',
    'M': '〽️', 'N': '♑', 'O': '⭕', 'P': '🅿️', 'Q': '👑', 'R': '®️',
    'S': '💲', 'T': '✝️', 'U': '⛎', 'V': '✌️', 'W': '〰️', 'X': '❌',
    'Y': '💹', 'Z': '💤', ' ': '⬜', '1': '1️⃣', '2': '2️⃣', '3': '3️⃣',
    '4': '4️⃣', '5': '5️⃣', '6': '6️⃣', '7': '7️⃣', '8': '8️⃣', '9': '9️⃣',
    '0': '0️⃣'
}

REVERSE_EMOJI_CODE: Dict[str, str] = {v: k for k, v in EMOJI_CODE.items()}

# Dinosaur-themed mapping
DINO_CODE: Dict[str, str] = {
    'A': 'ANKYLO', 'B': 'BRACHI', 'C': 'CARNO', 'D': 'DIPLO', 'E': 'EORAP',
    'F': 'FALCA', 'G': 'GALLI', 'H': 'HERRERA', 'I': 'IGUAN', 'J': 'JURA',
    'K': 'KENTO', 'L': 'LIMA', 'M': 'MEGA', 'N': 'NANO', 'O': 'OURA',
    'P': 'PACHY', 'Q': 'QUETZ', 'R': 'REX', 'S': 'STEGO', 'T': 'TREX',
    'U': 'ULTRA', 'V': 'VELO', 'W': 'WANG', 'X': 'XENO', 'Y': 'YANG',
    'Z': 'ZINO', ' ': 'DINO'
}

REVERSE_DINO_CODE: Dict[str, str] = {v: k for k, v in DINO_CODE.items()}

# Superhero-themed mapping
HERO_CODE: Dict[str, str] = {
    'A': 'AVENGER', 'B': 'BATMAN', 'C': 'CAPTAIN', 'D': 'DAREDEVIL', 'E': 'ELEKTRA',
    'F': 'FLASH', 'G': 'GREEN', 'H': 'HULK', 'I': 'IRONMAN', 'J': 'JOKER',
    'K': 'KRYPTO', 'L': 'LOGAN', 'M': 'MARVEL', 'N': 'NOVA', 'O': 'ORACLE',
    'P': 'PANTHER', 'Q': 'QUINN', 'R': 'ROBIN', 'S': 'SPIDER', 'T': 'THOR',
    'U': 'ULTRA', 'V': 'VISION', 'W': 'WASP', 'X': 'XMEN', 'Y': 'YELLOW',
    'Z': 'ZORRO', ' ': 'HERO'
}

REVERSE_HERO_CODE: Dict[str, str] = {v: k for k, v in HERO_CODE.items()}

def emoji_encrypt(text: str) -> str:
    """Convert text to emoji code."""
    return ''.join(EMOJI_CODE.get(char.upper(), char) for char in text)

def emoji_decrypt(text: str) -> str:
    """Convert emoji code back to text."""
    result = ''
    i = 0
    while i < len(text):
        found = False
        for emoji_len in range(4, 0, -1):  # Check for emoji of different lengths
            if text[i:i+emoji_len] in REVERSE_EMOJI_CODE:
                result += REVERSE_EMOJI_CODE[text[i:i+emoji_len]]
                i += emoji_len
                found = True
                break
        if not found:
            result += text[i]
            i += 1
    return result

def dino_encrypt(text: str) -> str:
    """Convert text to dinosaur names."""
    return '-'.join(DINO_CODE.get(char.upper(), char) for char in text)

def dino_decrypt(text: str) -> str:
    """Convert dinosaur names back to text."""
    return ''.join(REVERSE_DINO_CODE.get(code, code) for code in text.split('-'))

def hero_encrypt(text: str) -> str:
    """Convert text to superhero names."""
    return '-'.join(HERO_CODE.get(char.upper(), char) for char in text)

def hero_decrypt(text: str) -> str:
    """Convert superhero names back to text."""
    return ''.join(REVERSE_HERO_CODE.get(code, code) for code in text.split('-'))

# Mapping of algorithms to their encryption/decryption functions
CIPHER_FUNCTIONS: Dict[CipherAlgorithm, tuple[Callable[[str], str], Callable[[str], str]]] = {
    CipherAlgorithm.MORSE: (morse_encrypt, morse_decrypt),
    CipherAlgorithm.SHADOW: (shadow_encrypt, shadow_decrypt),
    CipherAlgorithm.CAESAR: (caesar_encrypt, caesar_decrypt),
    CipherAlgorithm.EMOJI: (emoji_encrypt, emoji_decrypt),
    CipherAlgorithm.DINO: (dino_encrypt, dino_decrypt),
    CipherAlgorithm.SUPERHERO: (hero_encrypt, hero_decrypt),
}

def encrypt_message(message: str, algorithm: CipherAlgorithm) -> str:
    """Encrypt a message using the specified algorithm."""
    encrypt_func, _ = CIPHER_FUNCTIONS[algorithm]
    return encrypt_func(message)

def decrypt_message(message: str, algorithm: CipherAlgorithm) -> str:
    """Decrypt a message using the specified algorithm."""
    _, decrypt_func = CIPHER_FUNCTIONS[algorithm]
    return decrypt_func(message)

# Cipher descriptions for interactive learning
CIPHER_DESCRIPTIONS: Dict[str, Dict[str, str]] = {
    "morse": {
        "title": "Morse Code - Dots and Dashes!",
        "description": "Morse code uses dots (.) and dashes (-) to represent letters. It was used to send messages over telegraph wires!",
        "fun_fact": "SOS (... --- ...) is the most famous morse code signal for help!",
        "example": "Hello → .... . .-.. .-.. ---"
    },
    "shadow": {
        "title": "Shadow Cipher - Greek-style Letters!",
        "description": "This cipher turns your letters into mysterious Greek-looking symbols. It's like writing in an ancient language!",
        "fun_fact": "Many of these symbols are actually used in math and science!",
        "example": "Hi → ηι"
    },
    "caesar": {
        "title": "Caesar Cipher - The Roman Emperor's Secret Code!",
        "description": "This cipher shifts each letter by 3 positions. It was used by Julius Caesar to send secret messages!",
        "fun_fact": "Julius Caesar used this to communicate with his generals in battle.",
        "example": "ABC → DEF"
    },
    "emoji": {
        "title": "Emoji Cipher - Modern Day Hieroglyphics! 😎",
        "description": "Turn your message into fun emojis! Each letter becomes a special emoji symbol.",
        "fun_fact": "Emojis are like modern-day hieroglyphics - pictures that represent words!",
        "example": "Hi → 🏠💡"
    },
    "dinosaur": {
        "title": "Dinosaur Cipher - Prehistoric Messaging! 🦖",
        "description": "Each letter becomes a dinosaur name! Your message will roar with prehistoric power!",
        "fun_fact": "There were over 700 different species of dinosaurs!",
        "example": "Hi → HERRERA-IGUAN"
    },
    "superhero": {
        "title": "Superhero Cipher - Heroes Assemble! 🦸‍♂️",
        "description": "Transform your message using superhero names! Perfect for secret superhero communications!",
        "fun_fact": "The first superhero comic was published in 1938!",
        "example": "Hi → HULK-IRONMAN"
    }
}

def get_cipher_info(algorithm: CipherAlgorithm) -> Dict[str, str]:
    """Get the learning information for a cipher algorithm."""
    return CIPHER_DESCRIPTIONS[algorithm.value] 