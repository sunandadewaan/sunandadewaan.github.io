#!/usr/bin/env python3
"""Generates the static portfolio pages from one shared shell.
Run: python3 build.py   ->  writes *.html into this folder."""

import os

NAV = [
    ("index.html", "Home"),
    ("about.html", "About"),
    ("work.html", "Work"),
    ("research.html", "Research"),
    ("impact.html", "Impact"),
    ("article.html", "Articles"),
    ("contact.html", "Contact"),
]

SITE_NAME = "Sunanda Dewaan"
TAGLINE = "Climate Resilience &amp; Indigenous Food Systems"
EMAIL = "sunandadewan64@gmail.com"
LINKEDIN = "https://www.linkedin.com/in/sunanda-dewaan29"
JHUM = "https://sites.google.com/view/jhum-revolution/home"

SHELL = """<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{title}</title>
<meta name="description" content="{desc}">
<meta name="author" content="Sunanda Dewaan">
<meta property="og:title" content="{title}">
<meta property="og:description" content="{desc}">
<meta property="og:type" content="website">
<!-- Add a 1200x630 image named og-image.png to this folder, then uncomment:
<meta property="og:image" content="og-image.png"> -->
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Bricolage+Grotesque:opsz,wght@12..96,400;12..96,600;12..96,800&family=Newsreader:opsz,wght@6..72,300;6..72,400;6..72,500&display=swap" rel="stylesheet">
<link rel="stylesheet" href="style.css">
</head>
<body>
<a class="skip" href="#main">Skip to main content</a>

<header class="site-head">
  <div class="wrap head-inner">
    <a class="brand" href="index.html"><b>Sunanda Dewaan</b><span>Climate resilience &amp; indigenous food systems</span></a>
    <button class="nav-toggle" aria-expanded="false" aria-controls="nav">Menu</button>
    <nav class="site-nav" id="nav" aria-label="Main">
      <ul>{nav}</ul>
    </nav>
  </div>
</header>

<main id="main">
{body}
</main>

<footer class="site-foot">
  <div class="wrap">
    <div class="foot-grid">
      <div>
        <h3>Sunanda Dewaan</h3>
        <p style="margin:0;font-size:.9rem">Founder &amp; Executive Director, Jhum Revolution. Working on climate resilience and indigenous food systems in the Chittagong Hill Tracts.</p>
      </div>
      <div>
        <h3>Pages</h3>
        <ul>{footnav}</ul>
      </div>
      <div>
        <h3>Contact</h3>
        <ul>
          <li><a href="mailto:{email}">{email}</a></li>
          <li><a href="{linkedin}">LinkedIn</a></li>
          <li><a href="{jhum}">Jhum Revolution</a></li>
          <li>Chattogram, Bangladesh</li>
        </ul>
      </div>
    </div>
    <div class="copyright">&copy; 2026 Sunanda Dewaan</div>
  </div>
</footer>

<script src="script.js"></script>
</body>
</html>
"""


def nav_html(current):
    out = []
    for href, label in NAV:
        cur = ' aria-current="page"' if href == current else ""
        out.append(f'<li><a href="{href}"{cur}>{label}</a></li>')
    return "".join(out)


def foot_nav():
    return "".join(f'<li><a href="{h}">{l}</a></li>' for h, l in NAV)


def page(filename, title, desc, body):
    html = SHELL.format(
        title=title, desc=desc, nav=nav_html(filename), footnav=foot_nav(),
        body=body, email=EMAIL, linkedin=LINKEDIN, jhum=JHUM,
    )
    with open(os.path.join(os.path.dirname(__file__), filename), "w", encoding="utf-8") as f:
        f.write(html)
    print("wrote", filename)


CONTOURS = """<svg class="contours" viewBox="0 0 900 320" aria-hidden="true" preserveAspectRatio="none">
  <path d="M-20 300 C 120 250, 200 288, 300 236 S 520 200, 640 240 S 820 214, 930 176"/>
  <path d="M-20 264 C 140 214, 232 250, 330 196 S 540 158, 664 200 S 826 172, 930 132"/>
  <path d="M-20 228 C 156 176, 260 212, 356 156 S 556 118, 686 160 S 834 128, 930 88"/>
  <path d="M-20 192 C 172 138, 288 174, 382 116 S 572 78, 706 120 S 842 84, 930 44"/>
</svg>"""

PHOTO_SLOT = """<figure class="portrait">
  <div class="frame">
    <img src="portrait.jpg" alt="Sunanda Dewaan">
  </div>
  <figcaption>Chattogram, Bangladesh</figcaption>
</figure>"""

