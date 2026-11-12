#!/usr/bin/env python3
"""Rebuild the GY1983 text package from the preserved source bundle.

This recovery assembler was authored during the outage. It is not the supplied
kit/build_chapter.py and was not executed in the original environment.
Usage: python3 recover_GY1983.py GY1983_source_bundle.json [--compile]
The optional compilation requires XeLaTeX and BibTeX. It never creates a
placeholder PDF, and it records subprocess failures in GY1983_build_status.json.
"""
import argparse, csv, io, json, pathlib, shutil, subprocess, zipfile

def main():
    p = argparse.ArgumentParser()
    p.add_argument("bundle", type=pathlib.Path)
    p.add_argument("--out", type=pathlib.Path, default=pathlib.Path("GY1983_recovery"))
    p.add_argument("--compile", action="store_true")
    a = p.parse_args()
    b = json.loads(a.bundle.read_text(encoding="utf-8"))
    if a.out.exists():
        raise FileExistsError("Choose a fresh output directory: " + str(a.out))
    a.out.mkdir(parents=True, exist_ok=False)
    files = b["files"]
    owned = []
    for name, text in files.items():
        relative = pathlib.PurePosixPath(name)
        if relative.is_absolute() or ".." in relative.parts or "\\" in name or pathlib.PureWindowsPath(name).drive:
            raise ValueError("Unsafe package filename: " + name)
        target = a.out / name
        if a.out.resolve() not in target.resolve().parents:
            raise ValueError("Target escapes output directory: " + name)
        owned.append(target)
        target.parent.mkdir(parents=True, exist_ok=True)
        target.write_text(text, encoding="utf-8")
    status = {"text_files_written": sorted(files), "provided_builder_run": False,
              "recovery_assembler": True, "pdf_compiled": False,
              "pdf_visually_inspected": False, "commands": []}
    if a.compile:
        commands = [["xelatex", "-interaction=nonstopmode", "-halt-on-error", "GY1983_test.tex"],
                    ["bibtex", "GY1983_test"],
                    ["xelatex", "-interaction=nonstopmode", "-halt-on-error", "GY1983_test.tex"],
                    ["xelatex", "-interaction=nonstopmode", "-halt-on-error", "GY1983_test.tex"]]
        for n, command in enumerate(commands, 1):
            if not shutil.which(command[0]):
                status["error"] = "Missing executable: " + command[0]
                break
            r = subprocess.run(command, cwd=a.out, text=True, stdout=subprocess.PIPE,
                               stderr=subprocess.STDOUT, check=False)
            log = a.out / ("GY1983_build_%d.log" % n)
            log.write_text(r.stdout, encoding="utf-8")
            owned.append(log)
            status["commands"].append({"argv": command, "returncode": r.returncode})
            if r.returncode:
                status["error"] = "Build command failed; see its log."
                break
        else:
            status["pdf_compiled"] = (a.out / "GY1983_test.pdf").is_file()
    status_file = a.out / "GY1983_build_status.json"
    owned.append(status_file)
    status_file.write_text(
        json.dumps(status, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    archive = a.out.parent / "GY1983.zip"
    with zipfile.ZipFile(archive, "w", compression=zipfile.ZIP_DEFLATED) as z:
        if status["pdf_compiled"]:
            owned.append(a.out / "GY1983_test.pdf")
        for f in sorted(set(owned)):
            if f.is_file() and f.resolve() != archive.resolve():
                z.write(f, f.relative_to(a.out).as_posix())
    print(json.dumps({"archive": str(archive.resolve()), **status}, indent=2))
    return 0 if not a.compile or status["pdf_compiled"] else 1

if __name__ == "__main__":
    raise SystemExit(main())
