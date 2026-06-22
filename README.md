# Origin Structure Market

**Origin Structure Market** is a protocol-oriented framework for registering AI-era ideas, structures, prompts, schemas, and conceptual systems as **origin assets**, tracing their derivatives, and enabling royalty allocation back to the source.

It is designed as an experimental standard for the AI creator economy, where value should not only accumulate at the final product or platform layer, but also flow back to the structural origin.

---

## Core Principle

> Value should flow back to the structural origin.

In the AI era, ideas are no longer consumed only as finished content.
They are transformed into prompts, workflows, GPT instructions, schemas, agents, articles, applications, business models, and new intellectual systems.

Origin Structure Market provides a machine-readable way to record:

* who created an origin structure
* when it was registered
* what canonical form it had
* how it may be reused
* what royalty policy applies
* how future derivatives can trace back to it

This project does **not** attempt to claim ownership over abstract ideas themselves.
Instead, it records **structured origin expressions**, their fingerprints, permissions, and traceable contribution paths.

---

## Problem

Modern AI and platform ecosystems have a broken value loop:

* Original ideas are reused without attribution
* AI-generated derivatives obscure upstream contributors
* Platforms capture most of the value
* Creators lose traceability once their work is transformed
* Conceptual frameworks are difficult to register, compare, and reward

In short:

> Creation does not reliably lead to compensation.

Origin Structure Market addresses this by treating reusable structures as first-class protocol objects.

---

## What Is an Origin Asset?

An **Origin Asset** is a structured registration record for an upstream intellectual structure.

Examples include:

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

An Origin Asset is not merely raw text.
It is a structured record containing:

* title
* creator
* asset type
* description
* canonical hash
* timestamp
* permission policy
* royalty policy
* trace links
* supporting evidence hashes

---

## Repository Status

**Version:** v0.1.0-candidate
**Stage:** Experimental protocol
**Current scope:** Origin Asset registration and validation

The first version focuses on one core function:

> Register an origin structure as a machine-readable asset.

Future versions will add derivative tracking, origin audits, contribution scoring, and royalty allocation graphs.

---

## Current Features

* JSON Schema for Origin Asset registration
* YAML example for an Origin Asset record
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
│   └── origin-asset.example.yaml
├── schemas/
│   └── origin-asset.schema.json
├── scripts/
│   └── validate_examples.py
├── CHANGELOG.md
└── README.md
```

---

## Origin Asset Schema

The main schema is located at:

```text
schemas/origin-asset.schema.json
```

It defines the structure of an origin asset record.

A valid record must include:

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

## Example

Example file:

```text
examples/origin-asset.example.yaml
```

Minimal structure:

```yaml
origin_asset:
  id: origin-2026-0001
  title: Origin Structure Market
  creator: SamuraiWriter7
  asset_type: ai_structure_framework
  description: >
    Origin Structure Market is a protocol-oriented framework for registering
    reusable AI-era ideas, structures, prompts, schemas, and conceptual systems
    as origin assets.

  canonical_hash: sha256:aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa
  timestamp: "2026-06-21T00:00:00Z"
  version: v0.1.0-candidate
  jurisdiction: global

  permission:
    derivative_allowed: true
    commercial_use: true
    attribution_required: true
    ai_training_allowed: false
    ai_inference_allowed: true
    redistribution_allowed: true

  royalty_policy:
    default_rate: 0.05
    derivative_rate: 0.03
    audit_rate: 0.01
    protocol_fund_rate: 0.01
    currency: JPY
    settlement: hybrid

  trace:
    source_url: https://github.com/SamuraiWriter7/origin-structure-market
    repository_url: https://github.com/SamuraiWriter7/origin-structure-market
    related_assets:
      - ai-search-trace-receipt-standard
      - synchronization-audit-protocol
      - compute-access-royalty-os
```

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
[done] all examples are valid
```

---

## GitHub Actions

This repository includes a validation workflow:

```text
.github/workflows/validate.yml
```

The workflow runs on:

* push to `main`
* pull requests to `main`
* manual workflow dispatch

It validates YAML examples against the JSON Schema.

---

## Design Philosophy

Origin Structure Market is based on three principles.

### 1. Structure over content

The important unit is not only the finished text or product, but the reusable structure that generates future work.

### 2. Trace over ownership

The protocol focuses on traceable contribution rather than absolute ownership claims over abstract ideas.

### 3. Flow over storage

Value is defined by how structures move, transform, and generate downstream value.

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

v0.1 implements the first layer:

```text
Origin Asset Registration
```

---

## Relation to Other Protocols

Origin Structure Market is designed to connect with related Kazene ecosystem projects:

* AI Search Trace Receipt Standard
* Synchronization Audit Protocol
* Compute Access Royalty OS
* OKF Royalty OS Bridge
* Kazene Trace Receipt Protocol
* Structural Rumination Layer
* Multi-Wing Architecture

Together, these projects form a broader stack for:

```text
traceability → origin audit → contribution scoring → royalty allocation
```

---

## Roadmap

### v0.1 — Origin Asset Registration

* Define `origin-asset.schema.json`
* Add example YAML
* Add validation script
* Add GitHub Actions workflow

### v0.2 — Derivative Asset Registration

* Define derivative asset schema
* Track upstream origin assets
* Record transformation type
* Declare contribution claims

### v0.3 — Origin Audit Record

* Compare origin and derivative assets
* Record structural similarity
* Add confidence score
* Add human review boundary

### v0.4 — Royalty Allocation Graph

* Define revenue event structure
* Allocate revenue to origin creators, derivative creators, auditors, and protocol funds
* Support off-chain, on-chain, and hybrid settlement

### v0.5 — Marketplace Layer

* Define listing metadata
* Define license templates
* Add search and discovery fields
* Prepare for integration with external marketplaces or registries

---

## Non-Goals

This project does not attempt to:

* enforce legal ownership over all abstract ideas
* replace copyright law
* act as a court or final dispute resolver
* guarantee automatic royalty enforcement by itself
* require blockchain usage in v0.1

Instead, it provides a structured protocol foundation for future trace, audit, and allocation systems.

---

## License

License information will be defined in a future version.

Suggested initial direction:

```text
Kazene-Origin-License-0.1
```

or a compatible open license for experimental protocol development.

---

## Summary

Origin Structure Market is an experimental protocol for the AI era.

It asks a simple question:

> What if the origin of an idea could remain traceable after AI transforms it?

The answer is a new kind of market:

```text
not only a market for finished products,
but a market for reusable structures.
```

A system where:

* ideas become structured origin assets
* derivatives preserve lineage
* audits measure contribution
* revenue can flow back upstream
* creators become recognized as structural sources

In short:

> A market where value returns to the origin.
