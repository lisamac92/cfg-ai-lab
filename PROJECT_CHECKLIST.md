# CFG AI Lab — Project Checklist
**Last updated:** March 2026  
**Live URL:** https://8080-idglvrmshignkf4wht6zv-6a341fe9.us2.manus.computer

---

## ✅ DONE — Completed This Session

- [x] **Entrance door animation** — Glass doors with AI-generated interior image, people at tables visible through frosted glass
- [x] **Door-open cinematic transition** — Doors slide apart, interior zooms forward, warm amber wash fades to dark navy
- [x] **Brand colour update** — All `#F07A5A` copper replaced with `#EC8A01` amber-gold throughout
- [x] **Table lobby cards redesigned** — AI-generated overhead table photos replace flat SVG placards
- [x] **Home nav link** — Added to main navigation bar
- [x] **Email capture bars wired to GHL** — All four bars (Tables 01, 02, 03 + DemoDrop) create contacts in GHL CRM
- [x] **AI Builder page** — "Speak to an AI Builder" Genius Bar page with Alex portrait, iPad-style form, chip interest selector, GHL-wired submit
- [x] **All "Speak to an AI Builder" CTAs** — Nav, hero, and table buttons all navigate to the AI Builder page
- [x] **Flask server serves static + API on port 8080** — Unified server, no separate static file server needed

---

## 🔴 HIGH PRIORITY — Must Do Before Event

