# Create Product Requirements Document (PRD) — Web App

## Goal
Guide an AI assistant to produce a clear, actionable PRD (Markdown) from an initial idea/brief, suitable for a **junior developer** to implement in a modern **web app** (desktop + mobile layouts), with **email/Google authentication** and **Stripe billing (7‑day free trial)**.

---

## Process
1. **Receive Initial Prompt** — User provides idea/problem statement and any source docs (brief, journeys, epics).  
2. **Ask Clarifying Questions** — Focus on *what* and *why*; provide numbered options for easy replies.  
3. **Generate PRD** — Use the structure below.  
4. **Save (manual)** — Save as `[n]-prd-[feature-name].md` in `/docs/spec/` (4‑digit sequence).

---

## Clarifying Questions (Examples)
- **Problem/Goal** — What problem are we solving? Primary success outcomes?  
- **Target Users** — Segments; desktop vs mobile share.  
- **Core Functionality** — Key actions the user must perform.  
- **Auth** — Email + password and/or passwordless? Google via OAuth (OIDC)? Required scopes?  
- **Billing** — Stripe products/prices, 7‑day trial rules, what features are gated? Refunds/cancel rules?  
- **Landing/Marketing** — What’s on the landing page? Primary CTA? SEO keywords? Analytics?  
- **Responsive/Accessibility** — Breakpoints, mobile-first behaviors, WCAG goals.  
- **Data/Privacy** — PII stored? Cookies/consent banner? GDPR/CCPA needs?  
- **Motion/Animation** — Interaction/animation specs (with references).  
- **Tech/Infra** — Preferred stack (e.g., React/Next.js), hosting (Vercel/Netlify), envs (dev/stage/prod).  
- **Edge Cases** — Offline, rate limits, auth errors, payment failures, trial expiration flows.

---

## PRD Structure
1. **Title** — Clear feature/epic name.  
2. **Overview** — What the feature is; why it matters; target users.  
3. **Goals** — Specific, measurable objectives.  
4. **Non‑Goals** — What’s explicitly out of scope.  
5. **User Stories / Use Cases** — Narrative flows (happy + edge).  
6. **Requirements**
   - **Functional** — Numbered list of user‑visible behaviors.  
   - **Technical** — Integrations, schemas, APIs, rate limits, security notes.  
7. **Auth & Access Control**
   - Email login/signup (and/or passwordless), Google OAuth (OIDC).  
   - Session/cookie strategy; protected routes; role/plan entitlements.  
8. **Billing & Monetization (Stripe)**
   - Products/plans; 7‑day free trial; upgrade/downgrade; cancellation; webhooks; “Restore access” logic.  
   - Entitlements gating (what’s free vs paid).  
9. **Landing Page & Navigation**
   - Public marketing page; CTA → login/signup; top‑level IA; SEO/meta/OG; analytics events.  
10. **Responsive & Accessibility**
    - Breakpoints & layout rules; keyboard navigation; color contrast; focus states; reduced motion.  
11. **Motion / Animation Notes**
    - Key interactions (e.g., stacked cards), durations/easing, references (Figma/CodePen).  
12. **Success Metrics**
    - Activation %; trial→paid conversion; retention; task success rates; Core Web Vitals targets.  
13. **Risks & Open Questions**
    - Unknowns, dependencies, blockers.  
14. **Acceptance Criteria**
    - Checklist of DONE conditions covering behavior, auth, billing, responsive, a11y, analytics.

---

## Target Audience
Assume a **junior developer** is the primary reader. Avoid jargon; be explicit and unambiguous.

---

## Output
- **Format:** Markdown (`.md`)  
- **Location:** `/docs/spec/`  
- **Filename:** `[n]-prd-[feature-name].md`

---

## Final Instructions
1. Do **not** implement code.  
2. Ask clarifying questions first.  
3. Use answers to improve the PRD.
