# Project Planning Guidelines

**Goal:** effectively break down PRDs into actionable specific tasks.

## Prioritization Framework

When creating a task list or roadmap:

1.  **Phase 1: Critical Path / MVP**
    *   Core functionality without which the feature is useless.
    *   Fundamental infrastructure (Auth, Database Schema).
2.  **Phase 2: User Experience & Polish**
    *   Error states, loading states.
    *   Responsive layout adjustments.
    *   Animations.
3.  **Phase 3: Optimization & Scale**
    *   Performance tuning.
    *   Advanced analytics.

## Release Criteria

A task or epic is only "DONE" when:

1.  **Functionality**: Meets all requirements in the PRD.
2.  **Quality**:
    *   Linting passes.
    *   TypeScript compiles with no errors.
    *   Tests (Unit/Integration) pass.
3.  **UX/UI**:
    *   Verified on Mobile and Desktop viewports.
    *   Accessibility check (tab order, contrast) passed.
4.  **Billing**:
    *   Verified against subscription logic (e.g., free trial limits honored).

## Interaction Model

*   **Plan First**: Do not write code until a `task.md` or `implementation_plan.md` is approved.
*   **Iterate**: Break large tasks into smaller sub-tasks (1-2 hours of work).
*   **Verify**: Always include a verification step in the plan.
