"""
Problem 19 - Hospital-Residents Problem (Many-to-One Stable Matching) (SOLUTION)
===================================================================================
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
    free = deque(residents)
    next_idx = {r: 0 for r in residents}
    assigned: Dict[str, List[str]] = {h: [] for h in hospitals}

    while free:
        r = free.popleft()
        if next_idx[r] >= len(resident_prefs[r]):
            continue  # r has been rejected by every hospital on their list

        h = resident_prefs[r][next_idx[r]]
        next_idx[r] += 1

        assigned[h].append(r)
        if len(assigned[h]) > capacity[h]:
            worst = max(assigned[h], key=lambda x: hospital_prefs[h].index(x))
            assigned[h].remove(worst)
            free.append(worst)

    return assigned


if __name__ == "__main__":
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

    all_assigned = [r for residents_at_h in result.values() for r in residents_at_h]
    assert sorted(all_assigned) == sorted(residents)
    for h in hospitals:
        assert len(result[h]) <= capacity[h]

    assert "R1" in result["H1"]
    assert "R2" in result["H1"]

    print("All tests passed!")
