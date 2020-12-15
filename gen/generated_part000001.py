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


class CommutativeMatcher2315(CommutativeMatcher):
    _instance = None
    patterns = {
    0: (0, Multiset({0: 1}), [
      (VariableWithCount('i2.0', 1, 1, S(1)), Mul)
]),
    1: (1, Multiset({}), [
      (VariableWithCount('i2.0', 1, 1, None), Mul),
      (VariableWithCount('i2.0_1', 1, 1, S(1)), Mul)
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
        if CommutativeMatcher2315._instance is None:
            CommutativeMatcher2315._instance = CommutativeMatcher2315()
        return CommutativeMatcher2315._instance

    @staticmethod
    def get_match_iter(subject):
        subjects = deque([subject]) if subject is not None else deque()
        subst0 = Substitution()
        # State 2314
        subst1 = Substitution(subst0)
        try:
            subst1.try_add_variable('i2.2', S(1))
        except ValueError:
            pass
        else:
            pass
            # State 2316
            if len(subjects) >= 1:
                tmp2 = subjects.popleft()
                subst2 = Substitution(subst1)
                try:
                    subst2.try_add_variable('i2.1', tmp2)
                except ValueError:
                    pass
                else:
                    pass
                    if 'i2.2' not in subst2 or 'i2.1' not in subst2 or cons_f4(n=subst2["i2.2"], x=subst2["i2.1"]):
                        pass
                        if 'i2.0' not in subst2 or 'i2.1' not in subst2 or cons_f3(b=subst2["i2.0"], x=subst2["i2.1"]):
                            pass
                            # State 2317
                            if len(subjects) == 0:
                                pass
                                # 0: x**n /; (cons_f4) and (cons_f3) and (cons_a1)
                                yield 0, subst2
                subjects.appendleft(tmp2)
        if len(subjects) >= 1 and isinstance(subjects[0], Pow):
            tmp4 = subjects.popleft()
            subjects5 = deque(tmp4._args)
            # State 2318
            if len(subjects5) >= 1:
                tmp6 = subjects5.popleft()
                subst1 = Substitution(subst0)
                try:
                    subst1.try_add_variable('i2.1', tmp6)
                except ValueError:
                    pass
                else:
                    pass
                    if 'i2.2' not in subst1 or 'i2.1' not in subst1 or cons_f4(n=subst1["i2.2"], x=subst1["i2.1"]):
                        pass
                        if 'i2.0' not in subst1 or 'i2.1' not in subst1 or cons_f3(b=subst1["i2.0"], x=subst1["i2.1"]):
                            pass
                            # State 2319
                            subst2 = Substitution(subst1)
                            try:
                                subst2.try_add_variable('i2.2', 1)
                            except ValueError:
                                pass
                            else:
                                pass
                                if 'i2.2' not in subst2 or 'i2.1' not in subst2 or cons_f4(n=subst2["i2.2"], x=subst2["i2.1"]):
                                    pass
                                    if 'i2.2' not in subst2 or cons_a1(n=subst2["i2.2"]):
                                        pass
                                        # State 2320
                                        if len(subjects5) == 0:
                                            pass
                                            # State 2321
                                            if len(subjects) == 0:
                                                pass
                                                # 0: x**n /; (cons_f4) and (cons_f3) and (cons_a1)
                                                yield 0, subst2
                            if len(subjects5) >= 1:
                                tmp9 = subjects5.popleft()
                                subst2 = Substitution(subst1)
                                try:
                                    subst2.try_add_variable('i2.2', tmp9)
                                except ValueError:
                                    pass
                                else:
                                    pass
                                    if 'i2.2' not in subst2 or 'i2.1' not in subst2 or cons_f4(n=subst2["i2.2"], x=subst2["i2.1"]):
                                        pass
                                        if 'i2.2' not in subst2 or cons_a1(n=subst2["i2.2"]):
                                            pass
                                            # State 2320
                                            if len(subjects5) == 0:
                                                pass
                                                # State 2321
                                                if len(subjects) == 0:
                                                    pass
                                                    # 0: x**n /; (cons_f4) and (cons_f3) and (cons_a1)
                                                    yield 0, subst2
                                subjects5.appendleft(tmp9)
                subjects5.appendleft(tmp6)
            subjects.appendleft(tmp4)
        return
        yield


from collections import deque