"""
Indian Criminal Law Transitional Concordance & Precedent Continuity Engine.
Handles the legal transition effective July 1, 2024 from IPC/CrPC/IEA to BNS/BNSS/BSA,
and tracks Supreme Court precedent continuity under Article 141 of the Constitution.
"""

import re
from typing import Optional, Dict, Any, List

TRANSITION_DATE = "2024-07-01"

IPC_TO_BNS: Dict[str, Dict[str, str]] = {
    "378": {
        "old_act": "Indian Penal Code, 1860 (IPC)",
        "old_sec": "Section 378 / 379",
        "new_act": "Bharatiya Nyaya Sanhita, 2023 (BNS)",
        "new_sec": "Section 303(2)",
        "title": "Theft and punishment for theft",
        "note": "Theft of movable property without consent. BNS also creates a dedicated offence for Snatching under Section 304."
    },
    "379": {
        "old_act": "Indian Penal Code, 1860 (IPC)",
        "old_sec": "Section 379",
        "new_act": "Bharatiya Nyaya Sanhita, 2023 (BNS)",
        "new_sec": "Section 303(2)",
        "title": "Punishment for theft",
        "note": "Up to 3 years imprisonment or fine or both; for first-time minor theft (<Rs. 5,000 with return), community service may be ordered under BNS."
    },
    "415": {
        "old_act": "Indian Penal Code, 1860 (IPC)",
        "old_sec": "Section 415 / 420",
        "new_act": "Bharatiya Nyaya Sanhita, 2023 (BNS)",
        "new_sec": "Section 318(4)",
        "title": "Cheating and dishonestly inducing delivery of property",
        "note": "Punishment remains up to 7 years imprisonment with fine under Section 318(4) BNS."
    },
    "420": {
        "old_act": "Indian Penal Code, 1860 (IPC)",
        "old_sec": "Section 420",
        "new_act": "Bharatiya Nyaya Sanhita, 2023 (BNS)",
        "new_sec": "Section 318(4)",
        "title": "Cheating and dishonestly inducing delivery of property",
        "note": "Corresponds directly to Section 318(4) of BNS 2023."
    },
    "498a": {
        "old_act": "Indian Penal Code, 1860 (IPC)",
        "old_sec": "Section 498A",
        "new_act": "Bharatiya Nyaya Sanhita, 2023 (BNS)",
        "new_sec": "Section 85 / 86",
        "title": "Husband or relative of husband subjecting woman to cruelty",
        "note": "Section 85 BNS prescribes punishment (up to 3 years and fine). Section 86 defines cruelty."
    },
    "304b": {
        "old_act": "Indian Penal Code, 1860 (IPC)",
        "old_sec": "Section 304B",
        "new_act": "Bharatiya Nyaya Sanhita, 2023 (BNS)",
        "new_sec": "Section 80",
        "title": "Dowry death",
        "note": "Death of a woman within 7 years of marriage under suspicious circumstances with cruelty/harassment for dowry."
    },
    "302": {
        "old_act": "Indian Penal Code, 1860 (IPC)",
        "old_sec": "Section 302",
        "new_act": "Bharatiya Nyaya Sanhita, 2023 (BNS)",
        "new_sec": "Section 103(1)",
        "title": "Punishment for murder",
        "note": "Section 103(1) BNS retains death or life imprisonment. Section 103(2) introduces specific penalties for mob lynching."
    },
    "406": {
        "old_act": "Indian Penal Code, 1860 (IPC)",
        "old_sec": "Section 406",
        "new_act": "Bharatiya Nyaya Sanhita, 2023 (BNS)",
        "new_sec": "Section 316",
        "title": "Punishment for criminal breach of trust",
        "note": "Up to 5 years imprisonment or fine or both under Section 316(2) BNS."
    }
}

