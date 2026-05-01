# GHL AI Workflow Features — Video Analysis Notes
## Source: https://www.youtube.com/watch?v=FE14xueqU_I

## Key New GHL AI Features

### 1. AI Agent (Workflow Action)
- A single workflow action that replaces entire multi-branch if/else trees
- Configured with: Instructions (prompt), Model selection (GPT-5.2 low/high thinking), Tools
- Tools the AI Agent can use autonomously:
  - Send SMS (with "AI will fill this field" — dynamic content generation)
  - Send Live Chat Message (AI-generated content)
  - Create Opportunity (adds lead to a specific pipeline)
  - Update Opportunity (moves lead through pipeline stages autonomously)
  - Create Appointment / Booking Note (books into a calendar)
- All branching logic is inside the prompt — no if/else branches needed
- AI decides when and how to use each tool based on conversation context

### 2. Ask AI (Internal ChatGPT in GHL)
- Paste a prompt → instantly generates:
  - Complete pipeline structures (stages, names, order)
  - Full calendar setups (name, type, slots, availability, form fields, notifications)
- One-click approval and creation
- Massive time saver for setup

### 3. AI Studio (Beta)
- Generate complete landing pages from a prompt
- Includes live chat widget that connects to AI Agent workflow

### 4. AI Personalisation in Messages
- "AI will fill this field" option on Send SMS / Send Email actions
- AI generates message content dynamically based on conversation context
- No static templates needed

### 5. Autonomous Pipeline Management
- AI Agent moves leads through pipeline stages based on conversation
- Example rules in prompt:
  - "When lead first responds → move to Estimating"
  - "When estimate provided → move to Quoted"
  - "When appointment booked → move to Booking"
- No human intervention needed

## How This Applies to Our AI Opportunity Scan Workflow

### What we can build:
1. **Trigger**: Contact tag added = `ai-opportunity-scan`
2. **Immediate**: Send confirmation email (AI-personalised based on bottleneck/biz type)
3. **AI Agent action**: Conversational follow-up via SMS — AI knows their scan results
   (bottleneck, team size, magic wand answer from custom fields/notes)
4. **Pipeline movement**: AI moves contact through stages as they engage
5. **Booking**: AI can book a discovery call directly into the calendar
6. **Ask AI**: Use to generate the pipeline stages and calendar setup instantly

### Workflow stages to create via Ask AI:
- New Scan Lead
- Engaged (responded)
- Call Booked
- Call Completed
- Proposal Sent
- Client Won
- Not Ready (nurture)
