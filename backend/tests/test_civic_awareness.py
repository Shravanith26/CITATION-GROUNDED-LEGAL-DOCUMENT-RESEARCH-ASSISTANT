"""
Unit tests for Civic Awareness & Rights Advisory Module.
Tests Situations DB (38 situations), Scenarios DB (16 scenarios, 13 categories, 4 difficulties),
RightsEvaluator (12-point structured output), and QuizEngine (scoring & feedback).
"""
import pytest
from backend.app.civic_awareness import (
    SITUATIONS_DB,
    SITUATION_CATEGORIES,
    SCENARIOS_DB,
    SCENARIO_CATEGORIES,
    RightsEvaluator,
    QuizEngine,
)


def test_situations_db_integrity():
    """Verify SITUATIONS_DB contains >= 35 situations with all required schema fields."""
    assert len(SITUATIONS_DB) >= 35, f"Expected >= 35 situations, found {len(SITUATIONS_DB)}"

    required_keys = [
        "id", "title", "category", "summary", "legal_issue",
        "classification", "statutory_provisions", "immediate_steps",
        "evidence_checklist", "reporting_channels", "police_refusal_escalation",
        "know_the_difference", "confidence_level", "related_issues"
    ]

    for sid, sit in SITUATIONS_DB.items():
        assert sit["id"] == sid
        for key in required_keys:
            assert key in sit, f"Situation '{sid}' is missing required key '{key}'"
        assert len(sit["statutory_provisions"]) >= 1, f"Situation '{sid}' has no statutory provisions"
        assert len(sit["immediate_steps"]) >= 1, f"Situation '{sid}' has no immediate steps"
        assert len(sit["evidence_checklist"]) >= 1, f"Situation '{sid}' has no evidence checklist"
        assert len(sit["reporting_channels"]) >= 1, f"Situation '{sid}' has no reporting channels"


def test_scenarios_db_integrity():
    """Verify SCENARIOS_DB covers categories, difficulties, 5 questions, and 12-point breakdowns."""
    assert len(SCENARIOS_DB) >= 14, f"Expected >= 14 scenarios, found {len(SCENARIOS_DB)}"

    diffs_found = set()
    cats_found = set()

    for sc_id, sc in SCENARIOS_DB.items():
        diffs_found.add(sc["difficulty"])
        cats_found.add(sc["category"])

        # Check 5 questions
        questions = sc.get("questions", [])
        assert len(questions) == 5, f"Scenario '{sc_id}' must have exactly 5 questions, found {len(questions)}"
        for q_idx, q in enumerate(questions):
            assert "question" in q
            assert len(q["options"]) == 4, f"Question {q_idx} in '{sc_id}' must have 4 options"
            assert 0 <= q["correct_index"] < 4, f"Question {q_idx} in '{sc_id}' has invalid correct_index"
            assert "explanation" in q and len(q["explanation"]) > 10

        # Check educational breakdown
        eb = sc.get("educational_breakdown", {})
        assert eb, f"Scenario '{sc_id}' is missing educational breakdown"
        assert "case_summary" in eb
        assert "legal_classification" in eb
        assert "statutory_provisions" in eb
        assert "immediate_action_protocol" in eb
        assert "evidence_preservation_protocol" in eb
        assert "reporting_forums" in eb
        assert "remedies_against_refusal" in eb
        assert "key_takeaways" in eb

    assert len(diffs_found) == 4, f"Expected 4 difficulty levels, found {diffs_found}"
    assert len(cats_found) >= 10, f"Expected >= 10 categories covered, found {len(cats_found)}"


def test_rights_evaluator():
    """Test RightsEvaluator search and 12-point advisory generation."""
    evaluator = RightsEvaluator()

    # Search
    results = evaluator.search_situations("phone")
    assert any(r["id"] == "theft_belongings" for r in results)

    results_scam = evaluator.search_situations("digital arrest")
    assert any(r["id"] == "digital_arrest_scam" for r in results_scam)

    # Evaluate advice
    eval_res = evaluator.evaluate_situation("theft_belongings", {"Was physical force used?": "No, secret taking"})
    assert eval_res["situation_id"] == "theft_belongings"
    assert "1_situation_summary" in eval_res
    assert "2_immediate_danger" in eval_res
    assert "3_possible_rights" in eval_res
    assert "4_legal_provisions" in eval_res
    assert "5_what_to_do_right_now" in eval_res
    assert "6_evidence_to_preserve" in eval_res
    assert "7_where_to_report" in eval_res
    assert "8_police_refusal_remedies" in eval_res
    assert "9_know_the_difference" in eval_res
    assert "10_confidence_uncertainty" in eval_res
    assert "11_related_legal_issues" in eval_res
    assert "12_educational_disclaimer" in eval_res

    # Emergency situation check
    snatch_res = evaluator.evaluate_situation("chain_bag_snatching")
    assert snatch_res["2_immediate_danger"]["is_emergency"] is True


def test_quiz_engine():
    """Test QuizEngine filtering, quiz evaluation, scoring, and feedback."""
    engine = QuizEngine()

    all_scenarios = engine.get_all_scenarios()
    assert len(all_scenarios) >= 14

    # Filter
    basic_scenarios = engine.filter_scenarios(difficulty="Basic")
    assert len(basic_scenarios) >= 1

    # Perfect score evaluation
    first_sc = all_scenarios[0]["id"]
    scenario = engine.get_scenario(first_sc)
    perfect_answers = {i: q["correct_index"] for i, q in enumerate(scenario["questions"])}

    eval_perfect = engine.evaluate_quiz(first_sc, perfect_answers)
    assert eval_perfect["correct_count"] == 5
    assert eval_perfect["percentage"] == 100.0
    assert "Champion" in eval_perfect["tier"]

    # Partial score evaluation
    partial_answers = {0: scenario["questions"][0]["correct_index"]}  # Only 1 correct
    eval_partial = engine.evaluate_quiz(first_sc, partial_answers)
    assert eval_partial["correct_count"] == 1
    assert eval_partial["percentage"] == 20.0
