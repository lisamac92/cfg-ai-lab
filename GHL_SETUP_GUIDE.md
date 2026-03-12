# GHL Voice AI — 5-Minute Setup Guide

Follow these five steps to configure the Voice AI agent and get the embed code I need to wire it into the AI Lab. This should take about 5-10 minutes.

---

### Step 1: Enable the Labs Feature (2 mins)

The browser-based voice widget is a new feature in GHL. You may need to enable it first.

1. Log in to your GoHighLevel agency account.

1. Navigate to the **ClickFlow Grow** sub-account.

1. Go to **Settings** (in the bottom-left menu).

1. Click on **Labs**.

1. Find **"Voice AI Chat Widget"** in the list and toggle it **ON**.

If it's already on, you're all set.

---

### Step 2: Create the Voice AI Agent (3 mins)

Next, we'll create Aria, the AI agent who will conduct the demos.

1. Go to **Automation** (in the left menu).

1. Click on **AI Agents**, then select the **Voice AI** tab.

1. Click the **+ Create New** button.

1. **Agent Name:** `Aria — AI Receptionist Demo`

1. **System Prompt:** Open the `ARIA_PROMPT.md` file I sent you, copy the entire text, and paste it into this field.

1. **Voice:** Choose a female voice you like (e.g., "Nicole" or "Sarah").

1. Click **Save**.

---

### Step 3: Create a Knowledge Base (1 min)

The agent needs a knowledge base, even if it's empty for the demo (since Aria gathers info live).

1. Go to **AI Agents**, then select the **Knowledge Base** tab.

1. Click **+ Create New**.

1. **Name:** `AI Lab Demo KB`

1. Click **Save**. You don't need to add any URLs or files to it.

---

### Step 4: Create the Embedded Widget (3 mins)

This is where you'll generate the code snippet for the website.

1. Go to **Sites** (in the left menu).

1. Click on **Chat Widgets**.

1. Click **+ Create Widget**.

1. **Widget Type:** Select **Voice AI**.

1. In the widget builder, go to the **Style** tab.

1. Under **Widget Placement**, select **Embedded/Inline**.

1. (Optional) You can customize the colours to match the AI Lab design, but I can also override this in the code.

1. Click **Save**.

1. Now, click the **Get Code** button.

---

### Step 5: Send Me the Code

A popup will appear with a `<script>` tag. It will look something like this:

```html
<script
    src="https://widgets.leadconnector.com/voice-widget/xxxxxxxx.js"
    data-widget-id="xxxxxxxxxxxxxxxxxxxxxxxx"
    data-location-id="E4vxxqsZzDt35YcgEH2d"
    data-agent-id="xxxxxxxxxxxxxxxxxxxxxxxx"
    data-chat-widget-version="v1"
    defer>
</script>
```

**Copy that entire script tag and paste it back into our chat.**



Once I have that code, I will embed it directly into the "Talk to Aria" button on the AI Lab page, and the live voice demo will be fully functional.

