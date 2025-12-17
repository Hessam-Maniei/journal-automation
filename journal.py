from datetime import datetime
import os

def create_journal():
    today = datetime.now().strftime("%Y-%m-%d")

    folder = "journal"
    os.makedirs(folder, exist_ok=True)

    path = os.path.join(folder, f"{today}.md")

    if not os.path.exists(path):
        with open(path, "w", encoding="utf-8") as f:
            f.write(f"# Journal Entry – {today}\n\n")
            f.write("## What I learned today\n\n- \n")
        print(f"Created: {path}")
    else:
        print(f"Already exists: {path}")

if __name__ == "__main__":
    create_journal()

