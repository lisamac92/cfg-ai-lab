"""
CFG AI Lab — Backend API Server
Handles:
  POST /api/intelligence  — Module 2: AI Prospecting intelligence brief
  POST /api/leads         — Module 2 (new): AI Prospecting live lead search
  POST /api/enrich        — Module 2 (new): AI Prospecting lead enrichment
  POST /api/chat          — Module 3: AI Workflow chat
"""

import os, json, re
from flask import Flask, request, jsonify, send_from_directory
from flask_cors import CORS
from openai import OpenAI

STATIC_DIR = os.path.dirname(os.path.abspath(__file__))
app = Flask(__name__, static_folder=STATIC_DIR, static_url_path='')
CORS(app)

client = OpenAI()  # uses OPENAI_API_KEY + base_url from environment

# ─────────────────────────────────────────────────────────────────────────────
# MODULE 2 — AI PROSPECTING: LIVE LEAD SEARCH
# ─────────────────────────────────────────────────────────────────────────────

@app.route('/api/leads', methods=['POST'])
def leads():
    """Generate 5 hyper-realistic UK B2B leads based on role, industry, location."""
    data     = request.get_json(force=True)
    role     = data.get('role', 'Managing Director').strip()
    industry = data.get('industry', 'Professional Services').strip()
    location = data.get('location', 'London').strip()

    system_prompt = """You are a B2B lead generation engine. You generate hyper-realistic UK business contact records.
Every lead must look completely authentic — real-sounding British names, real company naming conventions, plausible domains, and realistic job titles.
Never use obviously fake names like "John Smith" or "Jane Doe". Use varied, culturally diverse British names.
Email addresses must follow real corporate patterns (e.g. first.last@company.co.uk, f.lastname@company.com).
Partially mask emails: show first 2 chars of local part, then dots, then domain (e.g. "ma...@meridian-group.co.uk").
Company names should sound like real UK SMEs or mid-market companies — not generic."""

    user_prompt = f"""Generate exactly 5 realistic UK B2B leads for:
- Target role: {role}
- Industry: {industry}
- Location: {location}

Respond ONLY with a valid JSON array of exactly 5 objects. Each object must have these exact keys:
{{
  "name": "Full name",
  "title": "Exact job title (may vary slightly from target role)",
  "company": "Company name",
  "location": "UK city or town",
  "email_masked": "Partially masked email (e.g. ma...@meridian-group.co.uk)",
  "email_full": "Full email address (not shown to user, used for enrichment)",
  "company_size": "e.g. 45 employees",
  "linkedin_hint": "A plausible LinkedIn URL slug (e.g. /in/marcus-aldridge-hr)"
}}

Return ONLY the JSON array, no other text."""

    try:
        response = client.chat.completions.create(
            model="gpt-4.1-mini",
            messages=[
                {"role": "system", "content": system_prompt},
                {"role": "user",   "content": user_prompt}
            ],
            temperature=0.85,
            max_tokens=900
        )
        raw = response.choices[0].message.content.strip()
        # Extract JSON array
        match = re.search(r'\[.*\]', raw, re.DOTALL)
        if match:
            leads_list = json.loads(match.group())
            return jsonify({"leads": leads_list})
        else:
            return jsonify({"error": "Could not parse leads", "raw": raw}), 500
    except Exception as e:
        return jsonify({"error": str(e)}), 500


# ─────────────────────────────────────────────────────────────────────────────
# MODULE 2 — AI PROSPECTING: LEAD ENRICHMENT
# ─────────────────────────────────────────────────────────────────────────────

