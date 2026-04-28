# CFG AI Lab — ClickFlow Grow
**GitHub:** https://github.com/lisamac92/cfg-ai-lab (public, branch: `main`)
**Last checkpoint:** 25 April 2025

---

## What this project is

A premium, dark-themed interactive website for ClickFlow Grow — showcasing AI solutions for UK SME business owners. Built in vanilla HTML/CSS/JavaScript with a Python Flask backend. Three main pages:

1. **AI Lab** (`index.html`) — interactive product showroom with three live demo tables
2. **Homepage** (`homepage.html`) — ClickFlowGrow.com homepage with animated hero and 5Fs framework
3. **AI Opportunity Scan** (`opportunity-scan.html` + `scan-results.html`) — three-act lead generation journey

---

## Design System

| Token | Value |
|---|---|
| Background | `#0a0f1e` (deep navy) |
| Card background | `#111827` |
| Accent | `#00d4aa` (teal) |
| Accent dark | `#00a88a` |
| White | `#ffffff` |
| Grey | `#94a3b8` |
| Fonts | Inter (body), Manrope (headings) |
| Border | `rgba(0, 212, 170, 0.2)` |

---

## Pages & Status

### index.html — AI Lab
Three interactive product tables, each a full immersive demo experience:

- **Table 01 — AI Receptionist:** Live chat demo with scenario selector (restaurant, accountant, trades, dental). Aria voice AI widget embedded. Lead capture form (Alex iPad screen) → GHL via `/api/ghl-capture`.
- **Table 02 — AI Prospecting:** Live lead generation (role + industry + location), lead enrichment with personalised outreach copy, intelligence brief generator. Lead capture → GHL.
- **Table 03 — AI Workflows:** Chat-based workflow audit with scenario selector. Lead capture → GHL.

**Booking CTAs wired:**
- "Talk to an AI Builder →" (Table 02) → GHL calendar
- "Book a free Workflow Audit →" (Table 03) → GHL calendar
- "Speak to an AI Builder" (nav + lobby) → internal Alex contact form → GHL

**Status:** ✅ Complete and committed

---

### homepage.html — ClickFlowGrow Homepage
- Animated orb hero with data-pulse canvas animation
- Trust bar
- 5Fs framework section — five cards with real photography backgrounds (v2 images at 90% opacity), two-part card layout (top label + bottom content)
- **AI Opportunity Scan band** — full-width section between 5Fs and AI Lab showcase, with preview card showing example signal bars
- AI Lab showcase section
- How it works (3 steps)
- Testimonials / social proof
- CTA band with booking link
- Footer

**Status:** ✅ Complete and committed

---

### opportunity-scan.html — AI Opportunity Scan (Act 1)
Conversational 11-question form — one question at a time with smooth slide animations.

**Question structure:**
| Q | Topic | F-dimension |
|---|---|---|
| 1 | Business type | Formulate |
| 2 | Team size | Formulate |
| 3 | Biggest bottleneck | Formulate |
| 4 | Online visibility | Be Found |
| 5 | Out-of-hours availability | Be Found |
| 6 | Lead follow-up speed | Find |
| 7 | Repetitive questions (interruptions) | Fulfil |
| 8 | Repetitive tasks (manual processes) | Fulfil |
| 9 | Google Reviews process | Fanfare |
| 10 | How clients refer you | Fanfare |
| 11 | **Magic wand question** (free text) | The Big One |

After Q11: contact capture screen (first name, last name, email, phone optional) → 6-step loading animation → redirect to `scan-results.html` with URL params.

**Scoring logic:** Each F scored 0–100 based on answer combinations. Passed as URL params: `?name=&f1=&f2=&f3=&f4=&f5=&magic=&bottleneck=&team=&biz=`

**Status:** ✅ Complete and committed

---

### scan-results.html — AI Opportunity Scan (Acts 2 & 3)
Personalised results page — reads URL params and builds everything dynamically.

**Sections:**
1. **Magic wand callout** — their exact words reflected back prominently at the top
2. **5F Signal Strength** — five visual signal bar columns (like mobile signal bars), colour-coded: green (strong, 70+), amber (moderate, 45–69), red (gap, <45). Weakest F highlighted with red border, strongest with green border.
3. **AI idea stories** — 2 stories based on the two lowest-scoring Fs, plus a dedicated card for their magic wand answer. Stories written in plain English with real examples ("Ask Sam before you wake Sam" for Fulfil, "11pm Sunday plumber" for Be Found, etc.)
4. **"See more ideas"** — expandable section with additional AI use cases for remaining Fs
5. **Three pathways:**
   - Try it live → `index.html` (AI Lab)
   - Book a free call → GHL calendar (featured/recommended)
   - See more ideas → scrolls to expandable section

**Status:** ✅ Complete and committed

---

## Backend — api_server.py (Flask)

