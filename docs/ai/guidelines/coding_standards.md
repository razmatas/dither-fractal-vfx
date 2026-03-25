# Coding Standards

**Goal:** Ensure consistent, high-quality, and maintainable code.

## General Principles

1.  **TypeScript Everywhere**: No `any`. Use strict typing.
2.  **Idempotency**: Scripts and migrations should be re-runnable without side effects.
3.  **Secrets Management**: NEVER hardcode secrets. Use `.env` and `process.env`.

## Frontend Development

1.  **Component Structure**:
    *   Colocate tests with components if possible.
    *   Use functional components and hooks.
2.  **Styling**:
    *   Use **Tailwind CSS**.
    *   Ensure responsive design is implemented using Tailwind utility classes (`md:`, `lg:`).
3.  **Accessibility (a11y)**:
    *   All interactive elements must be keyboard accessible.
    *   Images must have `alt` text.
    *   Use semantic HTML (`<button>`, `<nav>`, `<main>`).
4.  **Performance**:
    *   Optimize images (Next.js Image component).
    *   Minimize bundle size.
    *   Target good **Core Web Vitals**.

## Backend & API

1.  **Security**:
    *   Validate all inputs (e.g., using Zod).
    *   Implement proper CSRF protection.
    *   Rate limit API routes.
2.  **Database**:
    *   Use migrations for schema changes.
    *   Index frequently queried fields.

## Testing

1.  **Requirement**: Tests are required for all user-visible changes and critical logic (e.g., billing, auth).
2.  **Types**:
    *   **Unit**: For utilities and complex logic.
    *   **Integration**: For API routes and component interactions.
    *   **E2E**: For critical user flows (Signup -> Checkout).
3.  **Do Not Reduce Coverage**: Verify tests pass before merging/completing tasks.

## Documentation

1.  **Self-Documenting Code**: Clear variable and function names.
2.  **Comments**: Explain *why*, not *what*, for complex logic.
3.  **CHANGELOG**: Update `CHANGELOG.md` when completing significant features.
