# Antigravity Workflow

This document outlines the optimal workflow for building software with Antigravity. Unlike previous prompt-based workflows, Antigravity can read context directly. Instead of copy-pasting prompts, you will direct the agent to read specific **Guidelines**.

## 1. Project Initialization

When starting a new feature or epic, instruct the agent to read the PRD standards first.

**User Prompt:**
> "I want to build [Feature Name]. Please read `docs/ai/guidelines/prd_standards.md` help me plan this out."

The agent will:
1.  Ask clarifying questions based on the standards.
2.  Draft a PRD (Product Requirements Document) that covers all necessary details (Auth, Billing, responsive design, etc.).

## 2. Planning Phase

Before writing code, the agent should create a plan.

**User Prompt:**
> "Create an implementation plan and task list for this feature."

The agent will:
1.  Create `implementation_plan.md` in the brain artifacts folder.
2.  Create `task.md` to track progress.
3.  Cross-reference `docs/ai/guidelines/project_planning.md` to ensure the plan is robust (e.g., includes testing, release criteria).

## 3. Execution Phase

When the plan is approved, the agent moves to execution.

**User Prompt:**
> "Go ahead and execute step 1."

The agent will:
1.  Read `docs/ai/guidelines/coding_standards.md` to ensure code quality (TypeScript, testing, security).
2.  Write code and tests.
3.  Update `task.md` as it progresses.

## 4. Verification & Handover

Before marking a task as done, the agent must verify the work.

**User Prompt:**
> "Verify the work and update the walkthrough."

The agent will:
1.  Run tests and linting.
2.  Check against the **Release Criteria** in `docs/ai/guidelines/project_planning.md`.
3.  Update `walkthrough.md` with proof of work (screenshots, logs).

---

## Directory Structure

-   `docs/ai/guidelines/`: The source of truth for how we build software.
    -   `prd_standards.md`: Requirements for PRDs.
    -   `coding_standards.md`: Rules for code quality and stack.
    -   `project_planning.md`: Rules for roadmaps and task breakdowns.
-   `docs/ai/archive/`: Old prompt-based recipes (for reference only).
-   `docs/spec/`: Where active PRDs and specifications live.
