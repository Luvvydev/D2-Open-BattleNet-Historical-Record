from pathlib import Path

page = Path("_site/index.html")
html = page.read_text(encoding="utf-8")
marker = '<section class="section" id="people">'
section = '''<section class="section d2kicker-story" id="d2kicker"><div class="wrap narrow"><div class="chapter-marker"><span class="chapter-index">2007</span><span class="chapter-line"></span><span>AN OLD FORUM POST</span></div><h2>D2Kicker, another piece of the story.</h2><p>It wasn't all duels and character builds. I also made a small program called <strong>D2Kicker</strong> to help hosts identify the name and IP address of a player in their game and kick them if needed.</p><p>Years later, I found it listed in JayOfTerror's Diablo II downloads thread, dated July 26, 2007. Jay described it as a utility made by “Azreal]AMF[ also known as Thor.” Seeing both names there on an old forum brought back a part of those years I hadn't included in this story.</p><figure class="kicker-figure"><a href="https://web.archive.org/web/20071011195114/http://www.jayofteror.com/index.php?showtopic=9929" target="_blank" rel="noopener"><img src="assets/screenshots/JayOfTerror_D2Kicker_2007.webp" loading="lazy" alt="Screenshot of JayOfTerror's 2007 Diablo II downloads thread mentioning D2Kicker"/></a><figcaption>From JayOfTerror's downloads thread, saved by the Wayback Machine in October 2007. <a href="https://web.archive.org/web/20071011195114/http://www.jayofteror.com/index.php?showtopic=9929" target="_blank" rel="noopener">Read the archived page ↗</a></figcaption></figure></div></section>
'''
if 'id="d2kicker"' not in html:
    if marker not in html:
        raise SystemExit("Unable to locate website insertion point")
    html = html.replace(marker, section + marker, 1)
    page.write_text(html, encoding="utf-8")

css = Path("_site/overhaul.css")
addition = """
.d2kicker-story{border-top:1px solid #5b5247;border-bottom:1px solid #5b5247}
.d2kicker-story p{max-width:69ch}
.kicker-figure{margin:30px 0 0;padding:14px;background:#181818;border:1px solid #6a5840}
.kicker-figure img{width:100%;height:auto;display:block;object-fit:contain}
.kicker-figure figcaption{font-size:13px;line-height:1.65;margin-top:12px;color:#c7b89d}
.kicker-figure a{color:#d7b176}
"""
styles = css.read_text(encoding="utf-8")
if ".d2kicker-story{" not in styles:
    css.write_text(styles + addition, encoding="utf-8")
