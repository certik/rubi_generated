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


class CommutativeMatcher72785(CommutativeMatcher):
    _instance = None
    patterns = {
    0: (0, Multiset({0: 1}), [
      (VariableWithCount('i3.1.2.1.0', 1, 1, S(1)), Mul)
]),
    1: (1, Multiset({1: 1}), [
      (VariableWithCount('i3.1.2.1.0', 1, 1, S(1)), Mul)
]),
    2: (2, Multiset({2: 1}), [
      (VariableWithCount('i3.1.2.1.0', 1, 1, S(1)), Mul)
]),
    3: (3, Multiset({3: 1}), [
      (VariableWithCount('i3.1.2.1.0', 1, 1, S(1)), Mul)
]),
    4: (4, Multiset({4: 1}), [
      (VariableWithCount('i3.1.2.1.0', 1, 1, S(1)), Mul)
]),
    5: (5, Multiset({5: 1}), [
      (VariableWithCount('i3.1.2.1.0', 1, 1, S(1)), Mul)
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
        if CommutativeMatcher72785._instance is None:
            CommutativeMatcher72785._instance = CommutativeMatcher72785()
        return CommutativeMatcher72785._instance

    @staticmethod
    def get_match_iter(subject):
        subjects = deque([subject]) if subject is not None else deque()
        subst0 = Substitution()
        # State 72784
        if len(subjects) >= 1 and isinstance(subjects[0], Pow):
            tmp1 = subjects.popleft()
            subjects2 = deque(tmp1._args)
            # State 72786
            if len(subjects2) >= 1:
                tmp3 = subjects2.popleft()
                subst1 = Substitution(subst0)
                try:
                    subst1.try_add_variable('i3.1.2.1.1', tmp3)
                except ValueError:
                    pass
                else:
                    pass
                    # State 72787
                    if len(subjects2) >= 1:
                        tmp5 = subjects2.popleft()
                        subst2 = Substitution(subst1)
                        try:
                            subst2.try_add_variable('i3.1.2.1.2', tmp5)
                        except ValueError:
                            pass
                        else:
                            pass
                            # State 72788
                            if len(subjects2) == 0:
                                pass
                                # State 72789
                                if len(subjects) == 0:
                                    pass
                                    # 0: x**n /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f378) and (cons_f167)
                                    yield 0, subst2
                                    # 1: x**n /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f198)
                                    yield 1, subst2
                                    # 2: x**n /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f491)
                                    yield 2, subst2
                                    # 3: x**n /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f4)
                                    yield 3, subst2
                                    # 4: x**n /; (cons_f4) and (cons_f70) and (cons_f71)
                                    yield 4, subst2
                                    # 5: x**n /; (cons_f4) and (cons_f70)
                                    yield 5, subst2
                        subjects2.appendleft(tmp5)
                subjects2.appendleft(tmp3)
            subjects.appendleft(tmp1)
        return
        yield


from collections import deque