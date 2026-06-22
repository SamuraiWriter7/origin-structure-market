# Marketplace Listing

## 1. Overview

**Marketplace Listing** is the v0.5 layer of Origin Structure Market.

v0.1 defines how to register an upstream structure as an **Origin Asset**.
v0.2 defines how to register a downstream **Derivative Asset**.
v0.3 defines how to evaluate derivative claims through an **Origin Audit Record**.
v0.4 defines how to convert revenue events and audited lineage into a **Royalty Allocation Graph**.
v0.5 defines how to prepare traceable assets for marketplace discovery, licensing, pricing, and monetization.

In short:

```text
Origin Asset
    ↓
Derivative Asset
    ↓
Origin Audit Record
    ↓
Royalty Allocation Graph
    ↓
Marketplace Listing
```

The Marketplace Listing layer does not run a full marketplace by itself.
It defines the machine-readable listing metadata that marketplaces, registries, AI agents, external platforms, or future settlement systems can consume.

---

## 2. Purpose

Marketplace Listing asks:

> How can a traceable asset be listed, licensed, discovered, priced, and monetized?

The purpose of v0.5 is to create a structured bridge between:

```text
traceable asset → license terms → pricing model → royalty reference → marketplace discovery
```

This allows Origin Assets, Derivative Assets, royalty bundles, or related structural products to be listed while preserving lineage, audit, royalty, and human review metadata.

---

## 3. Design Principles

### 3.1 Listing before marketplace automation

A marketplace should not expose, sell, license, or recommend an asset before its listing metadata is clear.

Marketplace Listing records the listing first.
Discovery, payment, smart contracts, subscriptions, licensing, or agentic commerce can then happen later.

### 3.2 Trace-aware discovery

Marketplace search should not only index titles and tags.

It should also preserve:

* upstream origin references
* derivative lineage
* audit records
* royalty allocation graph references
* license requirements
* quality signals
* human review status

This prevents a listed asset from being detached from its source.

### 3.3 License and royalty visibility

A listing should make reuse terms visible before commercial use.

The listing records:

* commercial use permission
* derivative permission
* attribution requirements
* AI training permission
* AI inference permission
* royalty requirement
* allocation mode
* Royalty Allocation Graph reference

### 3.4 Human review boundary

Marketplace listings may affect real monetization, licensing, reputation, and downstream reuse.

For this reason, v0.5 preserves a human review boundary before a listing becomes active.

### 3.5 Marketplace-neutral design

v0.5 does not require a specific platform.

It can support:

* GitHub-based registries
* GPT marketplaces
* custom creator marketplaces
* royalty OS systems
* agent-readable catalogues
* smart contract registries
* off-chain licensing workflows

---

## 4. Schema Location

The Marketplace Listing schema is located at:

```text
schemas/marketplace-listing.schema.json
```

The example record is located at:

```text
examples/marketplace-listing.example.yaml
```

---

## 5. Required Fields

A valid Marketplace Listing must include:

```text
marketplace_listing:
  id
  title
  listing_type
  listed_asset
  summary
  timestamp
  status
  pricing
  license
  royalty
  discovery
  human_review
  trace
```

These fields define what is being listed, how it is priced, how it may be used, how royalties are handled, how it can be discovered, and how it remains traceable.

---

## 6. Field Structure

### 6.1 id

Unique identifier for the marketplace listing.

Example:

```yaml
id: listing-2026-0001
```

The identifier must follow this pattern:

```text
listing-YYYY-NNNN
```

---

### 6.2 title

Human-readable marketplace title.

Example:

```yaml
title: Origin Asset Generator GPT
```

The title should be concise enough for discovery, search results, and marketplace cards.

---

### 6.3 listing_type

Category of the listing.

Example:

```yaml
listing_type: derivative_asset
```

Supported listing types include:

```text
origin_asset
derivative_asset
gpt_instruction
prompt_pack
schema
workflow
article_framework
book_framework
software_tool
business_model
license_offer
royalty_bundle
other
```

This field describes the marketplace-facing type of the listing.

---

## 7. Listed Asset

The `listed_asset` section identifies what is being listed.

Example:

```yaml
listed_asset:
  asset_id: derivative-2026-0001
  asset_type: derivative_asset
  version: v0.5.0-candidate
  canonical_hash: sha256:1111111111111111111111111111111111111111111111111111111111111111
```

