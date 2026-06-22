# Origin Structure Market

**Origin Structure Market** is a protocol-oriented framework for registering AI-era ideas, structures, prompts, schemas, and conceptual systems as **Origin Assets**, tracing their derivatives, auditing derivative claims, and enabling royalty allocation back to the structural origin.

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
* what derivative assets were created from it
* how derivative claims can be audited
* how revenue can be allocated back to contributors

This project does **not** attempt to claim ownership over abstract ideas themselves.
Instead, it records **structured origin expressions**, their fingerprints, permissions, lineage, audit evidence, and allocation paths.

---

## Problem

Modern AI and platform ecosystems have a broken value loop:

* Original ideas are reused without attribution
* AI-generated derivatives obscure upstream contributors
* Platforms capture most of the value
* Creators lose traceability once their work is transformed
* Conceptual frameworks are difficult to register, compare, audit, and reward
* Revenue distribution rarely reaches the structural origin

In short:

> Creation does not reliably lead to compensation.

Origin Structure Market addresses this by treating reusable structures, derivative lineage, audit records, and allocation graphs as first-class protocol objects.

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

## What Is a Derivative Asset?

A **Derivative Asset** is a downstream asset derived from one or more upstream Origin Assets or Derivative Assets.

It records:

* upstream asset ID
* upstream asset role
* contribution claim
* transformation type
* shared concepts
* shared structure
* evidence hashes
* output metadata
* proposed royalty split
* human review status

This allows a downstream asset to declare:

> This asset was created from these upstream structures, through these transformations, with this claimed contribution weight.

---

## What Is an Origin Audit Record?

An **Origin Audit Record** is a structured audit record for evaluating whether a derivative claim is credible.

It records:

* target asset ID
* target asset type
* auditor
* audit method
* audit scope
* compared upstream assets
* structural similarity
* conceptual similarity
* lineage similarity
* workflow similarity
* overall similarity
* contribution scores
* royalty relevance
* audit judgment
* supporting evidence
* human review boundary

This layer does not make AI the final judge.
It records structured audit evidence and preserves a human review boundary.

---

## What Is a Royalty Allocation Graph?

A **Royalty Allocation Graph** is a structured record for converting a revenue event, audited lineage, contribution scores, and allocation policy into a proposed distribution of value.

It records:

* revenue event ID
* revenue-generating product or derivative asset
* gross revenue
* net revenue
* revenue source
* allocation basis
* audit record references
* contribution scores
* allocation policy
* recipient allocation entries
* settlement mechanism
* human review status
* trace links and evidence hashes

This layer does not execute payment by itself.

Instead, it provides a machine-readable allocation graph that can be used by:

* off-chain accounting systems
* marketplace logic
* royalty OS layers
* smart contracts
* human reviewers
* future settlement systems

---

## Repository Status

**Version:** v0.4.0-candidate
**Stage:** Experimental protocol
**Current scope:** Origin Asset registration + Derivative Asset registration + Origin Audit Record + Royalty Allocation Graph

The current version implements four core layers:

```text
Origin Asset
    ↓
Derivative Asset
    ↓
Origin Audit Record
    ↓
Royalty Allocation Graph
```

v0.1 established the origin registration layer.
v0.2 added the derivative lineage layer.
v0.3 added the origin audit layer.
v0.4 adds the royalty allocation layer, allowing audited lineage and contribution scores to be converted into proposed revenue distribution graphs.

---

## Current Features

* JSON Schema for Origin Asset registration
* YAML example for an Origin Asset record
* JSON Schema for Derivative Asset registration
* YAML example for a Derivative Asset record
* JSON Schema for Origin Audit Record
* YAML example for an Origin Audit Record
* JSON Schema for Royalty Allocation Graph
* YAML example for a Royalty Allocation Graph
* Python validation script
* GitHub Actions workflow for CI validation
* Protocol overview document
* Derivative Asset registration documentation
* Origin Audit Record documentation