# ---------------------------------------------------------------- HOME
home = f"""
<section class="hero">
  <div class="wrap">
    {CONTOURS}
    <div class="hero-grid">
      <div class="hero-text">
        <p class="eyebrow">Researcher &amp; youth climate leader</p>
        <h1>Climate resilience begins with what people already know.</h1>
        <p class="lede">I work with jhum farming families in the Chittagong Hill Tracts on
        indigenous food systems, nutrition, and climate adaptation &mdash; building
        programmes from what communities have practised for generations rather than
        around them.</p>
        <p class="hero-meta">Founder &amp; Executive Director, Jhum Revolution &nbsp;·&nbsp; Chattogram, Bangladesh</p>
        <div class="actions">
          <a class="btn btn-primary" href="contact.html">Get in touch</a>
          <a class="btn" href="work.html">See the work</a>
        </div>
      </div>
      {PHOTO_SLOT}
    </div>
  </div>
</section>

<section>
  <div class="wrap">
    <div class="counters">
      <div><div class="num" data-count="300" data-suffix="+">300+</div><div class="cap">Families reached through Jhum Revolution</div></div>
      <div><div class="num" data-count="250" data-suffix="+">250+</div><div class="cap">Students engaged in the ICCCAD-funded campaign</div></div>
      <div><div class="num" data-count="3">3</div><div class="cap">Research projects supported as Research Assistant</div></div>
      <div><div class="num" data-count="2">2</div><div class="cap">UN-linked youth appointments</div></div>
    </div>
  </div>
</section>

<section>
  <div class="wrap">
    <p class="eyebrow">At a glance</p>
    <h2>Key facts for quick reference.</h2>
    <p>Short, verifiable statements for anyone reviewing an application, proposal, or invitation.</p>
    <div class="glance">
      <dl>
        <dt>Name</dt><dd>Sunanda Dewaan</dd>
        <dt>Current role</dt><dd>Founder &amp; Executive Director, Jhum Revolution</dd>
        <dt>Based in</dt><dd>Chattogram, Bangladesh</dd>
        <dt>Studying</dt><dd>MSc, Environmental Science and Disaster Management, Noakhali Science and Technology University</dd>
        <dt>Prior degree</dt><dd>BSc, Food Technology and Nutrition Science, NSTU (2020&ndash;2025)</dd>
        <dt>Appointments</dt><dd>Member, United Nations Youth Advisory Group Bangladesh &mdash; Climate Change &amp; Green Growth (July 2026&ndash;); World Food Forum Youth Representative for Bangladesh, FAO (2025&ndash;26)</dd>
        <dt>Fellowship</dt><dd>Fellow, Climate Policy Negotiation Fellowship 2026</dd>
        <dt>Award</dt><dd>Winner, ICCCAD Youth Innovation Fund, October 2024 &mdash; BDT 300,000, Promote Green Ideas / Campaign category</dd>
        <dt>Languages</dt><dd>Bangla (native), English (professional working proficiency)</dd>
        <dt>Core focus</dt><dd>Indigenous food systems, dietary diversity, post-flood food security, digital well-being, youth-led climate action</dd>
        <dt>Contact</dt><dd><a href="mailto:{EMAIL}">{EMAIL}</a></dd>
      </dl>
    </div>
  </div>
</section>

<section>
  <div class="wrap">
    <p class="eyebrow">Focus</p>
    <h2>Where I work.</h2>
    <div class="grid-2">
      <div class="entry"><h3>Indigenous food systems</h3><p>Jhum cultivation cycles, seed-saving, and traditional food knowledge in the Chittagong Hill Tracts, documented with the communities that hold them.</p></div>
      <div class="entry"><h3>Nutrition &amp; dietary diversity</h3><p>How food access and dietary quality shift for marginalised hill and coastal households under climate pressure.</p></div>
      <div class="entry"><h3>Post-flood recovery</h3><p>Food security, livelihoods, and the poverty&ndash;gender nexus after flooding &mdash; grounded in fieldwork in Noakhali, Feni, and Cumilla.</p></div>
      <div class="entry"><h3>Digital well-being</h3><p>The effect of digital life on maternal and child health and dietary diversity in the CHT.</p></div>
      <div class="entry"><h3>Youth-led climate action</h3><p>Designing programmes that put young people in charge of research, delivery, and advocacy rather than in the audience.</p></div>
      <div class="entry"><h3>Policy &amp; advocacy</h3><p>Translating community evidence into policy language through UN and FAO youth platforms.</p></div>
    </div>
    <div class="actions"><a class="btn" href="work.html">Full experience</a></div>
  </div>
</section>

<section>
  <div class="wrap">
    <p class="eyebrow">Get in touch</p>
    <h2>Open to collaboration.</h2>
    <p>Research partnerships, programme design, fellowships, and speaking on
    indigenous food systems and youth-led climate work.</p>
    <div class="actions">
      <a class="btn btn-primary" href="contact.html">Contact</a>
      <a class="btn" href="{LINKEDIN}">LinkedIn</a>
    </div>
  </div>
</section>
"""

# ---------------------------------------------------------------- ABOUT
about = f"""
<section class="hero">
  <div class="wrap">
    {CONTOURS}
    <div class="hero-text">
      <p class="eyebrow">About</p>
      <h1>A practice built in the field.</h1>
    </div>
  </div>
</section>

<section>
  <div class="wrap">
    <figure style="margin:0 0 2.5rem">
      <img src="community-discussion.jpg" alt="Group discussion with jhum farming households in the Chittagong Hill Tracts" style="width:100%;border:1px solid var(--stone)" loading="lazy">
      <figcaption style="font-family:var(--sans);font-size:.85rem;color:var(--moss);margin-top:.6rem">Community discussion with jhum farming households in the Chittagong Hill Tracts.</figcaption>
    </figure>

    <p class="lede">I am a researcher and youth climate leader from Chattogram, working at the
    intersection of nutrition, indigenous food systems, and climate resilience in the
    Chittagong Hill Tracts.</p>

    <p>I founded Jhum Revolution, a youth-led organisation supporting jhum farming families
    in the CHT. What began as a campaign funded by the ICCCAD Youth Innovative Fund has
    grown into ongoing work with more than 300 families &mdash; capacity building,
    indigenous knowledge documentation, and programmes designed alongside the communities
    they serve rather than for them.</p>

    <p>My academic background sits in food technology and nutrition science, and I am now
    completing a master's in Environmental Science and Disaster Management. That combination
    shapes how I read a problem: food is where climate stress becomes visible first, in what
    a household can grow, afford, and put on a plate.</p>

    <p>Most of what I know comes from fieldwork. I have sat with farming households through
    a season, walked flood-damaged land in Noakhali, Feni, and Cumilla, and listened to
    people name their own problem before a proposal was written about it. I try to keep that
    order intact in everything I design.</p>

    <p>Alongside the organisation I have worked as a research assistant on three studies
    spanning digital addiction and maternal health, youth-led water security monitoring, and
    the poverty&ndash;gender nexus in post-flood food insecurity. I served as President of the NSTU
    Science Club, and represented Bangladesh as a World Food Forum Youth Representative
    with the Food and Agriculture Organization.</p>

    <!-- TODO: add a personal paragraph here in your own words if you want one — what
         drew you to this work, or what you want the next five years to look like. -->

    <div class="gallery" style="margin-top:2.5rem">
      <figure>
        <img src="nstu-presentation.jpg" alt="Presenting the Jhum Revolution campaign at the NSTU seminar" loading="lazy">
        <figcaption>Presenting at the capacity building seminar, IQAC, NSTU.</figcaption>
      </figure>
      <figure>
        <img src="school-session.jpg" alt="Speaking to students in a classroom in the Chittagong Hill Tracts" loading="lazy">
        <figcaption>School session in the hills.</figcaption>
      </figure>
      <figure>
        <img src="filming.jpg" alt="Filming an interview with a community member" loading="lazy">
        <figcaption>Documenting indigenous knowledge on camera.</figcaption>
      </figure>
      <figure>
        <img src="summit-team.jpg" alt="The Jhum Revolution team at the Environment Innovation Summit" loading="lazy">
        <figcaption>With the team at the Environment Innovation Summit &amp; Awards, Dhaka.</figcaption>
      </figure>
      <figure>
        <img src="sapling.jpg" alt="Handing a sapling to a student" loading="lazy">
        <figcaption>Sapling distribution with school students.</figcaption>
      </figure>
      <figure>
        <img src="seminar-group.jpg" alt="Seminar participants at NSTU" loading="lazy">
        <figcaption>Seminar participants at NSTU.</figcaption>
      </figure>
    </div>
  </div>
</section>

<section>
  <div class="wrap">
    <p class="eyebrow">Education</p>
    <h2>Academic foundation.</h2>
    <ul class="ledger">
      <li>
        <div class="when">2025 &ndash; present</div>
        <div class="what"><strong>MSc, Environmental Science and Disaster Management</strong>
        <span>Noakhali Science and Technology University, Bangladesh</span></div>
      </li>
      <li>
        <div class="when">2020 &ndash; 2025</div>
        <div class="what"><strong>BSc, Food Technology and Nutrition Science</strong>
        <span>Noakhali Science and Technology University, Bangladesh</span></div>
      </li>
    </ul>

    <figure style="margin:2rem 0 0;max-width:26rem">
      <img src="thesis.jpg" alt="Thesis submission at the Department of Food Technology and Nutrition Science, NSTU" style="width:100%;border:1px solid var(--stone)" loading="lazy">
      <figcaption style="font-family:var(--sans);font-size:.85rem;color:var(--moss);margin-top:.6rem">Thesis submission, Department of Food Technology and Nutrition Science, NSTU.</figcaption>
    </figure>
    <!-- TODO: add certifications and trainings as a third ledger item each. -->
  </div>
</section>

<section>
  <div class="wrap">
    <p class="eyebrow">Skills</p>
    <h2>What I bring to a team.</h2>
    <div class="grid-2">
      <div class="entry"><h3>Programme &amp; field</h3><p>Activity planning and implementation, field coordination, community engagement, stakeholder communication, monitoring and reporting.</p></div>
      <div class="entry"><h3>Financial &amp; administrative</h3><p>Budget management, grant proposal writing, requisitions and procurement support.</p></div>
      <div class="entry"><h3>Research &amp; analysis</h3><p>Survey design, household data collection, quantitative analysis in SPSS and R, literature review, scientific writing.</p></div>
      <div class="entry"><h3>Technical</h3><p>R and Python; SPSS; Google Workspace and Google Apps Script automation; MS Word, Excel, PowerPoint; Canva.</p></div>
      <div class="entry"><h3>Languages</h3><p>Bangla &mdash; native and fluent. English &mdash; professional working proficiency.</p></div>
      <div class="entry"><h3>Community engagement</h3><p>Long-term trust-building with indigenous farming households; training facilitation and public speaking; cross-cultural collaboration across CHT communities.</p></div>
    <!-- TODO: add any CHT languages you speak to the Languages entry above. -->
  </div>
</section>
"""

