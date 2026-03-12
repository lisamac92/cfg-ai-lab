# CFG AI Lab — Project Checklist
**Last updated:** March 2026  
**Live URL (sandbox):** https://8080-idglvrmshignkf4wht6zv-6a341fe9.us2.manus.computer  
**GitHub:** https://github.com/lisamac92/cfg-ai-lab

---

## ✅ DONE — Completed

- [x] Entrance door animation — glass doors, cinematic zoom, amber wash to dark navy
- [x] Brand colour update — `#EC8A01` amber-gold throughout
- [x] Table lobby cards — AI-generated overhead table photos
- [x] Home nav link added to main navigation
- [x] Email capture bars wired to GHL CRM (all 4 bars)
- [x] AI Builder page — Alex portrait, iPad-style form, chip interest selector, GHL-wired submit
- [x] All "Speak to an AI Builder" CTAs wired to AI Builder page
- [x] Flask server — unified static + API on port 8080
- [x] HTML structure fix — view-table-2 and view-table-3 nesting bug resolved
- [x] GHL Voice AI widget embedded in Table 01 Step 3
- [x] Shadow DOM injection — avatar hidden, pill styled dark navy with teal border
- [x] Pulsing teal rings around the Talk to Aria widget
- [x] Mint green divider lines between Step 1 / Step 2 / Step 3
- [x] Widget pill properly sized — 380×72px, white text, large mic button

---

## 🔴 TIER 1 — Blockers (must do before event)

### 1. Production Deployment
- [ ] **Choose a host** — Netlify, Vercel, Railway, or VPS (e.g. `ailab.clickflowgrow.com`)
- [ ] **Set up GitHub Actions CI/CD** — Manus to add workflow so every push to `main` auto-deploys
- [ ] **Update all GHL email templates** — replace sandbox URLs with production domain
- [ ] **Test all GHL email sends** from production domain

### 2. GHL Booking Calendar URL
- [ ] **Get the GHL calendar URL** for "Speak to an AI Builder" appointments
- [ ] **Send to Manus** — will wire into all "Book a call" buttons in ~5 minutes

### 3. Stripe Payment Link
- [ ] **Get the Stripe payment link** for £600 AI Receptionist activation
- [ ] **Send to Manus** — will replace placeholder `https://buy.stripe.com/placeholder`
- [ ] **Confirm pricing** — currently shows "£600 setup + £499/month"

---

## 🟠 TIER 2 — Voice AI Loop (flagship feature)

### 4. GHL Voice AI Agent Setup (You — ~5 mins)
- [ ] Go to GHL → Automation → AI Agents → Voice AI → + Create New
- [ ] Agent name: `Aria — AI Receptionist Demo`
- [ ] Paste full prompt from `ARIA_PROMPT.md`
- [ ] Choose a female voice (e.g. Nicole or Sarah)
- [ ] Save and confirm widget ID `69b2e92d6a7fada2ec2e45f7` is linked

### 5. Session ID + Polling JS (Manus — ~20 mins)
- [ ] Add UUID generation to the widget embed so each browser session gets a unique ID
- [ ] Pass session ID as a custom variable to the GHL widget
- [ ] Start polling `/api/poll-call-data` when widget loads
- [ ] Auto-fill the booking form below the widget when call data arrives

### 6. Post-Call GHL Workflow Webhook (You — ~10 mins in GHL)
- [ ] Create a GHL Workflow: trigger = "Voice AI Call Ended"
- [ ] Add action: "Send Webhook" → POST to `{production_url}/api/voice-webhook`
- [ ] Payload must include: `transcript`, `session_id`, `contact_id`
- [ ] The server will parse the transcript with GPT, extract contact details, upsert in CRM, and store for polling

---

## 🟡 TIER 3 — Table Improvements (polish before event)

### 7. Table 01 — AI Receptionist
- [ ] **Confirm industry tabs** — currently Plumbing / Law / Estate Agency — right for the audience?
- [ ] **Confirm audio files** — pre-recorded demo calls final and matched to each industry?
- [ ] **Step 2 business name input** — currently generates a text greeting; consider upgrading to live voice call

### 8. Table 02 — AI Prospecting (IN PROGRESS)
- [ ] **Review and improve the full Table 02 experience**
- [ ] **Email body improvement** — update email_t2.html to include the actual intelligence brief generated on screen
- [ ] **"My key sales trigger is..."** placeholder — confirm wording is clear for event visitors
- [ ] **Step 3 result display** — review design and copy quality

### 9. Table 03 — AI Workflows
- [ ] **Confirm scenario tabs** — Plumber / Accountant / Restaurant — right for the audience?
- [ ] **"Get your booking confirmation" email** — confirm email_t3.html content is correct

### 10. DemoDrop Experience
- [ ] **Test the full DemoDrop flow** — business name + website → AI greeting → activation panel
- [ ] **Confirm pricing copy** — "£600 setup + £499/month"
- [ ] **DemoDrop email** — confirm personalised demo email template is set up in GHL

### 11. AI Builder Page
- [ ] **Confirm "Alex" name and photo** — or replace with real team member
- [ ] **Add direct calendar booking link** as alternative CTA ("Prefer to book a call? →")
- [ ] **Test GHL contact creation** from AI Builder form with real data

---

## 🟢 TIER 4 — Nice to Have (post-event)

### 12. Analytics & Tracking
- [ ] Add Google Analytics or GHL tracking pixel
- [ ] Track email capture conversion rate per table
- [ ] Track AI Builder form submissions vs. page views

### 13. Mobile Optimisation
- [ ] Test entrance animation on mobile
- [ ] Adjust font sizes for smaller screens
- [ ] Test iPad form layout on mobile

### 14. Performance
- [ ] Compress large images (interior_bg.jpg, table0x_surface.jpg, ai_builder.jpg)
- [ ] Add lazy loading to table surface images
- [ ] Test page load speed on mobile connection

### 15. Content Review
- [ ] Proofread all copy across all tables and AI Builder page
- [ ] Confirm "ClickFlow Grow" branding is consistent throughout
- [ ] Review all three email templates (email_t1/t2/t3.html)

---

## 🔗 Key Links & IDs

| Item | Value |
|---|---|
| GHL Location ID | `E4vxxqsZzDt35YcgEH2d` |
| GHL Pipeline (AI Lab leads) | `q6uFBb0ktjT1AO8gGmMX` |
| GHL Pipeline Stage (new leads) | `1e353e29-7d12-48b3-ba00-51c2d250cb98` |
| GHL Voice Widget ID | `69b2e92d6a7fada2ec2e45f7` |
| Live URL (sandbox) | https://8080-idglvrmshignkf4wht6zv-6a341fe9.us2.manus.computer |
| GitHub repo | https://github.com/lisamac92/cfg-ai-lab |
| Brand colour (amber-gold) | `#EC8A01` |
| Brand colour (teal) | `#0BEAB5` |
| Stripe payment link | **PLACEHOLDER — needs replacing** |
| Booking calendar URL | **PLACEHOLDER — needs replacing** |
