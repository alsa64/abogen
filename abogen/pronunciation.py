#!/usr/bin/env -S uv run --script
# /// script
# requires-python = ">=3.12"
# dependencies = []
# ///

import os
import re
from pathlib import Path
from typing import Dict


def get_xdg_config_dir() -> Path:
    """Get XDG config directory for abogen."""
    xdg_config_home = os.environ.get("XDG_CONFIG_HOME")
    if xdg_config_home:
        return Path(xdg_config_home) / "abogen"
    else:
        return Path.home() / ".config" / "abogen"


def get_pronunciation_config_path() -> Path:
    """Get path to pronunciation override config file."""
    return get_xdg_config_dir() / "pronunciation.toml"


def load_pronunciation_config() -> Dict:
    """Load pronunciation override configuration from TOML file."""
    config_path = get_pronunciation_config_path()

    if not config_path.exists():
        return create_default_config()

    try:
        import tomllib

        with open(config_path, "rb") as f:
            return tomllib.load(f)
    except ImportError:
        try:
            import tomli as tomllib

            with open(config_path, "rb") as f:
                return tomllib.load(f)
        except ImportError:
            return create_default_config()
    except Exception:
        return create_default_config()


def create_default_config() -> Dict:
    """Create default pronunciation configuration and save to file."""
    default_config = {
        "word_replacements": {
            # Common programming terms
            "API": "A P I",
            "URL": "U R L",
            "HTTP": "H T T P",
            "HTTPS": "H T T P S",
            "JSON": "Jason",
            "XML": "X M L",
            "CSS": "C S S",
            "HTML": "H T M L",
            "SQL": "S Q L",
            "regex": "regular expression",
            "CLI": "C L I",
            "GUI": "G U I",
            "AI": "A I",
            "ML": "M L",
            "CPU": "C P U",
            "GPU": "G P U",
            "RAM": "R A M",
            "SSD": "S S D",
            "HDD": "H D D",
            "USB": "U S B",
            # Common symbols and abbreviations
            "vs": "versus",
            "etc": "et cetera",
            "e.g.": "for example",
            "i.e.": "that is",
            "aka": "also known as",
            "FAQ": "F A Q",
            "PDF": "P D F",
            "PNG": "P N G",
            "JPG": "J P G",
            "JPEG": "J P E G",
            "GIF": "G I F",
            "SVG": "S V G",
            "MP3": "M P 3",
            "MP4": "M P 4",
            "WAV": "wave",
            "FLAC": "F L A C",
        },
        "symbol_replacements": {
            # Mathematical and technical symbols
            "+": "plus",
            "-": "minus",
            "×": "times",
            "÷": "divided by",
            "=": "equals",
            "≠": "not equal to",
            "≤": "less than or equal to",
            "≥": "greater than or equal to",
            "<": "less than",
            ">": "greater than",
            "±": "plus or minus",
            "∞": "infinity",
            "π": "pi",
            "°": "degrees",
            "%": "percent",
            "&": "and",
            "@": "at",
            "#": "hash",
            "$": "dollar",
            "€": "euro",
            "£": "pound",
            "¥": "yen",
            "™": "trademark",
            "®": "registered trademark",
            "©": "copyright",
            # Programming symbols
            "::": "double colon",
            "->": "arrow",
            "=>": "arrow",
            "==": "double equals",
            "!=": "not equals",
            "<=": "less than or equals",
            ">=": "greater than or equals",
            "&&": "and",
            "||": "or",
            "++": "increment",
            "--": "decrement",
            "+=": "plus equals",
            "-=": "minus equals",
            "*=": "times equals",
            "/=": "divided by equals",
        },
        "pronunciation_overrides": {
            # Words that TTS often mispronounces
            "cache": "cash",
            "OAuth": "O auth",
            "nginx": "engine x",
            "PostgreSQL": "postgres Q L",
            "MySQL": "my S Q L",
            "SQLite": "S Q L ite",
            "GitHub": "git hub",
            "iOS": "i O S",
            "macOS": "mac O S",
            "Linux": "lin ux",
            "Ubuntu": "oo bun too",
            "Debian": "deb ee an",
            "CentOS": "cent O S",
            "WiFi": "wi fi",
            "Bluetooth": "blue tooth",
            "EPUB": "E pub",
            "MOBI": "mo bi",
            "PDF": "P D F",
            "DOCX": "doc x",
            "XLSX": "excel x",
            "PPTX": "power point x",
        },
        "regex_replacements": [
            # Email addresses
            {
                "pattern": r"\b[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}\b",
                "replacement": "email address",
                "description": "Replace email addresses with generic text",
            },
            # URLs
            {
                "pattern": r"https?://[^\s]+",
                "replacement": "web link",
                "description": "Replace URLs with generic text",
            },
            # Version numbers
            {
                "pattern": r"v?(\d+)\.(\d+)\.(\d+)",
                "replacement": r"version \1 dot \2 dot \3",
                "description": "Replace version numbers with spoken format",
            },
            # File paths (Unix/Linux)
            {
                "pattern": r"/[a-zA-Z0-9._/-]+",
                "replacement": "file path",
                "description": "Replace Unix file paths with generic text",
            },
            # File paths (Windows)
            {
                "pattern": r"[A-Z]:\\[a-zA-Z0-9._\\-]+",
                "replacement": "file path",
                "description": "Replace Windows file paths with generic text",
            },
        ],
    }

    save_pronunciation_config(default_config)
    return default_config


