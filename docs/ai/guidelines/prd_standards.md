# PRD Standards

**Goal:** Create clear, actionable Product Requirements Documents (PRDs) suitable for implementation by an AI agent or junior developer.

## Core Requirements

Every PRD must address these core pillars if relevant:

1.  **Authentication & Access**:
    *   Email/Password vs. Passwordless vs. OAuth (Google).
    *   Role-based access (USER, ADMIN, etc.).
    *   Session management details.

2.  **Billing & Monetization (Stripe)**:
    *   **7-Day Free Trial** (Standard unless specified otherwise).
    *   Product/Plan definitions (Monthly/Yearly).
    *   Entitlement gating (what happens when trial ends?).
    *   Webhook handling for subscription lifecycle.

3.  **User Interface (UI/UX)**:
    *   **Responsive Design**: Mobile-first approach.
    *   **Accessibility**: WCAG compliance, keyboard navigation, contrast.
    *   **Motion**: Micro-interactions and loading states.

4.  **Technical Stack**:
    *   **Frontend**: React / Next.js (unless specified otherwise).
    *   **Styling**: Tailwind CSS.
    *   **State Management**: Context / Zustand / etc.
    *   **SEO**: Meta tags, OG tags, sitemaps for public pages.

## PRD Structure Template

When generating a PRD, structure it as follows:

```markdown
# [Feature Name] PRD

## 1. Overview
*   **Goal**: One-sentence summary.
*   **Target Audience**: Who is this for?
*   **Problem Statement**: What are we solving?

## 2. Functional Requirements
*   [ ] User Story 1
*   [ ] User Story 2
*   ...

## 3. Technical Requirements
*   **API Interactions**: Endpoints needed.
*   **Database Schema**: New tables or fields.
*   **Security**: Validation, authorization checks.

## 4. Design & UX
*   **Key Screens**: List of screens/components.
*   **States**: Empty, Loading, Error, Success.
*   **Responsive Behavior**: Mobile vs Desktop layout changes.

## 5. Billing & Entitlements
*   How does this interact with the subscription model?
*   Is it gated?

## 6. Success Metrics & Analytics
*   What events should be tracked? (e.g., "Clicked Signup", "Completed Onboarding")
```
