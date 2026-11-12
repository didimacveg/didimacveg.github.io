#!/usr/bin/env python3
"""Build the one-page CV PDFs from cv.en.json and cv.es.json.

Usage (from the repository root):  make cv
Edit the JSON files, run the command again. The build fails if a CV no longer fits on one page.
"""
import json
import sys
from pathlib import Path

from reportlab.lib import colors
from reportlab.lib.enums import TA_RIGHT
from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import ParagraphStyle
from reportlab.lib.units import mm
from reportlab.platypus import HRFlowable, Paragraph, SimpleDocTemplate, Spacer, Table, TableStyle

HERE = Path(__file__).parent
INK = colors.HexColor("#15171a")
GREY = colors.HexColor("#555a61")
ACCENT = colors.HexColor("#1f5fbf")  # print-safe version of the site's Cherenkov blue
MARGIN = 15 * mm
WIDTH = A4[0] - 2 * MARGIN - 12  # the frame adds 6 pt of padding on each side


def style(name, **kw):
    base = dict(fontName="Helvetica", fontSize=9.4, leading=12.2, textColor=INK)
    base.update(kw)
    return ParagraphStyle(name, **base)


NAME = style("name", fontName="Helvetica-Bold", fontSize=21, leading=24)
TAG = style("tag", fontSize=10.2, leading=13.2, textColor=GREY)
CONTACT = style("contact", fontSize=9, leading=12, textColor=GREY)
SECTION = style("section", fontName="Helvetica-Bold", fontSize=8.6, leading=11, textColor=ACCENT)
HEAD = style("head", fontSize=10, leading=13)
RIGHT = style("right", fontSize=9, leading=13, textColor=GREY, alignment=TA_RIGHT)
BODY = style("body")
BULLET = style("bullet", leftIndent=9, bulletIndent=1)


def build(path):
    cv = json.loads(path.read_text(encoding="utf-8"))
    text = json.dumps(cv, ensure_ascii=False)
    if "—" in text:
        sys.exit(f"{path.name}: contains an em dash; rephrase it")
    out = HERE / cv["output"]
    story = [
        Paragraph(cv["name"], NAME),
        Spacer(1, 2),
        Paragraph(cv["tagline"], TAG),
        Spacer(1, 2),
        Paragraph("  |  ".join(cv["contact"]), CONTACT),
    ]
    for sec in cv["sections"]:
        story += [
            Spacer(1, 8),
            Paragraph(sec["title"].upper(), SECTION),
            HRFlowable(width="100%", thickness=0.6, color=ACCENT, spaceBefore=1.5, spaceAfter=3.5),
        ]
        for line in sec.get("lines", []):
            story += [Paragraph(line, BODY), Spacer(1, 1.5)]
        for e in sec.get("entries", []):
            head = f"<b>{e['head']}</b>" + (f"  <font color='#555a61'>{e['org']}</font>" if e.get("org") else "")
            row = Table([[Paragraph(head, HEAD), Paragraph(e.get("right", ""), RIGHT)]], colWidths=[WIDTH - 34 * mm, 34 * mm])
            row.setStyle(TableStyle([
                ("VALIGN", (0, 0), (-1, -1), "TOP"),
                ("LEFTPADDING", (0, 0), (-1, -1), 0), ("RIGHTPADDING", (0, 0), (-1, -1), 0),
                ("TOPPADDING", (0, 0), (-1, -1), 0), ("BOTTOMPADDING", (0, 0), (-1, -1), 0.5),
            ]))
            story.append(row)
            for b in e.get("bullets", []):
                story.append(Paragraph(b, BULLET, bulletText="•"))
            story.append(Spacer(1, 3))
    doc = SimpleDocTemplate(
        str(out), pagesize=A4, leftMargin=MARGIN, rightMargin=MARGIN, topMargin=13 * mm, bottomMargin=11 * mm,
        title=f"{cv['name']} · CV", author=cv["name"],
    )
    doc.build(story)
    if doc.page != 1:
        sys.exit(f"{out.name}: {doc.page} pages. Shorten {path.name} until it fits on one.")
    print(f"wrote cv/{out.name} (1 page)")


if __name__ == "__main__":
    for f in sorted(HERE.glob("cv.*.json")):
        build(f)
