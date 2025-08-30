from pathlib import Path
import csv

def make_subject_lines_csv(idea, outdir, n=500):
    out = Path(outdir); out.mkdir(parents=True, exist_ok=True)
    path = out / "subject_lines.csv"
    with path.open("w", newline="", encoding="utf-8") as f:
        w = csv.writer(f)
        w.writerow(["subject","preheader","angle","tone"])
        for i in range(n):
            w.writerow([
                f"{idea['title'].split(':')[0]}: idea #{i+1}",
                "Quick win inside—no fluff.",
                "deliverability",
                "friendly"
            ])
    return str(path)

def make_warmup_calendar_csv(idea, outdir, days=30):
    out = Path(outdir); out.mkdir(parents=True, exist_ok=True)
    path = out / "warmup_calendar.csv"
    with path.open("w", newline="", encoding="utf-8") as f:
        w = csv.writer(f)
        w.writerow(["day","daily_sends","goal","notes"])
        baseline = 50
        for d in range(1, days+1):
            w.writerow([d, min(2000, baseline + d*50), "Keep complaint rate <0.1%", ""])
    return str(path)
