# Rental Document Review Assistant Explainability

## Decision and Reasoning Process

The agent's decision support compares submitted documents with the approved application checklist. Its reasoning identifies present, missing, expired, unreadable, or inconsistent items without judging applicant suitability.

## Inputs and Data Sources Used

Input data includes the approved checklist and applicant-submitted documents authorized for review. No protected attributes, unrelated personal information, or external profiling data sources are used.

## Outputs and Supporting Evidence

The output contains a completeness summary, document-level issues, and clarification requests. Every issue is tied to a checklist requirement and the observed document status.

## Limits, Constraints, and Known Issues

A limitation is that the agent cannot authenticate documents or determine legal eligibility. It is constrained from approving, rejecting, scoring, or ranking housing applicants.

## Uncertainty and Human Review

Uncertainty is reported for unreadable, ambiguous, or inconsistent material. Authorized human review is mandatory for all housing decisions.

## Implementation in This Repository

This repository implements a declarative OpenGAP worker through `agent.yaml`, `SOUL.md`, this document, and `README.md`. The manifest defines the rental-document evidence accepted and the completeness or inconsistency report returned, while the policy documents prohibit applicant scoring or autonomous housing decisions.

No document-authentication service, tenant-screening database, or approval endpoint exists in the repository. A compatible host must preserve uncertainty and route all findings to authorized human review.
