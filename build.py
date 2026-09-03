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
        <p style="margin:0;font-size:.9rem">Founder &amp; Managing Director, Jhum Revolution. Working on climate resilience and indigenous food systems in the Chittagong Hill Tracts.</p>
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
    <img src="portrait.jpg" alt="Sunanda Dewaan" width="900" height="900">
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
        <p class="hero-meta">Founder &amp; Managing Director, Jhum Revolution &nbsp;·&nbsp; Chattogram, Bangladesh</p>
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
      <div><div class="num" data-count="2">2</div><div class="cap">UN-linked youth advisory appointments</div></div>
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
        <dt>Current role</dt><dd>Founder &amp; Managing Director, Jhum Revolution</dd>
        <dt>Based in</dt><dd>Chattogram, Bangladesh</dd>
        <dt>Studying</dt><dd>MSc, Environmental Science and Disaster Management, Noakhali Science and Technology University</dd>
        <dt>Prior degree</dt><dd>BSc, Food Technology and Nutrition Science, NSTU (2020&ndash;2025)</dd>
        <dt>Appointments</dt><dd>World Food Forum Youth Representative for Bangladesh (FAO); Member, UN Youth Advisory Group Bangladesh &mdash; Climate Change &amp; Green Growth</dd>
        <dt>Fellowship</dt><dd>Fellow, Climate Policy Negotiation Fellowship 2026</dd>
        <dt>Award</dt><dd>ICCCAD Youth Innovative Fund, 2024</dd>
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
    the poverty&ndash;gender nexus in post-flood food insecurity. I also coordinate the NSTU
    Science Club and represent Bangladesh as a World Food Forum Youth Representative with
    the Food and Agriculture Organization.</p>

    <!-- TODO: add a personal paragraph here in your own words if you want one — what
         drew you to this work, or what you want the next five years to look like. -->
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
    <!-- TODO: add certifications and trainings as a third ledger item each. -->
  </div>
</section>

<section>
  <div class="wrap">
    <p class="eyebrow">Skills</p>
    <h2>What I bring to a team.</h2>
    <div class="grid-2">
      <div class="entry"><h3>Research &amp; analysis</h3><p>Survey design, field data collection, quantitative analysis in SPSS and R, literature review, scientific writing.</p></div>
      <div class="entry"><h3>Programme design &amp; delivery</h3><p>Concept development, budgeting, volunteer recruitment and onboarding, safeguarding and grant-compliance documentation.</p></div>
      <div class="entry"><h3>Research communication</h3><p>Turning field evidence into proposals, policy briefs, and public writing that non-specialists can act on.</p></div>
      <div class="entry"><h3>Community engagement</h3><p>Long-term trust-building with indigenous farming households; cross-cultural collaboration across CHT communities.</p></div>
      <div class="entry"><h3>Public speaking &amp; facilitation</h3><p>Seminars, training sessions, and youth convenings, including capacity-building workshops with ICCCAD.</p></div>
      <div class="entry"><h3>Organisational leadership</h3><p>Founding and running a volunteer-based organisation: team structure, recruitment cycles, and operational systems.</p></div>
    </div>
    <!-- TODO: add a Languages entry (Bangla, English, and any CHT languages you speak). -->
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
        <div class="when">Present</div>
        <div class="what"><strong>Founder &amp; Managing Director</strong><span class="tag">Current</span>
        <span>Jhum Revolution &mdash; Chittagong Hill Tracts, Bangladesh</span>
        <p>Lead a youth-led organisation working on climate resilience, indigenous food
        systems, and community empowerment. Responsible for programme design, grant
        applications, partnerships, volunteer recruitment and onboarding, safeguarding
        policy, and financial reporting.</p></div>
      </li>
      <li>
        <div class="when">2026 &ndash; present</div>
        <div class="what"><strong>Fellow, Climate Policy Negotiation Fellowship</strong><span class="tag">Current</span>
        <span>Two-year programme in climate policy and multilateral negotiation</span></div>
      </li>
      <li>
        <div class="when">2025 &ndash; present</div>
        <div class="what"><strong>Youth Representative for Bangladesh, World Food Forum</strong>
        <span>Food and Agriculture Organization of the United Nations</span>
        <p>Represent Bangladeshi youth in global food systems dialogue, bringing
        evidence from indigenous and climate-affected communities into the conversation.</p></div>
      </li>
      <li>
        <div class="when">2025 &ndash; present</div>
        <div class="what"><strong>Member, UN Youth Advisory Group Bangladesh</strong>
        <span>Climate Change and Green Growth thematic area</span></div>
      </li>
      <li>
        <div class="when">Ongoing</div>
        <div class="what"><strong>Coordinator, NSTU Science Club</strong>
        <span>Noakhali Science and Technology University</span></div>
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
        <div class="when">2024</div>
        <div class="what"><strong>Winner, Youth Innovation Fund</strong>
        <span>ICCCAD, Independent University Bangladesh, with the Embassy of Sweden &mdash; Promote Green Ideas / Campaigns category</span>
        <p>An award of BDT 300,000 that funded the six-month Jhum Revolution Campaign,
        which engaged more than 250 students and established the organisation's first
        community programmes.</p></div>
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
        <a href="https://www.linkedin.com/pulse/indigenous-communities-bangladesh-victims-climate-change-dewaan-9smkc/">Read the article</a></p></div>
      </li>
    </ul>
  </div>
