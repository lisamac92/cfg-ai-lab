# GHL Workflow Setup Guide — AI Opportunity Scan Follow-Up
## ClickFlowGrow CRM
## Last updated: 1 May 2026 — all field keys verified against live GHL custom fields

---

## Status Checklist

- [x] Pipeline created: **AI Opportunity Scan** (7 stages)
- [x] Calendar created: **AI Discovery Call** — https://link.clickflowgrow.com/widget/booking/4zgS77DacE6RnoPTJ4WL
- [x] Custom fields created (all 9 — see table below)
- [ ] Workflow built (follow Steps 1–5 below)

---

## Custom Fields Reference

All 9 fields are live in ClickFlowGrow. Use these exact merge tags in your workflow messages:

| Field Name | GHL Merge Tag | Type | Contains |
|---|---|---|---|
| Scan Bottleneck | `{{contact.scan_bottleneck}}` | Text | Their biggest business challenge |
| Scan Business Type | `{{contact.scan_business_type}}` | Text | Type of business |
| Scan Team Size | `{{contact.scan_team_size}}` | Text | Number of people in the business |
| Scan Magic Wand | `{{contact.scan_magic_wand}}` | Text | What they'd fix if they could wave a magic wand |
| Scan F1 Formulate | `{{contact.scan_f1_formulate}}` | Number | Formulate score (0–100) |
| Scan F2 Be Found | `{{contact.scan_f2_be_found}}` | Number | Be Found score (0–100) |
| Scan F3 Find | `{{contact.scan_f3_find}}` | Number | Find score (0–100) |
| Scan F4 Fulfil | `{{contact.scan_f4_fulfil}}` | Number | Fulfil score (0–100) |
| Scan F5 Fanfare | `{{contact.scan_f5_fanfare}}` | Number | Fanfare score (0–100) |

These fields are populated automatically when someone submits the scan on clickflowgrow.com.

---

## Step 1 — Create the Workflow

Go to **Automation → Workflows → + New Workflow → Start from Scratch**

Name it: `AI Opportunity Scan — Follow-Up`

---

## Step 2 — Set the Trigger

**Trigger:** Contact Tag Added
**Tag value:** `ai-opportunity-scan`

This fires the moment someone completes the scan on the website.

---

## Step 3 — Add Workflow Actions (in order)

### Action 1: Create Opportunity
- **Pipeline:** AI Opportunity Scan
- **Stage:** New Scan Lead
- **Opportunity Name:** `{{contact.first_name}} — AI Scan`
- **Assigned To:** Your user

### Action 2: Wait
- **Duration:** 2 minutes
*(Gives the results page time to load before the first message arrives)*

### Action 3: Send Email
- **Subject:** `Your AI Opportunity Scan results, {{contact.first_name}}`
- **From:** hello@clickflowgrow.com
- **Content:** Set to **"AI will fill this field"**
- **AI Instructions for this email:**

> *Write a warm, personal email to {{contact.first_name}} who has just completed the AI Opportunity Scan on clickflowgrow.com. Their biggest bottleneck is {{contact.scan_bottleneck}}. Their business type is {{contact.scan_business_type}}. Their team size is {{contact.scan_team_size}}. Their magic wand answer was: "{{contact.scan_magic_wand}}".*
>
> *Write 3 short paragraphs: (1) acknowledge what they shared and validate it — make them feel understood, (2) give them one specific, concrete insight about what AI could do for their type of business based on their bottleneck, (3) invite them to book a free 30-minute discovery call at https://link.clickflowgrow.com/widget/booking/4zgS77DacE6RnoPTJ4WL.*
>
> *Tone: warm, direct, no jargon. UK English. Sign off as Alex from ClickFlowGrow.*

### Action 4: Wait
- **Duration:** 5 minutes

### Action 5: AI Agent (SMS)
This is the core autonomous follow-up action.

