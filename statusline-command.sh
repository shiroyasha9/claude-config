#!/usr/bin/env bash
input=$(cat)

cwd=$(echo "$input" | jq -r '.workspace.current_dir // .cwd')
model=$(echo "$input" | jq -r '.model.display_name')
used=$(echo "$input" | jq -r '.context_window.used_percentage // empty')

# Shorten cwd: replace $HOME with ~
home="$HOME"
short_cwd="${cwd/#$home/\~}"

# Git branch (skip optional locks)
git_branch=""
if git -C "$cwd" rev-parse --git-dir --no-optional-locks > /dev/null 2>&1; then
  branch=$(git -C "$cwd" symbolic-ref --short HEAD 2>/dev/null || git -C "$cwd" rev-parse --short HEAD 2>/dev/null)
  if [ -n "$branch" ]; then
    git_branch=" $branch"
    # Check for active PR on this branch
    pr_num=$(gh pr view --json number -q '.number' 2>/dev/null)
  fi
fi

# Context usage
ctx_info=""
if [ -n "$used" ] && [ "$used" != "null" ]; then
  used_int=$(printf "%.0f" "$used")
  ctx_info="  ${used_int}%"
fi

if [ -n "$pr_num" ]; then
  printf "\033[34m%s\033[0m\033[90m%s \033[32mPR #%s\033[0m  \033[33m%s\033[0m%s" \
    "$short_cwd" "$git_branch" "$pr_num" "$model" "$ctx_info"
else
  printf "\033[34m%s\033[0m\033[90m%s\033[0m  \033[33m%s\033[0m%s" \
    "$short_cwd" "$git_branch" "$model" "$ctx_info"
fi
