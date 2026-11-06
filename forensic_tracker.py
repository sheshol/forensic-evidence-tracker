"""
Forensic Evidence Tracker
Author: [sheshol]
Date: [06/11/2026]
Purpose: Search evidence records by Evidence ID for GCSec's DFIP.
Version: 1.0
"""

# ---------------------------------------------------------------------------
# Data: the evidence records held by the tracker.
# Each record is a dictionary with an ID, type and priority.
# ---------------------------------------------------------------------------
evidence_records = [
    {"id": "EV001", "type": "Laptop", "priority": 2},
    {"id": "EV002", "type": "Mobile Phone", "priority": 1},
    {"id": "EV003", "type": "USB Drive", "priority": 3},
    {"id": "EV004", "type": "Hard Drive", "priority": 2},
    {"id": "EV005", "type": "SIM Card", "priority": 1},
]


# ---------------------------------------------------------------------------
# Functions
# ---------------------------------------------------------------------------
def search_evidence(evidence_list, evidence_id):
    """Return the evidence record matching evidence_id, or None if not found.

    Uses a linear search: each record is checked in order until a match
    is found or the list is exhausted.
    """
    for evidence in evidence_list:
        if evidence["id"] == evidence_id:
            return evidence
    return None


def get_evidence_id():
    """Prompt the user for an Evidence ID and normalise the input.

    Spaces are removed and the text is converted to upper case so that
    inputs such as '  ev002  ' still match 'EV002'.
    """
    return input("Enter Evidence ID: ").strip().upper()


def display_result(result):
    """Print the matching record, or a not-found message if result is None."""
    if result:
        print("Evidence found:", result)
    else:
        print("Evidence not found")


def main():
    """Run the tracker: get an ID, search the records, display the result."""
    evidence_id = get_evidence_id()
    result = search_evidence(evidence_records, evidence_id)
    display_result(result)


# ---------------------------------------------------------------------------
# Entry point
# ---------------------------------------------------------------------------
if __name__ == "__main__":
    main()