</section>

<section>
  <div class="wrap">
    <h2>Organisations I have worked with</h2>
    <div class="grid-2">
      <div class="entry"><h3>ICCCAD</h3><p>Youth Innovative Fund recipient; co-organised a capacity building seminar at NSTU.</p></div>
      <div class="entry"><h3>FAO &mdash; World Food Forum</h3><p>Youth Representative for Bangladesh.</p></div>
      <div class="entry"><h3>United Nations Bangladesh</h3><p>Member, UN Youth Advisory Group &mdash; Climate Change and Green Growth.</p></div>
      <div class="entry"><h3>Noakhali Science and Technology University</h3><p>Research assistantships and Science Club coordination.</p></div>
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
    <h2>Research assistantships</h2>
    <ul class="ledger">
      <li>
        <div class="when">Research Assistant</div>
        <div class="what"><strong>Impact of Digital Addiction on Maternal and Child Health and Dietary Diversity in the Chittagong Hill Tracts</strong>
        <span>Supervisor: Dr. Mansura Mokbul, Dept. of Food Technology &amp; Nutrition Science, NSTU</span>
        <p>Examined how digital media use among mothers relates to child health outcomes
        and household dietary diversity in hill communities.</p></div>
      </li>
      <li>
        <div class="when">Research Assistant</div>
        <div class="what"><strong>Capacity Building of Youth to Improve Drinking Water Security and Climate Resilience through a Youth-led Participatory Sensing Model</strong>
        <span>Hatiya Island, Noakhali &nbsp;·&nbsp; PI: Md. Saiful Islam, ICCCAD Fellowship Holder</span>
        <p>Supported a participatory model training young people to monitor drinking water
        security in a climate-exposed island community.</p></div>
      </li>
      <li>
        <div class="when">Research Assistant</div>
        <div class="what"><strong>After the Floods: The Poverty&ndash;Gender Nexus in Food Insecurity in Bangladesh</strong>
        <span>PI: Dr. Md. Abdullah Al Mamun, Associate Professor, Dept. of Food Technology &amp; Nutrition Science, NSTU</span>
        <p>Investigated how poverty and gender interact to shape food insecurity in
        flood-affected households.</p></div>
      </li>
    </ul>
  </div>
</section>

<section>
  <div class="wrap">
    <h2>Current research</h2>
    <p>My master's research examines planetary health awareness and the relationship
    between climate stress, agriculture, and diet in coastal Noakhali, alongside work on
    post-flood recovery and resilience in the Chittagong Hill Tracts.</p>
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
      <div><div class="num" data-count="50">50</div><div class="cap">Participants at the NSTU capacity building seminar with ICCCAD</div></div>
      <div><div class="num" data-count="32">32</div><div class="cap">Applicants to the 2026 volunteer cohort</div></div>
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
    <p>The flagship project, <em>Integrating Jhum Cultivation with Agroforestry, Contouring
    and Terracing through 3D Educational Tools to Enhance Climate Resilience in Chittagong
    Hill Tracts, Bangladesh</em>, uses physical 3D models and Bangla-language booklets to
    teach climate-resilient practice in hill schools and farming communities.</p>
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
        <div class="when">2024 &ndash; 2025</div>
        <div class="what"><strong>Jhum Revolution Campaign</strong>
        <span>Six-month programme funded by the ICCCAD Youth Innovative Fund</span>
        <p>Engaged over 250 students and established the organisation's first
        community-facing programmes in the CHT.</p></div>
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
        <span>IQAC, NSTU &mdash; 12 December 2024, with Independent University Bangladesh, ICCCAD, and the Embassy of Sweden &mdash; 50 participants</span></div>
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
      <!-- TODO: add WhatsApp if you want it public:
      <li><span class="lbl">WhatsApp</span> <a href="https://wa.me/8801XXXXXXXXX">+880 1XXX-XXXXXX</a></li> -->
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
    page("contact.html", "Contact | Sunanda Dewaan",
         "Get in touch with Sunanda Dewaan for research collaboration, programme partnerships, and speaking.", contact)