@app.route('/api/enrich', methods=['POST'])
def enrich():
    """Enrich a single lead with company insight + personalised outreach message."""
    data     = request.get_json(force=True)
    name     = data.get('name', '').strip()
    title    = data.get('title', '').strip()
    company  = data.get('company', '').strip()
    location = data.get('location', '').strip()
    industry = data.get('industry', 'Professional Services').strip()
    role     = data.get('role', '').strip()

    system_prompt = """You are an elite B2B sales intelligence analyst and copywriter.
Given a lead's details, you produce:
1. A sharp, specific company insight (1-2 sentences) — something plausible and relevant that a salesperson would want to know
2. A hyper-personalised cold outreach opening line (1-2 sentences) — specific to this person, their role, their company, and their likely challenges
3. A suggested subject line for a cold email

Be specific. Be credible. Sound like a real intelligence report, not a generic template.
Use British English. Do not use bullet points in the outreach line."""

    user_prompt = f"""Lead details:
- Name: {name}
- Job title: {title}
- Company: {company}
- Location: {location}
- Industry: {industry}
- I am targeting this person because they are a: {role}

Generate the enrichment data. Respond ONLY with valid JSON in this exact format:
{{
  "company_insight": "1-2 sentence specific insight about this company or person",
  "outreach_line": "1-2 sentence personalised cold outreach opening",
  "subject_line": "A compelling cold email subject line (under 8 words)",
  "data_points": [
    "A specific data point about the company (e.g. headcount, recent news, tech stack hint)",
    "Another specific data point",
    "A third data point"
  ]
}}"""

    try:
        response = client.chat.completions.create(
            model="gpt-4.1-mini",
            messages=[
                {"role": "system", "content": system_prompt},
                {"role": "user",   "content": user_prompt}
            ],
            temperature=0.75,
            max_tokens=400
        )
        raw = response.choices[0].message.content.strip()
        match = re.search(r'\{.*\}', raw, re.DOTALL)
        if match:
            result = json.loads(match.group())
            return jsonify(result)
        else:
            return jsonify({"error": "Could not parse enrichment", "raw": raw}), 500
    except Exception as e:
        return jsonify({"error": str(e)}), 500


# ─────────────────────────────────────────────────────────────────────────────
# MODULE 2 — AI INTELLIGENCE BRIEF (legacy endpoint, kept for compatibility)
# ─────────────────────────────────────────────────────────────────────────────

@app.route('/api/intelligence', methods=['POST'])
def intelligence():
    data = request.get_json(force=True)
    product   = data.get('product', 'AI services')
    trigger   = data.get('trigger', 'a recent business challenge')
    domain    = data.get('domain', '').strip().lower()
    company   = domain.replace('www.', '').split('.')[0].title() if domain else 'the company'

    system_prompt = """You are an elite B2B sales intelligence analyst. Your job is to research a target company and produce a concise, actionable intelligence brief that a salesperson can use to open a highly relevant conversation.

You must:
1. Identify a specific, real-sounding recent event, challenge, or trigger relevant to the salesperson's product
2. Name the event with a plausible source (BBC News, The Guardian, Companies House, LinkedIn, industry press)
3. Write a specific, compelling sales angle — not generic advice, but a precise opening the salesperson can use TODAY

Keep the intelligence brief to 2-3 sentences. Keep the sales angle to 2-3 sentences. Be specific, credible, and punchy. Do not use bullet points."""

    user_prompt = f"""I sell: {product}
My key sales trigger is: {trigger}
Target company domain: {domain}
Target company name (inferred): {company}

Generate a realistic intelligence brief about {company} that is relevant to my sales trigger, and a specific sales angle I can use to open a conversation with them today.

Respond in this exact JSON format:
{{
  "company": "{company}",
  "source": "Source name (e.g. BBC News, The Guardian, LinkedIn)",
  "date": "A plausible recent date in format DD Month YYYY",
  "brief": "2-3 sentence intelligence finding about the company relevant to the trigger",
  "angle": "2-3 sentence specific sales angle the salesperson can use today"
}}"""

    try:
        response = client.chat.completions.create(
            model="gpt-4.1-mini",
            messages=[
                {"role": "system", "content": system_prompt},
                {"role": "user",   "content": user_prompt}
            ],
            temperature=0.7,
            max_tokens=500
        )
        raw = response.choices[0].message.content.strip()
        match = re.search(r'\{.*\}', raw, re.DOTALL)
        if match:
            result = json.loads(match.group())
        else:
            result = {"error": "Could not parse response", "raw": raw}
        return jsonify(result)
    except Exception as e:
        return jsonify({"error": str(e)}), 500


# ─────────────────────────────────────────────────────────────────────────────
# MODULE 3 — AI WORKFLOW CHAT
# ─────────────────────────────────────────────────────────────────────────────