# ---------------------------------------------------------------- WORK
work = f"""
<section class="hero">
  <div class="wrap">
    {CONTOURS}
    <div class="hero-text">
      <p class="eyebrow">Experience</p>
      <h1>Roles, appointments, and recognition.</h1>
    </div>
  </div>
</section>

<section>
  <div class="wrap">
    <h2>Career path</h2>
    <ul class="ledger">
      <li>
        <div class="when">2024 &ndash; present</div>
        <div class="what"><strong>Founder &amp; Executive Director</strong><span class="tag">Current</span>
        <span>Jhum Revolution &mdash; Chittagong Hill Tracts, Bangladesh</span>
        <p>Lead a youth-led organisation working on climate resilience, indigenous food
        systems, and community empowerment, reaching 300+ families across the Chittagong Hill
        Tracts. Direct programme design, field coordination, and community engagement. Wrote
        and secured the ICCCAD grant that launched the six-month Jhum Revolution Campaign, and
        managed the project end to end. Built the organisation's volunteer recruitment,
        onboarding, and administrative systems, including a Google Apps Script dashboard and
        automated communications workflows. Responsible for partnerships, safeguarding policy,
        and financial reporting.</p></div>
      </li>
      <li>
        <div class="when">2026 &ndash; present</div>
        <div class="what"><strong>Fellow, Climate Policy Negotiation Fellowship</strong><span class="tag">Current</span>
        <span>Two-year programme in climate policy and multilateral negotiation</span></div>
      </li>
      <li>
        <div class="when">Jul 2026 &ndash; present</div>
        <div class="what"><strong>Member, United Nations Youth Advisory Group, Bangladesh</strong><span class="tag">Current</span>
        <span>Climate Change and Green Growth thematic area</span></div>
      </li>
      <li>
        <div class="when">Apr 2025 &ndash; Apr 2026</div>
        <div class="what"><strong>Office Intern</strong>
        <span>Ranking and Strategic Development Cell, Noakhali Science and Technology University</span>
        <p>Contributed to data collection, analysis, and entry for global university ranking
        databases, and assisted in preparing institutional reports and documentation.</p></div>
      </li>
      <li>
        <div class="when">2025 &ndash; 2026</div>
        <div class="what"><strong>Youth Representative for Bangladesh, World Food Forum</strong>
        <span>Food and Agriculture Organization of the United Nations</span>
        <p>Represented Bangladeshi youth in global food systems dialogue, bringing evidence
        from indigenous and climate-affected communities into the conversation.</p></div>
      </li>
      <li>
        <div class="when">2024 &ndash; 2025</div>
        <div class="what"><strong>President, NSTU Science Club</strong>
        <span>Noakhali Science and Technology University</span>
        <p>Organised the 3rd NSTU National Science Fest in 2025 and coordinated club
        programming. Previously served as Research and Development Secretary, 2023&ndash;24.</p></div>
      </li>
    </ul>
    <!-- TODO: add any paid roles, internships, or consultancies here, newest first.
         Copy one <li> block and edit it. -->
  </div>
</section>

<section>
  <div class="wrap">
    <h2>Recognition</h2>
    <ul class="ledger">
      <li>
        <div class="when">Oct 2024</div>
        <div class="what"><strong>Winner, Youth Innovation Fund</strong>
        <span>ICCCAD, Independent University Bangladesh, with the Embassy of Sweden &mdash; Promote Green Ideas / Campaigns category</span>
        <p>An award of BDT 300,000 that funded the Jhum Revolution Campaign
        (August 2024 &ndash; January 2025), which engaged more than 250 students and
        established the organisation's first community programmes.</p></div>
      </li>
    </ul>
  </div>
</section>

<section>
  <div class="wrap">
    <h2>Speaking &amp; writing</h2>
    <ul class="ledger">
      <li>
        <div class="when">2026</div>
        <div class="what"><strong>Keynote speaker</strong>
        <p><a href="https://www.linkedin.com/posts/sunanda-dewaan29_it-was-an-honor-to-serve-as-the-keynote-speaker-activity-7371879066464878592-D9oD">Read the post on LinkedIn</a></p>
        <!-- TODO: replace the title above with the event name, and add a one-line
             description of what you spoke about. --></div>
      </li>
      <li>
        <div class="when">Nov 2025</div>
        <div class="what"><strong>Guest speaker, Behind The Journey &mdash; Season 2, Episode 28</strong>
        <span>Youth School for Social Entrepreneurs (YSSE) &mdash; broadcast live on Facebook, YouTube, and LinkedIn</span>
        <p>A conversation on the founding of Jhum Revolution: the vision behind it, the
        challenges, and what social entrepreneurship actually asks of you.
        <a href="https://www.linkedin.com/events/behindthejourney-season2-episod7400515779894394880/theater/">Event page</a></p></div>
      </li>
      <li>
        <div class="when">Article</div>
        <div class="what"><strong>Indigenous Communities in Bangladesh: Victims of Climate Change</strong>
        <span>Published on LinkedIn</span>
        <p>On how climate change is reshaping life for indigenous communities in Bangladesh,
        and what adaptation looks like from inside those communities.
        <a href="article-indigenous-communities.html">Read the article</a></p></div>
      </li>
    </ul>
  </div>
</section>

<section>
  <div class="wrap">
    <h2>Organisations I have worked with</h2>
    <div class="grid-2">
      <div class="entry"><h3>ICCCAD</h3><p>Youth Innovative Fund recipient; co-organised a capacity building seminar at NSTU.</p></div>
      <div class="entry"><h3>FAO &mdash; World Food Forum</h3><p>Youth Representative for Bangladesh, 2025&ndash;26.</p></div>
      <div class="entry"><h3>United Nations Bangladesh</h3><p>Member, UN Youth Advisory Group &mdash; Climate Change and Green Growth.</p></div>
      <div class="entry"><h3>Noakhali Science and Technology University</h3><p>Research assistantships, the Ranking &amp; Strategic Development Cell, and the Science Club.</p></div>
    </div>
  </div>
</section>
"""

