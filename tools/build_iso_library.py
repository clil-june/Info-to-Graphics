"""Build the Flat Isometric asset library into index.html.

Reads assets/flat-isometric/manifest.json and its SVG files, compacts each drawing
(rounds coordinates, drops ids and titles), measures where its accent part sits,
and writes the result as `const ISO_LIBRARY = {...};` between the markers
/*ISO_LIBRARY:START*/ and /*ISO_LIBRARY:END*/ in index.html.

Run from the repository root (standard library only):
    python tools/build_iso_library.py
"""
import json
import re
import sys
import xml.etree.ElementTree as ET
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
LIB = ROOT / "assets" / "flat-isometric"
INDEX = ROOT / "index.html"
SVG = "{http://www.w3.org/2000/svg}"
START, END = "/*ISO_LIBRARY:START*/", "/*ISO_LIBRARY:END*/"
KEEP = {"d", "fill", "fill-rule", "cx", "cy", "rx", "ry", "data-accent", "data-recolor-fill", "data-tone"}
NUM = re.compile(r"-?\d+(?:\.\d+)?")


def r1(m):
    v = round(float(m.group(0)), 1)
    return str(int(v)) if v == int(v) else str(v)


def points(el):
    """Rough extent of a shape: every coordinate pair in an absolute path, or an ellipse's box."""
    tag = el.tag.replace(SVG, "")
    if tag == "ellipse":
        cx, cy, rx, ry = (float(el.get(a, 0)) for a in ("cx", "cy", "rx", "ry"))
        return [(cx - rx, cy - ry), (cx + rx, cy + ry)]
    d = el.get("d", "")
    out = []
    for cmd, args in re.findall(r"([MLCZA])([^MLCZA]*)", d):
        nums = [float(x) for x in NUM.findall(args)]
        if cmd == "A":  # rx ry rot large sweep x y: keep the end points only
            out += [(nums[i + 5], nums[i + 6]) for i in range(0, len(nums) - 6, 7)]
        else:
            out += list(zip(nums[0::2], nums[1::2]))
    return out


def compact(el):
    tag = el.tag.replace(SVG, "")
    attrs = "".join(f' {k}="{NUM.sub(r1, v) if k in ("d", "cx", "cy", "rx", "ry") else v}"'
                    for k, v in el.attrib.items() if k in KEEP)
    kids = "".join(compact(c) for c in el if c.tag.replace(SVG, "") in ("g", "path", "ellipse"))
    return f"<{tag}{attrs}>{kids}</{tag}>" if kids or tag == "g" else f"<{tag}{attrs}/>"


def build():
    manifest = json.loads((LIB / "manifest.json").read_text(encoding="utf-8"))
    lib = {}
    for a in manifest["assets"]:
        tree = ET.parse(LIB / a["file"]).getroot()
        vx, vy, vw, vh = (float(n) for n in tree.get("viewBox").split())
        body = "".join(compact(c) for c in tree if c.tag.replace(SVG, "") in ("g", "path", "ellipse"))
        accent = [p for g in tree.iter(SVG + "g") if g.get("data-accent")
                  for el in g.iter() if el.tag in (SVG + "path", SVG + "ellipse") for p in points(el)]
        at = None
        if accent:
            xs, ys = [p[0] for p in accent], [p[1] for p in accent]
            at = [round(((min(xs) + max(xs)) / 2 - vx) / vw, 2), round(((min(ys) + max(ys)) / 2 - vy) / vh, 2)]
        lib[a["id"]] = {"label": a["label"], "cat": a["category"], "vb": [vx, vy, vw, vh],
                        "accent": a.get("accent_layers") or [], "at": at, "svg": body}
    return lib


def main():
    lib = build()
    blob = json.dumps(lib, ensure_ascii=False, separators=(",", ":")).replace("</", "<\\/")
    src = INDEX.read_bytes().decode("utf-8")
    i, j = src.index(START), src.index(END)
    src = src[:i + len(START)] + "const ISO_LIBRARY = " + blob + ";" + src[j:]
    INDEX.write_bytes(src.encode("utf-8"))
    print(f"{len(lib)} assets, {len(blob):,} characters inlined")
    for k, v in lib.items():
        print(f"  {k:16} {v['cat']:9} {v['vb'][2]:.0f}x{v['vb'][3]:.0f} at={v['at']}")


if __name__ == "__main__":
    sys.exit(main())