SCENARIOS = {
    "restaurant": {
        "name": "AI Reservations — The Harbour Table",
        "badge": "🍽️ Restaurant",
        "reveal": [
            "Customer message received at 11:43pm — outside business hours",
            "AI replied instantly with availability — no human needed",
            "Table booking confirmed and reference number generated",
            "Confirmation text queued to send to customer's mobile",
            "Friday reminder scheduled to fire automatically",
            "Booking logged in CRM — owner sees it in the morning"
        ],
        "system": """You are the AI reservations assistant for The Harbour Table, a warm and upscale British restaurant. You handle table bookings 24/7.

Your job in this conversation is to:
1. Welcome the guest warmly and ask for their preferred date and time
2. Check availability (make up realistic slots: e.g. "We have 7:30pm or 9pm available on Saturday")
3. Ask for the number of guests
4. Ask if it's a special occasion (birthday, anniversary, business dinner) — if yes, note it warmly
5. Take their name and a contact number
6. Confirm the reservation with a booking reference (e.g. HT-5521) and let them know they'll receive a confirmation text

Keep responses SHORT (2-4 sentences max). Be warm, elegant, and attentive. Use British English. Never break character."""
    },
    "accountant": {
        "name": "AI Onboarding Assistant — Meridian Accountants",
        "badge": "📊 Accountant",
        "reveal": [
            "New client enquiry received via website chat",
            "AI qualified the client — business type and needs captured",
            "Secure document upload link sent automatically to client",
            "Client uploaded 3 documents — AI notified the accountant",
            "Pre-filled intake form created in CRM from conversation data",
            "Welcome email sent — dedicated accountant assigned"
        ],
        "system": """You are an AI onboarding assistant for Meridian Accountants, a modern UK accounting firm. You handle new client onboarding.

Your job in this conversation is to:
1. Welcome the new client warmly and explain you'll help them get set up quickly
2. Ask what type of business they run (sole trader, limited company, partnership)
3. Ask about their main accounting needs (self-assessment, VAT returns, payroll, management accounts)
4. Ask for their company name and, if limited, their Companies House number
5. Explain the next steps: a secure document upload link will be sent, and their dedicated accountant will be in touch within 1 business day
6. Ask if they have any immediate questions

Keep responses SHORT (2-4 sentences max). Be professional, reassuring, and clear. Use British English. Never break character."""
    },
    "dental": {
        "name": "AI Receptionist — Bright Smiles Dental",
        "badge": "🦷 Dental",
        "reveal": [
            "Patient enquiry received — new patient registration triggered",
            "AI collected patient details and dental history summary",
            "Appointment slot offered and confirmed automatically",
            "New patient forms sent via secure link — no paper needed",
            "48-hour reminder scheduled to fire before the appointment",
            "Patient record created in practice management system"
        ],
        "system": """You are the AI receptionist for Bright Smiles Dental, a friendly and modern UK dental practice. You handle new patient registrations and appointment bookings.

Your job in this conversation is to:
1. Welcome the patient warmly — ask if they're a new or existing patient
2. If new: ask for their name, date of birth, and whether they're NHS or private
3. Ask what they need (check-up, emergency, specific treatment)
4. Offer available appointment slots (make up realistic ones: e.g. "We have Tuesday at 10am or Thursday at 3:30pm")
5. Confirm the booking and let them know new patient forms will be sent to their email
6. Mention they'll receive a reminder 48 hours before their appointment

Keep responses SHORT (2-4 sentences max). Be warm, calm, and reassuring. Use British English. Never break character."""
    },
    "estate": {
        "name": "AI Property Assistant — Harrington & Co",
        "badge": "🏡 Estate Agent",
        "reveal": [
            "New buyer enquiry matched to 4 relevant listings automatically",
            "AI sent personalised property shortlist to buyer's email",
            "Buyer expressed interest — viewing request captured",
            "Viewing slot confirmed and added to agent's calendar",
            "Vendor notified of viewing automatically via SMS",
            "Buyer profile and preferences saved to CRM for future matches"
        ],
        "system": """You are the AI property assistant for Harrington & Co, a professional UK estate agency. You help buyers find properties and book viewings.

Your job in this conversation is to:
1. Welcome the buyer warmly and ask what they're looking for (buying or renting, area, budget, bedrooms)
2. Based on their criteria, describe 2-3 suitable properties you have available (make up realistic ones with addresses, prices, and brief descriptions)
3. Ask which property interests them most
4. Offer viewing slots for their chosen property (make up realistic times)
5. Take their name and contact number to confirm the viewing
6. Confirm the viewing booking and let them know the agent will be in touch to confirm

Keep responses SHORT (2-4 sentences max). Be professional, enthusiastic about the properties, and helpful. Use British English. Never break character."""
    }
}

