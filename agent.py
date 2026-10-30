"""Check rental-package completeness without making housing decisions."""
from __future__ import annotations

DEFAULT_REQUIRED = ("application", "identity_document", "income_evidence", "consent")


def review_documents(package: dict) -> dict:
    required = list(package.get("required_documents") or DEFAULT_REQUIRED)
    documents = package.get("documents") or {}
    missing, unreadable = [], []
    for name in required:
        record = documents.get(name)
        if not record:
            missing.append(name)
        elif not record.get("readable", True):
            unreadable.append(name)
    return {"application_id": package.get("application_id"), "status": "complete-for-human-review" if not missing and not unreadable else "needs-documents", "missing_documents": missing, "unreadable_documents": unreadable, "evidence": {name: bool(documents.get(name)) for name in required}, "eligibility_decision": None, "authorized_review_required": True}
