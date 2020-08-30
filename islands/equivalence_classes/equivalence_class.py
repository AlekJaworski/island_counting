from __future__ import annotations


class EquivalenceTable:
    # todo: perhaps this could be improved to keep the 'Tree' balanced and decrease the worst case lookup o(N) time that it has currently.
    # todo: However I have run out of time at this point.
    def __init__(self):
        self.members = {}

    def __setitem__(self, key, item):
        self.members[key] = item

    def __getitem__(self, key):
        retrieved = self.members[key]
        while self.members[retrieved] != retrieved:
            retrieved = self.members[retrieved]
        return retrieved

    def __repr__(self):
        return repr({x for x, y in self.members.items() if x == y})

    def join(self, new_root, joined):
        """ joins a to b"""
        self[self[joined]] = self[new_root]

    @staticmethod
    def create_from_list(l):
        members = {x: x for x in l}
        res = EquivalenceTable()
        res.members = members
        return res