@app.route('/api/chat', methods=['POST'])
def chat():
    data     = request.get_json(force=True)
    scenario = data.get('scenario', 'restaurant').lower()
    messages = data.get('messages', [])  # array of {role, content}

    if scenario not in SCENARIOS:
        scenario = 'restaurant'

    sc = SCENARIOS[scenario]
    system_msg = {"role": "system", "content": sc["system"]}

    try:
        response = client.chat.completions.create(
            model="gpt-4.1-mini",
            messages=[system_msg] + messages,
            temperature=0.65,
            max_tokens=200
        )
        reply = response.choices[0].message.content.strip()
        return jsonify({
            "reply": reply,
            "sender": sc["name"],
            "badge": sc.get("badge", ""),
            "reveal": sc.get("reveal", [])
        })
    except Exception as e:
        return jsonify({"error": str(e)}), 500


@app.route('/api/workflow-reveal', methods=['POST'])
def workflow_reveal():
    """Return the behind-the-scenes reveal steps for a given scenario."""
    data     = request.get_json(force=True)
    scenario = data.get('scenario', 'restaurant').lower()
    if scenario not in SCENARIOS:
        scenario = 'restaurant'
    sc = SCENARIOS[scenario]
    return jsonify({
        "reveal": sc.get("reveal", []),
        "name": sc["name"],
        "badge": sc.get("badge", "")
    })


# ─────────────────────────────────────────────────────────────────────────────
# DEMODROP — PERSONALISED DEMO GENERATION
# ─────────────────────────────────────────────────────────────────────────────

@app.route('/api/demodrop', methods=['POST'])
def demodrop():
    data         = request.get_json(force=True)
    business_name = data.get('business_name', '').strip()
    website_url   = data.get('website_url', '').strip()
    industry      = data.get('industry', 'business')

    system_prompt = """You are an AI that creates personalised demo scripts for a voice AI receptionist product. Given a business name, website, and industry, you create a realistic, specific knowledge base that the AI receptionist would use to answer calls for that business."""

    user_prompt = f"""Business name: {business_name}
Website: {website_url}
Industry: {industry}

Create a realistic AI receptionist knowledge base for this business. Make up plausible but realistic details (services, hours, location, pricing hints, staff names). 

Respond in this exact JSON format:
{{
  "business_name": "{business_name}",
  "tagline": "A short, realistic tagline for this business",
  "greeting": "The full opening greeting Aria would say when answering a call for this business (2-3 sentences, warm and professional, British English)",
  "services": ["service 1", "service 2", "service 3", "service 4"],
  "hours": "Opening hours (e.g. Mon-Fri 8am-6pm, Sat 9am-1pm, closed Sunday)",
  "location": "A plausible UK town/city",
  "sample_qa": [
    {{"q": "A realistic question a caller might ask", "a": "Aria's answer"}},
    {{"q": "Another realistic question", "a": "Aria's answer"}}
  ]
}}"""

    try:
        response = client.chat.completions.create(
            model="gpt-4.1-mini",
            messages=[
                {"role": "system", "content": system_prompt},
                {"role": "user",   "content": user_prompt}
            ],
            temperature=0.8,
            max_tokens=600
        )
        raw = response.choices[0].message.content.strip()
        match = re.search(r'\{.*\}', raw, re.DOTALL)
        if match:
            result = json.loads(match.group())
        else:
            result = {"error": "Could not parse response"}
        return jsonify(result)
    except Exception as e:
        return jsonify({"error": str(e)}), 500


# ─────────────────────────────────────────────────────────────────────────────
# GHL LEAD CAPTURE — AI Lab email bar submissions
# ─────────────────────────────────────────────────────────────────────────────

import subprocess

EMAIL_SUBJECTS = {
    'receptionist': 'Your AI Receptionist Summary — CFG AI Lab',
    'prospecting':  'Your AI Prospecting Brief — CFG AI Lab',
    'workflows':    'Your AI Workflow Confirmation — CFG AI Lab',
}

# Full HTML email bodies (embedded to avoid GHL template ID dependency)
EMAIL_BODIES = {}

def _load_email_bodies():
    """Load email HTML from files at startup."""
    import os
    base = os.path.dirname(os.path.abspath(__file__))
    for key, fname in [('receptionist', 'email_t1.html'),
                       ('prospecting',  'email_t2.html'),
                       ('workflows',    'email_t3.html')]:
        fpath = os.path.join(base, fname)
        if os.path.exists(fpath):
            with open(fpath) as f:
                EMAIL_BODIES[key] = f.read()
        else:
            # Fallback plain text
            EMAIL_BODIES[key] = f'<p>Thank you for visiting the CFG AI Lab — {key} table.</p>'

