from sympy.abc import *
from matchpy.matching.many_to_one import CommutativeMatcher
from matchpy import *
from matchpy.utils import VariableWithCount
from collections import deque
from multiset import Multiset
from sympy.integrals.rubi.constraints import *
from sympy.integrals.rubi.utility_function import *
from sympy.integrals.rubi.rules.miscellaneous_integration import *
from sympy import *


class CommutativeMatcher142286(CommutativeMatcher):
    _instance = None
    patterns = {
    0: (0, Multiset({}), [
      (VariableWithCount('i3.1.2.0', 1, 1, None), Mul),
      (VariableWithCount('i3.1.2.0_1', 1, 1, S(1)), Mul)
])
}
    subjects = {}
    subjects_by_id = {}
    bipartite = BipartiteGraph()
    associative = Mul
    max_optional_count = 1
    anonymous_patterns = set()

    def __init__(self):
        self.add_subject(None)

    @staticmethod
    def get():
        if CommutativeMatcher142286._instance is None:
            CommutativeMatcher142286._instance = CommutativeMatcher142286()
        return CommutativeMatcher142286._instance

    @staticmethod
    def get_match_iter(subject):
        subjects = deque([subject]) if subject is not None else deque()
        subst0 = Substitution()
        # State 142285
        return
        yield


from collections import deque