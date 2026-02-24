# Claude Code Config

[@shiroyasha9](https://github.com/shiroyasha9)'s configuration for [Claude Code](https://docs.anthropic.com/en/docs/claude-code).

## Files

| File | Purpose |
|---|---|
| `CLAUDE.md` | System prompt — tone, code style, workflow rules, core principles |
| `settings.json` | Runtime config — env vars, permissions, plugins, statusline |
| `keybindings.json` | Full keybinding overrides across all UI contexts |
| `statusline-command.sh` | Custom statusline: cwd, git branch, active PR, model, context % |
| `agents/DocsExplorer.md` | Subagent that fetches library docs via Context7 MCP with web fallback |

## Highlights

- Default mode: `plan` — forces planning before execution
- Package manager: `bun`
- Plugins: safety-net, code-review, typescript-lsp, ui-ux-pro-max, frontend-design
- `.env` files are denied from read/write/bash access
- Agent teams enabled via `CLAUDE_CODE_EXPERIMENTAL_AGENT_TEAMS`
- Statusline shows git branch + open PR number (via `gh`) + context window usage
