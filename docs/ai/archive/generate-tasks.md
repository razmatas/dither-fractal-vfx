# Generate Task List from a PRD — Web App

## Goal
From a PRD, create a step‑by‑step task list (Markdown) for a **junior developer** building a responsive web app with email/Google auth and Stripe billing with a 7‑day trial.

---

## Process
1. **Receive PRD Reference** — PRD file/content provided.  
2. **Analyze PRD** — Read functional/technical requirements, auth, billing, responsive/a11y, landing/SEO.  
3. **Assess Current State** — Consider existing code and patterns if files are provided (routing, UI lib, state mgmt).  
4. **Phase 1: Parent Tasks** — Propose ~5–8 high‑level tasks across tracks (Auth, Billing, App Core, Landing/SEO, Infra/CI, QA). **Present parent tasks only** first.  
   - Tell user: *“High‑level tasks ready. Reply ‘Go’ to generate sub‑tasks.”*  
5. **Phase 2: Sub‑Tasks** — On “Go”, expand each parent task into concrete steps.  
6. **Relevant Files** — List files to create/modify (include tests).  
7. **Final Output** — Full Markdown with *Relevant Files*, *Notes*, and *Tasks*.  
8. **Save** — `tasks-[prd-file-name].md` in `/docs/spec/` (manual).

---

## Output Format
```markdown
## Relevant Files
- `app/(marketing)/page.tsx` — Landing page route, SEO tags.
- `app/(app)/dashboard/page.tsx` — Auth‑protected route.
- `lib/auth/*` — Auth utilities (email/Google, sessions).
- `lib/billing/stripe.ts` — Stripe client & webhook handlers.
- `pages/api/stripe/webhook.ts` — Webhook endpoint.
- `components/ui/*` — Reusable components.
- `__tests__/*` — Unit/integration tests.

### Notes
- Keep tests next to code where possible; e2e in `/e2e` (e.g., Playwright).
- Environment variables via `.env.local` (never hardcode secrets).

## Tasks
- [ ] 1.0 Auth & Sessions
  - [ ] 1.1 Email signup/login (password or magic link)
  - [ ] 1.2 Google OAuth (OIDC) provider
  - [ ] 1.3 Protected routes & session cookie strategy
- [ ] 2.0 Billing (Stripe, 7‑day trial)
  - [ ] 2.1 Create products/prices in Stripe dashboard
  - [ ] 2.2 Checkout/Portal integration; free trial config
  - [ ] 2.3 Webhook handling for subscription lifecycle
  - [ ] 2.4 Entitlements gating in app (trial/active/canceled)
- [ ] 3.0 Landing & SEO
  - [ ] 3.1 Marketing page with responsive layout
  - [ ] 3.2 Meta/OG tags; sitemap/robots
  - [ ] 3.3 Analytics events (signup click, conversion)
- [ ] 4.0 App Core UI
  - [ ] 4.1 Responsive breakpoints & layout system
  - [ ] 4.2 Accessibility pass (keyboard, labels, contrast)
  - [ ] 4.3 Key module screens + empty/error/loading states
- [ ] 5.0 Infrastructure & Quality
  - [ ] 5.1 CI pipeline: lint, type‑check, unit, e2e
  - [ ] 5.2 Error handling & logging; 4xx/5xx pages
  - [ ] 5.3 Security headers; rate‑limit API routes
```

---

## Interaction Model
- Present **parent tasks first**, wait for **“Go”**, then generate sub‑tasks.  
- Keeps alignment before deep expansion.

---

## Target Audience
Assume a **junior developer**. Be explicit and implementation‑ready.
