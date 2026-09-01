"""Executable tests for the bounded CapabilityPort conformance profile."""

from __future__ import annotations

from copy import deepcopy
import unittest

from conformance.capability_port import validate_capability_port


def valid_port() -> dict[str, object]:
    return {
        "port_id": "port:titan:reader:crystal",
        "semantic_version": "0.1.0",
        "source_domain": "Titan",
        "target_domain": "Crystal",
        "capability_name": "bounded-reader-request",
        "capability_owner": "Crystal",
        "transport": "interface:reader/v1",
        "input_contract": "reader-request/v1",
        "output_contract": "reader-result/v1",
        "provenance_contract": "source-span/v1",
        "transformations": "NONE",
        "declared_loss": {
            "classification": "NONE",
            "check": "exact source identity and span retained",
        },
        "side_effects": "NONE",
        "target_admission_required": True,
        "compatibility_constraints": "source=v1,target=v1; otherwise reject",
        "revocation_semantics": "target may revoke port_id at any time",
    }


class CapabilityPortConformanceTests(unittest.TestCase):
    def test_valid_transfer_conforms(self) -> None:
        self.assertTrue(validate_capability_port(valid_port()).conforming)

    def test_missing_provenance_fails_closed(self) -> None:
        port = valid_port()
        del port["provenance_contract"]
        result = validate_capability_port(port)
        self.assertFalse(result.conforming)
        self.assertIn("missing required fields: provenance_contract", result.errors)

    def test_unknown_critical_field_fails_closed(self) -> None:
        port = valid_port()
        port["provenance_contract"] = "UNKNOWN"
        result = validate_capability_port(port)
        self.assertFalse(result.conforming)
        self.assertIn(
            "provenance_contract must be a non-empty known string",
            result.errors,
        )

    def test_declared_loss_requires_classification_and_check(self) -> None:
        port = valid_port()
        port["declared_loss"] = {"classification": "PARTIAL"}
        self.assertFalse(validate_capability_port(port).conforming)

    def test_incompatible_or_ambiguous_versions_fail_closed(self) -> None:
        port = valid_port()
        port["semantic_version"] = "latest"
        self.assertFalse(validate_capability_port(port).conforming)

    def test_revocation_semantics_are_required(self) -> None:
        port = valid_port()
        port["revocation_semantics"] = ""
        self.assertFalse(validate_capability_port(port).conforming)

    def test_target_cannot_waive_admission(self) -> None:
        port = valid_port()
        port["target_admission_required"] = False
        self.assertFalse(validate_capability_port(port).conforming)

    def test_side_effects_must_be_explicit_and_bounded(self) -> None:
        port = valid_port()
        port["side_effects"] = []
        self.assertFalse(validate_capability_port(port).conforming)

    def test_attempted_authority_escalation_fails_closed(self) -> None:
        for field in (
            "truth_authority",
            "identity_authority",
            "action_authority",
            "target_admission_waived",
            "production_authorized",
        ):
            with self.subTest(field=field):
                port = deepcopy(valid_port())
                port[field] = True
                result = validate_capability_port(port)
                self.assertFalse(result.conforming)
                self.assertTrue(any("forbidden authority fields" in e for e in result.errors))

    def test_unsupported_authority_field_fails_closed(self) -> None:
        port = valid_port()
        port["governance_authority"] = "global"
        result = validate_capability_port(port)
        self.assertFalse(result.conforming)
        self.assertIn("unsupported fields: governance_authority", result.errors)

    def test_validation_is_deterministic(self) -> None:
        port = valid_port()
        port["semantic_version"] = "bad"
        port["target_admission_required"] = False
        self.assertEqual(validate_capability_port(port), validate_capability_port(port))


if __name__ == "__main__":
    unittest.main()