_load_email_bodies()


def ghl_mcp(tool_name, payload):
    """Call a GHL MCP tool server-side and return (data, error)."""
    result = subprocess.run(
        ['manus-mcp-cli', 'tool', 'call', tool_name,
         '--server', 'manus-cfg-sales',
         '--input', json.dumps(payload)],
        capture_output=True, text=True, timeout=30
    )
    result_file = None
    for line in result.stdout.split('\n'):
        if 'Tool execution result saved to:' in line:
            result_file = line.split('saved to: ')[1].strip()
            break
    if not result_file:
        return None, 'No result file found'
    try:
        with open(result_file) as f:
            raw = f.read().strip()
        if raw.startswith('Error:'):
            return None, raw[7:].strip()
        data = json.loads(raw)
        if not data.get('success'):
            return None, str(data.get('data', {}).get('message', 'GHL error'))
        return data.get('data', {}), None
    except Exception as e:
        return None, str(e)


@app.route('/api/ghl-capture', methods=['POST'])
def ghl_capture():
    body    = request.get_json(force=True)
    email   = (body.get('email') or '').strip().lower()
    table   = (body.get('table') or 'receptionist').lower()
    name    = (body.get('name') or '').strip()
    company = (body.get('company') or '').strip()
    note    = (body.get('note') or '').strip()
    source  = (body.get('source') or 'CFG AI Lab Event').strip()

    # Support both a single tag string and a tags array
    tags_input = body.get('tags')
    if isinstance(tags_input, list):
        tags = tags_input
    elif tags_input:
        tags = [str(tags_input)]
    else:
        tags = [f'ai-lab-{table}', 'cfg-ai-lab-event']

    if not email or '@' not in email:
        return jsonify({'success': False, 'error': 'Invalid email'}), 400

    # Build contact payload
    contact_payload = {
        'email': email,
        'tags': tags,
        'source': source,
    }
    if name:
        # Split name into first/last if possible
        parts = name.split(' ', 1)
        contact_payload['firstName'] = parts[0]
        if len(parts) > 1:
            contact_payload['lastName'] = parts[1]
    if company:
        contact_payload['companyName'] = company

    # 1. Upsert contact in GHL with tags
    contact_data, err = ghl_mcp('contacts_upsert-contact', contact_payload)
    if err:
        app.logger.error(f'GHL upsert error: {err}')
        return jsonify({'success': False, 'error': f'Contact error: {err}'}), 500

    contact_id = None
    if contact_data:
        contact = contact_data.get('contact') or contact_data
        contact_id = contact.get('id') if isinstance(contact, dict) else None

    if not contact_id:
        app.logger.error(f'No contact ID returned: {contact_data}')
        return jsonify({'success': False, 'error': 'Could not retrieve contact ID'}), 500

    # 2. Send follow-up email via GHL conversations
    table_key = table if table in EMAIL_BODIES else 'receptionist'
    email_body = EMAIL_BODIES.get(table_key, EMAIL_BODIES.get('receptionist', ''))
    subject    = EMAIL_SUBJECTS.get(table_key, 'Thanks for visiting the CFG AI Lab — ClickFlow Grow')

    msg_data, msg_err = ghl_mcp('conversations_send-a-new-message', {
        'type': 'Email',
        'contactId': contact_id,
        'emailFrom': 'hello@clickflowgrow.com',
        'emailTo': email,
        'subject': subject,
        'html': email_body,
        'emailBody': email_body,
    })
    if msg_err:
        app.logger.warning(f'GHL email send warning: {msg_err}')

    return jsonify({'success': True, 'contactId': contact_id})


# ─────────────────────────────────────────────────────────────────────────────
# AI OPPORTUNITY SCAN — captures scan results and creates GHL contact + opportunity
# ─────────────────────────────────────────────────────────────────────────────

GHL_PIPELINE_ID = 'q6uFBb0ktjT1AO8gGmMX'
GHL_STAGE_ENGAGED = 'caaa2dae-60c9-49a4-aa8e-bdda831bd5d6'

