import pytest
from app.rag.legal_currency import LegalCurrencyService, TRANSITION_DATE

def test_transition_date():
    assert TRANSITION_DATE == "2024-07-01"
    summary = LegalCurrencyService.get_transition_summary()
    assert summary["effective_date"] == "2024-07-01"
    assert "Section 358 BNS" in summary["repeal_provisions"]["IPC"]
    assert "Section 531 BNSS" in summary["repeal_provisions"]["CrPC"]

def test_statutory_concordance():
    # Test Section 438 CrPC
    concordance = LegalCurrencyService.get_statutory_concordance("Can I get anticipatory bail under Section 438?")
    assert len(concordance) > 0
    item = concordance[0]
    assert "482" in item["new_sec"]
    assert "Bharatiya Nagarik Suraksha Sanhita" in item["new_act"]

    # Test Section 379 IPC theft
    concordance_theft = LegalCurrencyService.get_statutory_concordance("My mobile was stolen, Section 379 IPC")
    assert any("303" in c["new_sec"] for c in concordance_theft)

    # Test Section 41A CrPC arrest notice
    concordance_arrest = LegalCurrencyService.get_statutory_concordance("Notice of appearance under Section 41A")
    assert any("35(3)" in c["new_sec"] for c in concordance_arrest)

def test_precedent_continuity():
    precedents = LegalCurrencyService.get_precedent_status("Gurbaksh Singh Sibbia Constitution Bench")
    assert len(precedents) > 0
    assert "Constitution Bench" in precedents[0]["bench"]
    assert "Binding precedent" in precedents[0]["status_under_bnss"]

    precedents_arnesh = LegalCurrencyService.get_precedent_status("Arnesh Kumar arrest guidelines")
    assert len(precedents_arnesh) > 0
    assert "Section 35" in precedents_arnesh[0]["status_under_bnss"]
