# Origin Audit Record

## 1. Overview

**Origin Audit Record** is the v0.3 layer of Origin Structure Market.

v0.1 defines how to register an upstream structure as an **Origin Asset**.
v0.2 defines how to register a downstream **Derivative Asset**.
v0.3 defines how to evaluate whether a derivative claim is credible.

In short:

```text
Origin Asset
    ↓
Derivative Asset
    ↓
Origin Audit Record
```

The Origin Audit Record provides a machine-readable audit format for evaluating:

* derivative claims
* structural similarity
* conceptual similarity
* lineage similarity
* workflow similarity
* contribution scores
* royalty relevance
* supporting evidence
* human review boundaries

This layer does not make AI the final judge.
It records structured audit evidence and preserves a human review boundary.

---

## 2. Purpose

Derivative Asset Registration allows a creator to declare:

> This asset was derived from these upstream structures.

Origin Audit Record asks:

> How credible is that claim?

The purpose of v0.3 is to move from simple declaration to structured evaluation.

It creates an auditable bridge between:

```text
declared lineage → evaluated lineage → future royalty allocation
```

---

## 3. Design Principles

### 3.1 Audit before allocation

Royalty allocation should not depend only on self-declared derivative claims.

Before value flows back to an origin, the claimed relationship should be auditable.

### 3.2 Evidence over assertion

An audit record should not simply say that two assets are related.

It should record why they are considered related:

* shared concepts
* shared structure
* trace references
* evidence hashes
* differentiating factors

### 3.3 AI as assistant, not judge

AI may assist with similarity scoring, evidence extraction, and structural comparison.

However, the protocol should not automatically treat AI-generated scores as final truth.

Human review remains a boundary when:

* royalty allocation is affected
* contribution scores are disputed
* derivative claims are ambiguous
* legal or economic consequences may arise

---

## 4. Schema Location

The Origin Audit Record schema is located at:

```text
schemas/origin-audit-record.schema.json
```

The example record is located at:

```text
examples/origin-audit-record.example.yaml
```

---

## 5. Required Fields

A valid Origin Audit Record must include:

```text
origin_audit_record:
  id
  target_asset_id
  target_asset_type
  auditor
  timestamp
  audit_scope
  compared_assets
  similarity
  judgment
  evidence
  human_review
```

These fields define what is being audited, who audited it, what assets were compared, what similarity was found, what judgment was made, what evidence supports it, and whether human review is required.

---

## 6. Field Structure

### 6.1 id

Unique identifier for the audit record.

Example:

```yaml
id: audit-2026-0001
```

The identifier must follow this pattern:

```text
audit-YYYY-NNNN
```

---

### 6.2 target_asset_id

Identifier of the asset being audited.

Example:

```yaml
target_asset_id: derivative-2026-0001
```

The target may be a derivative asset, listing, product, or other downstream asset depending on future protocol versions.

---

### 6.3 target_asset_type

Type of asset being audited.

Example:

```yaml
target_asset_type: derivative_asset
```

Supported values include:

```text
origin_asset
derivative_asset
marketplace_listing
final_product
other
```

In v0.3, the most common target type is:

```text
derivative_asset
```

---

### 6.4 auditor

Identifier, handle, name, DID, or agent ID of the auditor.

Example:

```yaml
auditor: SamuraiWriter7
```

The auditor may be:

* a human reviewer
* an AI-assisted review process
* a multi-agent review system
* a protocol maintainer
* a hybrid review process

---

### 6.5 audit_method

Optional method used to conduct the audit.

Example:

```yaml
audit_method: hybrid_review
```

Supported values include:

```text
human_review
ai_assisted_review
multi_agent_review
hybrid_review
automated_similarity_check
other
```

---

## 7. Audit Scope

The `audit_scope` field defines what the audit is evaluating.

Example:

```yaml
audit_scope:
  - derivative_claim
  - origin_similarity
  - structural_similarity
  - conceptual_similarity
  - contribution_score
  - royalty_relevance
  - human_review_boundary
```

