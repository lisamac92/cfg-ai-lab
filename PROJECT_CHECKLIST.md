# CFG AI Lab — Project Checklist
**Last updated:** 25 April 2025
**GitHub:** https://github.com/lisamac92/cfg-ai-lab (public, branch: main)

---

## ✅ COMPLETED

### Core Pages
- [x] `index.html` — AI Lab with three interactive product tables (Table 01, 02, 03)
- [x] `homepage.html` — ClickFlowGrow homepage with animated hero, 5Fs section, scan band, AI Lab showcase
- [x] `opportunity-scan.html` — AI Opportunity Scan Act 1 (11-question conversational form)
- [x] `scan-results.html` — AI Opportunity Scan Acts 2 & 3 (personalised results + three pathways)

### AI Lab — Table 01: AI Receptionist
- [x] Live chat demo with scenario selector (restaurant, accountant, trades, dental)
- [x] Aria voice AI widget embedded (GHL widget ID: `69b2e92d6a7fada2ec2e45f7`)
- [x] Pulsing teal rings around widget, shadow DOM styling
- [x] Step 1 / Step 2 / Step 3 layout with mint green dividers
- [x] Lead capture → GHL via `/api/ghl-capture`

### AI Lab — Table 02: AI Prospecting
- [x] Live lead generation (role + industry + location dropdowns)
- [x] 5 AI-generated hyper-realistic UK leads with masked emails
- [x] One-click enrichment: company insight + personalised opening line + copy button
- [x] Intelligence brief generator
- [x] Lead capture → GHL
- [x] "Talk to an AI Builder →" CTA → GHL calendar ✅ WIRED

### AI Lab — Table 03: AI Workflow Audit
- [x] Business type selector (restaurant, accountant, dental, estate agent)
- [x] Animated workflow visualisation
- [x] Live chat via OpenAI with scenario-specific AI personas
- [x] Lead capture → GHL
- [x] "Book a free Workflow Audit →" CTA → GHL calendar ✅ WIRED

### AI Lab — AI Builder View
- [x] Alex portrait + iPad-style contact form
- [x] Interest chip selector (AI Receptionist, AI Prospecting, AI Workflows, Not sure yet, All of it)
- [x] Form submission → GHL contact creation
- [x] "Speak to an AI Builder" nav + lobby CTAs → AI Builder view

### AI Opportunity Scan
- [x] Act 1: 11-question conversational form (one at a time, animated transitions, progress bar)
- [x] Magic wand question: "If you could wave a magic wand, what's the one thing you'd want AI to fix in your business today?" — free text, Q11
- [x] Contact capture screen (first name, last name, email, phone optional)
- [x] 6-step loading animation with F-dimension labels
- [x] Scoring logic: each F scored 0–100 from answer combinations
- [x] Redirect to scan-results.html with URL params
- [x] Act 2: 5F Signal Strength visual (signal bars, colour-coded green/amber/red)
- [x] Act 2: Magic wand callout — their words reflected back prominently
- [x] Act 2: 2–3 personalised AI idea stories based on lowest-scoring Fs
- [x] Act 2: "Ask Sam before you wake Sam" story (Fulfil)
- [x] Act 2: "11pm Sunday plumber" story (Be Found)
- [x] Act 2: Magic wand dedicated idea card
- [x] Act 2: "See more ideas" expandable section
- [x] Act 3: Three pathways — Try it live (AI Lab), Book a call (GHL calendar), See more ideas
- [x] Backend: `/api/opportunity-scan` endpoint

### Backend API (api_server.py)
- [x] `/api/leads` — live lead generation
- [x] `/api/enrich` — lead enrichment
- [x] `/api/intelligence` — intelligence brief (legacy, kept for compatibility)
- [x] `/api/chat` — workflow chat (Table 03)
- [x] `/api/ghl-capture` — AI Lab lead capture → GHL contact upsert + follow-up email
- [x] `/api/opportunity-scan` — scan submission → GHL contact + opportunity + note
- [x] `/api/voice-webhook` — post-call transcript processing + GPT extraction
- [x] `/api/poll-call-data` — voice call session polling

### GHL Integration
- [x] MCP connection: `manus-cfg-sales` server, Location ID `E4vxxqsZzDt35YcgEH2d`
- [x] Contact upsert on all form submissions
- [x] Tags applied on scan submissions (biz type, team size, bottleneck)
- [x] Opportunity created in "Leads → Sales Pipeline" at "Engaged Lead" stage
- [x] Magic wand answer saved as note on contact record
- [x] Follow-up emails sent via GHL conversations (Tables 01–03)
- [x] Calendar created: "AI-Driven Business Growth"
- [x] Booking URL wired across all pages: `https://link.clickflowgrow.com/widget/booking/1oQg9EeqtweL4ewewqP7`

### Homepage
- [x] Animated orb hero with data-pulse canvas animation
- [x] Trust bar
- [x] 5Fs framework section — five cards with v2 photography backgrounds (90% opacity)
- [x] AI Opportunity Scan band (between 5Fs and AI Lab sections)
- [x] AI Lab showcase section
- [x] How it works (3 steps)
- [x] Testimonials / social proof
- [x] CTA band with live booking link
- [x] Footer