# ---------------------------------------------------------------- RESEARCH
research = f"""
<section class="hero">
  <div class="wrap">
    {CONTOURS}
    <div class="hero-text">
      <p class="eyebrow">Research</p>
      <h1>Field studies in food, water, and climate.</h1>
      <p class="lede">Three research assistantships across hill and coastal Bangladesh,
      each grounded in household-level data collection.</p>
    </div>
  </div>
</section>

<section>
  <div class="wrap">
    <h2>Research experience</h2>
    <ul class="ledger">
      <li>
        <div class="when">Researcher<br>Ongoing</div>
        <div class="what"><strong>Water Security and WASH Practices: Implications for the Livelihood of the Bede Community in Noakhali, Bangladesh</strong>
        <span>Supervisor: Dr. Md. Shohel Khan, Associate Professor, Dept. of Environmental Science and Disaster Management, NSTU</span></div>
      </li>
      <li>
        <div class="when">Research Assistant<br>Sep &ndash; Oct 2024</div>
        <div class="what"><strong>After the Floods: The Poverty&ndash;Gender Nexus in Food Insecurity in Bangladesh</strong>
        <span>A multi-institutional household survey by Noakhali Science and Technology University, Hong Kong Baptist University, and the Australian National University &mdash; Principal Investigator: Dr. Md. Abdullah Al Mamun, Associate Professor, Dept. of Food Technology and Nutrition Science, NSTU</span>
        <p>Completed over 50 household surveys, covering data collection, quality control, and
        informed consent protocols across international ethics frameworks.</p></div>
      </li>
      <li>
        <div class="when">Research Assistant</div>
        <div class="what"><strong>Impact of Digital Addiction on Maternal and Child Health and Dietary Diversity in the Chittagong Hill Tracts</strong>
        <span>Undergraduate research &mdash; Supervisor: Dr. Mansura Mokbul, Chairman and Associate Professor, Dept. of Food Technology and Nutrition Science, NSTU</span></div>
      </li>
      <li>
        <div class="when">Research Assistant</div>
        <div class="what"><strong>Capacity Building of Youth to Improve Drinking Water Security and Climate Resilience through a Youth-led Participatory Sensing Model</strong>
        <span>Hatiya Island, Noakhali &mdash; Principal Investigator: Md. Saiful Islam, ICCCAD Fellowship Holder</span></div>
      </li>
    </ul>
  </div>
</section>

<section>
  <div class="wrap">
    <h2>Reference</h2>
    <p>Dr. Md. Abdullah Al Mamun, Associate Professor in the Department of Food Technology
    and Nutrition Science at NSTU, supervised the <em>After the Floods</em> fieldwork and has
    provided a written letter of recommendation.</p>
    <div class="actions"><a class="btn" href="recommendation-letter-nstu.pdf">Read the letter (PDF)</a></div>
  </div>
</section>

<section>
  <div class="wrap">
    <h2>Current research</h2>
    <p>My master's research sits in environmental science and disaster management, examining
    the relationship between climate stress, agriculture, and diet in coastal Noakhali,
    alongside work on post-flood recovery and resilience in the Chittagong Hill Tracts.</p>
    <!-- TODO: update this paragraph once your thesis topic is finalised. -->
  </div>
</section>

<section>
  <div class="wrap">
    <h2>Publications &amp; presentations</h2>
    <p>Forthcoming.</p>
    <!-- TODO: when you have papers, posters, or conference talks, replace the line above
         with a <ul class="ledger"> block using the same structure as the section above. -->
  </div>
</section>
"""

