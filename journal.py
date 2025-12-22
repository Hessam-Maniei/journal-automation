from pathlib import Path
from datetime import datetime
import requests

# ---------- Config ----------
CITY = "Dortmund"
LAT = 51.5136
LON = 7.4653

MARKER = "<!-- MANUAL NOTES BELOW THIS LINE -->"

journal_dir = Path("journal")
journal_dir.mkdir(exist_ok=True)

today = datetime.utcnow().strftime("%Y-%m-%d")
file_path = journal_dir / f"{today}.md"

# ---------- Weather ----------
weather_url = (
    "https://api.open-meteo.com/v1/forecast"
    f"?latitude={LAT}&longitude={LON}&current_weather=true"
)

weather_data = requests.get(weather_url, timeout=10).json()
weather = weather_data["current_weather"]

weather_block = f"""
## 🌤 Weather ({CITY})
- Temperature: {weather['temperature']} °C
- Wind speed: {weather['windspeed']} km/h
"""

# ---------- Header ----------
auto_block = f"""# {today}

{weather_block}

{MARKER}
"""

# ---------- File logic ----------
if file_path.exists():
    content = file_path.read_text(encoding="utf-8")
    if MARKER in content:
        manual_part = content.split(MARKER, 1)[1]
    else:
        manual_part = "\n\n## ✍️ Manual Notes\n\n"
else:
    manual_part = "\n\n## ✍️ Manual Notes\n\n"

file_path.write_text(
    auto_block + manual_part,
    encoding="utf-8"
)

print(f"Journal updated: {file_path}")
