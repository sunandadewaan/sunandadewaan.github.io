# Sunanda Dewaan — portfolio website

Six pages, plain HTML/CSS/JS. No build tools, no hosting cost.

## Files

| File | What it is |
|---|---|
| `index.html` | Home |
| `about.html` | About, education, skills |
| `work.html` | Career path, recognition, organisations |
| `research.html` | Research assistantships, current research, publications |
| `impact.html` | Jhum Revolution — reach, programme areas, activities |
| `article.html` | Full article: "Are Indigenous Communities in Bangladesh Victims of Climate Change?" (published 22 July 2026) |
| `recommendation-letter-nstu.pdf` | Letter of recommendation, linked from the Research page |
| `contact.html` | Contact details |
| `style.css` | All styling. Colours are at the top under `:root`. |
| `script.js` | Mobile menu + the counting-up numbers |
| `build.py` | Optional. Regenerates all six pages from one shared template. |

## Publish it free

**Netlify Drop — easiest, ~30 seconds**
1. Go to https://app.netlify.com/drop
2. Drag this whole folder onto the page
3. It goes live at a `something.netlify.app` address
4. Sign up (free) to rename it, e.g. `sunandadewaan.netlify.app`

**GitHub Pages — looks more professional on a CV**
1. Create a GitHub account
2. New repository named exactly `yourusername.github.io`
3. Upload every file in this folder
4. Settings → Pages → Source: `main` branch → Save
5. Live at `https://yourusername.github.io` within a few minutes

**Custom domain (optional, ~$10–12/year)**
Buy `sunandadewaan.com` from Namecheap or Cloudflare, then point it at
Netlify or GitHub Pages. Both support custom domains free, with free HTTPS.

## Editing

**Changing text:** open the `.html` file in any text editor and edit between the
tags. Everything marked `<!-- TODO: ... -->` is a gap waiting for your content.

**Adding your photo:**
1. Save a portrait as `portrait.jpg` in this folder (portrait orientation, at
   least 800px wide)
2. In `index.html`, find the block marked `photo-slot` and replace the whole
   `<div class="photo-slot">...</div>` with:
   `<img src="portrait.jpg" alt="Sunanda Dewaan">`

**Adding field photographs:** put the image files in this folder and add
`<img src="filename.jpg" alt="short description">` wherever you want them.
The `impact.html` page has a marked spot for these.

**Changing colours:** edit the hex values at the top of `style.css`.

**If you edit `build.py` instead:** run `python3 build.py` to regenerate all six
pages at once. Useful for changing the header, footer, or navigation, since
those live in one place in that file. If you edit the `.html` files directly,
don't run `build.py` afterwards — it will overwrite your changes.

## Before you publish — checklist

- [x] Add your photo
- [x] Add field photographs
- [ ] Add phone/WhatsApp on `contact.html` if you want it public
- [ ] Name the 2026 keynote event on `work.html`
- [ ] Add languages you speak, in the Skills section of `about.html`
- [ ] Add certifications and trainings to `about.html`
- [ ] Add any paid roles, internships, or consultancies to `work.html`
- [ ] Check that every number on `impact.html` is one you're happy to publish
- [ ] Rewrite the About paragraphs in your own words
- [ ] Make a 1200×630 image named `og-image.png` for link previews, then
      uncomment the `og:image` line in each page's `<head>`
