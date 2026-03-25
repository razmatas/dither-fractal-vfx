# Starter Workflow — Web App

This is your human‑facing playbook from idea → PRDs → tasks → roadmap → execution for a **web app** with email/Google auth and Stripe (7‑day trial).

---

## Step 1. Idea & Problem (ChatGPT Phase)
Use the idea template (vision, problem, audience, features, design notes, success metrics, constraints). Include:
- Platform: **web app** (desktop + mobile layouts)
- Auth: **email login + Google OAuth**
- Billing: **Stripe**, **7‑day trial**, gated features

---

## Step 2. Project Setup
```
my-webapp/
  docs/
    ai/    ← copy these recipes
    spec/  ← PRDs, tasks, roadmap
  src/
```
Copy: `create-prd.md`, `generate-tasks.md`, `process-task-list.md`, `starter-prompt.md`, this workflow, and `prompt-prd.md` into `docs/ai/`.

---

## Step 3. Create PRD

### ⭐ First Windsurf Message (Template)
```
Use /docs/ai/starter-prompt.md as guardrails.
Generate a PRD using /docs/ai/create-prd.md based on these sources:

- /docs/spec/0000-brief.md
- /docs/spec/0000-user-journeys.md
- /docs/spec/0000-epics.md

Please create a PRD for "[Epic Name]".
Ensure requirements cover web app (responsive), email/Google auth, and Stripe 7‑day trial where relevant.
Save as /docs/spec/[n]-prd-[epic-name].md
```

---

## Step 4. Generate Tasks

### ⭐ Windsurf Message (Template)
```
Using /docs/ai/generate-tasks.md, create a task list from /docs/spec/[n]-prd-[epic-name].md.
Stop after parent tasks and wait for my "Go" before expanding to sub‑tasks.
Include tracks: Auth, Billing, App Core UI, Landing/SEO, Infra/QA (as applicable).
Save as /docs/spec/tasks-[n]-prd-[epic-name].md
```

---

## Step 5. Process into Roadmap

### ⭐ Windsurf Message (Template)
```
Refine /docs/spec/tasks-[n]-prd-[epic-name].md using /docs/ai/process-task-list.md.
Prioritize, capture dependencies, and organize into sprints/milestones.
Define release criteria (tests, a11y, Core Web Vitals, billing checks).
Save as /docs/spec/roadmap-[epic-name].md
```

---

## Step 6. Execution Loop (per sprint)
```
Use /docs/ai/starter-prompt.md as guardrails.
Execute Sprint <N> from /docs/spec/roadmap-[epic-name].md.
Propose diffs → await OK → apply → update tests/docs.
If UI work, cross‑check against Figma via MCP when provided.
```

End each sprint with verification (tests, type‑check, lint; Stripe flows; docs updated).

---

## Step 7. Landing & Monetization
- Keep a dedicated PRD/epic for **Landing/Marketing** (SEO, analytics).  
- Keep a dedicated PRD/epic for **Billing & Monetization** (Stripe products, trial rules, webhooks, entitlements).

---
