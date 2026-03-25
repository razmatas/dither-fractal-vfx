# Windsurf Starter Prompt — Web App

Use this at the start of any Windsurf session. It defines rules and workflow for a modern **web app** (responsive UI, email/Google auth, Stripe billing with a 7‑day trial).

## General Rules
- Read `README.md`, `/docs/spec/**`, and `/docs/ai/**` before changes.
- Summarize the request back to me before executing.
- Explain key decisions briefly (libraries, trade‑offs).

## Coding Guardrails
- TypeScript everywhere; clean, idempotent diffs.
- Tests for user‑visible changes; don’t reduce coverage.
- Do **not** hardcode secrets; use `.env.example` and runtime configs.
- Security: input validation, auth checks, CSRF where relevant, Stripe webhook signature verification.
- Performance: aim for good **Core Web Vitals**.
- Accessibility: keyboard support, focus states, labels, contrast, prefers‑reduced‑motion.
- Analytics: instrument key events (signup, checkout, conversion).

## Workflow
1. **Planning**
   - Use `generate-tasks.md` to break PRDs into tasks across tracks (Auth, Billing, App, Landing/SEO, Infra, QA).
2. **Execution**
   - For each task: propose a diff → await OK → apply → update tests/docs.
3. **Documentation**
   - Keep PRDs/specs in `/docs/spec/`; add/update `CHANGELOG.md` per sprint.
4. **Review**
   - End of sprint checklist:
     - [ ] Tests green (unit/integration/e2e if present)
     - [ ] Type‑check & lint pass
     - [ ] Core Web Vitals targets met (where measurable)
     - [ ] A11y checks addressed
     - [ ] Billing flows verified (trial, upgrade, cancel)
     - [ ] Docs updated
