import re, yaml, random, hashlib
from pathlib import Path

def slugify(s): 
    s = re.sub(r"[^a-z0-9]+", "-", s.lower()).strip("-")
    return s[:60]

def pick_topic(niche, product):
    # In production: score keywords via search volumes & competition.
    # Here: simple seed + angle.
    angles = [
        "High-deliverability cold outreach",
        "Agency onboarding sequences",
        "Re-engagement after bounces",
        "Zero-spam warm-up plan",
    ]
    title = f"{niche}: {random.choice(angles)}"
    subtitle = f"{product} that converts without spam triggers."
    keywords = [niche, product, "email", "deliverability", "subject lines"]
    slug = slugify(title + "-" + product)
    return {"title": title, "subtitle": subtitle, "keywords": keywords, "slug": slug}
