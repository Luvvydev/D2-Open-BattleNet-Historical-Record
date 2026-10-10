from pathlib import Path

page = Path("_site/index.html")
text = page.read_text(encoding="utf-8")
old = """<div class="closing"><span>WHY IT MATTERED</span><p>It was never just about being the strongest. It was about finding something the world didn't know yet, and having a world of people who cared.</p></div>"""
new = """<div class="closing"><span>THE WORLD WE LOST</span><p>We weren't simply playing a game that would one day change. We were part of a community that could only have emerged at that particular moment in gaming and internet history.</p><p class="closing-reflection">When the people left, the forums disappeared, and the internet changed, that world went with them.</p><p class="closing-final">The game survived. The world we built around it largely didn't.</p></div>"""
if old in text:
    page.write_text(text.replace(old, new), encoding="utf-8")
elif new not in text:
    raise SystemExit("Could not find closing passage to update")

style = Path("_site/overhaul.css")
css = """.closing .closing-reflection{font-size:clamp(19px,2.3vw,28px);font-style:normal;line-height:1.65;margin:20px 0;max-width:790px}.closing .closing-final{font-size:clamp(26px,3.5vw,43px);font-weight:600;line-height:1.3;margin-top:28px;max-width:790px}"""
existing = style.read_text(encoding="utf-8")
if css not in existing:
    style.write_text(existing + "\n" + css + "\n", encoding="utf-8")
