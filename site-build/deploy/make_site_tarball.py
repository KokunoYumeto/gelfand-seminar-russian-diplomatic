"""Pack the built site into WORK/dist/site-YYYY-MM-DD[-n].tar.gz for .github/workflows/pages.yml.

Refuses when the checks (build/g10_check.py) have not passed on this build: WORK/reports/g10_summary.tsv must exist,
be newer than every file of the site and show no FAIL.  Prints the publishing commands; it runs none of them:
    gh release create site-YYYY-MM-DD -R KokunoYumeto/gelfand-seminar-russian-diplomatic --prerelease \\
        --title "Site build YYYY-MM-DD" --notes "..." WORK/dist/site-YYYY-MM-DD.tar.gz
    gh workflow run pages.yml -R KokunoYumeto/gelfand-seminar-russian-diplomatic --ref main -f tag=site-YYYY-MM-DD
"""
import datetime
import sys
import tarfile
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent / "build"))
from common import DIST, REPO_SLUG, REPORTS, site_dir  # noqa: E402


def main():
    site = site_dir()
    summ = REPORTS / "g10_summary.tsv"
    newest = max(p.stat().st_mtime for p in site.rglob("*") if p.is_file())
    if not summ.exists() or summ.stat().st_mtime < newest:
        sys.exit("run build/g10_check.py on this build first")
    if "\tFAIL\t" in summ.read_text(encoding="utf-8"):
        sys.exit("the checks failed on this build (reports/g10_summary.tsv)")
    DIST.mkdir(parents=True, exist_ok=True)
    day = datetime.datetime.now(datetime.timezone.utc).date().isoformat()
    name = f"site-{day}"
    n = 1
    while (DIST / f"{name}.tar.gz").exists():
        n += 1
        name = f"site-{day}-{n}"
    out = DIST / f"{name}.tar.gz"
    with tarfile.open(out, "w:gz") as tf:
        for p in sorted(site.rglob("*")):
            if p.is_file():
                tf.add(p, arcname=p.relative_to(site).as_posix())
    print(f"{out} ({out.stat().st_size / 1e6:.1f} MB)")
    print(f'gh release create {name} -R {REPO_SLUG} --prerelease --title "Site build {day}" '
          f'--notes "Built website; the Pages workflow deploys it and deletes this release." "{out}"')
    print(f"gh workflow run pages.yml -R {REPO_SLUG} --ref main -f tag={name}")


if __name__ == "__main__":
    main()
