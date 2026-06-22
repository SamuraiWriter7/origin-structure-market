## Repository Status

**Version:** v0.2.0-candidate
**Stage:** Experimental protocol
**Current scope:** Origin Asset registration + Derivative Asset registration

The current version implements two core layers:

```text
Origin Asset
    ↓
Derivative Asset
```

v0.1 established the origin registration layer.
v0.2 adds the derivative lineage layer, allowing downstream assets to declare their upstream origins, transformation types, contribution claims, trace evidence, and proposed royalty splits.

---

## Current Features

* JSON Schema for Origin Asset registration
* YAML example for an Origin Asset record
* JSON Schema for Derivative Asset registration
* YAML example for a Derivative Asset record
* Python validation script
* GitHub Actions workflow for CI validation
* Protocol overview document

---

## Directory Structure

```text
origin-structure-market/
├── .github/
│   └── workflows/
│       └── validate.yml
├── docs/
│   └── origin-structure-market-overview.md
├── examples/
│   ├── origin-asset.example.yaml
│   └── derivative-asset.example.yaml
├── schemas/
│   ├── origin-asset.schema.json
│   └── derivative-asset.schema.json
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

This allows a derivative asset to declare:

> This asset was created from these upstream structures, through these transformations, with this claimed contribution weight.

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
[done] all examples are valid
```

---

## Conceptual Architecture

```text
Origin Asset
    ↓
Derivative Asset
    ↓
Origin Audit
    ↓
Contribution Score
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

Together, v0.1 and v0.2 establish the first traceable lineage:

```text
source structure → downstream derivative
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

Planned additions:

* Compare origin and derivative assets
* Record structural similarity
* Record conceptual similarity
* Add confidence score
* Add AI-assisted audit evidence
* Add human review boundary

### v0.4 — Royalty Allocation Graph

Planned additions:

* Define revenue event structure
* Allocate revenue to origin creators, derivative creators, auditors, and protocol funds
* Support off-chain, on-chain, and hybrid settlement

### v0.5 — Marketplace Layer

Planned additions:

* Define listing metadata
* Define license templates
* Add search and discovery fields
* Prepare for integration with external marketplaces or registries