CRPC_TO_BNSS: Dict[str, Dict[str, str]] = {
    "438": {
        "old_act": "Code of Criminal Procedure, 1973 (CrPC)",
        "old_sec": "Section 438",
        "new_act": "Bharatiya Nagarik Suraksha Sanhita, 2023 (BNSS)",
        "new_sec": "Section 482",
        "title": "Direction for grant of bail to person apprehending arrest (Anticipatory Bail)",
        "note": "Section 482 BNSS mirrors Section 438 CrPC. Sub-section (3) clarifies that physical presence of applicant in court is not mandatory at the time of hearing unless ordered."
    },
    "482": {
        "old_act": "Code of Criminal Procedure, 1973 (CrPC)",
        "old_sec": "Section 482 (Inherent Powers) / Section 438",
        "new_act": "Bharatiya Nagarik Suraksha Sanhita, 2023 (BNSS)",
        "new_sec": "Section 528 (Inherent Powers) / Section 482 (Anticipatory Bail)",
        "title": "Inherent Powers of High Court / Anticipatory Bail in BNSS",
        "note": "Note: Inherent powers of High Court (quashing FIR/proceedings) are under Section 528 BNSS. Section 482 in BNSS is for Anticipatory Bail."
    },
    "154": {
        "old_act": "Code of Criminal Procedure, 1973 (CrPC)",
        "old_sec": "Section 154",
        "new_act": "Bharatiya Nagarik Suraksha Sanhita, 2023 (BNSS)",
        "new_sec": "Section 173",
        "title": "Information in cognizable cases (First Information Report - FIR)",
        "note": "Section 173 BNSS explicitly recognizes Zero FIR and electronic information (e-FIR) with signature required within 3 days."
    },
    "41a": {
        "old_act": "Code of Criminal Procedure, 1973 (CrPC)",
        "old_sec": "Section 41A",
        "new_act": "Bharatiya Nagarik Suraksha Sanhita, 2023 (BNSS)",
        "new_sec": "Section 35(3)",
        "title": "Notice of appearance before police officer",
        "note": "Mandatory notice of appearance for offences punishable with up to 7 years imprisonment. Failure to comply allows arrest under Section 35(6) BNSS."
    },
    "437": {
        "old_act": "Code of Criminal Procedure, 1973 (CrPC)",
        "old_sec": "Section 437",
        "new_act": "Bharatiya Nagarik Suraksha Sanhita, 2023 (BNSS)",
        "new_sec": "Section 480",
        "title": "When bail may be taken in case of non-bailable offence",
        "note": "Regular bail powers before Magistrates; includes special protections for women, sick, or infirm accused."
    },
    "439": {
        "old_act": "Code of Criminal Procedure, 1973 (CrPC)",
        "old_sec": "Section 439",
        "new_act": "Bharatiya Nagarik Suraksha Sanhita, 2023 (BNSS)",
        "new_sec": "Section 483",
        "title": "Special powers of High Court or Court of Session regarding bail",
        "note": "Powers of Sessions Court and High Court to grant regular bail or set aside bail conditions."
    },
    "167": {
        "old_act": "Code of Criminal Procedure, 1973 (CrPC)",
        "old_sec": "Section 167",
        "new_act": "Bharatiya Nagarik Suraksha Sanhita, 2023 (BNSS)",
        "new_sec": "Section 187",
        "title": "Procedure when investigation cannot be completed in 24 hours (Remand)",
        "note": "Section 187 BNSS allows police custody of 15 days to be taken in whole or in parts during the first 40 or 60 days of detention."
    }
}

PRECEDENT_CONTINUITY: Dict[str, Dict[str, str]] = {
    "gurbaksh singh sibbia": {
        "bench": "5-Judge Constitution Bench (1980)",
        "citation": "(1980) 2 SCC 565",
        "statute_interpreted": "Section 438 CrPC -> Section 482 BNSS 2023",
        "binding_holding": "Anticipatory bail discretion must not be truncated by reading fetters not in the statute. No blanket bail orders; applicant must show reasonable apprehension of arrest for specific offences.",
        "status_under_bnss": "Binding precedent under Article 141 as Section 482 BNSS is pari materia with Section 438 CrPC."
    },
    "sushila aggarwal": {
        "bench": "5-Judge Constitution Bench (2020)",
        "citation": "(2020) 5 SCC 1",
        "statute_interpreted": "Section 438 CrPC -> Section 482 BNSS 2023",
        "binding_holding": "Anticipatory bail is not ordinarily limited to a fixed duration and continues till conclusion of trial. It does not automatically lapse upon filing of charge sheet under Section 173(2).",
        "status_under_bnss": "Fully applicable to Section 482 BNSS 2023."
    },
    "arnesh kumar": {
        "bench": "Division Bench (2014)",
        "citation": "(2014) 8 SCC 273",
        "statute_interpreted": "Section 41 & 41A CrPC -> Section 35(1) & 35(3) BNSS 2023",
        "binding_holding": "Mandatory checklist must be filled and furnished to Magistrate for offences punishable with up to 7 years. Arrest should not be casual or automatic.",
        "status_under_bnss": "Codified and strengthened in Section 35 of BNSS 2023."
    },
    "satender kumar antil": {
        "bench": "Division Bench (2022)",
        "citation": "(2022) 10 SCC 51",
        "statute_interpreted": "Bail jurisprudence & Sections 41, 41A, 88, 170, 204, 209 CrPC -> BNSS",
        "binding_holding": "Categorisation of offences (Categories A to D) for bail. Non-arrest during investigation warrants bail without remand upon charge sheet submission.",
        "status_under_bnss": "Binding law guiding bail decisions under BNSS 2023."
    },
    "lalita kumari": {
        "bench": "5-Judge Constitution Bench (2014)",
        "citation": "(2014) 2 SCC 1",
        "statute_interpreted": "Section 154 CrPC -> Section 173 BNSS 2023",
        "binding_holding": "Registration of FIR is mandatory under Section 154 CrPC if information discloses commission of a cognizable offence.",
        "status_under_bnss": "Directly enacted into statutory mandate in Section 173 BNSS."
    }
}

