# Changelog

All notable changes to this project will be documented in this file.

This project follows a candidate-based release flow during early protocol development.

---

## [v0.1.0-candidate] - 2026-06-22

### Added

* Added initial **Origin Asset** schema.

  * `schemas/origin-asset.schema.json`
  * Defines the machine-readable registration format for upstream intellectual structures.
  * Supports creator identity, asset type, canonical hash, timestamp, permissions, royalty policy, and trace links.

* Added initial Origin Asset example.

  * `examples/origin-asset.example.yaml`
  * Demonstrates how the Origin Structure Market itself can be registered as an origin asset.

* Added validation script.

  * `scripts/validate_examples.py`
  * Validates YAML examples against JSON Schema using `jsonschema` and `PyYAML`.

* Added GitHub Actions validation workflow.

  * `.github/workflows/validate.yml`
  * Runs schema validation on push, pull request, and manual dispatch.

* Added protocol overview document.

  * `docs/origin-structure-market-overview.md`
  * Explains the core concept, problem, solution, architecture, MVP scope, and long-term vision.

* Added initial README.

  * `README.md`
  * Introduces Origin Structure Market as a protocol-oriented framework for registering origin assets, tracing derivatives, and enabling royalty allocation back to the source.

---

### Defined

* Defined **Origin Structure Market** as an experimental protocol for AI-era structural provenance and royalty circulation.

* Defined **Origin Asset** as a structured registration record for reusable intellectual structures such as:

  * GPT instructions
  * Prompt architecture
  * AI workflow schemas
  * Trace receipt schemas
  * Royalty allocation templates
  * Origin audit rubrics
  * Article frameworks
  * Book frameworks
  * Business models
  * Conceptual frameworks
  * AI structure frameworks

* Established the v0.1 scope as:

  > Origin Asset Registration

* Established the core principle:

  > Value should flow back to the structural origin.

---

### Validation

The following validation target is included:

```text
Origin Asset
  schema : schemas/origin-asset.schema.json
  example: examples/origin-asset.example.yaml
```

Expected validation result:

```text
[validate] Origin Asset
  schema : schemas/origin-asset.schema.json
  example: examples/origin-asset.example.yaml
[ok] Origin Asset example is valid
[done] all examples are valid
```

---

### Notes

This version does not implement derivative tracking, origin audits, contribution scoring, or royalty allocation graphs yet.

Those layers are planned for future versions:

* v0.2 — Derivative Asset Registration
* v0.3 — Origin Audit Record
* v0.4 — Royalty Allocation Graph
* v0.5 — Marketplace Layer

---

## Roadmap

### v0.2 — Derivative Asset Registration

Planned additions:

* `schemas/derivative-asset.schema.json`
* `examples/derivative-asset.example.yaml`
* upstream origin references
* transformation type records
* contribution claim fields
* proposed royalty split declarations

### v0.3 — Origin Audit Record

Planned additions:

* structural similarity records
* conceptual similarity records
* contribution score calculation fields
* AI-assisted audit evidence
* human review boundary

### v0.4 — Royalty Allocation Graph

Planned additions:

* revenue event records
* allocation graph schema
* origin creator allocation
* derivative creator allocation
* auditor allocation
* protocol fund allocation

### v0.5 — Marketplace Layer

Planned additions:

* listing metadata
* license templates
* search and discovery fields
* marketplace integration preparation
