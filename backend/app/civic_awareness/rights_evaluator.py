"""
Rights Evaluator for 'My Rights in This Situation'.
Takes user situation input and answers to dynamic follow-up questions,
producing structured, practical legal advisory in the exact prescribed sequence.
Adheres to current Indian statutes (BNS 2023, BNSS 2023, BSA 2023, and Special Acts).
"""
from typing import Dict, List, Any, Optional
from .situations_db import SITUATIONS_DB, SITUATION_CATEGORIES


class RightsEvaluator:
    """Evaluates everyday citizen situations and provides structured rights guidance."""

    def __init__(self):
        self.situations = SITUATIONS_DB
        self.categories = SITUATION_CATEGORIES

    def get_categories(self) -> List[str]:
        """Return all situation categories."""
        return self.categories

    def get_all_situations(self) -> List[Dict[str, Any]]:
        """Return list of all situation summaries for dropdown/chips."""
        result = []
        for sid, s in self.situations.items():
            result.append({
                "id": s["id"],
                "title": s["title"],
                "category": s["category"],
                "is_emergency": s.get("is_emergency", False)
            })
        return result

    def get_situations_by_category(self, category: str) -> List[Dict[str, Any]]:
        """Filter situations by category."""
        return [
            {"id": s["id"], "title": s["title"], "category": s["category"], "is_emergency": s.get("is_emergency", False)}
            for s in self.situations.values()
            if s.get("category") == category
        ]

    def search_situations(self, query: str) -> List[Dict[str, Any]]:
        """Search situations by keyword match in title, summary, or legal issue."""
        q = query.lower().strip()
        if not q:
            return self.get_all_situations()
        
        matches = []
        for sid, s in self.situations.items():
            text = f"{s['title']} {s['summary']} {s['legal_issue']} {' '.join(s.get('classification', []))}".lower()
            if q in text or any(word in text for word in q.split() if len(word) > 2):
                matches.append({
                    "id": s["id"],
                    "title": s["title"],
                    "category": s["category"],
                    "is_emergency": s.get("is_emergency", False)
                })
        return matches

    def get_situation(self, situation_id: str) -> Optional[Dict[str, Any]]:
        """Get full details of a specific situation."""
        return self.situations.get(situation_id)

    def evaluate_situation(self, situation_id: str, follow_up_answers: Optional[Dict[str, str]] = None) -> Dict[str, Any]:

        """
        Evaluate situation and produce structured output in strict prescribed order:
        1. Situation Summary
        2. Is anyone in immediate danger?
        3. Your possible rights
        4. Possible legal provisions (current BNS, BNSS, BSA, Special Acts)
        5. What to do right now
        6. Evidence to preserve
        7. Where to report
        8. What if police refuse to take action?
        9. Know the difference (Constitutional vs Criminal vs Civil vs Regulatory vs Consumer)
        10. Confidence and uncertainty breakdown
        11. Related legal issues
        12. Educational disclaimer
        """
        sit = self.situations.get(situation_id)
        if not sit:
            # Fallback to general diagnostic
            sit = self.situations.get("general_diagnostic_unsure", list(self.situations.values())[0])

        follow_up_answers = follow_up_answers or {}

        # 1. Situation Summary
        summary = sit["summary"]
        if follow_up_answers:
            notes = [f"{q}: {ans}" for q, ans in follow_up_answers.items() if ans]
            if notes:
                summary += f" (Context noted: {'; '.join(notes)})"

        # 2. Immediate danger assessment
        is_emergency = sit.get("is_emergency", False)
        # Check if user selected high-danger follow-up option
        for ans in follow_up_answers.values():
            if any(term in ans.lower() for term in ["emergency", "deadly", "kill", "firearm", "locked out", "hostel", "acid", "minor child", "golden hour"]):
                is_emergency = True

        danger_info = {
            "is_emergency": is_emergency,
            "banner_text": (
                "🚨 **URGENT EMERGENCY ALERT: IMMEDIATE SAFETY FIRST!**\n"
                "If you or anyone else is in imminent physical danger or under active attack, do NOT read legal documents. "
                "Reach a crowded/safe space immediately and call emergency helplines:\n"
                "- **National Emergency Number**: 112\n"
                "- **Women Distress Helpline**: 1090 / 181\n"
                "- **Childline**: 1098\n"
                "- **Cyber Financial Fraud**: 1930 (Golden Hour)\n"
                "- **Senior Citizen Elderline**: 14567"
            ) if is_emergency else (
                "ℹ️ **No Immediate Physical Danger Detected**: Proceed with standard legal documentation and reporting steps outlined below."
            )
        }

        # 3. Possible rights
        possible_rights = self._derive_rights(sit, follow_up_answers)

        # 4. Possible legal provisions
        legal_provisions = {
            "statutes": sit.get("statutory_provisions", []),
            "constitutional": sit.get("constitutional_articles", []),
            "classification": sit.get("classification", [])
        }

        # 5. What to do right now
        what_to_do_now = list(sit.get("immediate_steps", []))

        # 6. Evidence to preserve
        evidence_checklist = list(sit.get("evidence_checklist", []))

        # 7. Where to report
        reporting_channels = list(sit.get("reporting_channels", []))

        # 8. What if police refuse
        police_refusal = sit.get(
            "police_refusal_escalation",
            "Under Section 173(4) BNSS, you can send the substance of your information in writing by registered post to the Superintendent of Police (SP). If no investigation is ordered, file an application before the Judicial Magistrate under Section 175(3) BNSS."
        )

        # 9. Know the difference
        know_the_difference = sit.get("know_the_difference", "")

        # 10. Confidence and uncertainty breakdown
        confidence_breakdown = self._derive_confidence_breakdown(sit, follow_up_answers)

        # 11. Related legal issues
        related_issues = sit.get("related_issues", [])

        # 12. Educational disclaimer
        disclaimer = (
            "⚖️ **Educational & Informational Disclaimer**: "
            "This structured guidance is provided for civic awareness, educational understanding, and procedural empowerment under the laws of India "
            "(including the Bharatiya Nyaya Sanhita, 2023, Bharatiya Nagarik Suraksha Sanhita, 2023, Bharatiya Sakshya Adhiniyam, 2023, and relevant Special Acts). "
            "It does not constitute formal legal advice, an attorney-client relationship, or a substitute for professional legal counsel. "
            "For active criminal defence, complex property litigation, or courtroom filing, please consult a qualified advocate or the District Legal Services Authority (DLSA / NALSA Toll-Free: 15100)."
        )

        return {
            "situation_id": sit["id"],
            "situation_title": sit["title"],
            "category": sit["category"],
            "1_situation_summary": summary,
            "2_immediate_danger": danger_info,
            "3_possible_rights": possible_rights,
            "4_legal_provisions": legal_provisions,
            "5_what_to_do_right_now": what_to_do_now,
            "6_evidence_to_preserve": evidence_checklist,
            "7_where_to_report": reporting_channels,
            "8_police_refusal_remedies": police_refusal,
            "9_know_the_difference": know_the_difference,
            "10_confidence_uncertainty": confidence_breakdown,
            "11_related_legal_issues": related_issues,
            "12_educational_disclaimer": disclaimer,
            "raw_follow_up_questions": sit.get("follow_up_questions", [])
        }

    def _derive_rights(self, sit: Dict[str, Any], follow_up_answers: Dict[str, str]) -> List[str]:
        """Derive citizen rights based on situation and answers."""
        rights = []

        # Classification based rights
        classes = sit.get("classification", [])
        if "Criminal Offence" in classes or "Cybercrime" in classes:
            rights.append("Right to mandatory registration of First Information Report (FIR) for cognizable offences under Section 173 BNSS.")
            rights.append("Right to receive a certified copy of the registered FIR immediately and free of cost.")
            rights.append("Right to register a 'Zero FIR' at any police station regardless of territorial boundaries.")

        if "Safety & Crimes Against Women" in sit.get("category", "") or any("women" in c.lower() for c in classes):
            rights.append("Right to have statements recorded exclusively by a woman police officer under Section 173(1) BNSS.")
            rights.append("Right to complete confidentiality of victim identity under Section 73 BNS.")
            rights.append("Right to free medical trauma treatment at all government and private hospitals under Section 397 BNSS.")
            rights.append("Strict statutory prohibition against the two-finger test in sexual assault medical examinations.")

        if "Crimes Against Children" in sit.get("category", ""):
            rights.append("Right to child-friendly recording of statements by police in civilian clothes at the child's residence.")
            rights.append("Right to complete confidentiality of child's identity under Section 33(7) of the POCSO Act.")
            rights.append("Right to interim financial compensation from the Special POCSO Court for rehabilitation.")

        if "Senior Citizens" in sit.get("category", ""):
            rights.append("Right to monthly maintenance from adult children/heirs under Section 4 & 9 of the MWPSC Act, 2007.")
            rights.append("Right to summary cancellation of property gift deeds under Section 23 of the MWPSC Act if care is denied.")
            rights.append("Right to lawyer-free, fast-track 90-day tribunal proceedings before the Sub-Divisional Magistrate (SDM).")

        if "Consumer Dispute" in classes:
            rights.append("Right to full refund, replacement, or compensation for defective goods/deficient services under Consumer Protection Act, 2019.")
            rights.append("Right to file digital consumer cases through the E-Daakhil portal (edaakhil.nic.in) without physical court appearance.")

        if sit.get("constitutional_articles"):
            for art in sit["constitutional_articles"]:
                rights.append(f"Constitutional entitlement under {art['article']} ({art['name']}): {art['connection']}")

        rights.append("Right to free legal aid through the District Legal Services Authority (DLSA / NALSA Helpline: 15100).")
        return rights

    def _derive_confidence_breakdown(self, sit: Dict[str, Any], follow_up_answers: Dict[str, str]) -> Dict[str, Any]:
        """Build confidence breakdown: Confirmed vs Potentially Applicable vs Depends on Facts."""
        confirmed = []
        potential = []
        fact_dependent = []

        # Confirmed
        for p in sit.get("statutory_provisions", []):
            confirmed.append(f"{p['act']} - {p['section']}: {p['deals_with']}")

        # Potential / contextual based on follow up
        if sit.get("constitutional_articles"):
            for a in sit["constitutional_articles"]:
                potential.append(f"{a['article']} ({a['name']}): Enforceable if state authority, public space, or fundamental rights are infringed.")

        # Fact dependent
        fact_dependent.append("Whether specific penal sections attract bailable or non-bailable classification depends on the investigating officer's FIR and medical/forensic reports.")
        fact_dependent.append("Exact quantum of victim compensation depends on the District Legal Services Authority (DLSA) assessment under Section 396 BNSS.")
        fact_dependent.append("Civil recovery of financial losses in cyber fraud depends on the speed of reporting to 1930 within the Golden Hour before funds leave the banking grid.")

        return {
            "overall_assessment": sit.get("confidence_level", "High confidence based on statutory provisions."),
            "confirmed_provisions": confirmed,
            "potentially_applicable": potential,
            "depends_on_facts": fact_dependent
        }

    # Backward compatibility alias
    evaluate = evaluate_situation

