# packager/package.py
from pathlib import Path
import zipfile

def package_dir(build_dir: str, dist_dir: str) -> str:
    """
    Zip the contents of build_dir into dist/<name>.zip and return the path.
    """
    b = Path(build_dir)
    dist = Path(dist_dir); dist.mkdir(parents=True, exist_ok=True)
    zip_path = dist / (b.name + ".zip")
    with zipfile.ZipFile(zip_path, "w", zipfile.ZIP_DEFLATED) as z:
        for p in b.iterdir():
            z.write(p, arcname=p.name)
    return str(zip_path)
