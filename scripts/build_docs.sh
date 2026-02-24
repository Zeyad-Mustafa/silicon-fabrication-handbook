#!/usr/bin/env bash
set -euo pipefail

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
REPO_ROOT="$(cd "${SCRIPT_DIR}/.." && pwd)"

PYTHON_BIN="${PYTHON_BIN:-python3}"
TOC_SCRIPT="${SCRIPT_DIR}/generate_toc.py"
LINK_SCRIPT="${SCRIPT_DIR}/check_links.py"

usage() {
  cat <<'EOF'
Usage: scripts/build_docs.sh [build|check] [paths...]

Modes:
  build   Update Markdown TOCs, then validate links (default)
  check   Verify TOCs are up to date, then validate links (no file writes)

Examples:
  scripts/build_docs.sh
  scripts/build_docs.sh check
  scripts/build_docs.sh build README.md docs
EOF
}

if ! command -v "${PYTHON_BIN}" >/dev/null 2>&1; then
  echo "Error: Python interpreter not found: ${PYTHON_BIN}" >&2
  exit 127
fi

if [[ ! -f "${TOC_SCRIPT}" || ! -f "${LINK_SCRIPT}" ]]; then
  echo "Error: expected scripts not found in ${SCRIPT_DIR}" >&2
  exit 1
fi

MODE="build"
if [[ $# -gt 0 ]]; then
  case "$1" in
    build|check)
      MODE="$1"
      shift
      ;;
    -h|--help)
      usage
      exit 0
      ;;
  esac
fi

DEFAULT_TOC_PATHS=("docs")
DEFAULT_LINK_PATHS=("README.md" "PROJECT_STRUCTURE.md" "docs")
USER_PATHS=("$@")

run_step() {
  local label="$1"
  shift
  echo ""
  echo "==> ${label}"
  "$@"
}

run_step_capture() {
  local label="$1"
  shift
  local rc=0
  echo ""
  echo "==> ${label}"
  set +e
  "$@"
  rc=$?
  set -e
  return "${rc}"
}

cd "${REPO_ROOT}"

if [[ "${MODE}" == "check" ]]; then
  toc_rc=0
  link_rc=0
  if [[ ${#USER_PATHS[@]} -gt 0 ]]; then
    run_step_capture "Checking TOCs" "${PYTHON_BIN}" "${TOC_SCRIPT}" --check "${USER_PATHS[@]}" || toc_rc=$?
    run_step_capture "Checking links" "${PYTHON_BIN}" "${LINK_SCRIPT}" "${USER_PATHS[@]}" || link_rc=$?
  else
    run_step_capture "Checking TOCs" "${PYTHON_BIN}" "${TOC_SCRIPT}" --check "${DEFAULT_TOC_PATHS[@]}" || toc_rc=$?
    run_step_capture "Checking links" "${PYTHON_BIN}" "${LINK_SCRIPT}" "${DEFAULT_LINK_PATHS[@]}" || link_rc=$?
  fi
  echo ""
  if [[ ${toc_rc} -eq 0 && ${link_rc} -eq 0 ]]; then
    echo "Docs pipeline completed (check)."
    exit 0
  fi
  echo "Docs pipeline failed (check): toc=${toc_rc}, links=${link_rc}" >&2
  exit 1
else
  if [[ ${#USER_PATHS[@]} -gt 0 ]]; then
    run_step "Updating TOCs" "${PYTHON_BIN}" "${TOC_SCRIPT}" "${USER_PATHS[@]}"
    run_step "Checking links" "${PYTHON_BIN}" "${LINK_SCRIPT}" "${USER_PATHS[@]}"
  else
    run_step "Updating TOCs" "${PYTHON_BIN}" "${TOC_SCRIPT}" "${DEFAULT_TOC_PATHS[@]}"
    run_step "Checking links" "${PYTHON_BIN}" "${LINK_SCRIPT}" "${DEFAULT_LINK_PATHS[@]}"
  fi
fi

echo ""
echo "Docs pipeline completed (${MODE})."