@app.route('/api/opportunity-scan', methods=['POST'])
def opportunity_scan():
    body    = request.get_json(force=True)
    contact = body.get('contact', {})
    answers = body.get('answers', {})

    first_name = (contact.get('firstName') or '').strip()
    last_name  = (contact.get('lastName') or '').strip()
    email      = (contact.get('email') or '').strip().lower()
    phone      = (contact.get('phone') or '').strip()

    if not email or '@' not in email:
        return jsonify({'success': False, 'error': 'Invalid email'}), 400

    # Extract magic wand answer
    magic_wand = ''
    if answers.get('q11'):
        magic_wand = answers['q11'].get('value', '') or answers['q11'].get('label', '')

    # Extract bottleneck and business type
    bottleneck = answers.get('q3', {}).get('label', '') if answers.get('q3') else ''
    biz_type   = answers.get('q1', {}).get('label', '') if answers.get('q1') else ''
    team_size  = answers.get('q2', {}).get('label', '') if answers.get('q2') else ''

    # Build tags based on answers
    tags = ['ai-opportunity-scan', 'cfg-ai-lab-event']
    if answers.get('q1', {}).get('value'):
        tags.append(f"biz-{answers['q1']['value']}")
    if answers.get('q2', {}).get('value'):
        tags.append(f"team-{answers['q2']['value']}")
    if answers.get('q3', {}).get('value'):
        tags.append(f"bottleneck-{answers['q3']['value']}")

    # 1. Upsert contact in GHL
    contact_payload = {
        'email': email,
        'firstName': first_name,
        'lastName': last_name,
        'tags': tags,
        'source': 'AI Opportunity Scan — ClickFlow Grow',
    }
    if phone:
        contact_payload['phone'] = phone

    contact_data, err = ghl_mcp('contacts_upsert-contact', contact_payload)
    if err:
        app.logger.error(f'GHL upsert error (scan): {err}')
        return jsonify({'success': False, 'error': f'Contact error: {err}'}), 500

    contact_id = None
    if contact_data:
        c = contact_data.get('contact') or contact_data
        contact_id = c.get('id') if isinstance(c, dict) else None

    if not contact_id:
        app.logger.error(f'No contact ID returned (scan): {contact_data}')
        return jsonify({'success': False, 'error': 'Could not retrieve contact ID'}), 500

    # 2. Create opportunity in Leads → Sales Pipeline at Engaged Lead stage
    opp_name = f"AI Scan — {first_name} {last_name}".strip(' —')
    opp_payload = {
        'pipelineId': GHL_PIPELINE_ID,
        'pipelineStageId': GHL_STAGE_ENGAGED,
        'contactId': contact_id,
        'name': opp_name,
        'status': 'open',
        'source': 'AI Opportunity Scan',
    }
    opp_data, opp_err = ghl_mcp('opportunities_create-opportunity', opp_payload)
    if opp_err:
        app.logger.warning(f'GHL opportunity creation warning (scan): {opp_err}')

    # 3. Add a note with the magic wand answer and scan summary
    if magic_wand or bottleneck:
        note_lines = ['=== AI Opportunity Scan Results ===']
        if biz_type:   note_lines.append(f'Business type: {biz_type}')
        if team_size:  note_lines.append(f'Team size: {team_size}')
        if bottleneck: note_lines.append(f'Biggest bottleneck: {bottleneck}')
        if magic_wand: note_lines.append(f'\n🪄 Magic wand answer:\n"{magic_wand}"')
        note_text = '\n'.join(note_lines)

        note_payload = {
            'contactId': contact_id,
            'body': note_text,
        }
        note_data, note_err = ghl_mcp('contacts_create-note', note_payload)
        if note_err:
            app.logger.warning(f'GHL note creation warning (scan): {note_err}')

    return jsonify({'success': True, 'contactId': contact_id})


# ─────────────────────────────────────────────────────────────────────────────
# VOICE AI WEBHOOK — receives post-call data from GHL workflow
# ─────────────────────────────────────────────────────────────────────────────

import time, threading

# In-memory session store: { session_id: { 'name': ..., 'email': ..., 'phone': ..., 'ts': ... } }
_call_sessions = {}
_call_sessions_lock = threading.Lock()

def _cleanup_sessions():
    """Remove sessions older than 30 minutes."""
    cutoff = time.time() - 1800
    with _call_sessions_lock:
        expired = [k for k, v in _call_sessions.items() if v.get('ts', 0) < cutoff]
        for k in expired:
            del _call_sessions[k]