# ---------------------------------------------------------------- IMPACT
impact = f"""
<section class="hero">
  <div class="wrap">
    {CONTOURS}
    <div class="hero-text">
      <p class="eyebrow">Impact</p>
      <h1>Jhum Revolution.</h1>
      <p class="lede">A youth-led organisation supporting jhum farming families in the
      Chittagong Hill Tracts, built on long relationships rather than short projects.</p>
    </div>
  </div>
</section>

<section>
  <div class="wrap">
    <div class="counters">
      <div><div class="num" data-count="300" data-suffix="+">300+</div><div class="cap">Families reached</div></div>
      <div><div class="num" data-count="250" data-suffix="+">250+</div><div class="cap">Students engaged through the ICCCAD-funded campaign</div></div>
      <div><div class="num" data-count="300">300</div><div class="cap">3D educational books published and distributed</div></div>
      <div><div class="num" data-count="75">75</div><div class="cap">Participants at the NSTU capacity building seminar with ICCCAD</div></div>
    </div>
  </div>
</section>

<section>
  <div class="wrap">
    <h2>How the organisation works</h2>
    <p>Jhum Revolution was co-founded to work with indigenous farming families in the CHT
    on climate resilience and food systems. The core asset is trust built over multi-year
    relationships with jhum farming households &mdash; which is why the programmes start
    from what communities already practise.</p>
    <p>The organisation runs on a volunteer cohort model with structured recruitment,
    onboarding, and CHT-specific fieldwork guidance, supported by internal operational
    systems for applications, scheduling, and reporting.</p>
    <p>The flagship project, <em>Capacity Building of the Local Youth through the Jhum
    Revolution Campaign and 3D Educational Tools to Enhance Climate Resilience in Chittagong
    Hill Tracts, Bangladesh</em>, works on three objectives: equipping young people in the
    Hill Tracts to integrate traditional jhum cultivation with agroforestry, contouring, and
    terracing; promoting climate-resilient and sustainable agricultural practice; and using
    3D educational tools alongside traditional teaching methods.</p>
    <p>The approach is integration rather than replacement. Where community members were
    hesitant that new techniques might displace jhum, the campaign demonstrated how
    agroforestry and contouring make existing practice more productive, and worked through
    elders and local leaders to build trust.</p>
    <div class="actions"><a class="btn" href="{JHUM}">Visit the organisation site</a></div>
  </div>
</section>

<section>
  <div class="wrap">
    <h2>Programme areas</h2>
    <ul class="diamonds">
      <li><strong>Jhum Climate Field Schools</strong> &mdash; practical, season-based learning with farming households.</li>
      <li><strong>Indigenous Knowledge Documentation</strong> &mdash; recording jhum cultivation cycles, seed-saving, and traditional food knowledge.</li>
      <li><strong>Youth Climate Action Fellowship</strong> &mdash; putting young people from the hills in charge of local climate work.</li>
      <li><strong>Women and Child Resilience Hubs</strong> &mdash; nutrition and resilience support where climate stress lands hardest.</li>
      <li><strong>Policy Advocacy</strong> &mdash; carrying community evidence into district and national conversations.</li>
    </ul>
    <p style="margin-top:1.5rem">These five areas form <em>Rooted &amp; Resilient</em>, the
    organisation's multi-year programme framework.</p>
  </div>
</section>

<section>
  <div class="wrap">
    <h2>Selected activities</h2>
    <ul class="ledger">
      <li>
        <div class="when">Aug 2024 &ndash; Jan 2025</div>
        <div class="what"><strong>Jhum Revolution Campaign</strong>
        <span>Funded by the ICCCAD Youth Innovation Fund &mdash; Monoghor Residential School and College, Rangapani, Rangamati</span>
        <p>Engaged 250+ students from across Rangamati, Khagrachhari, and Bandarban through
        a seminar and the distribution of 300 copies of a purpose-written 3D educational book,
        alongside an online seminar and training session for Indigenous students at NSTU.
        <a href="https://icccad.net/wp-content/uploads/2025/02/Club-fund_JHUM-REVOLUTION.pdf">Read the final report (ICCCAD)</a></p></div>
      </li>
      <li>
        <div class="when">Dec 2025</div>
        <div class="what"><strong>Exhibitor, Environment Innovation Summit &amp; Awards 2025</strong>
        <span>Bangladesh Sishu Academy Auditorium, Doyel Chattar, Dhaka &mdash; 22 December 2025</span>
        <p>Presented the Sustainable Jhum Model, a 3D teaching tool showing how terracing,
        contouring, agroforestry, rainwater harvesting, and compost fertilisation can be
        layered onto existing jhum practice.</p></div>
      </li>
      <li>
        <div class="when">Dec 2024</div>
        <div class="what"><strong>Seminar: Capacity Building of the Local Youth through the Jhum Revolution Campaign and 3D Educational Tools</strong>
        <span>IQAC, NSTU &mdash; 12 December 2024, with Independent University Bangladesh, ICCCAD, and the Embassy of Sweden &mdash; 75 participants</span>
        <p>Indigenous students at NSTU from Rangamati, Khagrachhari, and Bandarban took part.</p></div>
      </li>
      <li>
        <div class="when">2026</div>
        <div class="what"><strong>Volunteer cohort recruitment</strong>
        <span>32 applicants assessed, with structured role assignment and onboarding</span></div>
      </li>
    </ul>
  </div>
</section>

<section>
  <div class="wrap">
    <h2>From the field</h2>
    <p>Campaign work, seminars, school sessions, and community documentation across the
    Chittagong Hill Tracts and Noakhali.</p>
    <div class="gallery">

      <figure>
        <img src="community-discussion.jpg" alt="Group discussion with jhum farming women under a tree in the Chittagong Hill Tracts" loading="lazy">
        <figcaption>Community discussion with jhum farming households &mdash; the starting point for every programme.</figcaption>
      </figure>

      <figure>
        <img src="filming.jpg" alt="Filming an interview with a community member in the hills" loading="lazy">
        <figcaption>Documenting indigenous knowledge on camera, in the community's own words.</figcaption>
      </figure>

      <figure>
        <img src="nstu-presentation.jpg" alt="Presenting the Jhum Revolution campaign at the NSTU seminar" loading="lazy">
        <figcaption>Presenting at the capacity building seminar, IQAC, NSTU &mdash; December 2024.</figcaption>
      </figure>

      <figure>
        <img src="seminar-group.jpg" alt="Group photograph of seminar participants at NSTU" loading="lazy">
        <figcaption>Seminar participants at NSTU, held with Independent University Bangladesh, ICCCAD, and the Embassy of Sweden.</figcaption>
      </figure>

      <figure>
        <img src="school-session.jpg" alt="Speaking to students in a classroom in the Chittagong Hill Tracts" loading="lazy">
        <figcaption>School session in the hills, introducing climate-resilient jhum practices.</figcaption>
      </figure>

      <figure>
        <img src="seminar-guests.jpg" alt="Guests and team at a Jhum Revolution session with the project title projected behind" loading="lazy">
        <figcaption>Community leaders, teachers, and the Jhum Revolution team at a school programme.</figcaption>
      </figure>

      <figure>
        <img src="student-booklet.jpg" alt="A student reading the Jhum Revolution educational booklet in class" loading="lazy">
        <figcaption>A student reading the campaign booklet &mdash; the material is produced in Bangla for hill schools.</figcaption>
      </figure>

      <figure>
        <img src="sapling.jpg" alt="Handing a sapling to a student during a tree planting programme" loading="lazy">
        <figcaption>Sapling distribution with school students.</figcaption>
      </figure>

      <figure>
        <img src="field-planting.jpg" alt="Tree planting and climate awareness programme in Khagrachhari" loading="lazy">
        <figcaption>Tree planting and climate awareness programme, Khagrachhari district.</figcaption>
      </figure>

      <figure>
        <img src="summit-team.jpg" alt="The Jhum Revolution team at their stall at the Environment Innovation Summit" loading="lazy">
        <figcaption>The team at the Environment Innovation Summit &amp; Awards, Dhaka &mdash; December 2025.</figcaption>
      </figure>

      <figure>
        <img src="summit-poster.jpg" alt="Explaining the Sustainable Jhum Model to summit visitors" loading="lazy">
        <figcaption>Explaining the Sustainable Jhum Model &mdash; a 3D teaching tool showing terracing, contouring, agroforestry, rainwater harvesting, and compost fertilisation.</figcaption>
      </figure>

      <figure>
        <img src="summit-stall.jpg" alt="Visitors at the Jhum Revolution stall at the Environment Innovation Summit" loading="lazy">
        <figcaption>Bangladesh Sishu Academy Auditorium, Doyel Chattar &mdash; 22 December 2025.</figcaption>
      </figure>

      <figure>
        <img src="summit-banner.jpg" alt="The Jhum Revolution display banner at the summit" loading="lazy">
        <figcaption>Jhum Revolution: a climate-smart, eco-friendly, research-oriented agricultural method for the Chittagong Hill Tracts.</figcaption>
      </figure>

      <figure>
        <img src="nstu-stall.jpg" alt="Jhum Revolution booklets on display at the Noakhali Science and Technology University stall" loading="lazy">
        <figcaption>Campaign booklets on display at the NSTU research stall.</figcaption>
      </figure>

      <figure>
        <img src="icccad-award.jpg" alt="Receiving the Youth Innovation Fund award" loading="lazy">
        <figcaption>Receiving the Youth Innovation Fund award &mdash; ICCCAD, Independent University Bangladesh, and the Embassy of Sweden.</figcaption>
      </figure>

      <figure>
        <img src="thesis.jpg" alt="Thesis submission at Noakhali Science and Technology University" loading="lazy">
        <figcaption>Thesis submission, Department of Food Technology and Nutrition Science, NSTU.</figcaption>
      </figure>

    </div>
    <!-- TODO: add more field photographs here. Copy one <figure> block, put the image
         file in this folder, and change the src and the caption. -->
  </div>
</section>
"""