| Endpoint | Purpose |
|---|---|
| `POST /api/leads` | AI Prospecting: generate 5 UK B2B leads |
| `POST /api/enrich` | AI Prospecting: enrich a single lead |
| `POST /api/intelligence` | Legacy intelligence brief (kept for compatibility) |
| `POST /api/chat` | AI Workflow chat (Table 03) |
| `POST /api/ghl-capture` | AI Lab lead capture → GHL contact upsert + email |
| `POST /api/opportunity-scan` | Scan submission → GHL contact + opportunity + note |
| `POST /api/voice-webhook` | Receives post-call transcript from GHL workflow |
| `GET /api/poll-call-data` | Polls for voice call data by session ID |

**Status:** ✅ All endpoints complete and committed

---

## GHL Integration

| Setting | Value |
|---|---|
| MCP Server name | `manus-cfg-sales` |
| Location ID | `E4vxxqsZzDt35YcgEH2d` |
| Pipeline | "Leads → Sales Pipeline" (ID: `q6uFBb0ktjT1AO8gGmMX`) |
| Engaged Lead stage | ID: `caaa2dae-60c9-49a4-aa8e-bdda831bd5d6` |
| Calendar | AI-Driven Business Growth |
| Booking URL | `https://link.clickflowgrow.com/widget/booking/1oQg9EeqtweL4ewewqP7` |
| From email | `hello@clickflowgrow.com` |

**What the scan endpoint does in GHL:**
1. Upserts contact with tags: `ai-opportunity-scan`, `cfg-ai-lab-event`, `biz-{type}`, `team-{size}`, `bottleneck-{type}`
2. Creates opportunity in Leads → Sales Pipeline at Engaged Lead stage
3. Saves a note with business type, team size, bottleneck, and magic wand answer in their own words

---

## Key Credentials & Assets

| Item | Location / Value |
|---|---|
| Meta Pixel ID | `955639412997577` |
| Full credentials | `PROJECT_CREDENTIALS.md` |
| GHL setup guide | `GHL_SETUP_GUIDE.md` |
| Project checklist | `PROJECT_CHECKLIST.md` |
| Website audit notes | `CFG_WEBSITE_AUDIT.md` |
| Hero background | `homepage_hero_bg_web.jpg` |
| 5Fs card images | `5f_formulate_v2.jpg`, `5f_befound_v2.jpg`, `5f_find_v2.jpg`, `5f_fulfil_v2.jpg`, `5f_fanfare_v2.jpg` |
| GHL calendar banner | `calendar_banner_web.jpg` (112KB, upload-ready) |
| GHL calendar logo | `calendar_logo_web.jpg` (16KB, upload-ready) |

---

## The 5Fs Framework

| F | Full name | Meaning |
|---|---|---|
| F1 | Formulate | Business foundations, systems, knowledge |
| F2 | Be Found | Online visibility, Google, out-of-hours availability |
| F3 | Find | Lead generation, follow-up speed, prospecting |
| F4 | Fulfil | Delivering services, internal processes, team efficiency |
| F5 | Fanfare | Google Reviews, referrals, word of mouth |

> **Important:** F4 is "Fulfil" (delivering services/products to clients) — NOT "Be Full". Always use "Fulfil".

---

## Booking Links — Where They Live

| Page | Button | URL |
|---|---|---|
| index.html | "Talk to an AI Builder →" (Table 02) | GHL calendar |
| index.html | "Book a free Workflow Audit →" (Table 03) | GHL calendar |
| index.html | "Speak to an AI Builder" (nav + lobby) | Internal Alex form → GHL |
| homepage.html | "Book a call" (footer CTA band) | GHL calendar |
| scan-results.html | Sticky header "Book a call" | GHL calendar |
| scan-results.html | "Book a free call" featured pathway | GHL calendar |

---

## What's Still To Do

| Item | Status | Notes |
|---|---|---|
| Table 01 — AI Receptionist Stripe/pricing link | ⏳ Pending | Needs Stripe product URL from user |
| Table 02 — AI Prospecting Stripe/pricing link | ⏳ Pending | Needs Stripe product URL from user |
| Table 03 — AI Workflow Audit Stripe/pricing link | ⏳ Pending | Needs Stripe product URL from user |
| GHL Conversation AI site-wide chat widget | 🔮 Future phase | User wants a site-wide AI salesperson/guide — not yet built |
| GHL calendar banner + logo upload | ⏳ User action | Files ready: `calendar_banner_web.jpg`, `calendar_logo_web.jpg` |
| GHL confirmation + reminder email copy | ⏳ Optional | Drafted on request — boosts show-up rates |

---

## Running the Preview Server

```bash
cd /home/ubuntu/ai_lab_styled
python3 -m http.server 8080
```

Then expose port 8080 via the Manus expose tool.

For the Flask backend (API endpoints):
```bash
cd /home/ubuntu/ai_lab_styled
python3 api_server.py
```

---

## Brand Rules (non-negotiable)

- Always **ClickFlow Grow** or **ClickFlowGrow** — never "GHL" in user-facing content
- Always **UK English** — colour not color, organised not organized, etc.
- **Fulfil** not "Be Full" for F4
- No Manus branding anywhere on the site
- Dark navy/teal aesthetic — no light themes
