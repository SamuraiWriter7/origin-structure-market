# Derivative Asset Registration

## 1. Overview

**Derivative Asset Registration** is the v0.2 layer of Origin Structure Market.

v0.1 defines how to register an upstream structure as an **Origin Asset**.
v0.2 defines how to register a downstream asset derived from one or more upstream assets.

In short:

```text
Origin Asset
    ↓
Derivative Asset
```

This layer allows a derivative work to declare:

* what it was derived from
* how it transformed the upstream asset
* how much contribution is claimed
* what evidence supports the claim
* what royalty split is proposed
* whether human review is required

The purpose is to make derivative lineage visible, structured, and machine-readable.

---

## 2. Why Derivative Asset Registration Matters

AI-era creation is rarely linear.

A single upstream structure may become:

* a GPT instruction
* a prompt architecture
* a workflow schema
* an article framework
* a software tool
* a business model
* a marketplace listing
* another conceptual framework

Without derivative registration, the origin becomes invisible once transformed.

Derivative Asset Registration prevents this loss of lineage by recording:

> This downstream asset was created from these upstream structures, through these transformations, with this claimed contribution weight.

---

## 3. Design Principle

Derivative Asset Registration is based on three principles.

### 3.1 Trace before reward

Royalty allocation should not happen before lineage is recorded.

A derivative asset first declares its upstream dependencies.
Only after trace evidence exists can audit and allocation layers operate.

### 3.2 Claim before judgment

A derivative registration is not a final legal or economic judgment.

It is a structured claim.

The claim may later be:

* accepted
* audited
* revised
* disputed
* rejected
* converted into a royalty allocation graph

### 3.3 Human review boundary

AI can assist with structural comparison and contribution scoring, but should not be the final judge by default.

Derivative claims may require human review, especially when contribution weights or royalty splits affect real compensation.

---

## 4. Schema Location

The Derivative Asset schema is located at:

```text
schemas/derivative-asset.schema.json
```

The example record is located at:

```text
examples/derivative-asset.example.yaml
```

---

## 5. Required Fields

A valid Derivative Asset record must include:

```text
derivative_asset:
  id
  title
  creator
  asset_type
  description
  timestamp
  derived_from
  output
  proposed_royalty_split
  trace
```

These fields define the identity, upstream lineage, transformation path, output form, proposed economic split, and trace references of the derivative asset.

---

## 6. Field Structure

### 6.1 id

Unique identifier for the derivative asset.

Example:

```yaml
id: derivative-2026-0001
```

The identifier must follow this pattern:

```text
derivative-YYYY-NNNN
```

---

### 6.2 title

Human-readable title of the derivative asset.

Example:

```yaml
title: Origin Asset Generator GPT
```

---

### 6.3 creator

Identifier, handle, name, or DID of the derivative creator.

Example:

```yaml
creator: SamuraiWriter7
```

---

### 6.4 asset_type

Category of the derivative asset.

Supported examples include:

* `gpt_instruction`
* `prompt_architecture`
* `ai_workflow`
* `workflow_schema`
* `article_framework`
* `book_framework`
* `business_model`
* `software_tool`
* `documentation`
* `marketplace_listing`
* `other`

---

### 6.5 derived_from

The `derived_from` section is the core of v0.2.

It records upstream assets that contributed to the derivative asset.

Example:

```yaml
derived_from:
  - asset_id: origin-2026-0001
    asset_role: origin
    title: Origin Structure Market
    contribution_claim: 0.45
    transformation_type:
      - gpt_instruction
      - workflow_expansion
      - schema_application
```

Each upstream reference contains:

* `asset_id`
* `asset_role`
* `contribution_claim`
* `transformation_type`
* optional `evidence`

---

## 7. Upstream Asset Roles

The `asset_role` field describes how the upstream asset functions in the derivative.

Supported roles include:

```text
origin
intermediate_derivative
reference
inspiration
template
schema
workflow
other
```

Example:

```yaml
asset_role: origin
```

This means the upstream asset is treated as a primary origin source.

---

## 8. Contribution Claim

The `contribution_claim` field records the claimed contribution weight of the upstream asset.

Example:

```yaml
contribution_claim: 0.45
```

This means the registrant claims that the upstream asset contributed approximately 45% of the derivative asset’s structure.

Important:

> A contribution claim is not a final judgment.

It is a structured declaration that may later be audited in v0.3.

---

## 9. Transformation Type

The `transformation_type` field records how the upstream asset was transformed.

Examples:

