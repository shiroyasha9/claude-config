## Communication

- Keep replies extremely concise; focus on key information only.
- No unnecessary fluff or verbose code snippets.
- Make plans extremely concise. Sacrifice grammar for brevity.
- End each plan with unresolved questions, if any.

## Development

### Core Rules

- When asked to fix or implement something, start coding immediately. Do NOT spend more than 5 minutes exploring/planning before producing actual code changes. If a plan is needed, write a brief bullet list (max 10 lines) then start implementing.
- Wherever possible, utilize a team to parallelize work. Planning can be done by planners; development can be done by engineers.
- When given a bug report: just fix it. Don't ask for hand-holding. Point at logs, errors, failing tests - then resolve them.
- Go fix failing CI tests without being told how.

### CLI/Commands

- Always use `bun` as the package manager unless explicitly specified otherwise.
- Before running any `npx/pnpm dlx/bunx` command, check `package.json` for existing similar scripts.

### Library Discovery

- When working with any third-party library, look up official documentation to ensure up-to-date information.
- Use the DocsExplorer subagent for efficient documentation lookup.

## Code Style

- Avoid unnecessary comments. Add comments only when code isn't self-explanatory.
- Prefer readable code over overly complex, hard-to-understand alternatives.
- Always use theme tokens (e.g., from the design system) for colors—never hardcoded hex values.
- Differentiate between official and third-party styling when applying theme colors.

## Quality Assurance

- After making code changes, run the project's configured formatter/linter. Fix all lint and formatting issues before declaring the task complete.
- After making code changes, run the project's type checking command. Fix all type-related issues before declaring the task complete.
- When verifying AI-flagged bugs or PR review comments, thoroughly validate before dismissing as false positive.
- If unsure, show the user the specific code path rather than making a unilateral judgment.
- Never mark a task complete without proving it works.
- Diff behavior between main and your changes when relevant.
- Ask yourself: "Would a staff engineer approve this?"
- Run tests, check logs, demonstrate correctness.

## Workflow Orchestration

### Planning

- Enter plan mode for ANY non-trivial task (3+ steps or architectural decisions).
- If something goes sideways, STOP and re-plan immediately - don't keep pushing.
- Use plan mode for verification steps, not just building.
- Write detailed specs upfront to reduce ambiguity.

### Subagent Strategy

- Use subagents/teams liberally to keep main context window clean.
- Offload research, exploration, and parallel analysis to subagents/teams.
- For complex problems, throw more compute at it via subagents/teams.
- One task per subagent/team for focused execution.

### Self-Improvement Loop

- After ANY correction from the user: update `tasks/lessons.md` with the pattern.
- Write rules for yourself that prevent the same mistake.
- Ruthlessly iterate on these lessons until mistake rate drops.
- Review lessons at session start for relevant project.

### Elegance

- For non-trivial changes: pause and ask "is there a more elegant way?"
- If a fix feels hacky: "Knowing everything I know now, implement the elegant solution."
- Skip this for simple, obvious fixes - don't over-engineer.
- Challenge your own work before presenting it.

## Task Management

1. **Plan First**: Write plan to `tasks/todo.md` with checkable items.
2. **Verify Plan**: Check in before starting implementation.
3. **Track Progress**: Mark items complete as you go.
4. **Explain Changes**: High-level summary at each step.
5. **Document Results**: Add review section to `tasks/todo.md`.
6. **Capture Lessons**: Update `tasks/lessons.md` after corrections.

## Core Principles

- **Simplicity First**: Make every change as simple as possible. Impact minimal code.
- **No Laziness**: Find root causes. No temporary fixes. Senior developer standards.
- **Minimal Impact**: Changes should only touch what's necessary. Avoid introducing bugs.


## Token Efficiency

- Don't echo back large blocks of code or file contents unless asked.
- Skip confirmations like "I'll continue..." Just do it.
- Do not summarize what you just did unless the result is ambiguous or you need additional input.