class LegalCurrencyService:
    """Provides transitional law guidance and statutory concordance."""

    @classmethod
    def get_statutory_concordance(cls, text: str) -> List[Dict[str, Any]]:
        """Identifies mentions of statutory sections and returns concordance cards."""
        results = []
        lowered = text.lower()

        # Check CrPC / BNSS provisions
        for sec, data in CRPC_TO_BNSS.items():
            pattern = r"(?:section\s+|s\.\s*|sec\.?\s*)?" + re.escape(sec) + r"\b"
            if re.search(pattern, lowered) or (sec == "438" and "anticipatory bail" in lowered) or (sec == "154" and "fir" in lowered):
                results.append({"type": "procedural", "key": sec, **data})

        # Check IPC / BNS provisions
        for sec, data in IPC_TO_BNS.items():
            pattern = r"(?:section\s+|s\.\s*|sec\.?\s*)?" + re.escape(sec) + r"\b"
            if re.search(pattern, lowered) or (sec in ["378", "379"] and ("theft" in lowered or "stolen" in lowered)) or (sec in ["415", "420"] and ("cheating" in lowered or "fraud" in lowered)) or (sec == "498a" and "cruelty" in lowered):
                if not any(r["key"] == sec for r in results):
                    results.append({"type": "substantive", "key": sec, **data})

        return results

    @classmethod
    def get_precedent_status(cls, text: str) -> List[Dict[str, Any]]:
        """Checks if any landmark precedent is referenced and returns its status under the new codes."""
        lowered = text.lower()
        matched = []
        for name, data in PRECEDENT_CONTINUITY.items():
            if name in lowered or any(part in lowered for part in name.split() if len(part) > 4):
                matched.append({"case_name": name.title(), **data})
        return matched

    @classmethod
    def get_transition_summary(cls) -> Dict[str, Any]:
        """Returns standard overview of the July 1, 2024 Indian criminal law reform."""
        return {
            "effective_date": TRANSITION_DATE,
            "repeal_provisions": {
                "IPC": "Replaced by Bharatiya Nyaya Sanhita, 2023 (Section 358 BNS)",
                "CrPC": "Replaced by Bharatiya Nagarik Suraksha Sanhita, 2023 (Section 531 BNSS)",
                "IEA": "Replaced by Bharatiya Sakshya Adhiniyam, 2023 (Section 170 BSA)"
            },
            "rule_of_application": (
                "Under Section 531(2) BNSS and established constitutional principles against ex-post facto laws (Art. 20(1)): "
                "1. Offence committed BEFORE July 1, 2024: Substantive guilt and penalties are governed by IPC 1860; pending investigations/trials continue under CrPC 1973. "
                "2. Offence committed ON OR AFTER July 1, 2024: Substantive offence is charged under BNS 2023; procedures, investigation, and bail applications follow BNSS 2023."
            ),
            "precedent_status": (
                "Under Article 141 of the Constitution, authoritative interpretations rendered by the Supreme Court of India "
                "on sections of CrPC/IPC remain binding on all courts in India for corresponding provisions of BNSS/BNS that are pari materia."
            )
        }