# ---------------------------------------------------------------- CONTACT
contact = f"""
<section class="hero">
  <div class="wrap">
    {CONTOURS}
    <div class="hero-text">
      <p class="eyebrow">Contact</p>
      <h1>Let's work together.</h1>
      <p class="lede">Open to research collaboration, programme partnerships, fellowships,
      and speaking on indigenous food systems and youth-led climate work.</p>
    </div>
  </div>
</section>

<section>
  <div class="wrap">
    <h2>Reach me</h2>
    <ul class="contact-lines">
      <li><span class="lbl">Email</span> <a href="mailto:{EMAIL}">{EMAIL}</a></li>
      <li><span class="lbl">LinkedIn</span> <a href="{LINKEDIN}">linkedin.com/in/sunanda-dewaan29</a></li>
      <li><span class="lbl">Organisation</span> <a href="{JHUM}">Jhum Revolution</a></li>
      <li><span class="lbl">Based in</span> Chattogram, Bangladesh</li>
      <li><span class="lbl">Phone</span> <a href="tel:+8801624415216">+880 1624 415216</a></li>
    </ul>
  </div>
</section>

<section>
  <div class="wrap">
    <h2>What I am looking for</h2>
    <div class="grid-2">
      <div class="entry"><h3>Research collaboration</h3><p>Food systems, nutrition, climate adaptation, and post-disaster recovery in Bangladesh.</p></div>
      <div class="entry"><h3>Programme partnerships</h3><p>Organisations working in the Chittagong Hill Tracts or on indigenous knowledge and climate resilience.</p></div>
      <div class="entry"><h3>Speaking &amp; facilitation</h3><p>Youth convenings, university sessions, and policy dialogues on indigenous food systems.</p></div>
      <div class="entry"><h3>Fellowships &amp; further study</h3><p>Environmental science, disaster management, and climate policy programmes.</p></div>
    </div>
  </div>
</section>
"""


