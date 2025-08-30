# publishers/gumroad_web.py

def publish(build_dir: str, dist_zip: str) -> str:
    """
    Stub publisher for Gumroad.
    Right now it just pretends to publish and returns a fake URL.
    Replace later with Playwright automation once ready.
    """
    print(f"[PUBLISH] Would publish {dist_zip} from {build_dir} to Gumroad")
    return "https://gumroad.com/draft/sendflo-deliverability-starter"
