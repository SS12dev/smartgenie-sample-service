from pathlib import Path

from scripts.update_gitops_tags import update_tag_in_file


SAMPLE_PATCH = """apiVersion: helm.toolkit.fluxcd.io/v2
kind: HelmRelease
metadata:
  name: agent-assistant
spec:
  values:
    image:
      repository: ghcr.io/ss12dev/smartgenie-agent-assistant
      tag: qa-latest
      pullPolicy: IfNotPresent
"""


def test_update_tag_in_file_replaces_existing_tag(tmp_path: Path) -> None:
    patch_file = tmp_path / "agent-assistant-patch.yaml"
    patch_file.write_text(SAMPLE_PATCH, encoding="utf-8")

    changed = update_tag_in_file(patch_file, "sha-123abcd")

    assert changed is True
    assert "tag: sha-123abcd" in patch_file.read_text(encoding="utf-8")


def test_update_tag_in_file_is_idempotent_for_same_tag(tmp_path: Path) -> None:
    patch_file = tmp_path / "agent-assistant-patch.yaml"
    patch_file.write_text(SAMPLE_PATCH.replace("qa-latest", "sha-123abcd"), encoding="utf-8")

    changed = update_tag_in_file(patch_file, "sha-123abcd")

    assert changed is False
    assert patch_file.read_text(encoding="utf-8").count("sha-123abcd") == 1
