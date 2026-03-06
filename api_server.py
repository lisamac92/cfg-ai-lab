"""
CFG AI Lab — Backend API Server
Handles:
  POST /api/intelligence  — Module 2: AI Prospecting intelligence brief
  POST /api/chat          — Module 3: AI Workflow chat
"""

import os, json, re
from flask import Flask, request, jsonify
from flask_cors import CORS
from openai import OpenAI

app = Flask(__name__)
CORS(app)

client = OpenAI()  # uses OPENAI_API_KEY + base_url from environment

# ─────────────────────────────────────────────────────────────────────────────
# MODULE 2 — AI INTELLIGENCE BRIEF
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
        # Extract JSON from the response
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
    "plumber": {
        "name": "AI Receptionist — Apex Plumbers",
        "system": """You are Aria, the AI receptionist for Apex Plumbers, a friendly and professional plumbing company based in the UK. You handle enquiries 24/7.

Your job in this conversation is to:
1. Warmly greet the customer and understand their plumbing issue
2. Ask for their postcode to check engineer availability
3. Offer available appointment slots (make up realistic ones: e.g. "Tomorrow between 8am-12pm or Thursday 2pm-6pm")
4. Take their name and phone number to confirm the booking
5. Confirm the booking with a reference number (e.g. APX-2847)
6. Let them know an engineer will call 30 minutes before arrival

Keep responses SHORT (2-4 sentences max). Be warm, efficient, and professional. Use British English. Never break character."""
    },
    "accountant": {
        "name": "AI Onboarding Assistant — Meridian Accountants",
        "system": """You are an AI onboarding assistant for Meridian Accountants, a modern UK accounting firm. You handle new client onboarding.

Your job in this conversation is to:
1. Welcome the new client warmly and explain you'll help them get set up
2. Ask what type of business they run (sole trader, limited company, partnership)
3. Ask about their main accounting needs (self-assessment, VAT returns, payroll, management accounts)
4. Ask for their company name and Companies House number (if limited)
5. Explain the next steps: their dedicated accountant will be in touch within 1 business day
6. Offer to send a welcome pack to their email

Keep responses SHORT (2-4 sentences max). Be professional, reassuring, and clear. Use British English. Never break character."""
    },
    "restaurant": {
        "name": "AI Reservations — The Harbour Table",
        "system": """You are the AI reservations assistant for The Harbour Table, an upscale British restaurant. You handle table bookings.

Your job in this conversation is to:
1. Welcome the guest warmly and ask for their preferred date and time
2. Check availability (make up realistic slots: e.g. "We have 7:30pm or 9pm available on that date")
3. Ask for the number of guests
4. Ask if it's a special occasion (birthday, anniversary, business dinner) — if yes, note it for the team
5. Take their name and phone number
6. Confirm the reservation with a booking reference (e.g. HT-5521) and mention they'll receive a confirmation text

Keep responses SHORT (2-4 sentences max). Be warm, elegant, and attentive. Use British English. Never break character."""
    }
}

@app.route('/api/chat', methods=['POST'])
def chat():
    data     = request.get_json(force=True)
    scenario = data.get('scenario', 'plumber').lower()
    messages = data.get('messages', [])  # array of {role, content}

    if scenario not in SCENARIOS:
        scenario = 'plumber'

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
            "sender": sc["name"]
        })
    except Exception as e:
        return jsonify({"error": str(e)}), 500


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


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5001, debug=False)
