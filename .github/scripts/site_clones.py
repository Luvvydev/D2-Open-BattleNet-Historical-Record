from pathlib import Path

page = Path("_site/index.html")
html = page.read_text(encoding="utf-8")
anchor = '<section class="section d2kicker-story" id="d2kicker">'
marker = 'id="people"'
note = """<div class="kicker-followup"><h3>Clones were part of the research.</h3><p>That same forum post brought back another detail. People shared clones of established builds so others could study them, figure out how they worked, and develop counters. Jay listed WARgod_Clone as something to learn from, Carpathian Clone as a demonstration of Thorns, Funki Crusher as a character built to defeat Funki PI, and xXkillerXxNew as an example of the one-hit stun glitch. The downloads even included a tool for running two Diablo II clients on one computer to test builds.</p><p>When someone asked where to find the downloads, Jay answered that the files were free, but knowledge was something you had to earn. That was exactly the distinction Adeem taught me with Snowman. Having the character wasn't the same thing as knowing how it worked.</p></div>"""
if 'kicker-followup' not in html:
    start = html.index(anchor)
    next_section = html.rfind("<section", start, html.index(marker))
    if next_section < 0:
        raise SystemExit("Could not locate insertion point")
    html = html[:next_section] + note + html[next_section:]
    page.write_text(html, encoding="utf-8")

jsfile = Path("_site/script.js")
js = jsfile.read_text(encoding="utf-8")
original = "An NV stun-on-hit property reportedly produced a glitch-like sequence of extremely rapid attacks."
replacement = "I had forgotten the exact setup until I found an old forum reply describing it: 90% chance to cast level 10 Stun on attack and on hit. That was how we triggered the rapid attacks."
if original in js:
    js = js.replace(original, replacement)
    jsfile.write_text(js, encoding="utf-8")
elif replacement not in js:
    raise SystemExit("Could not find the stun discovery description")

cssfile = Path("_site/overhaul.css")
css = cssfile.read_text(encoding="utf-8")
addition = """
.kicker-followup{max-width:790px;margin:34px auto 0;padding:26px 30px;border-left:2px solid #a98954;background:#171614;color:#e6dac3}
.kicker-followup h3{font-size:22px;margin:0 0 13px;font-family:Georgia,serif;color:#e6d2a9}
.kicker-followup p{font-size:15px;line-height:1.8;margin:0 0 14px}
.kicker-followup p:last-child{margin-bottom:0}
"""
if ".kicker-followup{" not in css:
    cssfile.write_text(css + "\n" + addition, encoding="utf-8")
