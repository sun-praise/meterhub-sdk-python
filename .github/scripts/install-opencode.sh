#!/usr/bin/env bash

set -euo pipefail

OPENCODE_BIN_DIR="${OPENCODE_INSTALL_DIR:-${RUNNER_TOOL_CACHE:-$HOME/.cache}/opencode/bin}"
OPENCODE_CACHE_DIR="${XDG_CACHE_HOME:-$HOME/.cache}"
INSTALL_URL="${OPENCODE_INSTALL_URL:-https://opencode.ai/install}"
MAX_ATTEMPTS="${OPENCODE_INSTALL_ATTEMPTS:-3}"

mkdir -p "$OPENCODE_BIN_DIR"
mkdir -p "$OPENCODE_CACHE_DIR"

export OPENCODE_INSTALL_DIR="$OPENCODE_BIN_DIR"
export XDG_CACHE_HOME="$OPENCODE_CACHE_DIR"
export PATH="$OPENCODE_BIN_DIR:$PATH"

link_opencode_bin() {
  local source_bin="$1"

  if [ -x "$source_bin" ] && [ "$source_bin" != "$OPENCODE_BIN_DIR/opencode" ]; then
    ln -sf "$source_bin" "$OPENCODE_BIN_DIR/opencode"
  fi
}

if command -v opencode >/dev/null 2>&1; then
  echo "OpenCode already installed at: $(command -v opencode)"
  opencode --version || true
  exit 0
fi

attempt=1
while [ "$attempt" -le "$MAX_ATTEMPTS" ]; do
  echo "Installing OpenCode (attempt ${attempt}/${MAX_ATTEMPTS})"

  if curl \
    --fail \
    --silent \
    --show-error \
    --location \
    --retry 5 \
    --retry-all-errors \
    --retry-delay 2 \
    "$INSTALL_URL" | bash; then
    break
  fi

  if [ "$attempt" -eq "$MAX_ATTEMPTS" ]; then
    echo "OpenCode installation failed after ${MAX_ATTEMPTS} attempts" >&2
    exit 1
  fi

  sleep $((attempt * 5))
  attempt=$((attempt + 1))
done

if [ ! -x "$OPENCODE_BIN_DIR/opencode" ] && [ -x "$HOME/.opencode/bin/opencode" ]; then
  link_opencode_bin "$HOME/.opencode/bin/opencode"
fi

if ! command -v opencode >/dev/null 2>&1; then
  echo "OpenCode install script finished, but 'opencode' is still unavailable" >&2
  exit 1
fi

echo "OpenCode installed at: $(command -v opencode)"
opencode --version || true