# ------------------------------------------------- FULL ARTICLE (single post)
article_indigenous = f"""
<section class="hero article-hero" style="padding-bottom:1.5rem">
  <div class="wrap">
    <p class="eyebrow">Article &nbsp;·&nbsp; 22 July 2026</p>
    <h1 style="font-size:clamp(2rem,5.5vw,3.4rem);max-width:20ch">Are Indigenous Communities in Bangladesh Victims of Climate Change?</h1>
    <p class="byline">By Sunanda Dewaan &mdash; Founder, Jhum Revolution &nbsp;|&nbsp; Researcher: Food, Nutrition, Climate</p>
  </div>
</section>

<section style="border-top:none;padding-top:0">
  <div class="wrap">
    <img src="article-cover.jpg" alt="Indigenous women transplanting rice seedlings in a paddy field in the Chittagong Hill Tracts" loading="lazy" style="width:100%;border:1px solid var(--stone)">
  </div>
</section>

<section style="border-top:none">
  <div class="wrap">
    <div class="article-body">

      <p>If this question is asked in a seminar room, you will get a confident &ldquo;yes.&rdquo;
      But if it is asked in a remote village in the Chittagong Hill Tracts (CHT) and you will
      get a more complicated answer, with one that has less to do with helplessness and more
      to do with a system that has worked for generations but now being pushed past its limit.</p>

      <p>I&rsquo;ve spent time working with jhum families across Rangamati, Khagrachhari and
      Bandarban for my research projects and through Jhum Revolution. What I&rsquo;ve seen
      doesn&rsquo;t fit neatly into &ldquo;victim&rdquo; narrative that dominates climate
      reporting nor into the opposite, equally flattening narrative of the endlessly
      &ldquo;resilient&rdquo; Indigenous community. The truth sits in between: these
      communities have a working body of ecological knowledge and adaptive practice.</p>

      <p>What&rsquo;s failing the Indigenous communities isn&rsquo;t a lack of capacity &mdash;
      it&rsquo;s land tenure insecurity, deforestation, and policy neglect closing in on a
      system that used to have room to breathe.</p>

      <h2>When the Rain Won&rsquo;t Stop: The 2026 Floods as a Case in Point</h2>

      <p>This isn&rsquo;t hypothetical. As I write this, Bangladesh is still absorbing the
      damage from the monsoon floods that tore through Chattogram division and the Hill Tracts
      in July 2026. Several news media, e.g. Daily Star, Dhaka Tribune and Prothom Alo,
      reported over 50 people have died across Chattogram, Cox&rsquo;s Bazar, and the three
      hill districts of Rangamati, Khagrachhari, and Bandarban, with the toll driven largely by
      landslides, hill collapses, and drowning. More than a million people have been affected,
      hundreds of thousands of families displaced into shelters. Specifically in the Hill
      Tracts, roads to Bandarban and Sajek were cut off entirely for days, leaving tourists and
      residents alike stranded.</p>

      <p>The agricultural toll is just as severe. The Business Standard, citing government
      damage assessments, reported nearly 16,000 hectares of cropland damaged across the
      division, fisheries losses exceeding Tk91 crore, and more than 1.1 lakh livestock and
      poultry killed, with total livestock losses estimated at over Tk30 crore. For hill
      farmers, that isn&rsquo;t an abstract statistic, it&rsquo;s a wiped-out season, a
      submerged seedbed, a family that has to decide whether to rebuild on the same slope or
      not.</p>

      <figure style="margin:2.5rem 0">
        <img src="flood-village.jpg" alt="Families wading through floodwater in a hill village in Barkal Upazila, Rangamati" loading="lazy" style="width:100%;border:1px solid var(--stone)">
        <figcaption style="font-family:var(--sans);font-size:.85rem;color:var(--moss);margin-top:.6rem">July 9, 2026 | Barkal Upazila, Rangamati | Credit: Proti Bindu Wangza</figcaption>
      </figure>

      <p>None of this is new. The Hill Tracts flooded catastrophically in 2017, killing over
      150 people in landslides in a single week. The pattern that&rsquo;s emerging is not
      &ldquo;occasional disaster&rdquo; but &ldquo;recurring stress&rdquo; and recurring stress
      is exactly the kind of thing Indigenous adaptive systems were built to handle, provided
      they&rsquo;re given the land, time, and institutional support to do so. Right now, they
      aren&rsquo;t.</p>

      <h2>Agriculture Under Pressure: The Shrinking Jhum Cycle</h2>

      <p>Jhum, the traditional shifting cultivation system practiced by Chakma, Marma, Tripura,
      Mro, and other Indigenous communities in the CHT, was never a crude &ldquo;slash and
      burn&rdquo; it was a rotational system with a built-in recovery period. A plot would be
      cultivated for one or two seasons, then left fallow for 10 to 20 years to let the forest
      and soil regenerate before being farmed again.</p>

      <figure style="margin:2.5rem 0">
        <img src="jhum-hillside.jpg" alt="Indigenous farmers working a jhum plot on a hillside in Barkal Upazila, Rangamati" loading="lazy" style="width:100%;border:1px solid var(--stone)">
        <figcaption style="font-family:var(--sans);font-size:.85rem;color:var(--moss);margin-top:.6rem">Indigenous farmers working in the Jhum | July 21, 2026 | Barkal Upazila, Rangamati | Credit: Proti Bindu Wangza</figcaption>
      </figure>

      <p>Nowadays, that fallow cycle has collapsed. Population pressure, shrinking available
      land, and encroachment have pushed the cycle down to 2 to 3 years in many areas. It is
      nowhere near enough time for soil fertility or forest cover to recover. The result is a
      system running in overdraft: lower yields, more erosion, and land that becomes
      progressively less forgiving of the very practice that used to sustain it.</p>

      <p>This is the part of the story that gets lost when climate change is treated as a
      purely meteorological event. Erratic rainfall and hotter temperatures are compounding a
      stress that land scarcity was already creating. Farmers aren&rsquo;t just contending with
      a changing climate, they are contending with a changing climate on a shrinking, degrading
      land base, with far less institutional recognition of their land rights than lowland
      farmers have.</p>

      <h2>Food and Daily Life: The Quiet Disruptions</h2>

      <figure style="margin:2.5rem 0">
        <img src="monsoon-hills.jpg" alt="Villagers under umbrellas during a light shower on a hill" loading="lazy" style="width:100%;border:1px solid var(--stone)">
        <figcaption style="font-family:var(--sans);font-size:.85rem;color:var(--moss);margin-top:.6rem">A light shower at a silent hill | Credit: Proti Bindu Wangza</figcaption>
      </figure>

      <p>The headline numbers, e.g. deaths, hectares, taka lost don&rsquo;t capture what a
      changing climate actually does to daily life in a hill village. Year after year, not just
      during a single disaster.</p>

      <p>Erratic rainfall means the planting calendar that jhum farmers relied on for
      generations no longer holds rains arrive late, then all at once, then not at all for
      weeks, making it harder to know when to sow or when a crop is safe from either drought or
      flash flooding. Rising heat is shortening the growing window for some traditional crops
      and pushing families to alter what they plant and when.</p>

      <p>When heavy rainfall or landslide debris damage or destroy the Jhum or their rice
      field, families lose not just income but their immediate food supply, and in the hills
      specifically, landslide-blocked roads mean that even when relief reaches the district, it
      can take days to physically get to isolated communities.</p>

      <p>Their food system itself is built on labour, not just land. After a jhum harvest, rice
      still has to be threshed, winnowed, and sun-dried by hand. It is a communal process,
      often done together as families and neighbors, spread across tarpaulins in the open air,
      dependent on a few days of clear, dry weather to finish properly.</p>

      <figure style="margin:2.5rem 0">
        <img src="paddy-winnowing.jpg" alt="Farmers winnowing the rice harvest together on tarpaulins" loading="lazy" style="width:100%;border:1px solid var(--stone)">
        <figcaption style="font-family:var(--sans);font-size:.85rem;color:var(--moss);margin-top:.6rem">Hands that share a harvest, share a hill | Credit: Purna Moni Chakma</figcaption>
      </figure>

      <p>When rainfall becomes erratic, that drying window shrinks along with everything else:
      grain left out too long in unexpected rain, molds or sprouts, turning an already reduced
      yield into an even smaller usable one. A shrinking harvest that also can not be safely
      dried is a food security problem multiplying on itself, and it&rsquo;s rarely counted in
      official damage assessments the way a flooded field is.</p>

      <h2>Indigenous Knowledge: The System Nobody&rsquo;s Funding</h2>

      <p>The &ldquo;Machang Ghor&rdquo; an elevated bamboo stilt house, has long been a
      defining feature of traditional architecture in the Chittagong Hill Tracts. Built to
      withstand seasonal flooding while reducing the risks of landslides and encounters with
      wild animals, it reflects generations of practical knowledge shaped by close interaction
      with the local environment. More than a dwelling, the Machang Ghor represents an enduring
      form of climate adaptation embedded in Indigenous architectural traditions.</p>

      <figure style="margin:2.5rem 0">
        <img src="hills-cloud.jpg" alt="A Machang Ghor, an elevated bamboo stilt house, above cloud-filled hills" loading="lazy" style="width:100%;border:1px solid var(--stone)">
        <figcaption style="font-family:var(--sans);font-size:.85rem;color:var(--moss);margin-top:.6rem">A house in the cloud | Machang Ghor | Credit: Proti Bindu Wangza</figcaption>
      </figure>

      <p>This adaptive knowledge extends well beyond housing. Traditional food storage methods,
      seasonal foraging calendars, and community farming and social practices are all
      synchronized with environmental rhythms and guided by careful observation of natural
      indicators. These practices have enabled Indigenous communities to anticipate seasonal
      changes, manage resources sustainably, and strengthen their resilience to climate
      variability for generations. Long before the term climate adaptation entered global
      discourse, these Indigenous knowledge systems were already providing effective, locally
      grounded solutions for living with environmental change.</p>

      <p>However, the accelerating impacts of climate change are increasingly undermining the
      reliability of these traditional knowledge systems. Rainfall patterns have become more
      erratic, dry seasons are longer and hotter, and extreme weather events occur with greater
      frequency and intensity. Environmental cues that once guided planting, harvesting,
      foraging, and water management are becoming less predictable as weather patterns depart
      from historical norms. As a result, Indigenous communities are finding it more difficult
      to rely solely on inherited knowledge to make decisions that have sustained them for
      generations.</p>

      <p>At the same time, there has been limited investment in strengthening the adaptive
      capacity of these communities. Climate adaptation policies and development initiatives
      often overlook Indigenous knowledge or fail to meaningfully involve Indigenous peoples in
      planning and decision-making. While these communities continue to face increasing climate
      risks including landslides, prolonged droughts, flash floods, declining soil fertility,
      and water scarcity; there remains a significant gap in targeted adaptation measures that
      build upon and reinforce their existing resilience.</p>

      <p>This knowledge is not static folklore. It&rsquo;s a living, adaptive system, and
      increasingly it&rsquo;s being carried forward by youth and women&rsquo;s networks groups
      like UNESCO&rsquo;s Youth As Researchers initiative and the Hill Women&rsquo;s Federation
      who are documenting traditional practices while also pushing for formal recognition and
      policy inclusion. That combination matters: preserving the knowledge and fighting for the
      institutional standing to act on it.</p>

      <figure style="margin:2.5rem 0">
        <img src="household-interview.jpg" alt="Key informant interview with an Indigenous elder on a veranda" loading="lazy" style="width:100%;border:1px solid var(--stone)">
        <figcaption style="font-family:var(--sans);font-size:.85rem;color:var(--moss);margin-top:.6rem">Key Informant Interview (KII) with an Indigenous elder | UNESCO Dhaka | Credit: Sunanda Dewaan</figcaption>
      </figure>

      <p>Rather than replacing Indigenous knowledge, climate adaptation efforts should seek to
      complement and strengthen it. Integrating traditional ecological knowledge with
      scientific climate information, promoting climate-resilient agricultural practices,
      improving water harvesting and storage systems, supporting resilient housing, and
      ensuring Indigenous participation in policy development can enhance community resilience
      while preserving cultural heritage.</p>

      <p>By combining centuries of locally grounded experience with modern adaptation
      strategies, policymakers, researchers, and development practitioners can help ensure that
      Indigenous communities in the Chittagong Hill Tracts are better equipped to navigate an
      increasingly uncertain climate while maintaining their identity, livelihoods, and
      connection to the land.</p>

      <h2>So, Victims or Not?</h2>

      <p>The answer is neither simple nor binary. To portray Indigenous communities in the
      Chittagong Hill Tracts merely as victims is to ignore generations of knowledge,
      innovation, and adaptation that have enabled them to live with a dynamic and often
      challenging environment. Their agricultural systems, housing designs, food preservation
      practices, and ecological knowledge demonstrate that resilience is not a new concept but
      it has been embedded in their way of life for centuries.</p>

      <p>The honest answer is that these are communities with a functioning adaptive system
      operating under structural constraint. The real challenge is not their ability to adapt,
      but the structural barriers they face. The future of climate adaptation in the Chittagong
      Hill Tracts should not be built on replacing Indigenous knowledge with external
      solutions. Climate adaptation efforts must move beyond treating Indigenous peoples as
      beneficiaries and instead recognize them as partners, strengthening their resilience
      through secure land rights, community-led adaptation, inclusive governance, and the
      integration of Indigenous and scientific knowledge.</p>

      <p>If we fail to support these communities, we will not only lose more than livelihoods
      but also we risk losing one of Bangladesh&rsquo;s richest repositories of climate
      adaptation knowledge. But if we invest in Indigenous leadership and recognize their
      expertise, the Chittagong Hill Tracts can become a model of how traditional wisdom and
      modern science together can build a more resilient future.</p>

      <hr style="border:none;border-top:1px solid var(--stone);margin:3rem 0 1.5rem">
      <p style="font-size:.95rem;color:var(--moss)">Originally published on LinkedIn,
      22 July 2026.
      <a href="https://www.linkedin.com/pulse/indigenous-communities-bangladesh-victims-climate-change-dewaan-9smkc/">Read and comment there.</a></p>
      <p style="margin-top:1.5rem"><a class="btn" href="article.html">All articles</a></p>

    </div>
  </div>
</section>
"""