### 1. GHL Voice AI Integration (Table 01 — AI Receptionist)
**Context:** The YouTube video (https://youtu.be/mAcsHilWPjc) shows a "DemoDrop" system where:
- A contact is dragged into a GHL pipeline stage
- GHL automation scrapes their website and builds a knowledge base
- A personalised demo page is created with a live AI chat + **voice agent** for their specific business
- An email is sent to the prospect with a link to their live demo

**What this means for the AI Lab:**
- [ ] **Replace the pre-recorded audio demo** in Table 01 Step 2 with a **live GHL Voice AI call** — visitor types their business name, clicks a button, and can actually *call* the AI receptionist or have it call them
- [ ] **Set up GHL Voice AI agent** in the ClickFlowGrow sub-account (Automation → AI Agents → Voice AI)
- [ ] **Configure the DemoDrop pipeline automation** — when a contact is created from Table 01, trigger a GHL workflow that scrapes their website and personalises the voice agent greeting
- [ ] **Wire the "Hear Aria greet your callers" button** to trigger a live outbound call via GHL Voice AI API or a Twilio number connected to GHL

### 2. Booking Calendar Links
- [ ] **Get the GHL booking calendar URL** for "Speak to an AI Builder" appointments
- [ ] **Replace all placeholder `#` hrefs** on "Speak to an AI Builder" buttons with the real calendar link
- [ ] **Add the calendar link** to the AI Builder page as an alternative CTA ("Or book a call directly →")

### 3. Stripe Payment Link
- [ ] **Get the Stripe payment link** for the £600 AI Receptionist activation
- [ ] **Replace the placeholder** `https://buy.stripe.com/placeholder` in the DemoDrop activation panel
- [ ] **Confirm pricing copy** — currently shows "£600 setup + £499/month"

### 4. Deploy to Production Domain
- [ ] **Push to GitHub** — commit all current changes to the repo
- [ ] **Deploy to a permanent URL** (e.g. `ailab.clickflowgrow.com` or similar)
- [ ] **Update GHL email templates** — replace any localhost/sandbox URLs with the production domain
- [ ] **Test all GHL email sends** from the production domain

---

## 🟡 MEDIUM PRIORITY — Polish Before Event

### 5. Table 01 — AI Receptionist Improvements
- [ ] **Step 2 "Make it yours"** — The business name input currently generates a text greeting. Consider replacing with a live GHL Voice AI call (see item 1 above)
- [ ] **Industry tabs** — Currently 5 industries. Confirm these are the right ones for the target audience
- [ ] **Audio files** — Confirm the pre-recorded demo calls are final and correctly matched to each industry tab

### 6. Table 02 — AI Prospecting Improvements
- [ ] **Email send** — Currently sends a generic "AI Prospecting Brief" email. Consider making the email body include the actual intelligence brief that was generated on screen
- [ ] **"My key sales trigger is..."** placeholder text — confirm this is clear enough for event visitors

### 7. Table 03 — AI Workflows Improvements
- [ ] **Scenario tabs** — Currently Plumber / Accountant / Restaurant. Confirm these are the right demos for the audience
- [ ] **"Get your booking confirmation" email** — Confirm the email template content is correct

### 8. DemoDrop Experience
- [ ] **Test the full DemoDrop flow** — business name + website → AI greeting generation → activation panel
- [ ] **Activation panel copy** — Confirm "£600 setup + £499/month" pricing is correct
- [ ] **DemoDrop email** — Confirm the personalised demo email template is set up in GHL

### 9. AI Builder Page
- [ ] **Add a direct calendar booking link** as an alternative to the form ("Prefer to book a call? →")
- [ ] **Confirm "Alex" name and bio** — or replace with the real team member's name/photo
- [ ] **Test the GHL contact creation** from the AI Builder form with real data

---

## 🟢 NICE TO HAVE — Post-Event Improvements

### 10. Analytics & Tracking
- [ ] **Add Google Analytics or GHL tracking** to measure which tables get the most engagement
- [ ] **Track email capture conversion rate** per table
- [ ] **Track AI Builder form submissions** vs. page views

### 11. Mobile Optimisation
- [ ] **Test on mobile devices** — the entrance glass door and table cards need to look great on phones
- [ ] **Adjust font sizes** for smaller screens
- [ ] **Test the iPad form layout** on mobile

### 12. Performance
- [ ] **Compress the AI-generated images** — interior_bg.jpg, table01/02/03_surface.jpg, ai_builder.jpg are likely large
- [ ] **Add lazy loading** to the table surface images
- [ ] **Test page load speed** on a mobile connection

### 13. Content Review
- [ ] **Proofread all copy** across all tables and the AI Builder page
- [ ] **Confirm the "ClickFlow Grow" branding** is consistent throughout
- [ ] **Review the email templates** (email_t1.html, email_t2.html, email_t3.html) for content and design

---

## 📋 KEY CONTEXT — GHL Voice AI Demo Strategy

From the YouTube video **"How to Make $10K/Month Selling AI Agents with 10 Second Demos in GoHighLevel"**:

> The presenter's system automatically identifies businesses missing web chat or after-hours answering. By dragging a contact in the GHL pipeline, the system scrapes the prospect's website to build a knowledge base, then instantly creates a personalised demo page with a functional AI chat **and voice agent**. An email is sent to the prospect with a link to this live, interactive demo.

**How this applies to the AI Lab:**
The DemoDrop experience (Table 01 Step 3 + the DemoDrop room) is already built around this concept — visitor enters their business name and website, we generate a personalised AI receptionist. The missing piece is replacing the text-based output with a **live GHL Voice AI call** so the visitor can actually *hear* the AI answering calls for their business in real time.

**GHL Voice AI setup path:**
1. GHL sub-account → Automation → AI Agents → Voice AI
2. Create a new Voice AI agent with a dynamic prompt that uses the scraped knowledge base
3. Connect to a Twilio number (or use GHL's built-in calling)
4. Trigger via GHL workflow when a contact is created from the AI Lab
5. Use the GHL API to initiate an outbound call from the lab interface

---

## 🔗 KEY LINKS & IDs

| Item | Value |
|---|---|
| GHL Location ID | `E4vxxqsZzDt35YcgEH2d` |
| GHL Pipeline (AI Lab leads) | `q6uFBb0ktjT1AO8gGmMX` (Leads → Sales Pipeline) |
| GHL Pipeline Stage (new leads) | `1e353e29-7d12-48b3-ba00-51c2d250cb98` (New Lead) |
| Live URL (sandbox) | https://8080-idglvrmshignkf4wht6zv-6a341fe9.us2.manus.computer |
| YouTube reference | https://youtu.be/mAcsHilWPjc |
| Brand colour (amber-gold) | `#EC8A01` |
| Brand colour (teal) | `#0BEAB5` |
| Stripe payment link | **PLACEHOLDER — needs replacing** |
| Booking calendar URL | **PLACEHOLDER — needs replacing** |