### Assets
- [x] Homepage hero background (`homepage_hero_bg_web.jpg`)
- [x] 5Fs photography cards v2 (all five: formulate, befound, find, fulfil, fanfare)
- [x] GHL calendar banner (`calendar_banner_web.jpg` — 112KB, upload-ready)
- [x] GHL calendar logo (`calendar_logo_web.jpg` — 16KB, upload-ready)

### Version Control
- [x] GitHub repo: `github.com/lisamac92/cfg-ai-lab` (public, branch: main)
- [x] All files committed and pushed — checkpoint 25 April 2025

---

## ⏳ PENDING — Requires User Input

### Stripe / Pricing Links
- [ ] Table 01 — AI Receptionist: add Stripe product link to pricing CTA (currently no link)
- [ ] Table 02 — AI Prospecting: add Stripe product link to pricing CTA
- [ ] Table 03 — AI Workflow Audit: add Stripe product link to pricing CTA
- *Waiting on: user to create Stripe products and provide URLs*

### GHL Calendar Setup (user actions in GHL UI)
- [ ] Upload `calendar_banner_web.jpg` as calendar banner (Settings → Calendars → AI-Driven Business Growth)
- [ ] Upload `calendar_logo_web.jpg` as calendar profile image
- [ ] Set calendar availability hours and buffer times
- [ ] Write confirmation email copy (can be drafted on request)
- [ ] Write reminder SMS/email copy (can be drafted on request)

### Production Deployment
- [ ] Choose a host (Netlify, Vercel, Railway, or VPS — e.g. `ailab.clickflowgrow.com`)
- [ ] Set up CI/CD from GitHub → host
- [ ] Update all GHL email templates with production domain (currently sandbox URLs)

---

## 🔮 FUTURE PHASES (not started)

### GHL Conversation AI — Site-wide Chat Widget
- User wants a site-wide AI "salesperson/guide" chat widget
- Will use GHL Conversation AI (native, not third-party)
- The Opportunity Scan is the interim solution until this is built
- Requires: GHL Conversation AI setup, knowledge base, bot persona

### Additional GHL Calendars
- "New Client Onboarding" calendar (post-purchase)
- "Client Meetings" calendar (existing clients e.g. Bureau Veritas)
- Shared availability pool across all three calendars
- Sync to master Google Calendar

### GHL Workflow Automations (UI-only — cannot be built via MCP)
- "New scan submission" notification workflow
- "Engaged Lead" pipeline follow-up sequence
- Review request automation (post-service Google Review request)
- Voice AI post-call workflow (trigger: "Voice AI Call Ended" → webhook → `/api/voice-webhook`)

### AI Lab Future Tables
- Table 04 — AI Reviews (Google Review automation demo)
- Table 05 — AI Onboarding (client onboarding automation demo)

### Other
- Prompt library (separate project — do NOT build into current site)
- Blog / content section on homepage
- Case studies page

---

## 🔗 Key Reference Values

| Item | Value |
|---|---|
| GHL MCP Server | `manus-cfg-sales` |
| GHL Location ID | `E4vxxqsZzDt35YcgEH2d` |
| GHL Pipeline ID | `q6uFBb0ktjT1AO8gGmMX` (Leads → Sales Pipeline) |
| GHL Engaged Lead Stage | `caaa2dae-60c9-49a4-aa8e-bdda831bd5d6` |
| GHL Voice Widget ID | `69b2e92d6a7fada2ec2e45f7` |
| GHL Booking URL | `https://link.clickflowgrow.com/widget/booking/1oQg9EeqtweL4ewewqP7` |
| GHL From Email | `hello@clickflowgrow.com` |
| Meta Pixel ID | `955639412997577` |
| Brand teal | `#00d4aa` |
| Brand amber-gold (AI Lab) | `#EC8A01` |
| GitHub repo | https://github.com/lisamac92/cfg-ai-lab |

---

## 📁 Key Files

| File | Purpose |
|---|---|
| `index.html` | AI Lab — all three tables + AI Builder view |
| `homepage.html` | ClickFlowGrow homepage |
| `opportunity-scan.html` | AI Opportunity Scan — Act 1 (form) |
| `scan-results.html` | AI Opportunity Scan — Acts 2 & 3 (results) |
| `api_server.py` | Flask backend — all API endpoints |
| `README.md` | Full project documentation and design system |
| `PROJECT_CREDENTIALS.md` | Key credentials (Meta Pixel, GHL settings) |
| `GHL_SETUP_GUIDE.md` | Step-by-step GHL configuration guide |
| `CFG_WEBSITE_AUDIT.md` | Audit notes on current ClickFlowGrow.com website |
| `ARIA_PROMPT.md` | GHL Voice AI system prompt for Aria |
| `email_t1.html` | Follow-up email: AI Receptionist table |
| `email_t2.html` | Follow-up email: AI Prospecting table |
| `email_t3.html` | Follow-up email: AI Workflow Audit table |

---

## Brand Rules (non-negotiable)

- Always **ClickFlow Grow** or **ClickFlowGrow** — never "GHL" in user-facing content
- Always **UK English** — colour not color, organised not organized, fulfil not fulfill
- **Fulfil** not "Be Full" for F4 of the 5Fs framework
- No Manus branding anywhere on the site
- Dark navy/teal aesthetic throughout — no light themes