Supported audit scopes include:

```text
derivative_claim
origin_similarity
structural_similarity
conceptual_similarity
contribution_score
royalty_relevance
dispute_review
human_review_boundary
other
```

This allows the audit to be narrow or broad.

For example, an audit may only evaluate structural similarity, or it may also evaluate contribution scores and royalty relevance.

---

## 8. Compared Assets

The `compared_assets` section records which upstream assets were compared against the target.

Example:

```yaml
compared_assets:
  - asset_id: origin-2026-0001
    asset_type: origin_asset
    title: Origin Structure Market
    relationship_claim: direct_origin
```

Each compared asset includes:

* `asset_id`
* `asset_type`
* optional `title`
* `relationship_claim`

Supported relationship claims include:

```text
direct_origin
indirect_origin
intermediate_derivative
reference
inspiration
similar_structure
unrelated
disputed
other
```

This section establishes the comparison target for the audit.

---

## 9. Similarity Scores

The `similarity` section records multidimensional similarity scores.

Example:

```yaml
similarity:
  lexical_similarity: 0.32
  structural_similarity: 0.82
  conceptual_similarity: 0.88
  lineage_similarity: 0.91
  workflow_similarity: 0.76
  overall_similarity: 0.84
```

Scores range from `0` to `1`.

### 9.1 lexical_similarity

Surface-level textual similarity.

This is useful but should not dominate the audit, because derivatives may preserve structure while changing wording.

### 9.2 structural_similarity

Similarity of architecture, sequence, fields, workflow, schema, or structural pattern.

This is one of the most important dimensions in Origin Structure Market.

### 9.3 conceptual_similarity

Similarity of concepts, intent, abstraction, or semantic framing.

This helps detect deeper conceptual inheritance.

### 9.4 lineage_similarity

Similarity based on declared trace lineage, references, and derivation path.

This is especially important when derivative assets explicitly declare upstream dependencies.

### 9.5 workflow_similarity

Similarity of procedural workflow or operational logic.

This is useful for GPT instructions, protocols, schemas, and AI workflows.

### 9.6 overall_similarity

Combined similarity score after considering multiple dimensions.

This score should be treated as an audit estimate, not an absolute truth.

---

## 10. Judgment

The `judgment` section records the audit conclusion.

Example:

```yaml
judgment:
  likely_derivative: true
  confidence: 0.86
  contribution_scores:
    origin-2026-0001: 0.45
  royalty_relevance: high
  status: requires_human_review
  summary: >
    The target derivative asset appears to be strongly derived from the
    Origin Structure Market framework.
```

Judgment includes:

* whether the target is likely derivative
* confidence score
* contribution scores by upstream asset
* royalty relevance
* status
* optional summary

---

## 11. Contribution Scores

The `contribution_scores` field estimates how much each upstream asset contributed to the target.

Example:

```yaml
contribution_scores:
  origin-2026-0001: 0.45
```

This means the audit estimates that `origin-2026-0001` contributed approximately 45% of the target asset’s structure.

Important:

> Contribution scores are audit estimates, not automatic payment instructions.

They may later inform v0.4 Royalty Allocation Graphs.

---

## 12. Royalty Relevance

The `royalty_relevance` field indicates whether this audit may matter for future royalty allocation.

Supported values:

```text
none
low
medium
high
critical
```

Example:

```yaml
royalty_relevance: high
```

This means the audit may be important when future revenue allocation is calculated.

---

## 13. Judgment Status

The `status` field records the current status of the audit judgment.

Supported values:

```text
draft
provisional
accepted
rejected
disputed
requires_human_review
```

Example:

```yaml
status: requires_human_review
```

This is important because an audit may be useful without being final.

---

## 14. Evidence

The `evidence` section records the basis for the audit.

Example:

