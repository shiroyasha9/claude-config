## Tone 

- Keep replies extremely concise; focus on key information only.
- No unnecessary fluff or verbose code snippets.
- Keep plans extremely concise. Sacrifice grammar for brevity.
- End each plan or findings document with unresolved questions, if any.
- Use regular hyphens instead of em-dashes.


## Development

### Core Rules

- Always create a todo list to track progress of the plan. 
- Wherever possible, utilize a team to parallelize work. Planning can be done by planners; development can be done by engineers.

### CLI/Commands

- Always use `bun` as the package manager unless explicitly specified otherwise.
- Before running any `npx/pnpm dlx/bunx` command, check `package.json` for existing similar scripts.

### Library Discovery

- When working with any third-party library or something similar, you MUST always look up the official documentation to ensure you're working with up-to-date information.
- Use the DocsExplorer subagent for efficient documentation lookup.

### File Search: Finding Code / Files 

- For any file search or grep in the current git-indexed directory, use fff tools.
- This applies to delegated work too: when dispatching a subagent/team to search or explore, explicitly instruct it to use fff tools (Explore/general agents default to plain grep/glob otherwise).

## Code Style

- **No comments by default.** Zero. Identifiers and types carry the meaning. Restating what code does is banned (e.g. `// loop over users`, `// set the flag`, `// fetch data`).
- The ONLY allowed comments: documenting a workaround, a counterintuitive constraint, a non-obvious invariant, or a "why-not-the-obvious-thing" decision. If the comment explains WHAT, delete it; only WHY may survive.
- "Self-explanatory" / "non-obvious" are not escape hatches. Treat them as near-never. When in doubt, no comment.
- Do not add comments to satisfy perceived documentation norms. Match (or undercut) the surrounding file's comment density.
- Prefer readable code over overly complex, hard-to-understand alternatives.
- Always use theme tokens (e.g., from the design system) for colors—never hardcoded hex values.
- Differentiate between official and third-party styling when applying theme colors.

### Quality Assurance

- After making code changes, run the project's configured formatter/linter. Fix all lint and formatting issues before declaring the task complete.
- After making code changes, run the project's type checking command. Fix all type-related issues before declaring the task complete.
- When verifying AI-flagged bugs or PR review comments, thoroughly validate before dismissing as false positive.
- Ask yourself: "Would a staff engineer approve this?"

## Workflow Orchestration

### Planning

- Enter plan mode for ANY non-trivial task (3+ steps or architectural decisions).
- If something goes sideways, STOP and re-plan immediately - don't keep pushing.
- Write detailed specs upfront to reduce ambiguity.

### Subagent Strategy

- Use subagents/teams liberally to keep main context window clean.
- Offload research, exploration, and parallel analysis to subagents/teams.
- For complex problems, throw more compute at it via subagents/teams.
- One task per subagent/team for focused execution.

### Self-Improvement Loop

- At the end of each session, provide a one line summary of the session's learnings, in a way that can be copy pasted into the CLAUDE.md file.

### Elegance

- For non-trivial changes: pause and ask "is there a more elegant way?"
- If a fix feels hacky: "Knowing everything I know now, implement the elegant solution."

## Core Principles

- **No Laziness**: Always find root causes. No temporary fixes. Senior developer standards.
- Always think through the implications of your changes - to avoid any regressions or bugs.


## Token Efficiency

- Don't echo back large blocks of code or file contents unless asked.
- Skip confirmations like "I'll continue..." Just do it.
- Do not summarize what you just did unless the result is ambiguous or you need additional input.
