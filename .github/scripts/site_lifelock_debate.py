from pathlib import Path
p=Path("_site/index.html")
s=p.read_text(encoding="utf-8")
if 'id="lifelock-debate"' not in s:
    marker='id="old-calculators"'
    pos=s.find(marker)
    if pos<0: raise SystemExit("research section missing")
    start=s.rfind("<section",0,pos)
    addition='''<section class="section recovered-story" id="lifelock-debate"><div class="wrap narrow"><div class="chapter-marker"><span class="chapter-index">2007</span><span class="chapter-line"></span><span>KNOWLEDGE AND SECRECY</span></div><h2>Should we tell everyone?</h2><p>One archived forum listing had a poll titled <strong>Life Lock! Should we release it to public?</strong> By September 30, 2007, it showed 143 replies and 2,799 views. I haven't found the full conversation yet, but the fact that it happened says plenty about our scene.</p><p>When somebody found a new way to survive or kill an apparently unstoppable character, the next question wasn't always just how to use it. It was whether to tell other people. Publishing a discovery meant giving rivals the chance to copy it, understand it, and eventually counter it. Keeping it private protected the work and kept the ladder guessing. That tension was part of the game we made around Diablo II.</p><p>There were arguments over knowledge because knowledge was what everyone wanted.</p></div></section>'''
    s=s[:start]+addition+s[start:]
    p.write_text(s,encoding="utf-8")
