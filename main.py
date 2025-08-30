# main.py
import argparse, os, shutil
from pathlib import Path
from dotenv import load_dotenv

from generators import deliverability_kit
from packager.package import package_dir
from ops.qa import run_simple_checks
from publishers.gumroad_web import publish

def ensure_dirs():
    Path("build").mkdir(exist_ok=True)
    Path("dist").mkdir(exist_ok=True)

def generate(product: str) -> str:
    if product == "deliverability_kit":
        slug = "sendflo-deliverability-starter"
        out = Path("build") / slug
        if out.exists():
            shutil.rmtree(out)
        deliverability_kit.generate(str(out))
        return str(out)
    else:
        raise SystemExit(f"Unknown product: {product}")

def main():
    load_dotenv()
    ap = argparse.ArgumentParser()
    ap.add_argument("product", help="e.g. deliverability_kit")
    ap.add_argument("--publish", default="false", help="true/false")
    args = ap.parse_args()

    ensure_dirs()
    build_dir = generate(args.product)

    issues = run_simple_checks(build_dir)
    if issues:
        print("QA issues:")
        for i in issues:
            print(" -", i)

    dist_zip = package_dir(build_dir, "dist")
    print("Built:", dist_zip)

    if args.publish.lower() == "true":
        url = publish(build_dir, dist_zip)
        print("Published. Page:", url)

if __name__ == "__main__":
    main()
