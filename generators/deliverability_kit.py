
from pathlib import Path
import csv, json
from datetime import date
from PIL import Image, ImageDraw, ImageFont

def _write(path: Path, text: str):
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(text, encoding="utf-8")

def _cover_png(out: Path, title: str, subtitle: str):
    w, h = 1600, 900
    img = Image.new("RGB", (w,h), (15,23,42))
    d = ImageDraw.Draw(img)
    f1 = ImageFont.load_default()
    d.text((80,220), "SendFlo", font=f1, fill=(226,232,240))
    d.text((80,320), title, font=f1, fill=(241,245,249))
    d.text((80,400), subtitle, font=f1, fill=(203,213,225))
    img.save(out)

def generate(output_dir: str) -> dict:
    out = Path(output_dir); out.mkdir(parents=True, exist_ok=True)
    _write(out / "README.md", "(c) {} SendFlo deliverability kit".format(date.today().year))
    with (out / "warmup_calendar.csv").open("w", newline="", encoding="utf-8") as f:
        w = csv.writer(f); w.writerow(["day","daily_sends","unique_froms","engaged_list_%","goal","notes"])
        for d in range(1, 31):
            w.writerow([d, 100*d, 1, 80, "Complaints <0.1%, bounces <2%", ""])
    with (out / "seed_testing_checklist.csv").open("w", newline="", encoding="utf-8") as f:
        w = csv.writer(f); w.writerow(["check","status","notes"]); w.writerow(["SPF passes","",""])
    with (out / "dns_auth_planner.csv").open("w", newline="", encoding="utf-8") as f:
        w = csv.writer(f); w.writerow(["record_type","host","value_template","example","status"]); w.writerow(["TXT","@","v=spf1 include:{esp_domain} ~all","v=spf1 include:_spf.smtp2go.com ~all",""])
    _write(out / "bounce_complaint_playbook.md", "Bounce/Complaint Playbook")
    with (out / "subject_angles.csv").open("w", newline="", encoding="utf-8") as f:
        w = csv.writer(f); w.writerow(["subject","preheader","angle"]); w.writerow(["Quick win: fix DMARC","Clear preheader","deliverability"])
    svg = '<svg xmlns="http://www.w3.org/2000/svg" width="1600" height="900"><rect width="100%" height="100%" fill="#0f172a"/></svg>'
    (out / "cover.svg").write_text(svg, encoding="utf-8")
    _cover_png(out / "cover.png", "1M/Month Email Deliverability Kit", "Playbooks • Warm-up • DNS Planner • Checklists")
    meta = {"title":"SendFlo: 1M/Month Email Deliverability Kit (Starter)","subtitle":"Warm, authenticate, and scale.","price":29,"tags":["email","deliverability"],"files":["warmup_calendar.csv","seed_testing_checklist.csv","dns_auth_planner.csv","bounce_complaint_playbook.md","subject_angles.csv"],"images":["cover.png"],"description_md":"# Deliver","license":"Personal use only"}
    (out / "product.json").write_text(json.dumps(meta, indent=2), encoding="utf-8")
    return {"title": meta["title"], "subtitle": meta["subtitle"], "files": meta["files"], "images": meta["images"]}