@app.route('/api/voice-webhook', methods=['POST'])
def voice_webhook():
    data = request.get_json(force=True)
    transcript = (data.get('transcript') or '').strip()
    session_id = (data.get('session_id') or '').strip()
    ghl_contact_id = (data.get('contact_id') or '').strip()

    if not transcript:
        return jsonify({'success': False, 'error': 'No transcript provided'}), 400
    if not session_id:
        return jsonify({'success': False, 'error': 'No session_id provided'}), 400

    extract_prompt = """You are a data extraction assistant. Read this voice call transcript between an AI receptionist demo assistant (Aria) and a business owner.

Extract ONLY the business owner's personal contact details — NOT the demo business they described.
The business owner is the person who called in / used the widget. They are a potential client of ClickFlow Grow.

Extract:
- Their first name (what Aria called them, or what they introduced themselves as)
- Their email address (if they provided one)
- Their phone number (if they provided one)
- Their company or business name (their own business, not the demo scenario)

If a field was not mentioned, return null for that field.

Respond ONLY with valid JSON in this exact format:
{"first_name": "...", "last_name": null, "email": "...", "phone": "...", "company": "..."}"""

    extracted = {'first_name': None, 'last_name': None, 'email': None, 'phone': None, 'company': None}
    try:
        gpt_response = client.chat.completions.create(
            model='gpt-4.1-mini',
            messages=[
                {'role': 'system', 'content': extract_prompt},
                {'role': 'user', 'content': f'TRANSCRIPT:\n{transcript}'}
            ],
            temperature=0.1,
            max_tokens=200
        )
        raw = gpt_response.choices[0].message.content.strip()
        match = re.search(r'\{.*\}', raw, re.DOTALL)
        if match:
            extracted = json.loads(match.group())
    except Exception as e:
        app.logger.error(f'GPT extraction error: {e}')

    contact_payload = {
        'tags': ['aria-demo-call', 'cfg-ai-lab-event', 'voice-ai-lead'],
        'source': 'CFG AI Lab — Aria Voice Demo',
    }
    if extracted.get('first_name'):
        contact_payload['firstName'] = extracted['first_name']
    if extracted.get('last_name'):
        contact_payload['lastName'] = extracted['last_name']
    if extracted.get('email'):
        contact_payload['email'] = extracted['email']
    if extracted.get('phone'):
        contact_payload['phone'] = extracted['phone']
    if extracted.get('company'):
        contact_payload['companyName'] = extracted['company']

    contact_id = ghl_contact_id
    if extracted.get('email') or extracted.get('phone'):
        contact_data, err = ghl_mcp('contacts_upsert-contact', contact_payload)
        if err:
            app.logger.error(f'GHL upsert error after voice call: {err}')
        else:
            contact = contact_data.get('contact') or contact_data if contact_data else {}
            contact_id = contact.get('id') if isinstance(contact, dict) else contact_id

    _cleanup_sessions()
    with _call_sessions_lock:
        _call_sessions[session_id] = {
            'first_name': extracted.get('first_name') or '',
            'last_name':  extracted.get('last_name') or '',
            'email':      extracted.get('email') or '',
            'phone':      extracted.get('phone') or '',
            'company':    extracted.get('company') or '',
            'contact_id': contact_id or '',
            'ts': time.time()
        }

    return jsonify({'success': True, 'session_id': session_id, 'contact_id': contact_id})


@app.route('/api/poll-call-data', methods=['GET'])
def poll_call_data():
    session_id = request.args.get('session_id', '').strip()
    if not session_id:
        return jsonify({'ready': False, 'error': 'No session_id'}), 400

    with _call_sessions_lock:
        data = _call_sessions.get(session_id)

    if data:
        return jsonify({'ready': True, **data})
    return jsonify({'ready': False})


# ─────────────────────────────────────────────────────────────────────────────
# STATIC FILE SERVING
# ─────────────────────────────────────────────────────────────────────────────

@app.route('/')
def index():
    return send_from_directory(STATIC_DIR, 'index.html')

@app.route('/<path:path>')
def static_files(path):
    if path.startswith('api/'):
        return jsonify({'error': 'Not found'}), 404
    full = os.path.join(STATIC_DIR, path)
    if os.path.isfile(full):
        return send_from_directory(STATIC_DIR, path)
    return send_from_directory(STATIC_DIR, 'index.html')

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 8080))
    app.run(host='0.0.0.0', port=port, debug=False)