```yaml
transformation_type:
  - gpt_instruction
  - workflow_expansion
  - schema_application
  - marketplace_packaging
```

Supported transformation types include:

* `gpt_instruction`
* `prompt_expansion`
* `workflow_expansion`
* `schema_application`
* `documentation_expansion`
* `article_conversion`
* `book_conversion`
* `software_implementation`
* `business_model_conversion`
* `conceptual_reframing`
* `marketplace_packaging`
* `translation`
* `summarization`
* `other`

This field is required for each upstream asset reference.

---

## 10. Evidence

The optional `evidence` field supports the derivation claim.

Example:

```yaml
evidence:
  shared_concepts:
    - origin asset
    - structural fingerprint
    - traceable contribution
  shared_structure:
    - origin registration
    - permission layer
    - royalty policy layer
  evidence_hashes:
    - sha256:cccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccc
```

Evidence may include:

* shared concepts
* shared structural patterns
* hashes of drafts, commits, archives, or supporting records

This evidence is intended to support future origin audit.

---

## 11. Output

The `output` section describes the resulting derivative asset.

Example:

```yaml
output:
  asset_type: custom_gpt
  commercial_use: true
  distribution_channel: gpt_store
  canonical_hash: sha256:dddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddd
```

It records:

* output asset type
* whether commercial use is intended
* distribution channel
* optional canonical hash

---

## 12. Proposed Royalty Split

The `proposed_royalty_split` section records a proposed economic distribution.

Example:

```yaml
proposed_royalty_split:
  final_creator: 0.85
  origin_creator: 0.05
  derivative_creator: 0.07
  auditor: 0.02
  protocol_fund: 0.01
  settlement: hybrid
```

This does not execute payment by itself.

It provides a structured proposal that may later be used by:

* royalty allocation graphs
* smart contracts
* off-chain settlement systems
* marketplace rules
* human review processes

---

## 13. Human Review

The optional `human_review` section defines whether the derivative claim requires review.

Example:

```yaml
human_review:
  required: true
  status: pending
  reviewer: protocol-maintainer
  notes: >
    Human review is required before accepting the derivative contribution
    claim and proposed royalty split as final.
```

Supported review statuses include:

```text
not_required
pending
approved
rejected
disputed
```

This boundary prevents AI-generated contribution claims from becoming automatic final judgments.

---

## 14. Full Example

```yaml
derivative_asset:
  id: derivative-2026-0001
  title: Origin Asset Generator GPT
  creator: SamuraiWriter7
  asset_type: gpt_instruction
  description: >
    Origin Asset Generator GPT is a derivative asset based on the Origin
    Structure Market framework. It transforms the upstream Origin Asset
    registration concept into a practical GPT instruction and workflow.

  timestamp: "2026-06-22T00:00:00Z"
  version: v0.2.0-candidate

  derived_from:
    - asset_id: origin-2026-0001
      asset_role: origin
      title: Origin Structure Market
      contribution_claim: 0.45
      transformation_type:
        - gpt_instruction
        - workflow_expansion
        - schema_application
      evidence:
        shared_concepts:
          - origin asset
          - structural fingerprint
          - traceable contribution
        shared_structure:
          - origin registration
          - permission layer
          - royalty policy layer

  output:
    asset_type: custom_gpt
    commercial_use: true
    distribution_channel: gpt_store
    canonical_hash: sha256:dddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddd

  proposed_royalty_split:
    final_creator: 0.85
    origin_creator: 0.05
    derivative_creator: 0.07
    auditor: 0.02
    protocol_fund: 0.01
    settlement: hybrid

  trace:
    source_url: https://github.com/SamuraiWriter7/origin-structure-market
    repository_url: https://github.com/SamuraiWriter7/origin-structure-market

  human_review:
    required: true
    status: pending
```

---

## 15. Validation

Run:

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

## 16. Relationship to Future Layers

Derivative Asset Registration prepares the foundation for later protocol layers.

```text
v0.1 Origin Asset Registration
    ↓
v0.2 Derivative Asset Registration
    ↓
v0.3 Origin Audit Record
    ↓
v0.4 Royalty Allocation Graph
    ↓
v0.5 Marketplace Layer
```

v0.2 does not determine final truth.

It creates the structured claim that v0.3 can audit.

---

## 17. Summary

Derivative Asset Registration turns Origin Structure Market from a static origin registry into a lineage protocol.

v0.1 asks:

> What is the origin structure?

v0.2 asks:

> What was derived from it, how, and with what claimed contribution?

This is the first step toward a market where value can flow back through visible structural lineage.
