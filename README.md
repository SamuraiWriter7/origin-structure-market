## Repository Status

**Version:** v0.3.0-candidate
**Stage:** Experimental protocol
**Current scope:** Origin Asset registration + Derivative Asset registration + Origin Audit Record

The current version implements three core layers:

```text
Origin Asset
    ↓
Derivative Asset
    ↓
Origin Audit Record
```

v0.1 established the origin registration layer.
v0.2 added the derivative lineage layer.
v0.3 adds the origin audit layer, allowing derivative claims to be evaluated through similarity scores, contribution estimates, audit evidence, judgment status, and human review boundaries.

---

## Current Features

* JSON Schema for Origin Asset registration
* YAML example for an Origin Asset record
* JSON Schema for Derivative Asset registration
* YAML example for a Derivative Asset record
* JSON Schema for Origin Audit Record
* YAML example for an Origin Audit Record
* Python validation script
* GitHub Actions workflow for CI validation
* Protocol overview document
* Derivative Asset registration documentation

---

## Directory Structure

```text
origin-structure-market/
├── .github/
│   └── workflows/
│       └── validate.yml
├── docs/
│   ├── origin-structure-market-overview.md
│   └── derivative-asset-registration.md
├── examples/
│   ├── origin-asset.example.yaml
│   ├── derivative-asset.example.yaml
│   └── origin-audit-record.example.yaml
├── schemas/
│   ├── origin-asset.schema.json
│   ├── derivative-asset.schema.json
│   └── origin-audit-record.schema.json
├── scripts/
│   └── validate_examples.py
├── CHANGELOG.md
└── README.md
```

---

## Origin Asset Schema

The Origin Asset schema is located at:

```text
schemas/origin-asset.schema.json
```

It defines the structure of an upstream origin registration record.

A valid Origin Asset record must include:

* `id`
* `title`
* `creator`
* `asset_type`
* `description`
* `canonical_hash`
* `timestamp`
* `permission`
* `royalty_policy`
* `trace`

---

## Derivative Asset Schema

The Derivative Asset schema is located at:

```text
schemas/derivative-asset.schema.json
```

It defines the structure of a downstream asset derived from one or more upstream Origin Assets or Derivative Assets.

A valid Derivative Asset record must include:

* `id`
* `title`
* `creator`
* `asset_type`
* `description`
* `timestamp`
* `derived_from`
* `output`
* `proposed_royalty_split`
* `trace`

The `derived_from` section records:

* upstream asset ID
* upstream asset role
* contribution claim
* transformation type
* optional evidence

---

## Origin Audit Record Schema

The Origin Audit Record schema is located at:

```text
schemas/origin-audit-record.schema.json
```

It defines the structure of an audit record used to evaluate a derivative claim.

A valid Origin Audit Record must include:

* `id`
* `target_asset_id`
* `target_asset_type`
* `auditor`
* `timestamp`
* `audit_scope`
* `compared_assets`
* `similarity`
* `judgment`
* `evidence`
* `human_review`

The Origin Audit Record layer allows the protocol to record:

* compared upstream assets
* structural similarity
* conceptual similarity
* lineage similarity
* workflow similarity
* contribution scores
* royalty relevance
* audit judgment status
* evidence
* human review boundary

This layer does not make AI the final judge.
It records structured audit evidence and preserves a human review boundary.

---

## Validation

Install dependencies:

```bash
pip install jsonschema PyYAML
```

Run validation:

```bash
python scripts/validate_examples.py
```

Expected output:

```text
[validate] Origin Asset
  schema : schemas/origin-asset.schema.json
  example: examples/origin-asset.example.yaml
[ok] Origin Asset example is valid
[validate] Derivative Asset
  schema : schemas/derivative-asset.schema.json
  example: examples/derivative-asset.example.yaml
[ok] Derivative Asset example is valid
[validate] Origin Audit Record
  schema : schemas/origin-audit-record.schema.json
  example: examples/origin-audit-record.example.yaml
[ok] Origin Audit Record example is valid
[done] all examples are valid
```

---

## Conceptual Architecture

```text
Origin Asset
    ↓
Derivative Asset
    ↓
Origin Audit Record
    ↓
Royalty Allocation Graph
    ↓
Value Returned to Origin
```

v0.1 implements:

```text
Origin Asset Registration
```

v0.2 implements:

```text
Derivative Asset Registration
```

v0.3 implements:

```text
Origin Audit Record
```

Together, v0.1 to v0.3 establish the first verifiable lineage stack:

```text
source structure → downstream derivative → audit record
```

---

## Roadmap

### v0.1 — Origin Asset Registration

Implemented:

* Define `origin-asset.schema.json`
* Add example YAML
* Add validation script
* Add GitHub Actions workflow

### v0.2 — Derivative Asset Registration

Implemented:

* Define `derivative-asset.schema.json`
* Add derivative asset example YAML
* Track upstream origin or derivative assets
* Record transformation types
* Record contribution claims
* Record trace evidence
* Declare proposed royalty splits
* Add Derivative Asset validation to CI

### v0.3 — Origin Audit Record

Implemented:

* Define `origin-audit-record.schema.json`
* Add origin audit record example YAML
* Compare target assets with upstream assets
* Record structural, conceptual, lineage, workflow, and overall similarity
* Record contribution scores
* Record royalty relevance
* Record audit evidence
* Preserve human review boundary
* Add Origin Audit Record validation to CI

### v0.4 — Royalty Allocation Graph

Planned additions:

* Define revenue event structure
* Allocate revenue to origin creators, derivative creators, auditors, and protocol funds
* Support off-chain, on-chain, and hybrid settlement
* Connect audit contribution scores to proposed allocation logic

### v0.5 — Marketplace Layer

Planned additions:

* Define listing metadata
* Define license templates
* Add search and discovery fields
* Prepare for integration with external marketplaces or registries
