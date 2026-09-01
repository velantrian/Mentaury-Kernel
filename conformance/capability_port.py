"""Deterministic CapabilityPort v0 conformance profile.

This validates a bounded representation of the specification. It does not
execute a capability or grant semantic, truth, identity, action, or runtime
authority.
"""

from __future__ import annotations

from dataclasses import dataclass
import re
from typing import Any, Mapping

PROFILE_VERSION = "capability-port-conformance/0"
PORT_SPEC_VERSION = "0.1"

_REQUIRED_FIELDS = frozenset(
    {
        "port_id",
        "semantic_version",
        "source_domain",
        "target_domain",
        "capability_name",
        "capability_owner",
        "transport",
        "input_contract",
        "output_contract",
        "provenance_contract",
        "transformations",
        "declared_loss",
        "side_effects",
        "target_admission_required",
        "compatibility_constraints",
        "revocation_semantics",
    }
)
_FORBIDDEN_AUTHORITY_FIELDS = frozenset(
    {
        "truth_authority",
        "identity_authority",
        "action_authority",
        "target_admission_waived",
        "production_authorized",
    }
)
_SEMVER = re.compile(r"^(0|[1-9]\d*)\.(0|[1-9]\d*)\.(0|[1-9]\d*)$")


@dataclass(frozen=True)
class ConformanceResult:
    profile_version: str
    spec_version: str
    conforming: bool
    errors: tuple[str, ...]


def validate_capability_port(value: object) -> ConformanceResult:
    errors: list[str] = []
    if not isinstance(value, Mapping):
        return _result(("port must be an object",))

    keys = frozenset(value)
    missing = sorted(_REQUIRED_FIELDS - keys)
    forbidden = sorted(_FORBIDDEN_AUTHORITY_FIELDS & keys)
    unsupported = sorted(keys - _REQUIRED_FIELDS - _FORBIDDEN_AUTHORITY_FIELDS)
    if missing:
        errors.append(f"missing required fields: {', '.join(missing)}")
    if forbidden:
        errors.append(f"forbidden authority fields: {', '.join(forbidden)}")
    if unsupported:
        errors.append(f"unsupported fields: {', '.join(unsupported)}")

    for field in (
        "port_id",
        "semantic_version",
        "source_domain",
        "target_domain",
        "capability_name",
        "capability_owner",
        "transport",
        "input_contract",
        "output_contract",
        "provenance_contract",
        "compatibility_constraints",
        "revocation_semantics",
    ):
        if field in value and not _known_nonempty_string(value[field]):
            errors.append(f"{field} must be a non-empty known string")

    semantic_version = value.get("semantic_version")
    if _known_nonempty_string(semantic_version) and not _SEMVER.fullmatch(semantic_version):
        errors.append("semantic_version must use MAJOR.MINOR.PATCH")

    if (
        _known_nonempty_string(value.get("source_domain"))
        and value.get("source_domain") == value.get("target_domain")
    ):
        errors.append("source_domain and target_domain must differ")

    if value.get("target_admission_required") is not True:
        errors.append("target_admission_required must be true")

    _validate_string_list(value, "transformations", errors, allow_none_token=True)
    _validate_side_effects(value.get("side_effects"), errors)
    _validate_declared_loss(value.get("declared_loss"), errors)

    return _result(tuple(sorted(set(errors))))


def _validate_string_list(
    value: Mapping[str, Any],
    field: str,
    errors: list[str],
    *,
    allow_none_token: bool = False,
) -> None:
    item = value.get(field)
    if allow_none_token and item == "NONE":
        return
    if not isinstance(item, list) or not item:
        errors.append(f"{field} must be NONE or a non-empty known string list")
        return
    if any(not _known_nonempty_string(entry) for entry in item):
        errors.append(f"{field} entries must be non-empty known strings")
    elif len(set(item)) != len(item):
        errors.append(f"{field} entries must be unique")


def _validate_side_effects(value: object, errors: list[str]) -> None:
    if value == "NONE":
        return
    if not isinstance(value, list) or not value:
        errors.append("side_effects must be NONE or a non-empty bounded known string list")
        return
    if any(not _known_nonempty_string(entry) for entry in value):
        errors.append("side_effects entries must be non-empty known strings")
    elif len(set(value)) != len(value):
        errors.append("side_effects entries must be unique")


def _validate_declared_loss(value: object, errors: list[str]) -> None:
    if not isinstance(value, Mapping):
        errors.append("declared_loss must be an object")
        return
    if frozenset(value) != {"classification", "check"}:
        errors.append("declared_loss requires exact classification and check fields")
        return
    if not _known_nonempty_string(value.get("classification")):
        errors.append("declared_loss.classification must be a non-empty known string")
    if not _known_nonempty_string(value.get("check")):
        errors.append("declared_loss.check must be a non-empty known string")


def _known_nonempty_string(value: object) -> bool:
    return (
        isinstance(value, str)
        and bool(value)
        and value == value.strip()
        and value != "UNKNOWN"
    )


def _result(errors: tuple[str, ...]) -> ConformanceResult:
    return ConformanceResult(
        profile_version=PROFILE_VERSION,
        spec_version=PORT_SPEC_VERSION,
        conforming=not errors,
        errors=errors,
    )
