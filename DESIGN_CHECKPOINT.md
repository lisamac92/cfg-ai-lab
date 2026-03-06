'''
# Design Checkpoint: CFG AI Lab

**Date:** 2026-03-06
**GitHub Commit:** `1315c10`
**Live Preview:** [https://8080-idglvrmshignkf4wht6zv-6a341fe9.us2.manus.computer](https://8080-idglvrmshignkf4wht6zv-6a341fe9.us2.manus.computer)

This document captures the final, agreed-upon design system for the CFG AI Lab website as of the commit referenced above. All future work should adhere to these standards.

---

## 1. Colour Palette

The palette is built on a dark navy foundation, with two primary accent colours (Teal and Warm Coral) used to give each "room" a distinct identity. All interactive content sits on clean white "cards" to create contrast and focus.

| Role | Colour | Hex Code | Usage |
|---|---|---|---|
| **Background** | Dark Navy | `#060d1f` | Global page background, hero sections, step backgrounds. |
| **Accent 1** | Teal | `#0BEAB5` | Primary accent for Table 01 (Receptionist) and Table 03 (Workflows). Used for buttons, badges, borders, icons, and progress indicators. |
| **Accent 2** | Warm Coral | `#F07A5A` | Secondary accent, used exclusively for Table 02 (Prospecting) to create a distinct identity. |
| **Surface** | White | `#ffffff` | Background for all interactive "cards" (audio player, forms, chat panels, email bars) to lift them off the dark background. |
| **Text (on Dark)** | Off-White | `rgba(240, 244, 255, 0.82)` | Primary body text and headings on dark backgrounds. Opacity is increased from previous versions for better readability. |
| **Text (on White)** | Near-Black | `#111111` - `#444444` | All text appearing on white cards, ensuring high contrast and readability. |

### Colour Variables

The following CSS variables are defined in the `:root` and should be used for all new components:

```css
:root {
  --cfg-navy:       #0F2D60;
  --cfg-teal:       #0BEAB5;
  --cfg-coral:      #F07A5A;
  --bg:             #060d1f;
  --surface:        #ffffff; /* Simplified from rgba */
  --text-primary:   #F0F4FF;
  --text-secondary: rgba(200,215,255,0.82);
}
```

---

## 2. Layout System

The previous two-column layout has been **completely replaced** with a full-width, single-column, step-by-step flow for each table. This creates a more immersive and focused user journey.

- **Hero Section:** Each room begins with a full-screen hero element containing the title, a description, and a "call to action" button to scroll down.
- **Numbered Steps:** Content is broken down into sequential, clearly labelled steps (`Step 1 of X`).
- **Wayfinding:** A sticky top navigation bar and progress dots help users orient themselves within and between the three rooms.
- **White Cards:** All interactive modules are presented on distinct white cards that "float" above the dark navy background.

---

## 3. Component States

This section documents the styling for the primary interactive components.

| Component | Table | Key Styling Details |
|---|---|---|
| **Audio Player** | 01 | White card background. Waveform bars are grey by default, turning **Teal** when active. Transcript text is dark (`#222`) on the white card. |
| **Intelligence Form** | 02 | White card background with a **Warm Coral** border. All form labels and input text are dark. The "Run Intelligence Search" button has a solid **Warm Coral** background. |
| **Chat Panel** | 03 | White card background with a **Teal** border. AI message bubbles have a light teal tint; user message bubbles have a solid teal background with white text. The message input area is white. |
| **Email Bars** | All | White card background with an accent-coloured border (Teal or Coral depending on the room). |
| **Buttons** | All | Primary buttons use a solid fill of the room's accent colour (Teal or Coral) with dark text (`#060d1a`) for high contrast. |
| **Badges & Labels** | All | Eyebrow labels, step number circles, and other small badges use the room's accent colour. |

---

## 4. Typography

The font stack remains consistent across the entire site.

- **Headings:** `Manrope`, weights 700 and 800.
- **Body & UI:** `Inter`, weights 400, 500, and 600.

All text contrast ratios have been reviewed and improved for better readability, especially for lighter text on the dark navy background.

---

This checkpoint represents the definitive design direction. All team members should reference this document for any future development or design tasks.
'''