---

## Directory Structure

```text
origin-structure-market/
├── .github/
│   └── workflows/
│       └── validate.yml
├── docs/
│   ├── origin-structure-market-overview.md
│   ├── derivative-asset-registration.md
│   └── origin-audit-record.md
├── examples/
│   ├── origin-asset.example.yaml
│   ├── derivative-asset.example.yaml
│   ├── origin-audit-record.example.yaml
│   └── royalty-allocation-graph.example.yaml
├── schemas/
│   ├── origin-asset.schema.json
│   ├── derivative-asset.schema.json
│   ├── origin-audit-record.schema.json
│   └── royalty-allocation-graph.schema.json
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

---

## Royalty Allocation Graph Schema

The Royalty Allocation Graph schema is located at:

```text
schemas/royalty-allocation-graph.schema.json
```

It defines the structure of a proposed revenue allocation graph.

A valid Royalty Allocation Graph must include:

* `id`
* `revenue_event_id`
* `product_id`
* `timestamp`
* `currency`
* `gross_revenue`
* `allocation_basis`
* `allocations`
* `settlement`
* `human_review`
* `trace`

The Royalty Allocation Graph layer allows the protocol to record:

* revenue events
* revenue-generating products
* gross and net revenue
* audit-based allocation basis
* contribution scores
* allocation policy
* recipient roles
* allocation rates
* allocation amounts
* settlement status
* human review boundary

This transforms audited lineage into a proposed economic distribution.

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
[validate] Royalty Allocation Graph
  schema : schemas/royalty-allocation-graph.schema.json
  example: examples/royalty-allocation-graph.example.yaml
[ok] Royalty Allocation Graph example is valid
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

It validates YAML examples against the JSON Schemas.

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

v0.4 implements:

```text
Royalty Allocation Graph
```

Together, v0.1 to v0.4 establish the first verifiable economic lineage stack:

```text
source structure → downstream derivative → audit record → allocation graph
```

---

## Design Philosophy

Origin Structure Market is based on four principles.

### 1. Structure over content

The important unit is not only the finished text or product, but the reusable structure that generates future work.

### 2. Trace over ownership

The protocol focuses on traceable contribution rather than absolute ownership claims over abstract ideas.

### 3. Audit before allocation

Derivative claims should be evaluated before they influence economic distribution.

### 4. Flow over storage

Value is defined by how structures move, transform, generate revenue, and return value upstream.

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

Implemented:

* Define `royalty-allocation-graph.schema.json`
* Add royalty allocation graph example YAML
* Record revenue events
* Reference audit records
* Use contribution scores as allocation inputs
* Define allocation policy
* Record recipient roles, rates, amounts, and settlement status
* Preserve human review boundary
* Add Royalty Allocation Graph validation to CI

### v0.5 — Marketplace Layer

Planned additions:

* Define marketplace listing metadata
* Define license templates
* Add search and discovery fields
* Add listing status and availability fields
* Prepare for integration with external marketplaces or registries

---

## Non-Goals

This project does not attempt to:

* enforce legal ownership over all abstract ideas
* replace copyright law
* act as a court or final dispute resolver
* guarantee automatic royalty enforcement by itself
* execute payments directly in v0.4
* require blockchain usage in early versions

Instead, it provides a structured protocol foundation for future trace, audit, allocation, and settlement systems.

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

> What if the origin of an idea could remain traceable after AI transforms it, audits it, and monetizes it?

The answer is a new kind of market:

```text
not only a market for finished products,
but a market for reusable structures,
derivative lineage,
audit evidence,
and royalty allocation.
```

A system where:

* ideas become structured Origin Assets
* derivatives preserve lineage
* audits evaluate contribution
* revenue events generate allocation graphs
* value can flow back upstream
* creators are recognized as structural sources

In short:

> A market where value returns to the origin.
