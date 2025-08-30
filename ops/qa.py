from pathlib import Path

# Simple content guardrail; add more phrases as needed
BAD_WORDS = {"free $$$", "guaranteed inbox"}

def run_simple_checks(build_dir: str):
    """Return a list of issue strings if any banned phrases are found."""
    issues = []
    for p in Path(build_dir).glob("**/*"):
        if p.is_file() and p.suffix.lower() in {".md", ".csv", ".txt", ".json"}:
            try:
                text = p.read_text(encoding="utf-8", errors="ignore").lower()
            except Exception:
                continue
            for phrase in BAD_WORDS:
                if phrase in text:
                    issues.append(f"{p.name}: contains banned phrase '{phrase}'")
    return issues
