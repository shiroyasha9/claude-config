#!/usr/bin/env python3
"""Export the version-worthy slice of ~/.claude.json into the tracked repo.

~/.claude.json is 95% machine state (per-project token counts, feature-flag
caches, session ids) and lives outside this repo, so it is neither committable
nor worth committing wholesale. This mirrors only KEEP_KEYS.
"""

import json
import re
import sys
from pathlib import Path

SOURCE = Path.home() / ".claude.json"
TARGET = Path.home() / ".claude" / "exported" / "claude.json"

KEEP_KEYS = ("mcpServers",)

SECRET_PREFIXES = re.compile(
    r"(sk-|ctx7sk-|ghp_|gho_|github_pat_|xox[abpsr]-|AKIA|glpat-|Bearer\s)"
)
SECRET_NAMES = re.compile(r"(TOKEN|KEY|SECRET|PASSWORD|PASSWD|CREDENTIAL)", re.I)
EXPANSION = re.compile(r"^\$\{[^}]+\}$")


def find_secrets(node, trail=()):
    if isinstance(node, dict):
        for key, value in node.items():
            if (
                isinstance(value, str)
                and SECRET_NAMES.search(key)
                and not EXPANSION.match(value)
            ):
                yield ".".join((*trail, key))
            yield from find_secrets(value, (*trail, key))
    elif isinstance(node, list):
        for index, value in enumerate(node):
            yield from find_secrets(value, (*trail, str(index)))
    elif isinstance(node, str) and SECRET_PREFIXES.search(node):
        yield ".".join(trail)


def main():
    source = json.loads(SOURCE.read_text())
    exported = {key: source[key] for key in KEEP_KEYS if key in source}

    leaks = sorted(set(find_secrets(exported)))
    if leaks:
        print(
            "refusing to export, literal credentials found at:\n  "
            + "\n  ".join(leaks)
            + "\nreplace each with ${ENV_VAR} in ~/.claude.json and export the "
            "real value from your shell profile.",
            file=sys.stderr,
        )
        return 1

    TARGET.parent.mkdir(parents=True, exist_ok=True)
    TARGET.write_text(json.dumps(exported, indent=2, sort_keys=True) + "\n")
    return 0


if __name__ == "__main__":
    sys.exit(main())
