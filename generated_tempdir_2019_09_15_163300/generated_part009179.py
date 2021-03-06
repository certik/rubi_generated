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


class CommutativeMatcher122491(CommutativeMatcher):
    _instance = None
    patterns = {
    0: (0, Multiset({0: 1}), [
      (VariableWithCount('i3.1.2.0', 1, 1, S(0)), Add)
]),
    1: (1, Multiset({1: 1}), [
      (VariableWithCount('i3.1.2.0', 1, 1, S(0)), Add)
]),
    2: (2, Multiset({2: 1}), [
      (VariableWithCount('i3.1.2.0', 1, 1, S(0)), Add)
]),
    3: (3, Multiset({3: 1}), [
      (VariableWithCount('i3.1.2.0', 1, 1, S(0)), Add)
]),
    4: (4, Multiset({4: 1}), [
      (VariableWithCount('i3.1.2.0', 1, 1, S(0)), Add)
]),
    5: (5, Multiset({5: 1}), [
      (VariableWithCount('i3.1.2.0', 1, 1, S(0)), Add)
])
}
    subjects = {}
    subjects_by_id = {}
    bipartite = BipartiteGraph()
    associative = Add
    max_optional_count = 1
    anonymous_patterns = set()

    def __init__(self):
        self.add_subject(None)

    @staticmethod
    def get():
        if CommutativeMatcher122491._instance is None:
            CommutativeMatcher122491._instance = CommutativeMatcher122491()
        return CommutativeMatcher122491._instance

    @staticmethod
    def get_match_iter(subject):
        subjects = deque([subject]) if subject is not None else deque()
        subst0 = Substitution()
        # State 122490
        subst1 = Substitution(subst0)
        try:
            subst1.try_add_variable('i3.1.2.1.0', S(1))
        except ValueError:
            pass
        else:
            pass
            # State 122492
            if len(subjects) >= 1 and isinstance(subjects[0], Pow):
                tmp2 = subjects.popleft()
                subjects3 = deque(tmp2._args)
                # State 122493
                if len(subjects3) >= 1:
                    tmp4 = subjects3.popleft()
                    subst2 = Substitution(subst1)
                    try:
                        subst2.try_add_variable('i3.1.2.1.1', tmp4)
                    except ValueError:
                        pass
                    else:
                        pass
                        # State 122494
                        if len(subjects3) >= 1:
                            tmp6 = subjects3.popleft()
                            subst3 = Substitution(subst2)
                            try:
                                subst3.try_add_variable('i3.1.2.1.2', tmp6)
                            except ValueError:
                                pass
                            else:
                                pass
                                # State 122495
                                if len(subjects3) == 0:
                                    pass
                                    # State 122496
                                    if len(subjects) == 0:
                                        pass
                                        # 0: d*x**n /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f378) and (cons_f167)
                                        yield 0, subst3
                                        # 1: d*x**n /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f198)
                                        yield 1, subst3
                                        # 2: d*x**n /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f491)
                                        yield 2, subst3
                                        # 3: d*x**n /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f4)
                                        yield 3, subst3
                                        # 4: d*x**n /; (cons_f29) and (cons_f4) and (cons_f70) and (cons_f71)
                                        yield 4, subst3
                                        # 5: d*x**n /; (cons_f29) and (cons_f4) and (cons_f70)
                                        yield 5, subst3
                            subjects3.appendleft(tmp6)
                    subjects3.appendleft(tmp4)
                subjects.appendleft(tmp2)
        if len(subjects) >= 1 and isinstance(subjects[0], Mul):
            tmp8 = subjects.popleft()
            associative1 = tmp8
            associative_type1 = type(tmp8)
            subjects9 = deque(tmp8._args)
            matcher = CommutativeMatcher122498.get()
            tmp10 = subjects9
            subjects9 = []
            for s in tmp10:
                matcher.add_subject(s)
            for pattern_index, subst1 in matcher.match(tmp10, subst0):
                pass
                if pattern_index == 0:
                    pass
                    # State 122503
                    if len(subjects) == 0:
                        pass
                        # 0: d*x**n /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f378) and (cons_f167)
                        yield 0, subst1
                        # 1: d*x**n /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f198)
                        yield 1, subst1
                        # 2: d*x**n /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f491)
                        yield 2, subst1
                        # 3: d*x**n /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f4)
                        yield 3, subst1
                        # 4: d*x**n /; (cons_f29) and (cons_f4) and (cons_f70) and (cons_f71)
                        yield 4, subst1
                        # 5: d*x**n /; (cons_f29) and (cons_f4) and (cons_f70)
                        yield 5, subst1
            subjects.appendleft(tmp8)
        return
        yield


from matchpy.matching.many_to_one import CommutativeMatcher
from collections import deque
from .generated_part009180 import *
from matchpy.utils import VariableWithCount
from multiset import Multiset