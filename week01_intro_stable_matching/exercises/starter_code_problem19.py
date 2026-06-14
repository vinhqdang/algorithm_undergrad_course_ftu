"""
Problem 19 - Hospital-Residents Problem (Many-to-One Stable Matching)
=======================================================================

Generalize Gale-Shapley to the Hospital-Residents problem: each hospital h
has a capacity `capacity[h]` (it can accept up to that many residents).
Residents propose to hospitals; a hospital holds the best `capacity[h]`
residents it has seen so far (by its preference list) and rejects the rest.

Implement `hospital_resident_matching(residents, hospitals, resident_prefs,
hospital_prefs, capacity)`:

  - `residents`, `hospitals`: lists of names.
  - `resident_prefs[r]`: hospitals in order of preference (best first).
  - `hospital_prefs[h]`: residents in order of preference (best first).
  - `capacity[h]`: max number of residents hospital h can take.

Return a dict `hospital -> list of assigned residents`, where every hospital's
list has length <= capacity[h], and the assignment is stable: no resident r
and hospital h both prefer each other over r's current assignment / one of
h's current residents (the classic "no blocking pair" condition for HR).

See practical_exercises.pdf, Problem 19.
"""

from collections import deque
from typing import Dict, List


def hospital_resident_matching(
    residents: List[str],
    hospitals: List[str],
    resident_prefs: Dict[str, List[str]],
    hospital_prefs: Dict[str, List[str]],
    capacity: Dict[str, int],
) -> Dict[str, List[str]]:
    """Return a stable assignment hospital -> list of residents."""
    # TODO: implement (resident-proposing generalization of Gale-Shapley).
    raise NotImplementedError


if __name__ == "__main__":
    try:
        residents = ["R1", "R2", "R3", "R4"]
        hospitals = ["H1", "H2"]
        resident_prefs = {
            "R1": ["H1", "H2"],
            "R2": ["H1", "H2"],
            "R3": ["H2", "H1"],
            "R4": ["H1", "H2"],
        }
        hospital_prefs = {
            "H1": ["R1", "R2", "R4", "R3"],
            "H2": ["R3", "R1", "R2", "R4"],
        }
        capacity = {"H1": 2, "H2": 2}

        result = hospital_resident_matching(residents, hospitals, resident_prefs, hospital_prefs, capacity)

        # Every resident assigned exactly once; capacities respected.
        all_assigned = [r for residents_at_h in result.values() for r in residents_at_h]
        assert sorted(all_assigned) == sorted(residents)
        for h in hospitals:
            assert len(result[h]) <= capacity[h]

        # H1 (capacity 2) should end up with its two top choices among those
        # who rank it: R1 and R2 both rank H1 first, so both go to H1.
        assert "R1" in result["H1"]
        assert "R2" in result["H1"]

        print("All tests passed!")
    except NotImplementedError:
        print("TODO: implement the functions above.")