```yaml
evidence:
  shared_concepts:
    - origin asset
    - structural fingerprint
    - traceable contribution
  shared_structure:
    - origin registration
    - upstream asset reference
    - contribution claim
  differentiating_factors:
    - The target asset is packaged as a GPT-oriented workflow.
  trace_references:
    - https://github.com/SamuraiWriter7/origin-structure-market
  evidence_hashes:
    - sha256:eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee
  audit_notes: >
    This audit record is provisional.
```

Evidence may include:

* shared concepts
* shared structural patterns
* differentiating factors
* trace references
* evidence hashes
* audit notes

This section is where the audit becomes explainable.

---

## 15. Human Review Boundary

The `human_review` section prevents automated audit scores from becoming final by default.

Example:

```yaml
human_review:
  required: true
  status: pending
  reviewer: protocol-maintainer
  notes: >
    Human review is required before accepting the derivative likelihood,
    contribution score, and royalty relevance as final.
```

Supported review statuses:

```text
not_required
pending
approved
rejected
disputed
```

This boundary is essential when audits may affect real compensation, attribution, or disputes.

---

## 16. Full Example

```yaml
origin_audit_record:
  id: audit-2026-0001
  target_asset_id: derivative-2026-0001
  target_asset_type: derivative_asset
  auditor: SamuraiWriter7
  audit_method: hybrid_review
  timestamp: "2026-06-22T00:00:00Z"
  version: v0.3.0-candidate

  audit_scope:
    - derivative_claim
    - origin_similarity
    - structural_similarity
    - conceptual_similarity
    - contribution_score
    - royalty_relevance
    - human_review_boundary

  compared_assets:
    - asset_id: origin-2026-0001
      asset_type: origin_asset
      title: Origin Structure Market
      relationship_claim: direct_origin

  similarity:
    lexical_similarity: 0.32
    structural_similarity: 0.82
    conceptual_similarity: 0.88
    lineage_similarity: 0.91
    workflow_similarity: 0.76
    overall_similarity: 0.84

  judgment:
    likely_derivative: true
    confidence: 0.86
    contribution_scores:
      origin-2026-0001: 0.45
    royalty_relevance: high
    status: requires_human_review
    summary: >
      The target derivative asset appears to be strongly derived from the
      Origin Structure Market framework.

  evidence:
    shared_concepts:
      - origin asset
      - structural fingerprint
      - traceable contribution
      - royalty allocation
    shared_structure:
      - origin registration
      - upstream asset reference
      - contribution claim
      - transformation type declaration
    differentiating_factors:
      - The target asset is packaged as a GPT-oriented workflow rather than a general protocol overview.
    trace_references:
      - https://github.com/SamuraiWriter7/origin-structure-market
    evidence_hashes:
      - sha256:eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee
    audit_notes: >
      This audit record is provisional.

  human_review:
    required: true
    status: pending
    reviewer: protocol-maintainer

  trace:
    source_url: https://github.com/SamuraiWriter7/origin-structure-market
    repository_url: https://github.com/SamuraiWriter7/origin-structure-market
    related_assets:
      - origin-2026-0001
      - derivative-2026-0001
```

---

## 17. Validation

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
[validate] Origin Audit Record
  schema : schemas/origin-audit-record.schema.json
  example: examples/origin-audit-record.example.yaml
[ok] Origin Audit Record example is valid
[done] all examples are valid
```

---

## 18. Relationship to Future Layers

Origin Audit Record prepares the protocol for royalty allocation.

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

v0.3 does not execute payments.

It creates the structured audit basis that v0.4 can use when calculating royalty allocation.

---

## 19. Summary

Origin Audit Record upgrades Origin Structure Market from a lineage declaration protocol into an auditable lineage protocol.

v0.1 asks:

> What is the origin structure?

v0.2 asks:

> What was derived from it, how, and with what claimed contribution?

v0.3 asks:

> How credible is the derivative claim, and what evidence supports it?

This is the layer where the market gains a structured sense of judgment without turning AI into an unquestioned judge.
