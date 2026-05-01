# GHL Workflow Setup Guide — AI Opportunity Scan Follow-Up
## ClickFlowGrow CRM

This guide walks you through building the complete AI Opportunity Scan follow-up workflow in ClickFlowGrow (GoHighLevel). The workflow uses the new **AI Agent** action to handle the entire follow-up conversation autonomously — no if/else branches needed.

---

## Before You Start — Checklist

- [x] Pipeline created: **AI Opportunity Scan** (7 stages)
- [x] Calendar created: **AI Discovery Call** (30 min, booking link: https://link.clickflowgrow.com/widget/booking/4zgS77DacE6RnoPTJ4WL)
- [ ] Custom fields created for scan data (see Step 1 below)
- [ ] Workflow built (see Steps 2–6 below)

---

## Step 1 — Create Custom Fields for Scan Data

Go to **Settings → Custom Fields → Contacts** and create these fields (if not already present):

| Field Name | Field Key | Type |
|---|---|---|
| Scan Bottleneck | `scan_bottleneck` | Text |
| Scan Business Type | `scan_biz_type` | Text |
| Scan Team Size | `scan_team_size` | Text |
| Scan Magic Wand | `scan_magic_wand` | Text |
| Scan Score F1 — Formulate | `scan_f1` | Number |
| Scan Score F2 — Be Found | `scan_f2` | Number |
| Scan Score F3 — Find | `scan_f3` | Number |
| Scan Score F4 — Fulfil | `scan_f4` | Number |
| Scan Score F5 — Fanfare | `scan_f5` | Number |

These fields are populated automatically when someone completes the scan (the website API writes them to the GHL contact record).

---

## Step 2 — Create the Workflow

Go to **Automation → Workflows → + New Workflow → Start from Scratch**

**Name it:** `AI Opportunity Scan — Follow-Up`

---

## Step 3 — Set the Trigger

**Trigger:** Contact Tag Added
**Tag:** `ai-opportunity-scan`

This fires the moment someone completes the scan on the website.

---

## Step 4 — Add Workflow Actions (in order)

### Action 1: Create Opportunity
- **Pipeline:** AI Opportunity Scan
- **Stage:** New Scan Lead
- **Opportunity Name:** `{{contact.first_name}} — AI Scan`
- **Assigned To:** Your user

### Action 2: Wait
- **Duration:** 2 minutes
- *(Gives the results page time to load before the first message arrives)*

### Action 3: Send Email
- **Subject:** `Your AI Opportunity Scan results, {{contact.first_name}}`
- **From:** hello@clickflowgrow.com
- **Content:** Set to **"AI will fill this field"**
- **AI Instructions for this email:**
  > *Write a warm, personal email to {{contact.first_name}} who has just completed the AI Opportunity Scan. Their biggest bottleneck is {{contact.scan_bottleneck}}. Their business type is {{contact.scan_biz_type}}. Their team size is {{contact.scan_team_size}}. Their magic wand answer was: "{{contact.scan_magic_wand}}". Write 3 short paragraphs: (1) acknowledge what they shared and validate it, (2) give them one specific insight about what AI could do for their type of business, (3) invite them to book a free 30-minute discovery call at https://link.clickflowgrow.com/widget/booking/4zgS77DacE6RnoPTJ4WL. Tone: warm, direct, no jargon. Sign off as Alex from ClickFlowGrow.*

### Action 4: Wait
- **Duration:** 5 minutes

### Action 5: AI Agent (SMS)
This is the core autonomous follow-up action.

- **Channel:** SMS
- **AI Agent Instructions:** *(Paste the full prompt from the file `ghl_ai_agent_prompt.md`)*
- **Tools to enable:**
  - Send SMS ✓ (AI will fill content)
  - Update Opportunity ✓
  - Create Appointment ✓ (AI Discovery Call calendar)
- **Model:** GPT-4o or GPT-5.2 (whichever is available)
- **Max turns:** 20
- **Inactivity timeout:** 3 days

### Action 6: Wait (if no reply)
- **Duration:** 3 days
- **Condition:** Only continue if contact has NOT replied

### Action 7: Send SMS (Day 3 follow-up)
- **Content:** Set to **"AI will fill this field"**
- **AI Instructions:**
  > *Write a short, friendly 2-sentence SMS follow-up to {{contact.first_name}}. They completed an AI Opportunity Scan 3 days ago. Their main bottleneck was {{contact.scan_bottleneck}}. Reference this specifically and ask if they had a chance to look at their results. Keep it casual and human — not salesy.*

### Action 8: Wait
- **Duration:** 4 days

### Action 9: Send Email (Day 7 — final)
- **Subject:** `Still thinking about it, {{contact.first_name}}?`
- **Content:** Set to **"AI will fill this field"**
- **AI Instructions:**
  > *Write a short, warm final follow-up email to {{contact.first_name}}. They completed an AI Opportunity Scan 7 days ago and haven't booked a call yet. Their magic wand answer was "{{contact.scan_magic_wand}}". Acknowledge that timing isn't always right, remind them their results are still available, and leave the door open with the booking link: https://link.clickflowgrow.com/widget/booking/4zgS77DacE6RnoPTJ4WL. No pressure. Sign off as Alex from ClickFlowGrow.*

### Action 10: Add Tag
- **Tag:** `scan-sequence-complete`

### Action 11: Update Opportunity Stage
- **Stage:** Not Ready — Nurture
- *(Only reached if they haven't booked — the AI Agent will have moved them to Call Booked if they engaged)*

---

## Step 5 — Publish the Workflow

Click **Publish** (top right). The workflow is now live.

---

## Step 6 — Test It

1. Go to **Contacts → + New Contact**
2. Create a test contact with your own mobile number and email
3. Manually add the tag `ai-opportunity-scan`
4. Watch the workflow fire — you should receive the email within 2 minutes and the SMS within 7 minutes
5. Reply to the SMS and watch the AI Agent respond and move the opportunity through the pipeline

---

## What This Demonstrates to Potential Clients

This workflow is a live, working example of everything ClickFlowGrow sells:
- **Instant response** — contact is followed up within minutes, not hours
- **AI personalisation** — every message references their specific answers
- **Autonomous conversation** — the AI handles the entire follow-up without human input
- **Pipeline management** — the AI moves the lead through stages as the conversation progresses
- **Appointment booking** — the AI books the call directly into the calendar
- **Multi-channel** — email + SMS working together

When you demonstrate this to a prospect, you're not showing them a slide deck — you're showing them their own future.