# ---------------------------------------------------------------- ARTICLE INDEX
articles_index = f"""
<section class="hero">
  <div class="wrap">
    {CONTOURS}
    <div class="hero-text">
      <p class="eyebrow">Writing</p>
      <h1>Articles.</h1>
      <p class="lede">Essays on climate adaptation, indigenous knowledge, and food systems
      in the Chittagong Hill Tracts.</p>
    </div>
  </div>
</section>

<section>
  <div class="wrap">
    <article class="post-card">
      <a class="post-thumb" href="article-indigenous-communities.html">
        <img src="article-cover.jpg" alt="Indigenous women transplanting rice seedlings in a paddy field in the Chittagong Hill Tracts" loading="lazy">
      </a>
      <div class="post-meta">
        <p class="post-date">22 July 2026</p>
        <h2><a href="article-indigenous-communities.html">Are Indigenous Communities in Bangladesh Victims of Climate Change?</a></h2>
        <p>If this question is asked in a seminar room, you will get a confident &ldquo;yes.&rdquo;
        But if it is asked in a remote village in the Chittagong Hill Tracts you will get a more
        complicated answer &mdash; one that has less to do with helplessness and more to do with
        a system that has worked for generations but is now being pushed past its limit.</p>
        <p><a class="btn" href="article-indigenous-communities.html">Read the full article</a></p>
      </div>
    </article>

    <!-- TODO: to add another article, copy the <article class="post-card"> block above,
         create a new page for it, and point the links at that page. -->
  </div>
</section>
"""

if __name__ == "__main__":
    page("index.html", "Sunanda Dewaan — Climate Resilience & Indigenous Food Systems",
         "Sunanda Dewaan is a researcher and youth climate leader in Bangladesh, founder of Jhum Revolution, working on indigenous food systems, nutrition, and climate resilience in the Chittagong Hill Tracts.", home)
    page("about.html", "About | Sunanda Dewaan",
         "Researcher and youth climate leader from Chattogram working on nutrition, indigenous food systems, and climate resilience in the Chittagong Hill Tracts.", about)
    page("work.html", "Experience | Sunanda Dewaan",
         "Roles, appointments, and recognition — Jhum Revolution, World Food Forum, UN Youth Advisory Group Bangladesh, and the ICCCAD Youth Innovative Fund.", work)
    page("research.html", "Research | Sunanda Dewaan",
         "Research on dietary diversity, digital addiction and maternal health, drinking water security, and post-flood food insecurity in Bangladesh.", research)
    page("impact.html", "Impact | Sunanda Dewaan",
         "Jhum Revolution's work with jhum farming families in the Chittagong Hill Tracts — programmes, reach, and activities.", impact)
    page("article.html", "Articles | Sunanda Dewaan",
         "Writing by Sunanda Dewaan on climate adaptation, indigenous knowledge, and food systems in the Chittagong Hill Tracts, Bangladesh.", articles_index)
    page("article-indigenous-communities.html", "Are Indigenous Communities in Bangladesh Victims of Climate Change? | Sunanda Dewaan",
         "An article by Sunanda Dewaan on climate change, jhum cultivation, and indigenous adaptation in the Chittagong Hill Tracts, Bangladesh.", article_indigenous)
    page("contact.html", "Contact | Sunanda Dewaan",
         "Get in touch with Sunanda Dewaan for research collaboration, programme partnerships, and speaking.", contact)
