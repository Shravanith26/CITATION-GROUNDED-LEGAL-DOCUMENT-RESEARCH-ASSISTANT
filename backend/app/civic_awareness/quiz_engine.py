"""
Quiz Engine for Interactive Legal Case-Studies & Civic Awareness.
Powers scenario filtering, multi-question legal quizzes (5 questions per scenario),
scoring, question-by-question feedback, and 12-point educational deep-dives.
"""
from typing import Dict, List, Any, Optional
from .scenarios_db import SCENARIOS_DB, SCENARIO_CATEGORIES, DIFFICULTY_LEVELS


class QuizEngine:
    """Manages legal case studies, quizzes, and educational reviews."""

    def __init__(self):
        self.scenarios = SCENARIOS_DB
        self.categories = SCENARIO_CATEGORIES
        self.difficulties = DIFFICULTY_LEVELS

    def get_categories(self) -> List[str]:
        """Return all scenario categories."""
        return self.categories

    def get_difficulties(self) -> List[str]:
        """Return all difficulty levels."""
        return self.difficulties

    def get_all_scenarios(self) -> List[Dict[str, Any]]:
        """Return all scenarios metadata."""
        return [
            {
                "id": s["id"],
                "title": s["title"],
                "category": s["category"],
                "difficulty": s["difficulty"],
                "total_questions": len(s.get("questions", []))
            }
            for s in self.scenarios.values()
        ]

    def filter_scenarios(self, category: Optional[str] = None, difficulty: Optional[str] = None) -> List[Dict[str, Any]]:
        """Filter scenarios by category and/or difficulty level."""
        results = []
        for s in self.scenarios.values():
            if category and category != "All Categories" and s["category"] != category:
                continue
            if difficulty and difficulty != "All Difficulties" and s["difficulty"] != difficulty:
                continue
            results.append({
                "id": s["id"],
                "title": s["title"],
                "category": s["category"],
                "difficulty": s["difficulty"],
                "total_questions": len(s.get("questions", []))
            })
        return results

    def get_scenario(self, scenario_id: str) -> Optional[Dict[str, Any]]:
        """Fetch complete scenario object including story, questions, and breakdown."""
        return self.scenarios.get(scenario_id)

    def evaluate_quiz(self, scenario_id: str, user_answers: Dict[int, int]) -> Dict[str, Any]:
        """
        Evaluate user answers for the 5 scenario questions.
        user_answers: dict mapping question_index (0 to 4) -> selected_option_index (0 to 3)
        Returns:
            score, percentage, results_per_question, performance_tier, feedback
        """
        scenario = self.scenarios.get(scenario_id)
        if not scenario:
            return {"error": "Scenario not found"}

        questions = scenario.get("questions", [])
        total = len(questions)
        correct_count = 0
        details = []

        for idx, q in enumerate(questions):
            user_choice = user_answers.get(idx)
            correct_choice = q["correct_index"]
            is_correct = (user_choice == correct_choice)
            if is_correct:
                correct_count += 1

            details.append({
                "question_index": idx,
                "question": q["question"],
                "options": q["options"],
                "user_choice": user_choice,
                "user_choice_text": q["options"][user_choice] if user_choice is not None and 0 <= user_choice < len(q["options"]) else "Not Answered",
                "correct_choice": correct_choice,
                "correct_choice_text": q["options"][correct_choice],
                "is_correct": is_correct,
                "explanation": q["explanation"]
            })

        percentage = round((correct_count / total * 100), 1) if total > 0 else 0

        # Tier & Feedback
        if percentage == 100:
            tier = "🏆 Civic Law Champion"
            feedback = "Flawless! You possess exceptional legal awareness of Indian statutory protections, procedural rights, and forensic evidence standards."
        elif percentage >= 80:
            tier = "⚖️ Legal Literacy Expert"
            feedback = "Impressive performance! You demonstrate sound practical knowledge of Indian legal remedies and rights in crisis situations."
        elif percentage >= 60:
            tier = "📘 Informed Citizen"
            feedback = "Good foundation! You recognized the core legal avenues, but review the nuanced procedural details and evidence protocols below."
        else:
            tier = "🌱 Developing Awareness"
            feedback = "Valuable learning opportunity. Common legal myths often mislead citizens; carefully study the 12-point educational breakdown below to empower your civic rights."

        return {
            "scenario_id": scenario_id,
            "scenario_title": scenario["title"],
            "total_questions": total,
            "correct_count": correct_count,
            "percentage": percentage,
            "tier": tier,
            "feedback": feedback,
            "question_evaluations": details,
            "educational_breakdown": scenario.get("educational_breakdown", {})
        }

    def get_educational_breakdown(self, scenario_id: str) -> Optional[Dict[str, Any]]:
        """Return the 12-point educational breakdown for study mode."""
        s = self.scenarios.get(scenario_id)
        if not s:
            return None
        return s.get("educational_breakdown")

    # Backward compatibility alias
    get_educational_deep_dive = get_educational_breakdown