Required fields:

* `asset_id`
* `asset_type`

Optional fields:

* `version`
* `canonical_hash`

Supported asset ID prefixes include:

```text
origin
derivative
product
allocation
```

Supported asset types include:

```text
origin_asset
derivative_asset
final_product
royalty_bundle
other
```

The listed asset is the object that the marketplace record exposes for discovery, purchase, licensing, reuse, or evaluation.

---

## 8. Summary and Description

### 8.1 summary

Short marketplace-facing explanation.

Example:

```yaml
summary: >
  A GPT-oriented derivative asset that helps creators generate machine-readable
  Origin Asset records, YAML examples, trace metadata, and registration-ready
  structures for the Origin Structure Market.
```

The summary should be short enough to appear in search results or listing cards.

### 8.2 description

Longer explanation of the listing, buyer value, and intended use.

Example:

```yaml
description: >
  Origin Asset Generator GPT is a derivative asset based on the Origin
  Structure Market framework. It operationalizes the upstream origin asset
  registration concept into a practical workflow for creators, developers,
  and protocol maintainers.
```

The description may explain:

* what the asset does
* who it is for
* how it relates to upstream origin assets
* how it can be reused
* what commercial or protocol role it serves

---

## 9. Status

The `status` field records the current marketplace state.

Example:

```yaml
status: pending_review
```

Supported statuses include:

```text
draft
pending_review
active
paused
sold_out
archived
rejected
disputed
```

This allows listings to exist before they are publicly active.

---

## 10. Pricing

The `pricing` section defines commercial access terms.

Example:

```yaml
pricing:
  pricing_model: revenue_share
  amount: 0
  currency: JPY
  billing_period: none
  revenue_share_rate: 0.10
  notes: >
    The listing is initially offered with no upfront purchase price, but
    downstream commercial use may trigger royalty allocation.
```

Required fields:

* `pricing_model`
* `currency`

Supported pricing models include:

```text
free
one_time_purchase
subscription
license_fee
revenue_share
quote_required
hybrid
```

Supported billing periods include:

```text
none
monthly
yearly
per_use
custom
```

Pricing does not automatically execute payment.
It describes how marketplace access or downstream commercial use should be priced.

---

## 11. License

The `license` section defines usage terms.

Example:

```yaml
license:
  license_name: Kazene-Origin-Market-License-0.5
  license_url: https://github.com/SamuraiWriter7/origin-structure-market/blob/main/LICENSE
  commercial_use: true
  derivative_allowed: true
  attribution_required: true
  ai_training_allowed: false
  ai_inference_allowed: true
  redistribution_allowed: true
  restrictions:
    - Do not remove upstream trace references.
    - Do not claim exclusive ownership over the underlying origin structure.
    - Commercial derivatives should preserve royalty allocation metadata.
```

Required fields:

* `license_name`
* `commercial_use`
* `derivative_allowed`
* `attribution_required`

Optional fields:

* `license_url`
* `ai_training_allowed`
* `ai_inference_allowed`
* `redistribution_allowed`
* `restrictions`

This section makes reuse conditions visible before downstream use.

---

## 12. Royalty

The `royalty` section connects the listing to royalty allocation logic.

Example:

```yaml
royalty:
  royalty_required: true
  allocation_mode: royalty_allocation_graph
  royalty_allocation_graph_id: allocation-2026-0001
  default_origin_rate: 0.05
  default_derivative_rate: 0.07
  protocol_fund_rate: 0.01
  notes: >
    Royalty distribution should reference the linked Royalty Allocation Graph.
```

Required fields:

* `royalty_required`
* `allocation_mode`

Supported allocation modes include:

```text
none
declared_split
audit_based
royalty_allocation_graph
contract_based
marketplace_policy
hybrid
```

When `allocation_mode` is `royalty_allocation_graph`, the listing should reference a Royalty Allocation Graph ID.

Example:

```yaml
royalty_allocation_graph_id: allocation-2026-0001
```

This connects marketplace listing to the v0.4 allocation layer.

---

## 13. Discovery

The `discovery` section defines search and categorization metadata.

Example:

```yaml
discovery:
  categories:
    - gpt_instruction
    - workflow
    - royalty_template
    - conceptual_framework
  tags:
    - origin-structure-market
    - origin-asset
    - derivative-asset
    - royalty-allocation
    - traceability
    - creator-economy
    - ai-provenance
    - kazene
  keywords:
    - origin registration
    - structural fingerprint
    - derivative lineage
    - audit-based royalty
    - AI creator economy
    - marketplace listing
  language: en
  target_users:
    - creators
    - developers
    - researchers
    - business_users
    - ai_agents
    - protocol_maintainers
```

Required fields:

* `categories`
* `tags`

Optional fields:

* `keywords`
* `language`
* `target_users`

Supported categories include:

```text
ai_prompt
gpt_instruction
schema
workflow
royalty_template
origin_audit
article_framework
book_framework
business_model
software_tool
conceptual_framework
other
```

Supported target users include:

```text
creators
developers
researchers
business_users
educators
ai_agents
marketplaces
protocol_maintainers
other
```

Discovery metadata makes the listing searchable by humans, marketplaces, and AI agents.

---

## 14. Quality Signals

The optional `quality_signals` section records trust and validation metadata.

Example:

```yaml
quality_signals:
  origin_audit_record_ids:
    - audit-2026-0001
  validation_status: audit_validated
  documentation_url: https://github.com/SamuraiWriter7/origin-structure-market/blob/main/docs/royalty-allocation-graph.md
  example_url: https://github.com/SamuraiWriter7/origin-structure-market/blob/main/examples/marketplace-listing.example.yaml
```

Supported validation statuses include:

```text
not_validated
schema_validated
audit_validated
human_reviewed
disputed
```

Quality signals may include:

* audit record references
* schema validation status
* human review status
* documentation URL
* example or demo URL

This section helps marketplaces and users evaluate trustworthiness.

---

## 15. Human Review Boundary

The `human_review` section prevents listings from becoming active automatically.

Example:

```yaml
human_review:
  required: true
  status: pending
  reviewer: protocol-maintainer
  notes: >
    Human review is required before this listing becomes active because it
    references royalty allocation, derivative lineage, and commercial reuse
    terms.
```

Required fields:

* `required`
* `status`

Supported statuses include:

```text
not_required
pending
approved
rejected
disputed
```

Human review is especially important when a listing includes:

* commercial reuse
* royalty claims
* disputed lineage
* audit-based allocation
* AI training restrictions
* license obligations
* smart contract settlement plans

---

## 16. Trace

The `trace` section records links and evidence that connect the listing to its upstream context.

Example:

```yaml
trace:
  source_url: https://github.com/SamuraiWriter7/origin-structure-market
  repository_url: https://github.com/SamuraiWriter7/origin-structure-market
  listing_url: https://github.com/SamuraiWriter7/origin-structure-market
  related_assets:
    - origin-2026-0001
    - derivative-2026-0001
    - audit-2026-0001
    - allocation-2026-0001
  evidence_hashes:
    - sha256:2222222222222222222222222222222222222222222222222222222222222222
```

Required fields:

* `source_url`

Optional fields:

* `repository_url`
* `listing_url`
* `related_assets`
* `evidence_hashes`

Trace records may include:

* origin asset IDs
* derivative asset IDs
* audit record IDs
* royalty allocation graph IDs
* repository links
* documentation links
* listing snapshots
* evidence hashes

This ensures the marketplace listing remains connected to its structural origin.

---

## 17. Full Example