- **Channel:** SMS
- **AI Agent Instructions:** Paste the full content from the file `ghl_ai_agent_prompt.md`
- **Tools to enable:**
  - Send SMS (set content to: AI will fill this field)
  - Update Opportunity
  - Create Appointment (select: AI Discovery Call calendar)
- **Model:** GPT-4o or GPT-5.2 (whichever is available — choose highest available)
- **Max turns:** 20
- **Inactivity timeout:** 3 days

### Action 6: Wait (if no reply)
- **Duration:** 3 days
- **Condition:** Only continue if contact has NOT replied to the AI Agent

### Action 7: Send SMS (Day 3 follow-up)
- **Content:** Set to **"AI will fill this field"**
- **AI Instructions:**

> *Write a short, friendly 2-sentence SMS follow-up to {{contact.first_name}}. They completed an AI Opportunity Scan 3 days ago and haven't replied yet. Their main bottleneck was {{contact.scan_bottleneck}} and their magic wand wish was "{{contact.scan_magic_wand}}". Reference one of these specifically and ask if they had a chance to look at their results. Keep it casual and human — not salesy. No more than 2 sentences.*

### Action 8: Wait
- **Duration:** 4 days

### Action 9: Send Email (Day 7 — final touch)
- **Subject:** `Still thinking about it, {{contact.first_name}}?`
- **Content:** Set to **"AI will fill this field"**
- **AI Instructions:**

> *Write a short, warm final follow-up email to {{contact.first_name}}. They completed an AI Opportunity Scan 7 days ago and haven't booked a call yet. Their magic wand answer was "{{contact.scan_magic_wand}}" and their business type is {{contact.scan_business_type}}. Acknowledge that timing isn't always right, remind them their personalised results are still available at clickflowgrow.com/opportunity-scan.html, and leave the door open with the booking link: https://link.clickflowgrow.com/widget/booking/4zgS77DacE6RnoPTJ4WL. No pressure. 3 short paragraphs maximum. Sign off as Alex from ClickFlowGrow.*

### Action 10: Add Tag
- **Tag:** `scan-sequence-complete`

### Action 11: Update Opportunity Stage
- **Stage:** Not Ready — Nurture
*(Only reached if they haven't booked — the AI Agent will have already moved them to Call Booked if they engaged)*

---

## Step 4 — Publish the Workflow

Click **Publish** (top right). The workflow is now live.

---

## Step 5 — Test It

1. Go to **Contacts → + New Contact**
2. Create a test contact with your own mobile number and email address
3. Manually add the tag `ai-opportunity-scan`
4. Watch the workflow fire — you should receive the confirmation email within 2 minutes and the first SMS within 7 minutes
5. Reply to the SMS and watch the AI Agent respond, handle the conversation, and move the opportunity through the pipeline stages
6. Test booking — when the AI offers the call, accept it and confirm the appointment appears in the AI Discovery Call calendar

---

## Pipeline Stages Reference

| Stage | Meaning |
|---|---|
| New Scan Lead | Just completed the scan — workflow has fired |
| Engaged | Has replied to the AI Agent |
| Call Booked | Discovery call booked in the calendar |
| Call Completed | Discovery call has taken place |
| Proposal Sent | Follow-up proposal or quote sent |
| Client Won | Signed up as a client |
| Not Ready — Nurture | Not ready now — keep warm for future |

---

## What This Demonstrates to Potential Clients

This workflow is a live, working example of everything ClickFlowGrow sells:

- **Instant response** — contact is followed up within minutes, not hours
- **AI personalisation** — every message references their specific scan answers
- **Autonomous conversation** — the AI Agent handles the entire follow-up without human input
- **Pipeline management** — the AI moves the lead through stages as the conversation progresses
- **Appointment booking** — the AI books the call directly into the calendar
- **Multi-channel** — email and SMS working together in a coordinated sequence

When you demonstrate this to a prospect, you are not showing them a slide deck — you are showing them their own future.
