# Tone 

- Only report to me in ASD-STE100 Simplified Technical English.
- Don't echo large code blocks or file contents unless asked; no verbose snippets.
- End each plan or findings document with unresolved questions, if any.
- Use regular hyphens instead of em-dashes.

# Development

- Always use `bun` as the package manager unless explicitly specified otherwise.
- Before any `npx/pnpm dlx/bunx` command, check `package.json` for existing similar scripts.
- For any third-party library, always look up official documentation (use the DocsExplorer subagent) - training data may be stale.
- For any file search or grep in git-indexed directories, use fff tools - including delegated work: explicitly instruct subagents/teams to use fff (they default to plain grep/glob).

# Subagents

- Use subagents/teams liberally: offload research, exploration, and parallel analysis to keep main context clean. One task per subagent.
- Parallelize wherever possible: planning by planners, development by engineers.

# Code Style

- **No comments by default.** Only WHY comments survive: workarounds, counterintuitive constraints, non-obvious invariants, why-not-the-obvious-thing decisions. WHAT comments banned; when in doubt, no comment. Match or undercut the surrounding file's comment density.
- Always use theme tokens for colors - never hardcoded hex. Differentiate between official and third-party styling when applying theme colors.

# Quality Assurance

- After code changes: run the project's formatter/linter and type check; fix all issues before declaring the task complete.
- **No Laziness**: Always find root causes. No temporary fixes.