```yaml
marketplace_listing:
  id: listing-2026-0001
  title: Origin Asset Generator GPT
  listing_type: derivative_asset

  listed_asset:
    asset_id: derivative-2026-0001
    asset_type: derivative_asset
    version: v0.5.0-candidate
    canonical_hash: sha256:1111111111111111111111111111111111111111111111111111111111111111

  summary: >
    A GPT-oriented derivative asset that helps creators generate machine-readable
    Origin Asset records, YAML examples, trace metadata, and registration-ready
    structures for the Origin Structure Market.

  description: >
    Origin Asset Generator GPT is a derivative asset based on the Origin
    Structure Market framework. It operationalizes the upstream origin asset
    registration concept into a practical workflow for creators, developers,
    and protocol maintainers who want to register AI-era structures as
    traceable origin assets.

  timestamp: "2026-06-22T00:00:00Z"
  version: v0.5.0-candidate
  status: pending_review

  pricing:
    pricing_model: revenue_share
    amount: 0
    currency: JPY
    billing_period: none
    revenue_share_rate: 0.10

  license:
    license_name: Kazene-Origin-Market-License-0.5
    license_url: https://github.com/SamuraiWriter7/origin-structure-market/blob/main/LICENSE
    commercial_use: true
    derivative_allowed: true
    attribution_required: true
    ai_training_allowed: false
    ai_inference_allowed: true
    redistribution_allowed: true

  royalty:
    royalty_required: true
    allocation_mode: royalty_allocation_graph
    royalty_allocation_graph_id: allocation-2026-0001
    default_origin_rate: 0.05
    default_derivative_rate: 0.07
    protocol_fund_rate: 0.01

  discovery:
    categories:
      - gpt_instruction
      - workflow
      - royalty_template
      - conceptual_framework
    tags:
      - origin-structure-market
      - origin-asset
      - derivative-asset
      - royalty-allocation
      - traceability
      - creator-economy
      - ai-provenance
      - kazene
    keywords:
      - origin registration
      - structural fingerprint
      - derivative lineage
      - audit-based royalty
      - AI creator economy
      - marketplace listing
    language: en
    target_users:
      - creators
      - developers
      - researchers
      - business_users
      - ai_agents
      - protocol_maintainers

  quality_signals:
    origin_audit_record_ids:
      - audit-2026-0001
    validation_status: audit_validated
    documentation_url: https://github.com/SamuraiWriter7/origin-structure-market/blob/main/docs/royalty-allocation-graph.md
    example_url: https://github.com/SamuraiWriter7/origin-structure-market/blob/main/examples/marketplace-listing.example.yaml

  human_review:
    required: true
    status: pending
    reviewer: protocol-maintainer

  trace:
    source_url: https://github.com/SamuraiWriter7/origin-structure-market
    repository_url: https://github.com/SamuraiWriter7/origin-structure-market
    listing_url: https://github.com/SamuraiWriter7/origin-structure-market
    related_assets:
      - origin-2026-0001
      - derivative-2026-0001
      - audit-2026-0001
      - allocation-2026-0001
    evidence_hashes:
      - sha256:2222222222222222222222222222222222222222222222222222222222222222
```

---

## 18. Validation

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
[validate] Royalty Allocation Graph
  schema : schemas/royalty-allocation-graph.schema.json
  example: examples/royalty-allocation-graph.example.yaml
[ok] Royalty Allocation Graph example is valid
[validate] Marketplace Listing
  schema : schemas/marketplace-listing.schema.json
  example: examples/marketplace-listing.example.yaml
[ok] Marketplace Listing example is valid
[done] all examples are valid
```

---

## 19. Relationship to Previous Layers

Marketplace Listing depends on earlier protocol layers.

```text
v0.1 Origin Asset Registration
    ↓
v0.2 Derivative Asset Registration
    ↓
v0.3 Origin Audit Record
    ↓
v0.4 Royalty Allocation Graph
    ↓
v0.5 Marketplace Listing
```

A Marketplace Listing may reference:

* `origin-asset.schema.json`
* `derivative-asset.schema.json`
* `origin-audit-record.schema.json`
* `royalty-allocation-graph.schema.json`

This makes it possible for marketplace records to preserve provenance, audit evidence, and royalty allocation paths.

---

## 20. Relationship to Future Layers

Marketplace Listing prepares the protocol for v0.6 and beyond.

Possible future layers include:

```text
v0.6 License Template Registry
v0.7 Marketplace Policy Rules
v0.8 Agent Consumption Manifest
v0.9 Settlement Integration
```

v0.5 does not yet define reusable license template objects.
It records license terms inside the listing itself.

v0.6 can extract those terms into reusable, versioned license templates.

---

## 21. Summary

Marketplace Listing upgrades Origin Structure Market from a trace, audit, and allocation protocol into a marketplace-ready protocol.

v0.1 asks:

> What is the origin structure?

v0.2 asks:

> What was derived from it, how, and with what claimed contribution?

v0.3 asks:

> How credible is the derivative claim, and what evidence supports it?

v0.4 asks:

> How should revenue be allocated across creators, origins, derivatives, auditors, and protocol funds?

v0.5 asks:

> How can a traceable asset be listed, licensed, discovered, priced, and monetized?

This is the layer where traceable structures become market-facing records.

It does not run the market by itself.
It defines the shelf label, license card, royalty pointer, discovery metadata, and review boundary needed for a market to exist.
