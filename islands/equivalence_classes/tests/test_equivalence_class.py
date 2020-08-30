from equivalence_classes.equivalence_class import EquivalenceTable


def test_correct_root():
    members = {1: 1, 2: 5, 5: 8, 8: 1}
    equivalence_table = EquivalenceTable()
    equivalence_table.members = members

    assert equivalence_table[2] == 1
    assert equivalence_table[5] == 1
    assert equivalence_table[8] == 1
    assert equivalence_table[1] == 1
