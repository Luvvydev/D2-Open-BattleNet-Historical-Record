from pathlib import Path
page=Path("_site/index.html")
html=page.read_text(encoding="utf-8")
if 'id="game-beneath-game"' not in html:
    marker='id="rules-2007"'
    at=html.find(marker)
    if at<0: raise SystemExit("Rules section not found")
    pos=html.rfind("<section",0,at)
    if pos<0: raise SystemExit("Section start not found")
    section='''<section class="section reflection-chapter" id="game-beneath-game"><div class="wrap narrow"><div class="chapter-marker"><span class="chapter-index">THE OTHER GAME</span><span class="chapter-line"></span><span>WHAT MADE IT DIFFERENT</span></div><h2>The game beneath the game.</h2><p>Imagine opening Hero Editor for the first time, creating a character with impossible numbers, and thinking you'd become unbeatable. Then you challenge somebody who appears weaker than you, and die almost instantly.</p><p>That was where the real game began. You went back, changed a value, ran another test, read an argument on a forum, and slowly worked out why you lost. You built a counter and returned. Maybe you won. Then somebody else found an answer to your character. That could go on for years.</p><p>Sometimes more damage healed the other player. Sometimes changing one mana point mattered more than adding millions. Sometimes a nearly harmless summoned monster could break a character everyone thought was invincible. The answers were hiding in the game's own calculations.</p><p class="reflection-pull">The visible game was Diablo II.<span>The hidden game was understanding Diablo II better than everybody else.</span></p><p>Discoveries changed reputations, friendships, rivalries, and even the rules of the ladders. A clan might keep a breakthrough secret for months. A forum post might set off a dozen new experiments overnight. The same people who fought bitterly could also teach one another how to see something nobody else had noticed.</p><p>That's the experience I miss. We weren't just trying to master a finished game. We were competing to find out what else was possible.</p></div></section>'''
    html=html[:pos]+section+html[pos:]
    page.write_text(html,encoding="utf-8")
css=Path("_site/overhaul.css")
s=css.read_text(encoding="utf-8")
add="""
.reflection-chapter{border-top:1px solid rgba(210,179,120,.25);border-bottom:1px solid rgba(210,179,120,.25)}
.reflection-chapter p{max-width:70ch;line-height:1.85}
.reflection-chapter .reflection-pull{font-family:Georgia,serif;font-size:clamp(25px,3.1vw,40px);line-height:1.3;color:#e8dcc8;max-width:780px;border-left:3px solid #b69a70;padding:16px 0 16px 24px;margin:36px 0}
.reflection-chapter .reflection-pull span{display:block;color:#d4ae73;margin-top:8px}
"""
if ".reflection-chapter{" not in s:css.write_text(s+"\n"+add,encoding="utf-8")
