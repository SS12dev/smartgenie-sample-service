from __future__ import annotations

import argparse
import sys
from pathlib import Path
import re

SERVICE_FILES = {
    "agent-assistant": "agent-assistant-patch.yaml",
    "agent-analytics": "agent-analytics-patch.yaml",
}


def update_tag_in_file(file_path: Path, tag: str) -> bool:
    text = file_path.read_text(encoding="utf-8")
    updated_text, replacements = re.subn(
        r"(^\s*tag:\s*)(\S+)(\s*$)",
        lambda match: f"{match.group(1)}{tag}{match.group(3)}",
        text,
        count=1,
        flags=re.MULTILINE,
    )

    if replacements != 1:
        raise ValueError(f"Expected exactly one image tag in {file_path}, found {replacements}.")

    if updated_text == text:
        return False

    file_path.write_text(updated_text, encoding="utf-8")
    return True


def build_target_files(gitops_dir: Path, environment: str, services: list[str] | None) -> list[Path]:
    selected_services = services or list(SERVICE_FILES)
    env_dir = gitops_dir / "environments" / environment

    missing = [service for service in selected_services if service not in SERVICE_FILES]
    if missing:
        raise ValueError(f"Unsupported service selection: {', '.join(missing)}")

    target_files = [env_dir / SERVICE_FILES[service] for service in selected_services]
    for file_path in target_files:
        if not file_path.exists():
            raise FileNotFoundError(f"Expected patch file was not found: {file_path}")

    return target_files


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Update SmartGenie GitOps image tags for one environment.")
    parser.add_argument("--gitops-dir", required=True, help="Path to the checked-out sg-gitops repository")
    parser.add_argument("--environment", required=True, choices=["dev", "qa", "preprod", "prod"])
    parser.add_argument("--tag", required=True, help="Immutable image tag to write into the GitOps patch files")
    parser.add_argument(
        "--service",
        action="append",
        choices=sorted(SERVICE_FILES),
        help="Optional service name. Repeat to limit updates to specific services.",
    )
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    gitops_dir = Path(args.gitops_dir).resolve()

    updated_files: list[Path] = []
    for file_path in build_target_files(gitops_dir, args.environment, args.service):
        changed = update_tag_in_file(file_path, args.tag)
        state = "updated" if changed else "already-current"
        print(f"{state}: {file_path}")
        if changed:
            updated_files.append(file_path)

    if not updated_files:
        print("No GitOps files needed changes.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