def save_pronunciation_config(config: Dict) -> None:
    """Save pronunciation configuration to TOML file."""
    config_path = get_pronunciation_config_path()
    config_path.parent.mkdir(parents=True, exist_ok=True)

    try:
        import tomli_w

        with open(config_path, "wb") as f:
            tomli_w.dump(config, f)
    except ImportError:
        # Fallback: create the file manually
        config_content = _dict_to_toml(config)
        with open(config_path, "w", encoding="utf-8") as f:
            f.write(config_content)


def _dict_to_toml(data: Dict, indent: int = 0) -> str:
    """Simple TOML serialization for fallback when tomli-w is not available."""
    lines = []
    indent_str = "  " * indent

    for key, value in data.items():
        if isinstance(value, dict):
            if lines:  # Add blank line before sections (except first)
                lines.append("")
            lines.append(f"{indent_str}[{key}]")
            for subkey, subvalue in value.items():
                if isinstance(subvalue, str):
                    lines.append(f'{indent_str}{subkey} = "{subvalue}"')
                else:
                    lines.append(f"{indent_str}{subkey} = {subvalue}")
        elif isinstance(value, list):
            if lines:
                lines.append("")
            lines.append(f"{indent_str}[[{key}]]")
            for item in value:
                if isinstance(item, dict):
                    for subkey, subvalue in item.items():
                        if isinstance(subvalue, str):
                            lines.append(f'{indent_str}{subkey} = "{subvalue}"')
                        else:
                            lines.append(f"{indent_str}{subkey} = {subvalue}")
                    if item != value[-1]:  # Add blank line between array items
                        lines.append("")
        elif isinstance(value, str):
            lines.append(f'{indent_str}{key} = "{value}"')
        else:
            lines.append(f"{indent_str}{key} = {value}")

    return "\n".join(lines) + "\n"


def apply_pronunciation_overrides(text: str) -> str:
    """Apply pronunciation overrides to text."""
    if not text or not text.strip():
        return text

    config = load_pronunciation_config()
    processed_text = text

    # Apply regex replacements first (they can be more specific)
    regex_replacements = config.get("regex_replacements", [])
    for replacement in regex_replacements:
        pattern = replacement.get("pattern", "")
        replacement_text = replacement.get("replacement", "")
        if pattern and replacement_text:
            try:
                processed_text = re.sub(pattern, replacement_text, processed_text)
            except re.error:
                continue

    # Apply symbol replacements (exact matches)
    symbol_replacements = config.get("symbol_replacements", {})
    for symbol, replacement in symbol_replacements.items():
        if symbol in processed_text:
            processed_text = processed_text.replace(symbol, f" {replacement} ")

    # Apply word replacements (case-insensitive, word boundaries)
    word_replacements = config.get("word_replacements", {})
    pronunciation_overrides = config.get("pronunciation_overrides", {})

    # Combine word replacements and pronunciation overrides
    all_word_replacements = {**word_replacements, **pronunciation_overrides}

    for word, replacement in all_word_replacements.items():
        # Use word boundaries to avoid partial matches
        pattern = r"\b" + re.escape(word) + r"\b"
        processed_text = re.sub(
            pattern, replacement, processed_text, flags=re.IGNORECASE
        )

    # Clean up extra whitespace
    processed_text = re.sub(r"\s+", " ", processed_text.strip())

    return processed_text


def get_pronunciation_config_info() -> Dict[str, str]:
    """Get information about the pronunciation configuration."""
    config_path = get_pronunciation_config_path()
    return {
        "config_path": str(config_path),
        "exists": config_path.exists(),
        "config_dir": str(config_path.parent),
    }
