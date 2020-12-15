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


class CommutativeMatcher2732(CommutativeMatcher):
    _instance = None
    patterns = {
    0: (0, Multiset({}), [
      (VariableWithCount('i2.2.1.0', 1, 1, None), Mul),
      (VariableWithCount('i2.2.1.0_2', 1, 1, S(1)), Mul)
]),
    1: (1, Multiset({0: 1}), [
      (VariableWithCount('i2.2.1.0_1', 1, 1, S(1)), Mul)
]),
    2: (2, Multiset({1: 1}), [
      (VariableWithCount('i2.2.1.0_1', 1, 1, S(1)), Mul)
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
        if CommutativeMatcher2732._instance is None:
            CommutativeMatcher2732._instance = CommutativeMatcher2732()
        return CommutativeMatcher2732._instance

    @staticmethod
    def get_match_iter(subject):
        subjects = deque([subject]) if subject is not None else deque()
        subst0 = Substitution()
        # State 2731
        subst1 = Substitution(subst0)
        try:
            subst1.try_add_variable('i2.2.1.2_1', S(1))
        except ValueError:
            pass
        else:
            pass
            # State 2804
            if len(subjects) >= 1:
                tmp2 = subjects.popleft()
                subst2 = Substitution(subst1)
                try:
                    subst2.try_add_variable('i2.2.1.1', tmp2)
                except ValueError:
                    pass
                else:
                    pass
                    if 'i2.2.0' not in subst2 or 'i2.2.1.1' not in subst2 or cons_f2(a=subst2["i2.2.0"], x=subst2["i2.2.1.1"]):
                        pass
                        if 'i2.2.1.0' not in subst2 or 'i2.2.1.1' not in subst2 or cons_f3(b=subst2["i2.2.1.0"], x=subst2["i2.2.1.1"]):
                            pass
                            if 'i2.2.0_1' not in subst2 or 'i2.2.1.1' not in subst2 or cons_f8(c=subst2["i2.2.0_1"], x=subst2["i2.2.1.1"]):
                                pass
                                if 'i2.2.1.0_1' not in subst2 or 'i2.2.1.1' not in subst2 or cons_f29(d=subst2["i2.2.1.0_1"], x=subst2["i2.2.1.1"]):
                                    pass
                                    if 'i2.2' not in subst2 or 'i2.2.1.1' not in subst2 or cons_f19(m=subst2["i2.2"], x=subst2["i2.2.1.1"]):
                                        pass
                                        if 'i2.2.1.2' not in subst2 or 'i2.2.1.1' not in subst2 or cons_f4(n=subst2["i2.2.1.2"], x=subst2["i2.2.1.1"]):
                                            pass
                                            # State 2805
                                            if len(subjects) == 0:
                                                pass
                                                # 0: v**n /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f19) and (cons_f4) and (cons_f39)
                                                yield 0, subst2
                    if 'i2.2.0_1' not in subst2 or 'i2.2.1.1' not in subst2 or cons_f2(a=subst2["i2.2.0_1"], x=subst2["i2.2.1.1"]):
                        pass
                        if 'i2.2.1.0_1' not in subst2 or 'i2.2.1.1' not in subst2 or cons_f3(b=subst2["i2.2.1.0_1"], x=subst2["i2.2.1.1"]):
                            pass
                            if 'i2.2.0' not in subst2 or 'i2.2.1.1' not in subst2 or cons_f8(c=subst2["i2.2.0"], x=subst2["i2.2.1.1"]):
                                pass
                                if 'i2.2.1.0' not in subst2 or 'i2.2.1.1' not in subst2 or cons_f29(d=subst2["i2.2.1.0"], x=subst2["i2.2.1.1"]):
                                    pass
                                    if 'i2.2_1' not in subst2 or 'i2.2.1.1' not in subst2 or cons_f19(m=subst2["i2.2_1"], x=subst2["i2.2.1.1"]):
                                        pass
                                        if 'i2.2.1.2_1' not in subst2 or 'i2.2.1.1' not in subst2 or cons_f4(n=subst2["i2.2.1.2_1"], x=subst2["i2.2.1.1"]):
                                            pass
                                            if 'i2.2' not in subst2 or 'i2.2.1.1' not in subst2 or cons_f5(p=subst2["i2.2"], x=subst2["i2.2.1.1"]):
                                                pass
                                                # State 2805
                                                if len(subjects) == 0:
                                                    pass
                                                    # 1: v**n /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f19) and (cons_f4) and (cons_f5) and (cons_f7)
                                                    yield 1, subst2
                subjects.appendleft(tmp2)
        if len(subjects) >= 1 and isinstance(subjects[0], Pow):
            tmp4 = subjects.popleft()
            subjects5 = deque(tmp4._args)
            # State 2806
            if len(subjects5) >= 1:
                tmp6 = subjects5.popleft()
                subst1 = Substitution(subst0)
                try:
                    subst1.try_add_variable('i2.2.1.1', tmp6)
                except ValueError:
                    pass
                else:
                    pass
                    if 'i2.2.0' not in subst1 or 'i2.2.1.1' not in subst1 or cons_f2(a=subst1["i2.2.0"], x=subst1["i2.2.1.1"]):
                        pass
                        if 'i2.2.1.0' not in subst1 or 'i2.2.1.1' not in subst1 or cons_f3(b=subst1["i2.2.1.0"], x=subst1["i2.2.1.1"]):
                            pass
                            if 'i2.2.0_1' not in subst1 or 'i2.2.1.1' not in subst1 or cons_f8(c=subst1["i2.2.0_1"], x=subst1["i2.2.1.1"]):
                                pass
                                if 'i2.2.1.0_1' not in subst1 or 'i2.2.1.1' not in subst1 or cons_f29(d=subst1["i2.2.1.0_1"], x=subst1["i2.2.1.1"]):
                                    pass
                                    if 'i2.2' not in subst1 or 'i2.2.1.1' not in subst1 or cons_f19(m=subst1["i2.2"], x=subst1["i2.2.1.1"]):
                                        pass
                                        if 'i2.2.1.2' not in subst1 or 'i2.2.1.1' not in subst1 or cons_f4(n=subst1["i2.2.1.2"], x=subst1["i2.2.1.1"]):
                                            pass
                                            # State 2807
                                            subst2 = Substitution(subst1)
                                            try:
                                                subst2.try_add_variable('i2.2.1.2_1', 1)
                                            except ValueError:
                                                pass
                                            else:
                                                pass
                                                if 'i2.2.1.2' not in subst2 or 'i2.2.1.2_1' not in subst2 or cons_f39(n=subst2["i2.2.1.2"], q=subst2["i2.2.1.2_1"]):
                                                    pass
                                                    # State 2808
                                                    if len(subjects5) == 0:
                                                        pass
                                                        # State 2809
                                                        if len(subjects) == 0:
                                                            pass
                                                            # 0: v**n /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f19) and (cons_f4) and (cons_f39)
                                                            yield 0, subst2
                                            if len(subjects5) >= 1:
                                                tmp9 = subjects5.popleft()
                                                subst2 = Substitution(subst1)
                                                try:
                                                    subst2.try_add_variable('i2.2.1.2_1', tmp9)
                                                except ValueError:
                                                    pass
                                                else:
                                                    pass
                                                    if 'i2.2.1.2' not in subst2 or 'i2.2.1.2_1' not in subst2 or cons_f39(n=subst2["i2.2.1.2"], q=subst2["i2.2.1.2_1"]):
                                                        pass
                                                        # State 2808
                                                        if len(subjects5) == 0:
                                                            pass
                                                            # State 2809
                                                            if len(subjects) == 0:
                                                                pass
                                                                # 0: v**n /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f19) and (cons_f4) and (cons_f39)
                                                                yield 0, subst2
                                                subjects5.appendleft(tmp9)
                    if 'i2.2.0_1' not in subst1 or 'i2.2.1.1' not in subst1 or cons_f2(a=subst1["i2.2.0_1"], x=subst1["i2.2.1.1"]):
                        pass
                        if 'i2.2.1.0_1' not in subst1 or 'i2.2.1.1' not in subst1 or cons_f3(b=subst1["i2.2.1.0_1"], x=subst1["i2.2.1.1"]):
                            pass
                            if 'i2.2.0' not in subst1 or 'i2.2.1.1' not in subst1 or cons_f8(c=subst1["i2.2.0"], x=subst1["i2.2.1.1"]):
                                pass
                                if 'i2.2.1.0' not in subst1 or 'i2.2.1.1' not in subst1 or cons_f29(d=subst1["i2.2.1.0"], x=subst1["i2.2.1.1"]):
                                    pass
                                    if 'i2.2_1' not in subst1 or 'i2.2.1.1' not in subst1 or cons_f19(m=subst1["i2.2_1"], x=subst1["i2.2.1.1"]):
                                        pass
                                        if 'i2.2.1.2_1' not in subst1 or 'i2.2.1.1' not in subst1 or cons_f4(n=subst1["i2.2.1.2_1"], x=subst1["i2.2.1.1"]):
                                            pass
                                            if 'i2.2' not in subst1 or 'i2.2.1.1' not in subst1 or cons_f5(p=subst1["i2.2"], x=subst1["i2.2.1.1"]):
                                                pass
                                                # State 2807
                                                subst2 = Substitution(subst1)
                                                try:
                                                    subst2.try_add_variable('i2.2.1.2_1', 1)
                                                except ValueError:
                                                    pass
                                                else:
                                                    pass
                                                    if 'i2.2.1.2_1' not in subst2 or 'i2.2.1.1' not in subst2 or cons_f4(n=subst2["i2.2.1.2_1"], x=subst2["i2.2.1.1"]):
                                                        pass
                                                        if 'i2.2.1.2' not in subst2 or 'i2.2.1.2_1' not in subst2 or cons_f7(j=subst2["i2.2.1.2"], n=subst2["i2.2.1.2_1"]):
                                                            pass
                                                            # State 2808
                                                            if len(subjects5) == 0:
                                                                pass
                                                                # State 2809
                                                                if len(subjects) == 0:
                                                                    pass
                                                                    # 1: v**n /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f19) and (cons_f4) and (cons_f5) and (cons_f7)
                                                                    yield 1, subst2
                                                if len(subjects5) >= 1:
                                                    tmp12 = subjects5.popleft()
                                                    subst2 = Substitution(subst1)
                                                    try:
                                                        subst2.try_add_variable('i2.2.1.2_1', tmp12)
                                                    except ValueError:
                                                        pass
                                                    else:
                                                        pass
                                                        if 'i2.2.1.2_1' not in subst2 or 'i2.2.1.1' not in subst2 or cons_f4(n=subst2["i2.2.1.2_1"], x=subst2["i2.2.1.1"]):
                                                            pass
                                                            if 'i2.2.1.2' not in subst2 or 'i2.2.1.2_1' not in subst2 or cons_f7(j=subst2["i2.2.1.2"], n=subst2["i2.2.1.2_1"]):
                                                                pass
                                                                # State 2808
                                                                if len(subjects5) == 0:
                                                                    pass
                                                                    # State 2809
                                                                    if len(subjects) == 0:
                                                                        pass
                                                                        # 1: v**n /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f19) and (cons_f4) and (cons_f5) and (cons_f7)
                                                                        yield 1, subst2
                                                    subjects5.appendleft(tmp12)
                subjects5.appendleft(tmp6)
            subjects.appendleft(tmp4)
        return
        yield


from collections import deque