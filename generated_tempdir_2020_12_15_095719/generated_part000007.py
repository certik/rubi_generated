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


class CommutativeMatcher2351(CommutativeMatcher):
    _instance = None
    patterns = {
    0: (0, Multiset({0: 1}), [
      (VariableWithCount('i2.0', 1, 1, S(1)), Mul)
]),
    1: (1, Multiset({1: 1}), [
      (VariableWithCount('i2.0', 1, 1, S(1)), Mul)
]),
    2: (2, Multiset({2: 1}), [
      (VariableWithCount('i2.0', 1, 1, S(1)), Mul)
]),
    3: (3, Multiset({3: 1}), [
      (VariableWithCount('i2.0', 1, 1, S(1)), Mul)
]),
    4: (4, Multiset({4: 1}), [
      (VariableWithCount('i2.0', 1, 1, S(1)), Mul)
]),
    5: (5, Multiset({5: 1}), [
      (VariableWithCount('i2.0', 1, 1, S(1)), Mul)
]),
    6: (6, Multiset({6: 1}), [
      (VariableWithCount('i2.0', 1, 1, S(1)), Mul)
]),
    7: (7, Multiset({7: 1}), [
      (VariableWithCount('i2.0', 1, 1, None), Mul)
]),
    8: (8, Multiset({8: 1}), [
      (VariableWithCount('i2.0', 1, 1, None), Mul)
]),
    9: (9, Multiset({9: 1}), [
      (VariableWithCount('i2.0', 1, 1, None), Mul),
      (VariableWithCount('i2.0_1', 1, 1, None), Mul)
]),
    10: (10, Multiset({}), [
      (VariableWithCount('i2.0', 1, 1, None), Mul),
      (VariableWithCount('i2.0_1', 1, 1, None), Mul)
]),
    11: (11, Multiset({10: 1}), [
      (VariableWithCount('i2.0', 1, 1, None), Mul)
]),
    12: (12, Multiset({11: 1, 12: 1}), [
      (VariableWithCount('i2.0', 1, 1, S(1)), Mul)
]),
    13: (13, Multiset({13: 1, 14: 1}), [
      (VariableWithCount('i2.0', 1, 1, S(1)), Mul)
]),
    14: (14, Multiset({15: 1, 14: 1}), [
      (VariableWithCount('i2.0', 1, 1, S(1)), Mul)
]),
    15: (15, Multiset({16: 1, 14: 1}), [
      (VariableWithCount('i2.0', 1, 1, S(1)), Mul)
]),
    16: (16, Multiset({17: 1, 18: 1}), [
      (VariableWithCount('i2.0', 1, 1, S(1)), Mul)
]),
    17: (17, Multiset({19: 1, 20: 1}), [
      (VariableWithCount('i2.0', 1, 1, S(1)), Mul)
]),
    18: (18, Multiset({21: 1, 22: 1}), [
      (VariableWithCount('i2.0', 1, 1, S(1)), Mul)
]),
    19: (19, Multiset({23: 1, 24: 1}), [
      (VariableWithCount('i2.0', 1, 1, S(1)), Mul)
]),
    20: (20, Multiset({25: 1, 26: 1}), [
      (VariableWithCount('i2.0', 1, 1, S(1)), Mul)
]),
    21: (21, Multiset({27: 1, 28: 1}), [
      (VariableWithCount('i2.0', 1, 1, S(1)), Mul)
]),
    22: (22, Multiset({29: 1, 30: 1}), [
      (VariableWithCount('i2.0', 1, 1, S(1)), Mul)
]),
    23: (23, Multiset({31: 1, 32: 1}), [
      (VariableWithCount('i2.0', 1, 1, S(1)), Mul)
]),
    24: (24, Multiset({33: 1}), [
      (VariableWithCount('i2.0', 1, 1, S(1)), Mul)
]),
    25: (25, Multiset({34: 1}), [
      (VariableWithCount('i2.0', 1, 1, S(1)), Mul)
]),
    26: (26, Multiset({35: 1, 36: 1}), [
      
]),
    27: (27, Multiset({37: 1}), [
      (VariableWithCount('i2.0', 1, 1, S(1)), Mul)
]),
    28: (28, Multiset({38: 1}), [
      (VariableWithCount('i2.0', 1, 1, S(1)), Mul)
]),
    29: (29, Multiset({39: 1, 40: 1}), [
      
]),
    30: (30, Multiset({41: 1, 42: 1}), [
      
]),
    31: (31, Multiset({43: 1, 44: 1, 45: 1}), [
      
]),
    32: (32, Multiset({46: 1}), [
      (VariableWithCount('i2.0', 1, 1, None), Mul)
]),
    33: (33, Multiset({47: 1}), [
      (VariableWithCount('i2.0', 1, 1, None), Mul)
]),
    34: (34, Multiset({48: 1, 49: 1}), [
      (VariableWithCount('i2.0', 1, 1, S(1)), Mul)
]),
    35: (35, Multiset({50: 1}), [
      (VariableWithCount('i2.0', 1, 1, None), Mul),
      (VariableWithCount('i2.0_1', 1, 1, S(1)), Mul)
])
}
    subjects = {}
    subjects_by_id = {}
    bipartite = BipartiteGraph()
    associative = Mul
    max_optional_count = 1
    anonymous_patterns = {8, 9}

    def __init__(self):
        self.add_subject(None)

    @staticmethod
    def get():
        if CommutativeMatcher2351._instance is None:
            CommutativeMatcher2351._instance = CommutativeMatcher2351()
        return CommutativeMatcher2351._instance

    @staticmethod
    def get_match_iter(subject):
        subjects = deque([subject]) if subject is not None else deque()
        subst0 = Substitution()
        # State 2350
        subst1 = Substitution(subst0)
        try:
            subst1.try_add_variable('i2.2', S(1))
        except ValueError:
            pass
        else:
            pass
            # State 2352
            if len(subjects) >= 1 and isinstance(subjects[0], Add):
                tmp2 = subjects.popleft()
                associative1 = tmp2
                associative_type1 = type(tmp2)
                subjects3 = deque(tmp2._args)
                matcher = CommutativeMatcher2354.get()
                tmp4 = subjects3
                subjects3 = []
                for s in tmp4:
                    matcher.add_subject(s)
                for pattern_index, subst2 in matcher.match(tmp4, subst1):
                    pass
                    if pattern_index == 0:
                        pass
                        if 'i2.2.0' not in subst2 or 'i2.2.1.1' not in subst2 or cons_f2(a=subst2["i2.2.0"], x=subst2["i2.2.1.1"]):
                            pass
                            if 'i2.2.1.0' not in subst2 or 'i2.2.1.1' not in subst2 or cons_f3(b=subst2["i2.2.1.0"], x=subst2["i2.2.1.1"]):
                                pass
                                if 'i2.2.1.2' not in subst2 or 'i2.2.1.1' not in subst2 or cons_f4(n=subst2["i2.2.1.2"], x=subst2["i2.2.1.1"]):
                                    pass
                                    if 'i2.2' not in subst2 or 'i2.2.1.1' not in subst2 or cons_f5(p=subst2["i2.2"], x=subst2["i2.2.1.1"]):
                                        pass
                                        if 'i2.2.0' not in subst2 or cons_f1(a=subst2["i2.2.0"]):
                                            pass
                                            # State 2371
                                            if len(subjects) == 0:
                                                pass
                                                # 0: (a + a*v**m)**p /; (cons_f2) and (cons_f3) and (cons_f4) and (cons_f5) and (cons_f1)
                                                yield 0, subst2
                    if pattern_index == 1:
                        pass
                        if 'i2.2.0' not in subst2 or 'i2.2.1.1' not in subst2 or cons_f2(a=subst2["i2.2.0"], x=subst2["i2.2.1.1"]):
                            pass
                            if 'i2.2.1.0' not in subst2 or 'i2.2.1.1' not in subst2 or cons_f3(b=subst2["i2.2.1.0"], x=subst2["i2.2.1.1"]):
                                pass
                                if 'i2.2.1.2' not in subst2 or 'i2.2.1.1' not in subst2 or cons_f4(n=subst2["i2.2.1.2"], x=subst2["i2.2.1.1"]):
                                    pass
                                    if 'i2.2' not in subst2 or 'i2.2.1.1' not in subst2 or cons_f5(p=subst2["i2.2"], x=subst2["i2.2.1.1"]):
                                        pass
                                        if 'i2.2.1.0' not in subst2 or cons_f6(b=subst2["i2.2.1.0"]):
                                            pass
                                            # State 2474
                                            if len(subjects) == 0:
                                                pass
                                                # 1: (a + a*v**m)**p /; (cons_f2) and (cons_f3) and (cons_f4) and (cons_f5) and (cons_f6)
                                                yield 1, subst2
                    if pattern_index == 2:
                        pass
                        if 'i2.2.0' not in subst2 or 'i2.2.1.1' not in subst2 or cons_f2(a=subst2["i2.2.0"], x=subst2["i2.2.1.1"]):
                            pass
                            if 'i2.2' not in subst2 or 'i2.2.1.1' not in subst2 or cons_f5(p=subst2["i2.2"], x=subst2["i2.2.1.1"]):
                                pass
                                if 'i2.2.0' not in subst2 or cons_f1(a=subst2["i2.2.0"]):
                                    pass
                                    if 'i2.2.1.0_1' not in subst2 or 'i2.2.1.1' not in subst2 or cons_f3(b=subst2["i2.2.1.0_1"], x=subst2["i2.2.1.1"]):
                                        pass
                                        if 'i2.2.1.0' not in subst2 or 'i2.2.1.1' not in subst2 or cons_f8(c=subst2["i2.2.1.0"], x=subst2["i2.2.1.1"]):
                                            pass
                                            if 'i2.2.1.2_1' not in subst2 or 'i2.2.1.1' not in subst2 or cons_f4(n=subst2["i2.2.1.2_1"], x=subst2["i2.2.1.1"]):
                                                pass
                                                if 'i2.2.1.2' not in subst2 or 'i2.2.1.2_1' not in subst2 or cons_f7(j=subst2["i2.2.1.2"], n=subst2["i2.2.1.2_1"]):
                                                    pass
                                                    # State 2551
                                                    if len(subjects) == 0:
                                                        pass
                                                        # 2: (a + b*v**n + a*v**m)**p /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f4) and (cons_f5) and (cons_f7) and (cons_f1)
                                                        yield 2, subst2
                    if pattern_index == 3:
                        pass
                        if 'i2.2.0' not in subst2 or 'i2.2.1.1' not in subst2 or cons_f2(a=subst2["i2.2.0"], x=subst2["i2.2.1.1"]):
                            pass
                            if 'i2.2' not in subst2 or 'i2.2.1.1' not in subst2 or cons_f5(p=subst2["i2.2"], x=subst2["i2.2.1.1"]):
                                pass
                                if 'i2.2.1.0_1' not in subst2 or 'i2.2.1.1' not in subst2 or cons_f3(b=subst2["i2.2.1.0_1"], x=subst2["i2.2.1.1"]):
                                    pass
                                    if 'i2.2.1.0' not in subst2 or 'i2.2.1.1' not in subst2 or cons_f8(c=subst2["i2.2.1.0"], x=subst2["i2.2.1.1"]):
                                        pass
                                        if 'i2.2.1.2_1' not in subst2 or 'i2.2.1.1' not in subst2 or cons_f4(n=subst2["i2.2.1.2_1"], x=subst2["i2.2.1.1"]):
                                            pass
                                            if 'i2.2.1.2' not in subst2 or 'i2.2.1.2_1' not in subst2 or cons_f7(j=subst2["i2.2.1.2"], n=subst2["i2.2.1.2_1"]):
                                                pass
                                                if 'i2.2.1.0_1' not in subst2 or cons_f6(b=subst2["i2.2.1.0_1"]):
                                                    pass
                                                    # State 2579
                                                    if len(subjects) == 0:
                                                        pass
                                                        # 3: (a + b*v**n + a*v**m)**p /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f4) and (cons_f5) and (cons_f7) and (cons_f6)
                                                        yield 3, subst2
                    if pattern_index == 4:
                        pass
                        if 'i2.2.0' not in subst2 or 'i2.2.1.1' not in subst2 or cons_f2(a=subst2["i2.2.0"], x=subst2["i2.2.1.1"]):
                            pass
                            if 'i2.2' not in subst2 or 'i2.2.1.1' not in subst2 or cons_f5(p=subst2["i2.2"], x=subst2["i2.2.1.1"]):
                                pass
                                if 'i2.2.1.0_1' not in subst2 or 'i2.2.1.1' not in subst2 or cons_f3(b=subst2["i2.2.1.0_1"], x=subst2["i2.2.1.1"]):
                                    pass
                                    if 'i2.2.1.0' not in subst2 or 'i2.2.1.1' not in subst2 or cons_f8(c=subst2["i2.2.1.0"], x=subst2["i2.2.1.1"]):
                                        pass
                                        if 'i2.2.1.2_1' not in subst2 or 'i2.2.1.1' not in subst2 or cons_f4(n=subst2["i2.2.1.2_1"], x=subst2["i2.2.1.1"]):
                                            pass
                                            if 'i2.2.1.2' not in subst2 or 'i2.2.1.2_1' not in subst2 or cons_f7(j=subst2["i2.2.1.2"], n=subst2["i2.2.1.2_1"]):
                                                pass
                                                if 'i2.2.1.0' not in subst2 or cons_f9(c=subst2["i2.2.1.0"]):
                                                    pass
                                                    # State 2594
                                                    if len(subjects) == 0:
                                                        pass
                                                        # 4: (a + b*v**n + a*v**m)**p /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f4) and (cons_f5) and (cons_f7) and (cons_f9)
                                                        yield 4, subst2
                    if pattern_index == 5:
                        pass
                        if 'i2' not in subst2 or 'i2.2.1.0_1' not in subst2 or cons_f2(a=subst2["i2.2.1.0_1"], x=subst2["i2"]):
                            pass
                            if 'i2.2.1.0_2' not in subst2 or 'i2' not in subst2 or cons_f3(b=subst2["i2.2.1.0_2"], x=subst2["i2"]):
                                pass
                                if 'i2' not in subst2 or 'i2.2.1.0' not in subst2 or cons_f10(v=subst2["i2.2.1.0"], x=subst2["i2"]):
                                    pass
                                    # State 2624
                                    if len(subjects) == 0:
                                        pass
                                        # 5: (w + v*a + v*b)**p /; (cons_f2) and (cons_f3) and (cons_f10)
                                        yield 5, subst2
                    if pattern_index == 6:
                        pass
                        if 'i2' not in subst2 or 'i2.2.0' not in subst2 or cons_f2(a=subst2["i2.2.0"], x=subst2["i2"]):
                            pass
                            if 'i2' not in subst2 or 'i2.2.1.0_1' not in subst2 or cons_f3(b=subst2["i2.2.1.0_1"], x=subst2["i2"]):
                                pass
                                if 'i2.2.1.0_2' not in subst2 or 'i2.2.1.0_1' not in subst2 or 'i2.2.0' not in subst2 or 'i2.2.0_1' not in subst2 or cons_f27(a=subst2["i2.2.0"], b=subst2["i2.2.1.0_1"], c=subst2["i2.2.0_1"], d=subst2["i2.2.1.0_2"]):
                                    pass
                                    if 'i2' not in subst2 or 'i2.2.1.0_2' not in subst2 or 'i2.2.0_1' not in subst2 or 'i2.2.0' not in subst2 or 'i2.2_1' not in subst2 or 'i2.2.1.0_1' not in subst2 or cons_f28(a=subst2["i2.2.0"], b=subst2["i2.2.1.0_1"], c=subst2["i2.2.0_1"], d=subst2["i2.2.1.0_2"], n=subst2["i2.2_1"], x=subst2["i2"]):
                                        pass
                                        # State 2723
                                        if len(subjects) == 0:
                                            pass
                                            # 19: (a + v*a)**m /; (cons_f2) and (cons_f3) and (cons_f27) and (cons_f20) and (cons_f28)
                                            yield 19, subst2
                    if pattern_index == 7:
                        pass
                        if 'i2.2.0' not in subst2 or 'i2.2.1.1' not in subst2 or cons_f2(a=subst2["i2.2.0"], x=subst2["i2.2.1.1"]):
                            pass
                            if 'i2.2.1.0' not in subst2 or 'i2.2.1.1' not in subst2 or cons_f3(b=subst2["i2.2.1.0"], x=subst2["i2.2.1.1"]):
                                pass
                                if 'i2.2.1.2' not in subst2 or 'i2.2.1.1' not in subst2 or cons_f4(n=subst2["i2.2.1.2"], x=subst2["i2.2.1.1"]):
                                    pass
                                    if 'i2.2.0_1' not in subst2 or 'i2.2.1.1' not in subst2 or cons_f8(c=subst2["i2.2.0_1"], x=subst2["i2.2.1.1"]):
                                        pass
                                        if 'i2.2.1.0_1' not in subst2 or 'i2.2.1.1' not in subst2 or cons_f29(d=subst2["i2.2.1.0_1"], x=subst2["i2.2.1.1"]):
                                            pass
                                            if 'i2.2' not in subst2 or 'i2.2.1.1' not in subst2 or cons_f19(m=subst2["i2.2"], x=subst2["i2.2.1.1"]):
                                                pass
                                                if 'i2.2.1.2' not in subst2 or 'i2.2.1.2_1' not in subst2 or cons_f39(n=subst2["i2.2.1.2"], q=subst2["i2.2.1.2_1"]):
                                                    pass
                                                    if 'i2.2.1.0_1' not in subst2 or 'i2.2.1.0' not in subst2 or 'i2.2.0' not in subst2 or 'i2.2.0_1' not in subst2 or cons_f41(a=subst2["i2.2.0"], b=subst2["i2.2.1.0"], c=subst2["i2.2.0_1"], d=subst2["i2.2.1.0_1"]):
                                                        pass
                                                        if 'i2.2.1.2' not in subst2 or 'i2.2' not in subst2 or cons_f42(m=subst2["i2.2"], n=subst2["i2.2.1.2"]):
                                                            pass
                                                            # State 2792
                                                            if len(subjects) == 0:
                                                                pass
                                                                # 29: (a + a*v**m)**p /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f19) and (cons_f4) and (cons_f39) and (cons_f41) and (cons_f42)
                                                                yield 29, subst2
                    if pattern_index == 8:
                        pass
                        if 'i2.2' not in subst2 or 'i2.2.1.1' not in subst2 or cons_f5(p=subst2["i2.2"], x=subst2["i2.2.1.1"]):
                            pass
                            if 'i2.2.1.0_1' not in subst2 or 'i2.2.1.1' not in subst2 or cons_f3(b=subst2["i2.2.1.0_1"], x=subst2["i2.2.1.1"]):
                                pass
                                if 'i2.2.1.2_1' not in subst2 or 'i2.2.1.1' not in subst2 or cons_f4(n=subst2["i2.2.1.2_1"], x=subst2["i2.2.1.1"]):
                                    pass
                                    if 'i2.2.1.2' not in subst2 or 'i2.2.1.2_1' not in subst2 or cons_f7(j=subst2["i2.2.1.2"], n=subst2["i2.2.1.2_1"]):
                                        pass
                                        if 'i2.2.0_1' not in subst2 or 'i2.2.1.1' not in subst2 or cons_f2(a=subst2["i2.2.0_1"], x=subst2["i2.2.1.1"]):
                                            pass
                                            if 'i2.2.0' not in subst2 or 'i2.2.1.1' not in subst2 or cons_f8(c=subst2["i2.2.0"], x=subst2["i2.2.1.1"]):
                                                pass
                                                if 'i2.2.1.0' not in subst2 or 'i2.2.1.1' not in subst2 or cons_f29(d=subst2["i2.2.1.0"], x=subst2["i2.2.1.1"]):
                                                    pass
                                                    if 'i2.2_1' not in subst2 or 'i2.2.1.1' not in subst2 or cons_f19(m=subst2["i2.2_1"], x=subst2["i2.2.1.1"]):
                                                        pass
                                                        if 'i2.2.0' not in subst2 or 'i2.2.0_1' not in subst2 or 'i2.2.1.0_1' not in subst2 or 'i2.2.1.0' not in subst2 or cons_f44(a=subst2["i2.2.0_1"], b=subst2["i2.2.1.0_1"], c=subst2["i2.2.0"], d=subst2["i2.2.1.0"]):
                                                            pass
                                                            if 'i2.2.1.0' not in subst2 or cons_f46(d=subst2["i2.2.1.0"]):
                                                                pass
                                                                # State 2830
                                                                if len(subjects) == 0:
                                                                    pass
                                                                    # 32: (c + d*x**j)**p /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f19) and (cons_f4) and (cons_f5) and (cons_f7) and (cons_f43) and (cons_f44) and (cons_f46)
                                                                    yield 32, subst2
                    if pattern_index == 9:
                        pass
                        if 'i2.2.0' not in subst2 or 'i2.2.1.1' not in subst2 or cons_f2(a=subst2["i2.2.0"], x=subst2["i2.2.1.1"]):
                            pass
                            if 'i2.2.1.0_1' not in subst2 or 'i2.2.1.1' not in subst2 or cons_f3(b=subst2["i2.2.1.0_1"], x=subst2["i2.2.1.1"]):
                                pass
                                if 'i2.2.1.0' not in subst2 or 'i2.2.1.1' not in subst2 or cons_f8(c=subst2["i2.2.1.0"], x=subst2["i2.2.1.1"]):
                                    pass
                                    if 'i2.2.1.0' not in subst2 or 'i2.2.1.0_1' not in subst2 or 'i2.2.0' not in subst2 or cons_f47(a=subst2["i2.2.0"], b=subst2["i2.2.1.0_1"], c=subst2["i2.2.1.0"]):
                                        pass
                                        # State 2871
                                        if len(subjects) == 0:
                                            pass
                                            # 33: (a + b*x + c*x**2)**p /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f47) and (cons_f40)
                                            yield 33, subst2
                    if pattern_index == 10:
                        pass
                        if 'i2.2.0' not in subst2 or 'i2.2.1.1' not in subst2 or cons_f2(a=subst2["i2.2.0"], x=subst2["i2.2.1.1"]):
                            pass
                            if 'i2.2.1.0' not in subst2 or 'i2.2.1.1' not in subst2 or cons_f3(b=subst2["i2.2.1.0"], x=subst2["i2.2.1.1"]):
                                pass
                                if 'i2.2.1.2' not in subst2 or 'i2.2.1.1' not in subst2 or cons_f4(n=subst2["i2.2.1.2"], x=subst2["i2.2.1.1"]):
                                    pass
                                    if 'i2.2.1.0_1' not in subst2 or 'i2.2.1.1' not in subst2 or cons_f8(c=subst2["i2.2.1.0_1"], x=subst2["i2.2.1.1"]):
                                        pass
                                        if 'i2.2.1.2' not in subst2 or 'i2.2.1.2_1' not in subst2 or cons_f48(n=subst2["i2.2.1.2"], n2=subst2["i2.2.1.2_1"]):
                                            pass
                                            if 'i2.2.1.0_1' not in subst2 or 'i2.2.1.0' not in subst2 or 'i2.2.0' not in subst2 or cons_f47(a=subst2["i2.2.0"], b=subst2["i2.2.1.0"], c=subst2["i2.2.1.0_1"]):
                                                pass
                                                # State 2907
                                                if len(subjects) == 0:
                                                    pass
                                                    # 34: (a + b*v**n + d*x**j)**p /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f4) and (cons_f48) and (cons_f47) and (cons_f40)
                                                    yield 34, subst2
                    if pattern_index == 11:
                        pass
                        if 'i2.2.0' not in subst2 or 'i2.2.1.1' not in subst2 or cons_f2(a=subst2["i2.2.0"], x=subst2["i2.2.1.1"]):
                            pass
                            if 'i2.2' not in subst2 or 'i2.2.1.1' not in subst2 or cons_f5(p=subst2["i2.2"], x=subst2["i2.2.1.1"]):
                                pass
                                if 'i2.2.1.0_1' not in subst2 or 'i2.2.1.1' not in subst2 or cons_f3(b=subst2["i2.2.1.0_1"], x=subst2["i2.2.1.1"]):
                                    pass
                                    if 'i2.2.1.0' not in subst2 or 'i2.2.1.1' not in subst2 or cons_f8(c=subst2["i2.2.1.0"], x=subst2["i2.2.1.1"]):
                                        pass
                                        if 'i2.1.0' not in subst2 or 'i2.2.1.1' not in subst2 or cons_f29(d=subst2["i2.1.0"], x=subst2["i2.2.1.1"]):
                                            pass
                                            if 'i2.1.1.0' not in subst2 or 'i2.2.1.1' not in subst2 or cons_f50(e=subst2["i2.1.1.0"], x=subst2["i2.2.1.1"]):
                                                pass
                                                if 'i2.2.1.0' not in subst2 or 'i2.2.1.0_1' not in subst2 or 'i2.1.0' not in subst2 or 'i2.1.1.0' not in subst2 or cons_f49(b=subst2["i2.2.1.0_1"], c=subst2["i2.2.1.0"], d=subst2["i2.1.0"], e=subst2["i2.1.1.0"]):
                                                    pass
                                                    # State 2917
                                                    if len(subjects) == 0:
                                                        pass
                                                        # 35: (a + b*x + c*x**2)**p /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f50) and (cons_f5) and (cons_f49)
                                                        yield 35, subst2
                    if pattern_index == 12:
                        pass
                        if 'i2.2.1.0_1' not in subst2 or 'i2.2.1.1' not in subst2 or cons_f3(b=subst2["i2.2.1.0_1"], x=subst2["i2.2.1.1"]):
                            pass
                            if 'i2.2.1.0' not in subst2 or 'i2.2.1.1' not in subst2 or cons_f2(a=subst2["i2.2.1.0"], x=subst2["i2.2.1.1"]):
                                pass
                                if 'i2.2.1.2' not in subst2 or 'i2.2.1.1' not in subst2 or cons_f5(p=subst2["i2.2.1.2"], x=subst2["i2.2.1.1"]):
                                    pass
                                    if 'i2.2.1.2_1' not in subst2 or 'i2.2.1.1' not in subst2 or cons_f52(q=subst2["i2.2.1.2_1"], x=subst2["i2.2.1.1"]):
                                        pass
                                        if 'i2.2.1.2' not in subst2 or 'i2.2.1.2_1' not in subst2 or cons_f51(p=subst2["i2.2.1.2"], q=subst2["i2.2.1.2_1"]):
                                            pass
                                            # State 2942
                                            if len(subjects) == 0:
                                                pass
                                                # 37: (b*v**n + a*v**m)**m /; (cons_f2) and (cons_f3) and (cons_f5) and (cons_f52) and (cons_f20) and (cons_f51)
                                                yield 37, subst2
                    if pattern_index == 13:
                        pass
                        if 'i2.2.1.0_1' not in subst2 or 'i2.2.1.1' not in subst2 or cons_f3(b=subst2["i2.2.1.0_1"], x=subst2["i2.2.1.1"]):
                            pass
                            if 'i2.2.1.0' not in subst2 or 'i2.2.1.1' not in subst2 or cons_f2(a=subst2["i2.2.1.0"], x=subst2["i2.2.1.1"]):
                                pass
                                if 'i2.2.1.2' not in subst2 or 'i2.2.1.1' not in subst2 or cons_f5(p=subst2["i2.2.1.2"], x=subst2["i2.2.1.1"]):
                                    pass
                                    if 'i2.2.1.2_1' not in subst2 or 'i2.2.1.1' not in subst2 or cons_f52(q=subst2["i2.2.1.2_1"], x=subst2["i2.2.1.1"]):
                                        pass
                                        if 'i2.2.1.2' not in subst2 or 'i2.2.1.2_1' not in subst2 or cons_f51(p=subst2["i2.2.1.2"], q=subst2["i2.2.1.2_1"]):
                                            pass
                                            if 'i2.2.1.0_2' not in subst2 or 'i2.2.1.1' not in subst2 or cons_f8(c=subst2["i2.2.1.0_2"], x=subst2["i2.2.1.1"]):
                                                pass
                                                if 'i2.2.1.2_2' not in subst2 or 'i2.2.1.1' not in subst2 or cons_f54(r=subst2["i2.2.1.2_2"], x=subst2["i2.2.1.1"]):
                                                    pass
                                                    if 'i2.2.1.2' not in subst2 or 'i2.2.1.2_2' not in subst2 or cons_f53(p=subst2["i2.2.1.2"], r=subst2["i2.2.1.2_2"]):
                                                        pass
                                                        # State 2998
                                                        if len(subjects) == 0:
                                                            pass
                                                            # 38: (b*v**n + c*x**r + a*v**m)**m /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f5) and (cons_f52) and (cons_f54) and (cons_f20) and (cons_f51) and (cons_f53)
                                                            yield 38, subst2
                    if pattern_index == 14:
                        pass
                        if 'i2' not in subst2 or 'i2.2.0' not in subst2 or cons_f2(a=subst2["i2.2.0"], x=subst2["i2"]):
                            pass
                            if 'i2' not in subst2 or 'i2.2.1.0' not in subst2 or cons_f3(b=subst2["i2.2.1.0"], x=subst2["i2"]):
                                pass
                                if 'i2.2.1.2' not in subst2 or 'i2' not in subst2 or cons_f4(n=subst2["i2.2.1.2"], x=subst2["i2"]):
                                    pass
                                    if 'i2' not in subst2 or 'i2.2.1.1' not in subst2 or cons_f11(Pm=subst2["i2.2.1.1"], x=subst2["i2"]):
                                        pass
                                        if 'i2' not in subst2 or 'i2.2.1.1' not in subst2 or 'i2.2.1.0' not in subst2 or 'i2.2.0' not in subst2 or 'i2.0' not in subst2 or 'i2.2' not in subst2 or 'i2.2.1.2' not in subst2 or With35(Pm=subst2["i2.2.1.1"], Qm=subst2["i2.0"], a=subst2["i2.2.0"], b=subst2["i2.2.1.0"], n=subst2["i2.2.1.2"], p=subst2["i2.2"], x=subst2["i2"]):
                                            pass
                                            # State 3056
                                            if len(subjects) == 0:
                                                pass
                                                # 46: (a + a*v**m)**p /; (cons_f2) and (cons_f3) and (cons_f4) and (cons_f5) and (cons_f11) and (With35)
                                                yield 46, subst2
                    if pattern_index == 15:
                        pass
                        if 'i2' not in subst2 or 'i2.2.0' not in subst2 or cons_f2(a=subst2["i2.2.0"], x=subst2["i2"]):
                            pass
                            if 'i2.2.1.2' not in subst2 or 'i2.2.1.2_1' not in subst2 or cons_f48(n=subst2["i2.2.1.2"], n2=subst2["i2.2.1.2_1"]):
                                pass
                                if 'i2' not in subst2 or 'i2.2.1.0' not in subst2 or cons_f3(b=subst2["i2.2.1.0"], x=subst2["i2"]):
                                    pass
                                    if 'i2.2.1.2' not in subst2 or 'i2' not in subst2 or cons_f4(n=subst2["i2.2.1.2"], x=subst2["i2"]):
                                        pass
                                        if 'i2' not in subst2 or 'i2.2.1.1' not in subst2 or cons_f11(Pm=subst2["i2.2.1.1"], x=subst2["i2"]):
                                            pass
                                            if 'i2' not in subst2 or 'i2.2.1.0_1' not in subst2 or cons_f8(c=subst2["i2.2.1.0_1"], x=subst2["i2"]):
                                                pass
                                                if 'i2' not in subst2 or 'i2.2.1.1' not in subst2 or 'i2.2.1.0' not in subst2 or 'i2.2.0' not in subst2 or 'i2.0' not in subst2 or 'i2.2.1.2_1' not in subst2 or 'i2.2.1.2' not in subst2 or 'i2.2' not in subst2 or 'i2.2.1.0_1' not in subst2 or With36(Pm=subst2["i2.2.1.1"], Qm=subst2["i2.0"], a=subst2["i2.2.0"], b=subst2["i2.2.1.0"], c=subst2["i2.2.1.0_1"], n=subst2["i2.2.1.2"], n2=subst2["i2.2.1.2_1"], p=subst2["i2.2"], x=subst2["i2"]):
                                                    pass
                                                    # State 3069
                                                    if len(subjects) == 0:
                                                        pass
                                                        # 47: (a + b*v**n + a*v**m)**p /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f4) and (cons_f5) and (cons_f48) and (cons_f11) and (With36)
                                                        yield 47, subst2
                subjects.appendleft(tmp2)
            subst2 = Substitution(subst1)
            try:
                subst2.try_add_variable('i2.2.0', S(0))
            except ValueError:
                pass
            else:
                pass
                # State 2457
                subst3 = Substitution(subst2)
                try:
                    subst3.try_add_variable('i2.2.1.0', S(1))
                except ValueError:
                    pass
                else:
                    pass
                    # State 2458
                    subst4 = Substitution(subst3)
                    try:
                        subst4.try_add_variable('i2.2.1.2', S(1))
                    except ValueError:
                        pass
                    else:
                        pass
                        # State 2459
                        if len(subjects) >= 1:
                            tmp8 = subjects.popleft()
                            subst5 = Substitution(subst4)
                            try:
                                subst5.try_add_variable('i2.2.1.1', tmp8)
                            except ValueError:
                                pass
                            else:
                                pass
                                if 'i2.2.0' not in subst5 or 'i2.2.1.1' not in subst5 or cons_f2(a=subst5["i2.2.0"], x=subst5["i2.2.1.1"]):
                                    pass
                                    if 'i2.2.1.0' not in subst5 or 'i2.2.1.1' not in subst5 or cons_f3(b=subst5["i2.2.1.0"], x=subst5["i2.2.1.1"]):
                                        pass
                                        if 'i2.2.1.2' not in subst5 or 'i2.2.1.1' not in subst5 or cons_f4(n=subst5["i2.2.1.2"], x=subst5["i2.2.1.1"]):
                                            pass
                                            if 'i2.2' not in subst5 or 'i2.2.1.1' not in subst5 or cons_f5(p=subst5["i2.2"], x=subst5["i2.2.1.1"]):
                                                pass
                                                # State 2460
                                                if len(subjects) == 0:
                                                    pass
                                                    # 1: (a + a*v**m)**p /; (cons_f2) and (cons_f3) and (cons_f4) and (cons_f5) and (cons_f6)
                                                    yield 1, subst5
                                if 'i2' not in subst5 or 'i2.2.1.1' not in subst5 or cons_f11(Pm=subst5["i2.2.1.1"], x=subst5["i2"]):
                                    pass
                                    if 'i2' not in subst5 or 'i2.2.1.1' not in subst5 or 'i2.2.1.0' not in subst5 or 'i2.2.0' not in subst5 or 'i2.0' not in subst5 or 'i2.2' not in subst5 or 'i2.2.1.2' not in subst5 or With35(Pm=subst5["i2.2.1.1"], Qm=subst5["i2.0"], a=subst5["i2.2.0"], b=subst5["i2.2.1.0"], n=subst5["i2.2.1.2"], p=subst5["i2.2"], x=subst5["i2"]):
                                        pass
                                        # State 2460
                                        if len(subjects) == 0:
                                            pass
                                            # 46: (a + a*v**m)**p /; (cons_f2) and (cons_f3) and (cons_f4) and (cons_f5) and (cons_f11) and (With35)
                                            yield 46, subst5
                            subjects.appendleft(tmp8)
                    if len(subjects) >= 1 and isinstance(subjects[0], Pow):
                        tmp10 = subjects.popleft()
                        subjects11 = deque(tmp10._args)
                        # State 2461
                        if len(subjects11) >= 1:
                            tmp12 = subjects11.popleft()
                            subst4 = Substitution(subst3)
                            try:
                                subst4.try_add_variable('i2.2.1.1', tmp12)
                            except ValueError:
                                pass
                            else:
                                pass
                                if 'i2.2.0' not in subst4 or 'i2.2.1.1' not in subst4 or cons_f2(a=subst4["i2.2.0"], x=subst4["i2.2.1.1"]):
                                    pass
                                    if 'i2.2.1.0' not in subst4 or 'i2.2.1.1' not in subst4 or cons_f3(b=subst4["i2.2.1.0"], x=subst4["i2.2.1.1"]):
                                        pass
                                        if 'i2.2.1.2' not in subst4 or 'i2.2.1.1' not in subst4 or cons_f4(n=subst4["i2.2.1.2"], x=subst4["i2.2.1.1"]):
                                            pass
                                            if 'i2.2' not in subst4 or 'i2.2.1.1' not in subst4 or cons_f5(p=subst4["i2.2"], x=subst4["i2.2.1.1"]):
                                                pass
                                                # State 2462
                                                subst5 = Substitution(subst4)
                                                try:
                                                    subst5.try_add_variable('i2.2.1.2', 1)
                                                except ValueError:
                                                    pass
                                                else:
                                                    pass
                                                    if 'i2.2.1.2' not in subst5 or 'i2.2.1.1' not in subst5 or cons_f4(n=subst5["i2.2.1.2"], x=subst5["i2.2.1.1"]):
                                                        pass
                                                        # State 2463
                                                        if len(subjects11) == 0:
                                                            pass
                                                            # State 2464
                                                            if len(subjects) == 0:
                                                                pass
                                                                # 1: (a + a*v**m)**p /; (cons_f2) and (cons_f3) and (cons_f4) and (cons_f5) and (cons_f6)
                                                                yield 1, subst5
                                                if len(subjects11) >= 1:
                                                    tmp15 = subjects11.popleft()
                                                    subst5 = Substitution(subst4)
                                                    try:
                                                        subst5.try_add_variable('i2.2.1.2', tmp15)
                                                    except ValueError:
                                                        pass
                                                    else:
                                                        pass
                                                        if 'i2.2.1.2' not in subst5 or 'i2.2.1.1' not in subst5 or cons_f4(n=subst5["i2.2.1.2"], x=subst5["i2.2.1.1"]):
                                                            pass
                                                            # State 2463
                                                            if len(subjects11) == 0:
                                                                pass
                                                                # State 2464
                                                                if len(subjects) == 0:
                                                                    pass
                                                                    # 1: (a + a*v**m)**p /; (cons_f2) and (cons_f3) and (cons_f4) and (cons_f5) and (cons_f6)
                                                                    yield 1, subst5
                                                    subjects11.appendleft(tmp15)
                                if 'i2' not in subst4 or 'i2.2.1.1' not in subst4 or cons_f11(Pm=subst4["i2.2.1.1"], x=subst4["i2"]):
                                    pass
                                    if 'i2' not in subst4 or 'i2.2.1.1' not in subst4 or 'i2.2.1.0' not in subst4 or 'i2.2.0' not in subst4 or 'i2.0' not in subst4 or 'i2.2' not in subst4 or 'i2.2.1.2' not in subst4 or With35(Pm=subst4["i2.2.1.1"], Qm=subst4["i2.0"], a=subst4["i2.2.0"], b=subst4["i2.2.1.0"], n=subst4["i2.2.1.2"], p=subst4["i2.2"], x=subst4["i2"]):
                                        pass
                                        # State 2462
                                        subst5 = Substitution(subst4)
                                        try:
                                            subst5.try_add_variable('i2.2.1.2', 1)
                                        except ValueError:
                                            pass
                                        else:
                                            pass
                                            if 'i2.2.1.2' not in subst5 or 'i2' not in subst5 or cons_f4(n=subst5["i2.2.1.2"], x=subst5["i2"]):
                                                pass
                                                if 'i2' not in subst5 or 'i2.2.1.1' not in subst5 or 'i2.2.1.0' not in subst5 or 'i2.2.0' not in subst5 or 'i2.0' not in subst5 or 'i2.2' not in subst5 or 'i2.2.1.2' not in subst5 or With35(Pm=subst5["i2.2.1.1"], Qm=subst5["i2.0"], a=subst5["i2.2.0"], b=subst5["i2.2.1.0"], n=subst5["i2.2.1.2"], p=subst5["i2.2"], x=subst5["i2"]):
                                                    pass
                                                    # State 2463
                                                    if len(subjects11) == 0:
                                                        pass
                                                        # State 2464
                                                        if len(subjects) == 0:
                                                            pass
                                                            # 46: (a + a*v**m)**p /; (cons_f2) and (cons_f3) and (cons_f4) and (cons_f5) and (cons_f11) and (With35)
                                                            yield 46, subst5
                                        if len(subjects11) >= 1:
                                            tmp18 = subjects11.popleft()
                                            subst5 = Substitution(subst4)
                                            try:
                                                subst5.try_add_variable('i2.2.1.2', tmp18)
                                            except ValueError:
                                                pass
                                            else:
                                                pass
                                                if 'i2.2.1.2' not in subst5 or 'i2' not in subst5 or cons_f4(n=subst5["i2.2.1.2"], x=subst5["i2"]):
                                                    pass
                                                    if 'i2' not in subst5 or 'i2.2.1.1' not in subst5 or 'i2.2.1.0' not in subst5 or 'i2.2.0' not in subst5 or 'i2.0' not in subst5 or 'i2.2' not in subst5 or 'i2.2.1.2' not in subst5 or With35(Pm=subst5["i2.2.1.1"], Qm=subst5["i2.0"], a=subst5["i2.2.0"], b=subst5["i2.2.1.0"], n=subst5["i2.2.1.2"], p=subst5["i2.2"], x=subst5["i2"]):
                                                        pass
                                                        # State 2463
                                                        if len(subjects11) == 0:
                                                            pass
                                                            # State 2464
                                                            if len(subjects) == 0:
                                                                pass
                                                                # 46: (a + a*v**m)**p /; (cons_f2) and (cons_f3) and (cons_f4) and (cons_f5) and (cons_f11) and (With35)
                                                                yield 46, subst5
                                            subjects11.appendleft(tmp18)
                            subjects11.appendleft(tmp12)
                        subjects.appendleft(tmp10)
                if len(subjects) >= 1 and isinstance(subjects[0], Mul):
                    tmp20 = subjects.popleft()
                    associative1 = tmp20
                    associative_type1 = type(tmp20)
                    subjects21 = deque(tmp20._args)
                    matcher = CommutativeMatcher2466.get()
                    tmp22 = subjects21
                    subjects21 = []
                    for s in tmp22:
                        matcher.add_subject(s)
                    for pattern_index, subst3 in matcher.match(tmp22, subst2):
                        pass
                        if pattern_index == 0:
                            pass
                            if 'i2.2.0' not in subst3 or 'i2.2.1.1' not in subst3 or cons_f2(a=subst3["i2.2.0"], x=subst3["i2.2.1.1"]):
                                pass
                                if 'i2.2.1.0' not in subst3 or 'i2.2.1.1' not in subst3 or cons_f3(b=subst3["i2.2.1.0"], x=subst3["i2.2.1.1"]):
                                    pass
                                    if 'i2.2.1.2' not in subst3 or 'i2.2.1.1' not in subst3 or cons_f4(n=subst3["i2.2.1.2"], x=subst3["i2.2.1.1"]):
                                        pass
                                        if 'i2.2' not in subst3 or 'i2.2.1.1' not in subst3 or cons_f5(p=subst3["i2.2"], x=subst3["i2.2.1.1"]):
                                            pass
                                            if 'i2.2.1.0' not in subst3 or cons_f6(b=subst3["i2.2.1.0"]):
                                                pass
                                                # State 2473
                                                if len(subjects) == 0:
                                                    pass
                                                    # 1: (a + a*v**m)**p /; (cons_f2) and (cons_f3) and (cons_f4) and (cons_f5) and (cons_f6)
                                                    yield 1, subst3
                        if pattern_index == 1:
                            pass
                            if 'i2' not in subst3 or 'i2.2.1.0' not in subst3 or cons_f3(b=subst3["i2.2.1.0"], x=subst3["i2"]):
                                pass
                                if 'i2.2.1.2' not in subst3 or 'i2' not in subst3 or cons_f4(n=subst3["i2.2.1.2"], x=subst3["i2"]):
                                    pass
                                    if 'i2' not in subst3 or 'i2.2.1.1' not in subst3 or cons_f11(Pm=subst3["i2.2.1.1"], x=subst3["i2"]):
                                        pass
                                        if 'i2' not in subst3 or 'i2.2.1.1' not in subst3 or 'i2.2.1.0' not in subst3 or 'i2.2.0' not in subst3 or 'i2.0' not in subst3 or 'i2.2' not in subst3 or 'i2.2.1.2' not in subst3 or With35(Pm=subst3["i2.2.1.1"], Qm=subst3["i2.0"], a=subst3["i2.2.0"], b=subst3["i2.2.1.0"], n=subst3["i2.2.1.2"], p=subst3["i2.2"], x=subst3["i2"]):
                                            pass
                                            # State 3054
                                            if len(subjects) == 0:
                                                pass
                                                # 46: (a + a*v**m)**p /; (cons_f2) and (cons_f3) and (cons_f4) and (cons_f5) and (cons_f11) and (With35)
                                                yield 46, subst3
                    subjects.appendleft(tmp20)
            subst2 = Substitution(subst1)
            try:
                subst2.try_add_variable('i2.2.0_1', S(1))
            except ValueError:
                pass
            else:
                pass
                # State 2672
                if len(subjects) >= 1:
                    tmp24 = subjects.popleft()
                    subst3 = Substitution(subst2)
                    try:
                        subst3.try_add_variable('i2.2.0', tmp24)
                    except ValueError:
                        pass
                    else:
                        pass
                        if 'i2.2.0_1' not in subst3 or 'i2.2.0' not in subst3 or cons_f8(c=subst3["i2.2.0_1"], x=subst3["i2.2.0"]):
                            pass
                            if 'i2.2.0' not in subst3 or 'i2.2' not in subst3 or cons_f19(m=subst3["i2.2"], x=subst3["i2.2.0"]):
                                pass
                                if 'i2.2.0' not in subst3 or 'i2.0' not in subst3 or cons_f18(u=subst3["i2.0"], x=subst3["i2.2.0"]):
                                    pass
                                    # State 2673
                                    if len(subjects) == 0:
                                        pass
                                        # 10: (x*c)**m /; (cons_f8) and (cons_f19) and (cons_f18)
                                        yield 10, subst3
                    subjects.appendleft(tmp24)
            if len(subjects) >= 1:
                tmp26 = subjects.popleft()
                subst2 = Substitution(subst1)
                try:
                    subst2.try_add_variable('i2.2.1.1', tmp26)
                except ValueError:
                    pass
                else:
                    pass
                    if 'i2.2.0' not in subst2 or 'i2.2.1.1' not in subst2 or cons_f2(a=subst2["i2.2.0"], x=subst2["i2.2.1.1"]):
                        pass
                        if 'i2.2.1.0' not in subst2 or 'i2.2.1.1' not in subst2 or cons_f3(b=subst2["i2.2.1.0"], x=subst2["i2.2.1.1"]):
                            pass
                            if 'i2.2.1.2' not in subst2 or 'i2.2.1.1' not in subst2 or cons_f4(n=subst2["i2.2.1.2"], x=subst2["i2.2.1.1"]):
                                pass
                                if 'i2.2' not in subst2 or 'i2.2.1.1' not in subst2 or cons_f19(m=subst2["i2.2"], x=subst2["i2.2.1.1"]):
                                    pass
                                    # State 3022
                                    if len(subjects) == 0:
                                        pass
                                        # 40: x**m /; (cons_f2) and (cons_f3) and (cons_f19) and (cons_f4) and (cons_f55)
                                        yield 40, subst2
                subjects.appendleft(tmp26)
            if len(subjects) >= 1 and isinstance(subjects[0], Mul):
                tmp28 = subjects.popleft()
                associative1 = tmp28
                associative_type1 = type(tmp28)
                subjects29 = deque(tmp28._args)
                matcher = CommutativeMatcher2675.get()
                tmp30 = subjects29
                subjects29 = []
                for s in tmp30:
                    matcher.add_subject(s)
                for pattern_index, subst2 in matcher.match(tmp30, subst1):
                    pass
                    if pattern_index == 0:
                        pass
                        if 'i2.2.0_1' not in subst2 or 'i2.2.0' not in subst2 or cons_f8(c=subst2["i2.2.0_1"], x=subst2["i2.2.0"]):
                            pass
                            if 'i2.2.0' not in subst2 or 'i2.2' not in subst2 or cons_f19(m=subst2["i2.2"], x=subst2["i2.2.0"]):
                                pass
                                if 'i2.2.0' not in subst2 or 'i2.0' not in subst2 or cons_f18(u=subst2["i2.0"], x=subst2["i2.2.0"]):
                                    pass
                                    # State 2676
                                    if len(subjects) == 0:
                                        pass
                                        # 10: (x*c)**m /; (cons_f8) and (cons_f19) and (cons_f18)
                                        yield 10, subst2
                subjects.appendleft(tmp28)
        subst1 = Substitution(subst0)
        try:
            subst1.try_add_variable('i2.2_1', S(1))
        except ValueError:
            pass
        else:
            pass
            # State 2692
            if len(subjects) >= 1:
                tmp32 = subjects.popleft()
                subst2 = Substitution(subst1)
                try:
                    subst2.try_add_variable('i2.2.0_1', tmp32)
                except ValueError:
                    pass
                else:
                    pass
                    # State 2693
                    if len(subjects) == 0:
                        pass
                        # 12: v**m /; (cons_f20)
                        yield 12, subst2
                subjects.appendleft(tmp32)
            if len(subjects) >= 1:
                tmp34 = subjects.popleft()
                subst2 = Substitution(subst1)
                try:
                    subst2.try_add_variable('i2.2.1.1', tmp34)
                except ValueError:
                    pass
                else:
                    pass
                    if 'i2.2.0' not in subst2 or 'i2.2.1.1' not in subst2 or cons_f2(a=subst2["i2.2.0"], x=subst2["i2.2.1.1"]):
                        pass
                        if 'i2.2.1.0' not in subst2 or 'i2.2.1.1' not in subst2 or cons_f3(b=subst2["i2.2.1.0"], x=subst2["i2.2.1.1"]):
                            pass
                            if 'i2.2.1.2' not in subst2 or 'i2.2.1.1' not in subst2 or cons_f4(n=subst2["i2.2.1.2"], x=subst2["i2.2.1.1"]):
                                pass
                                if 'i2.2' not in subst2 or 'i2.2.1.1' not in subst2 or cons_f5(p=subst2["i2.2"], x=subst2["i2.2.1.1"]):
                                    pass
                                    if 'i2.2_1' not in subst2 or 'i2.2.1.1' not in subst2 or cons_f19(m=subst2["i2.2_1"], x=subst2["i2.2.1.1"]):
                                        pass
                                        # State 3033
                                        if len(subjects) == 0:
                                            pass
                                            # 42: x**m /; (cons_f2) and (cons_f3) and (cons_f19) and (cons_f4) and (cons_f5) and (cons_f55)
                                            yield 42, subst2
                    if 'i2.2.1.2' not in subst2 or 'i2.2.1.1' not in subst2 or cons_f4(n=subst2["i2.2.1.2"], x=subst2["i2.2.1.1"]):
                        pass
                        if 'i2.2' not in subst2 or 'i2.2.1.1' not in subst2 or cons_f5(p=subst2["i2.2"], x=subst2["i2.2.1.1"]):
                            pass
                            if 'i2.2_1' not in subst2 or 'i2.2.1.1' not in subst2 or cons_f19(m=subst2["i2.2_1"], x=subst2["i2.2.1.1"]):
                                pass
                                if 'i2.2.0' not in subst2 or 'i2.2.1.1' not in subst2 or cons_f59(a1=subst2["i2.2.0"], x=subst2["i2.2.1.1"]):
                                    pass
                                    if 'i2.2.1.0' not in subst2 or 'i2.2.1.1' not in subst2 or cons_f60(b1=subst2["i2.2.1.0"], x=subst2["i2.2.1.1"]):
                                        pass
                                        if 'i2.2.0_1' not in subst2 or 'i2.2.1.1' not in subst2 or cons_f61(a2=subst2["i2.2.0_1"], x=subst2["i2.2.1.1"]):
                                            pass
                                            if 'i2.2.1.0_1' not in subst2 or 'i2.2.1.1' not in subst2 or cons_f62(b2=subst2["i2.2.1.0_1"], x=subst2["i2.2.1.1"]):
                                                pass
                                                # State 3033
                                                if len(subjects) == 0:
                                                    pass
                                                    # 45: x**m /; (cons_f59) and (cons_f60) and (cons_f61) and (cons_f62) and (cons_f19) and (cons_f4) and (cons_f5) and (cons_f58)
                                                    yield 45, subst2
                subjects.appendleft(tmp34)
            if len(subjects) >= 1 and isinstance(subjects[0], Add):
                tmp36 = subjects.popleft()
                associative1 = tmp36
                associative_type1 = type(tmp36)
                subjects37 = deque(tmp36._args)
                matcher = CommutativeMatcher2728.get()
                tmp38 = subjects37
                subjects37 = []
                for s in tmp38:
                    matcher.add_subject(s)
                for pattern_index, subst2 in matcher.match(tmp38, subst1):
                    pass
                    if pattern_index == 0:
                        pass
                        if 'i2.2.1.0_2' not in subst2 or 'i2.2.1.0_1' not in subst2 or 'i2.2.0' not in subst2 or 'i2.2.0_1' not in subst2 or cons_f27(a=subst2["i2.2.0"], b=subst2["i2.2.1.0_1"], c=subst2["i2.2.0_1"], d=subst2["i2.2.1.0_2"]):
                            pass
                            if 'i2' not in subst2 or 'i2.2.1.0_2' not in subst2 or 'i2.2.0_1' not in subst2 or 'i2.2.0' not in subst2 or 'i2.2_1' not in subst2 or 'i2.2.1.0_1' not in subst2 or cons_f28(a=subst2["i2.2.0"], b=subst2["i2.2.1.0_1"], c=subst2["i2.2.0_1"], d=subst2["i2.2.1.0_2"], n=subst2["i2.2_1"], x=subst2["i2"]):
                                pass
                                if 'i2' not in subst2 or 'i2.2.0_1' not in subst2 or cons_f8(c=subst2["i2.2.0_1"], x=subst2["i2"]):
                                    pass
                                    if 'i2.2.1.0_2' not in subst2 or 'i2' not in subst2 or cons_f29(d=subst2["i2.2.1.0_2"], x=subst2["i2"]):
                                        pass
                                        # State 2734
                                        if len(subjects) == 0:
                                            pass
                                            # 20: (c + v*b)**n /; (cons_f8) and (cons_f29) and (cons_f4) and (cons_f27) and (cons_f28)
                                            yield 20, subst2
                    if pattern_index == 1:
                        pass
                        if 'i2.2.0' not in subst2 or 'i2.2.1.1' not in subst2 or cons_f2(a=subst2["i2.2.0"], x=subst2["i2.2.1.1"]):
                            pass
                            if 'i2.2.1.0' not in subst2 or 'i2.2.1.1' not in subst2 or cons_f3(b=subst2["i2.2.1.0"], x=subst2["i2.2.1.1"]):
                                pass
                                if 'i2.2.1.2' not in subst2 or 'i2.2.1.1' not in subst2 or cons_f4(n=subst2["i2.2.1.2"], x=subst2["i2.2.1.1"]):
                                    pass
                                    if 'i2.2.0_1' not in subst2 or 'i2.2.1.1' not in subst2 or cons_f8(c=subst2["i2.2.0_1"], x=subst2["i2.2.1.1"]):
                                        pass
                                        if 'i2.2.1.0_1' not in subst2 or 'i2.2.1.1' not in subst2 or cons_f29(d=subst2["i2.2.1.0_1"], x=subst2["i2.2.1.1"]):
                                            pass
                                            if 'i2.2' not in subst2 or 'i2.2.1.1' not in subst2 or cons_f19(m=subst2["i2.2"], x=subst2["i2.2.1.1"]):
                                                pass
                                                if 'i2.2.1.2' not in subst2 or 'i2.2.1.2_1' not in subst2 or cons_f39(n=subst2["i2.2.1.2"], q=subst2["i2.2.1.2_1"]):
                                                    pass
                                                    if 'i2.2.1.0_1' not in subst2 or 'i2.2.1.0' not in subst2 or 'i2.2.0' not in subst2 or 'i2.2.0_1' not in subst2 or cons_f41(a=subst2["i2.2.0"], b=subst2["i2.2.1.0"], c=subst2["i2.2.0_1"], d=subst2["i2.2.1.0_1"]):
                                                        pass
                                                        # State 2811
                                                        if len(subjects) == 0:
                                                            pass
                                                            # 30: (c + b*v**n)**p /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f19) and (cons_f4) and (cons_f39) and (cons_f40) and (cons_f41)
                                                            yield 30, subst2
                    if pattern_index == 2:
                        pass
                        if 'i2.2' not in subst2 or 'i2.2.1.1' not in subst2 or cons_f5(p=subst2["i2.2"], x=subst2["i2.2.1.1"]):
                            pass
                            if 'i2.2.1.0_1' not in subst2 or 'i2.2.1.1' not in subst2 or cons_f3(b=subst2["i2.2.1.0_1"], x=subst2["i2.2.1.1"]):
                                pass
                                if 'i2.2.1.2_1' not in subst2 or 'i2.2.1.1' not in subst2 or cons_f4(n=subst2["i2.2.1.2_1"], x=subst2["i2.2.1.1"]):
                                    pass
                                    if 'i2.2.1.2' not in subst2 or 'i2.2.1.2_1' not in subst2 or cons_f7(j=subst2["i2.2.1.2"], n=subst2["i2.2.1.2_1"]):
                                        pass
                                        if 'i2.2.0_1' not in subst2 or 'i2.2.1.1' not in subst2 or cons_f2(a=subst2["i2.2.0_1"], x=subst2["i2.2.1.1"]):
                                            pass
                                            if 'i2.2.0' not in subst2 or 'i2.2.1.1' not in subst2 or cons_f8(c=subst2["i2.2.0"], x=subst2["i2.2.1.1"]):
                                                pass
                                                if 'i2.2.1.0' not in subst2 or 'i2.2.1.1' not in subst2 or cons_f29(d=subst2["i2.2.1.0"], x=subst2["i2.2.1.1"]):
                                                    pass
                                                    if 'i2.2_1' not in subst2 or 'i2.2.1.1' not in subst2 or cons_f19(m=subst2["i2.2_1"], x=subst2["i2.2.1.1"]):
                                                        pass
                                                        if 'i2.2.0' not in subst2 or 'i2.2.0_1' not in subst2 or 'i2.2.1.0_1' not in subst2 or 'i2.2.1.0' not in subst2 or cons_f44(a=subst2["i2.2.0_1"], b=subst2["i2.2.1.0_1"], c=subst2["i2.2.0"], d=subst2["i2.2.1.0"]):
                                                            pass
                                                            if 'i2.2.0_1' not in subst2 or cons_f45(a=subst2["i2.2.0_1"]):
                                                                pass
                                                                # State 2820
                                                                if len(subjects) == 0:
                                                                    pass
                                                                    # 31: (c + b*v**n)**p /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f19) and (cons_f4) and (cons_f5) and (cons_f7) and (cons_f43) and (cons_f44) and (cons_f45)
                                                                    yield 31, subst2
                subjects.appendleft(tmp36)
        if len(subjects) >= 1 and isinstance(subjects[0], Pow):
            tmp39 = subjects.popleft()
            subjects40 = deque(tmp39._args)
            # State 2372
            if len(subjects40) >= 1 and isinstance(subjects40[0], Add):
                tmp41 = subjects40.popleft()
                associative1 = tmp41
                associative_type1 = type(tmp41)
                subjects42 = deque(tmp41._args)
                matcher = CommutativeMatcher2374.get()
                tmp43 = subjects42
                subjects42 = []
                for s in tmp43:
                    matcher.add_subject(s)
                for pattern_index, subst1 in matcher.match(tmp43, subst0):
                    pass
                    if pattern_index == 0:
                        pass
                        if 'i2.2.0' not in subst1 or 'i2.2.1.1' not in subst1 or cons_f2(a=subst1["i2.2.0"], x=subst1["i2.2.1.1"]):
                            pass
                            if 'i2.2.1.0' not in subst1 or 'i2.2.1.1' not in subst1 or cons_f3(b=subst1["i2.2.1.0"], x=subst1["i2.2.1.1"]):
                                pass
                                if 'i2.2.1.2' not in subst1 or 'i2.2.1.1' not in subst1 or cons_f4(n=subst1["i2.2.1.2"], x=subst1["i2.2.1.1"]):
                                    pass
                                    if 'i2.2' not in subst1 or 'i2.2.1.1' not in subst1 or cons_f5(p=subst1["i2.2"], x=subst1["i2.2.1.1"]):
                                        pass
                                        if 'i2.2.0' not in subst1 or cons_f1(a=subst1["i2.2.0"]):
                                            pass
                                            # State 2391
                                            subst2 = Substitution(subst1)
                                            try:
                                                subst2.try_add_variable('i2.2', 1)
                                            except ValueError:
                                                pass
                                            else:
                                                pass
                                                if 'i2.2' not in subst2 or 'i2.2.1.1' not in subst2 or cons_f5(p=subst2["i2.2"], x=subst2["i2.2.1.1"]):
                                                    pass
                                                    # State 2392
                                                    if len(subjects40) == 0:
                                                        pass
                                                        # State 2393
                                                        if len(subjects) == 0:
                                                            pass
                                                            # 0: (a + a*v**m)**p /; (cons_f2) and (cons_f3) and (cons_f4) and (cons_f5) and (cons_f1)
                                                            yield 0, subst2
                                            if len(subjects40) >= 1:
                                                tmp45 = []
                                                tmp45.append(subjects40.popleft())
                                                while True:
                                                    if len(tmp45) > 1:
                                                        tmp46 = create_operation_expression(associative1, tmp45)
                                                    elif len(tmp45) == 1:
                                                        tmp46 = tmp45[0]
                                                    else:
                                                        assert False, "Unreachable"
                                                    subst2 = Substitution(subst1)
                                                    try:
                                                        subst2.try_add_variable('i2.2', tmp46)
                                                    except ValueError:
                                                        pass
                                                    else:
                                                        pass
                                                        if 'i2.2' not in subst2 or 'i2.2.1.1' not in subst2 or cons_f5(p=subst2["i2.2"], x=subst2["i2.2.1.1"]):
                                                            pass
                                                            # State 2392
                                                            if len(subjects40) == 0:
                                                                pass
                                                                # State 2393
                                                                if len(subjects) == 0:
                                                                    pass
                                                                    # 0: (a + a*v**m)**p /; (cons_f2) and (cons_f3) and (cons_f4) and (cons_f5) and (cons_f1)
                                                                    yield 0, subst2
                                                    if len(subjects40) == 0:
                                                        break
                                                    tmp45.append(subjects40.popleft())
                                                subjects40.extendleft(reversed(tmp45))
                    if pattern_index == 1:
                        pass
                        if 'i2.2.0' not in subst1 or 'i2.2.1.1' not in subst1 or cons_f2(a=subst1["i2.2.0"], x=subst1["i2.2.1.1"]):
                            pass
                            if 'i2.2.1.0' not in subst1 or 'i2.2.1.1' not in subst1 or cons_f3(b=subst1["i2.2.1.0"], x=subst1["i2.2.1.1"]):
                                pass
                                if 'i2.2.1.2' not in subst1 or 'i2.2.1.1' not in subst1 or cons_f4(n=subst1["i2.2.1.2"], x=subst1["i2.2.1.1"]):
                                    pass
                                    if 'i2.2' not in subst1 or 'i2.2.1.1' not in subst1 or cons_f5(p=subst1["i2.2"], x=subst1["i2.2.1.1"]):
                                        pass
                                        if 'i2.2.1.0' not in subst1 or cons_f6(b=subst1["i2.2.1.0"]):
                                            pass
                                            # State 2498
                                            subst2 = Substitution(subst1)
                                            try:
                                                subst2.try_add_variable('i2.2', 1)
                                            except ValueError:
                                                pass
                                            else:
                                                pass
                                                if 'i2.2' not in subst2 or 'i2.2.1.1' not in subst2 or cons_f5(p=subst2["i2.2"], x=subst2["i2.2.1.1"]):
                                                    pass
                                                    # State 2499
                                                    if len(subjects40) == 0:
                                                        pass
                                                        # State 2500
                                                        if len(subjects) == 0:
                                                            pass
                                                            # 1: (a + a*v**m)**p /; (cons_f2) and (cons_f3) and (cons_f4) and (cons_f5) and (cons_f6)
                                                            yield 1, subst2
                                            if len(subjects40) >= 1:
                                                tmp49 = []
                                                tmp49.append(subjects40.popleft())
                                                while True:
                                                    if len(tmp49) > 1:
                                                        tmp50 = create_operation_expression(associative1, tmp49)
                                                    elif len(tmp49) == 1:
                                                        tmp50 = tmp49[0]
                                                    else:
                                                        assert False, "Unreachable"
                                                    subst2 = Substitution(subst1)
                                                    try:
                                                        subst2.try_add_variable('i2.2', tmp50)
                                                    except ValueError:
                                                        pass
                                                    else:
                                                        pass
                                                        if 'i2.2' not in subst2 or 'i2.2.1.1' not in subst2 or cons_f5(p=subst2["i2.2"], x=subst2["i2.2.1.1"]):
                                                            pass
                                                            # State 2499
                                                            if len(subjects40) == 0:
                                                                pass
                                                                # State 2500
                                                                if len(subjects) == 0:
                                                                    pass
                                                                    # 1: (a + a*v**m)**p /; (cons_f2) and (cons_f3) and (cons_f4) and (cons_f5) and (cons_f6)
                                                                    yield 1, subst2
                                                    if len(subjects40) == 0:
                                                        break
                                                    tmp49.append(subjects40.popleft())
                                                subjects40.extendleft(reversed(tmp49))
                    if pattern_index == 2:
                        pass
                        if 'i2.2.0' not in subst1 or 'i2.2.1.1' not in subst1 or cons_f2(a=subst1["i2.2.0"], x=subst1["i2.2.1.1"]):
                            pass
                            if 'i2.2' not in subst1 or 'i2.2.1.1' not in subst1 or cons_f5(p=subst1["i2.2"], x=subst1["i2.2.1.1"]):
                                pass
                                if 'i2.2.0' not in subst1 or cons_f1(a=subst1["i2.2.0"]):
                                    pass
                                    if 'i2.2.1.0_1' not in subst1 or 'i2.2.1.1' not in subst1 or cons_f3(b=subst1["i2.2.1.0_1"], x=subst1["i2.2.1.1"]):
                                        pass
                                        if 'i2.2.1.0' not in subst1 or 'i2.2.1.1' not in subst1 or cons_f8(c=subst1["i2.2.1.0"], x=subst1["i2.2.1.1"]):
                                            pass
                                            if 'i2.2.1.2_1' not in subst1 or 'i2.2.1.1' not in subst1 or cons_f4(n=subst1["i2.2.1.2_1"], x=subst1["i2.2.1.1"]):
                                                pass
                                                if 'i2.2.1.2' not in subst1 or 'i2.2.1.2_1' not in subst1 or cons_f7(j=subst1["i2.2.1.2"], n=subst1["i2.2.1.2_1"]):
                                                    pass
                                                    # State 2565
                                                    subst2 = Substitution(subst1)
                                                    try:
                                                        subst2.try_add_variable('i2.2', 1)
                                                    except ValueError:
                                                        pass
                                                    else:
                                                        pass
                                                        if 'i2.2' not in subst2 or 'i2.2.1.1' not in subst2 or cons_f5(p=subst2["i2.2"], x=subst2["i2.2.1.1"]):
                                                            pass
                                                            # State 2566
                                                            if len(subjects40) == 0:
                                                                pass
                                                                # State 2567
                                                                if len(subjects) == 0:
                                                                    pass
                                                                    # 2: (a + b*v**n + a*v**m)**p /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f4) and (cons_f5) and (cons_f7) and (cons_f1)
                                                                    yield 2, subst2
                                                    if len(subjects40) >= 1:
                                                        tmp53 = []
                                                        tmp53.append(subjects40.popleft())
                                                        while True:
                                                            if len(tmp53) > 1:
                                                                tmp54 = create_operation_expression(associative1, tmp53)
                                                            elif len(tmp53) == 1:
                                                                tmp54 = tmp53[0]
                                                            else:
                                                                assert False, "Unreachable"
                                                            subst2 = Substitution(subst1)
                                                            try:
                                                                subst2.try_add_variable('i2.2', tmp54)
                                                            except ValueError:
                                                                pass
                                                            else:
                                                                pass
                                                                if 'i2.2' not in subst2 or 'i2.2.1.1' not in subst2 or cons_f5(p=subst2["i2.2"], x=subst2["i2.2.1.1"]):
                                                                    pass
                                                                    # State 2566
                                                                    if len(subjects40) == 0:
                                                                        pass
                                                                        # State 2567
                                                                        if len(subjects) == 0:
                                                                            pass
                                                                            # 2: (a + b*v**n + a*v**m)**p /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f4) and (cons_f5) and (cons_f7) and (cons_f1)
                                                                            yield 2, subst2
                                                            if len(subjects40) == 0:
                                                                break
                                                            tmp53.append(subjects40.popleft())
                                                        subjects40.extendleft(reversed(tmp53))
                    if pattern_index == 3:
                        pass
                        if 'i2.2.0' not in subst1 or 'i2.2.1.1' not in subst1 or cons_f2(a=subst1["i2.2.0"], x=subst1["i2.2.1.1"]):
                            pass
                            if 'i2.2' not in subst1 or 'i2.2.1.1' not in subst1 or cons_f5(p=subst1["i2.2"], x=subst1["i2.2.1.1"]):
                                pass
                                if 'i2.2.1.0_1' not in subst1 or 'i2.2.1.1' not in subst1 or cons_f3(b=subst1["i2.2.1.0_1"], x=subst1["i2.2.1.1"]):
                                    pass
                                    if 'i2.2.1.0' not in subst1 or 'i2.2.1.1' not in subst1 or cons_f8(c=subst1["i2.2.1.0"], x=subst1["i2.2.1.1"]):
                                        pass
                                        if 'i2.2.1.2_1' not in subst1 or 'i2.2.1.1' not in subst1 or cons_f4(n=subst1["i2.2.1.2_1"], x=subst1["i2.2.1.1"]):
                                            pass
                                            if 'i2.2.1.2' not in subst1 or 'i2.2.1.2_1' not in subst1 or cons_f7(j=subst1["i2.2.1.2"], n=subst1["i2.2.1.2_1"]):
                                                pass
                                                if 'i2.2.1.0_1' not in subst1 or cons_f6(b=subst1["i2.2.1.0_1"]):
                                                    pass
                                                    # State 2580
                                                    subst2 = Substitution(subst1)
                                                    try:
                                                        subst2.try_add_variable('i2.2', 1)
                                                    except ValueError:
                                                        pass
                                                    else:
                                                        pass
                                                        if 'i2.2' not in subst2 or 'i2.2.1.1' not in subst2 or cons_f5(p=subst2["i2.2"], x=subst2["i2.2.1.1"]):
                                                            pass
                                                            # State 2581
                                                            if len(subjects40) == 0:
                                                                pass
                                                                # State 2582
                                                                if len(subjects) == 0:
                                                                    pass
                                                                    # 3: (a + b*v**n + a*v**m)**p /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f4) and (cons_f5) and (cons_f7) and (cons_f6)
                                                                    yield 3, subst2
                                                    if len(subjects40) >= 1:
                                                        tmp57 = []
                                                        tmp57.append(subjects40.popleft())
                                                        while True:
                                                            if len(tmp57) > 1:
                                                                tmp58 = create_operation_expression(associative1, tmp57)
                                                            elif len(tmp57) == 1:
                                                                tmp58 = tmp57[0]
                                                            else:
                                                                assert False, "Unreachable"
                                                            subst2 = Substitution(subst1)
                                                            try:
                                                                subst2.try_add_variable('i2.2', tmp58)
                                                            except ValueError:
                                                                pass
                                                            else:
                                                                pass
                                                                if 'i2.2' not in subst2 or 'i2.2.1.1' not in subst2 or cons_f5(p=subst2["i2.2"], x=subst2["i2.2.1.1"]):
                                                                    pass
                                                                    # State 2581
                                                                    if len(subjects40) == 0:
                                                                        pass
                                                                        # State 2582
                                                                        if len(subjects) == 0:
                                                                            pass
                                                                            # 3: (a + b*v**n + a*v**m)**p /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f4) and (cons_f5) and (cons_f7) and (cons_f6)
                                                                            yield 3, subst2
                                                            if len(subjects40) == 0:
                                                                break
                                                            tmp57.append(subjects40.popleft())
                                                        subjects40.extendleft(reversed(tmp57))
                    if pattern_index == 4:
                        pass
                        if 'i2.2.0' not in subst1 or 'i2.2.1.1' not in subst1 or cons_f2(a=subst1["i2.2.0"], x=subst1["i2.2.1.1"]):
                            pass
                            if 'i2.2' not in subst1 or 'i2.2.1.1' not in subst1 or cons_f5(p=subst1["i2.2"], x=subst1["i2.2.1.1"]):
                                pass
                                if 'i2.2.1.0_1' not in subst1 or 'i2.2.1.1' not in subst1 or cons_f3(b=subst1["i2.2.1.0_1"], x=subst1["i2.2.1.1"]):
                                    pass
                                    if 'i2.2.1.0' not in subst1 or 'i2.2.1.1' not in subst1 or cons_f8(c=subst1["i2.2.1.0"], x=subst1["i2.2.1.1"]):
                                        pass
                                        if 'i2.2.1.2_1' not in subst1 or 'i2.2.1.1' not in subst1 or cons_f4(n=subst1["i2.2.1.2_1"], x=subst1["i2.2.1.1"]):
                                            pass
                                            if 'i2.2.1.2' not in subst1 or 'i2.2.1.2_1' not in subst1 or cons_f7(j=subst1["i2.2.1.2"], n=subst1["i2.2.1.2_1"]):
                                                pass
                                                if 'i2.2.1.0' not in subst1 or cons_f9(c=subst1["i2.2.1.0"]):
                                                    pass
                                                    # State 2595
                                                    subst2 = Substitution(subst1)
                                                    try:
                                                        subst2.try_add_variable('i2.2', 1)
                                                    except ValueError:
                                                        pass
                                                    else:
                                                        pass
                                                        if 'i2.2' not in subst2 or 'i2.2.1.1' not in subst2 or cons_f5(p=subst2["i2.2"], x=subst2["i2.2.1.1"]):
                                                            pass
                                                            # State 2596
                                                            if len(subjects40) == 0:
                                                                pass
                                                                # State 2597
                                                                if len(subjects) == 0:
                                                                    pass
                                                                    # 4: (a + b*v**n + a*v**m)**p /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f4) and (cons_f5) and (cons_f7) and (cons_f9)
                                                                    yield 4, subst2
                                                    if len(subjects40) >= 1:
                                                        tmp61 = []
                                                        tmp61.append(subjects40.popleft())
                                                        while True:
                                                            if len(tmp61) > 1:
                                                                tmp62 = create_operation_expression(associative1, tmp61)
                                                            elif len(tmp61) == 1:
                                                                tmp62 = tmp61[0]
                                                            else:
                                                                assert False, "Unreachable"
                                                            subst2 = Substitution(subst1)
                                                            try:
                                                                subst2.try_add_variable('i2.2', tmp62)
                                                            except ValueError:
                                                                pass
                                                            else:
                                                                pass
                                                                if 'i2.2' not in subst2 or 'i2.2.1.1' not in subst2 or cons_f5(p=subst2["i2.2"], x=subst2["i2.2.1.1"]):
                                                                    pass
                                                                    # State 2596
                                                                    if len(subjects40) == 0:
                                                                        pass
                                                                        # State 2597
                                                                        if len(subjects) == 0:
                                                                            pass
                                                                            # 4: (a + b*v**n + a*v**m)**p /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f4) and (cons_f5) and (cons_f7) and (cons_f9)
                                                                            yield 4, subst2
                                                            if len(subjects40) == 0:
                                                                break
                                                            tmp61.append(subjects40.popleft())
                                                        subjects40.extendleft(reversed(tmp61))
                    if pattern_index == 5:
                        pass
                        if 'i2' not in subst1 or 'i2.2.1.0_1' not in subst1 or cons_f2(a=subst1["i2.2.1.0_1"], x=subst1["i2"]):
                            pass
                            if 'i2.2.1.0_2' not in subst1 or 'i2' not in subst1 or cons_f3(b=subst1["i2.2.1.0_2"], x=subst1["i2"]):
                                pass
                                if 'i2' not in subst1 or 'i2.2.1.0' not in subst1 or cons_f10(v=subst1["i2.2.1.0"], x=subst1["i2"]):
                                    pass
                                    # State 2630
                                    subst2 = Substitution(subst1)
                                    try:
                                        subst2.try_add_variable('i2.2', 1)
                                    except ValueError:
                                        pass
                                    else:
                                        pass
                                        # State 2631
                                        if len(subjects40) == 0:
                                            pass
                                            # State 2632
                                            if len(subjects) == 0:
                                                pass
                                                # 5: (w + v*a + v*b)**p /; (cons_f2) and (cons_f3) and (cons_f10)
                                                yield 5, subst2
                                    if len(subjects40) >= 1:
                                        tmp65 = []
                                        tmp65.append(subjects40.popleft())
                                        while True:
                                            if len(tmp65) > 1:
                                                tmp66 = create_operation_expression(associative1, tmp65)
                                            elif len(tmp65) == 1:
                                                tmp66 = tmp65[0]
                                            else:
                                                assert False, "Unreachable"
                                            subst2 = Substitution(subst1)
                                            try:
                                                subst2.try_add_variable('i2.2', tmp66)
                                            except ValueError:
                                                pass
                                            else:
                                                pass
                                                # State 2631
                                                if len(subjects40) == 0:
                                                    pass
                                                    # State 2632
                                                    if len(subjects) == 0:
                                                        pass
                                                        # 5: (w + v*a + v*b)**p /; (cons_f2) and (cons_f3) and (cons_f10)
                                                        yield 5, subst2
                                            if len(subjects40) == 0:
                                                break
                                            tmp65.append(subjects40.popleft())
                                        subjects40.extendleft(reversed(tmp65))
                    if pattern_index == 6:
                        pass
                        if 'i2' not in subst1 or 'i2.2.0' not in subst1 or cons_f2(a=subst1["i2.2.0"], x=subst1["i2"]):
                            pass
                            if 'i2' not in subst1 or 'i2.2.1.0_1' not in subst1 or cons_f3(b=subst1["i2.2.1.0_1"], x=subst1["i2"]):
                                pass
                                if 'i2.2.1.0_2' not in subst1 or 'i2.2.1.0_1' not in subst1 or 'i2.2.0' not in subst1 or 'i2.2.0_1' not in subst1 or cons_f27(a=subst1["i2.2.0"], b=subst1["i2.2.1.0_1"], c=subst1["i2.2.0_1"], d=subst1["i2.2.1.0_2"]):
                                    pass
                                    if 'i2' not in subst1 or 'i2.2.1.0_2' not in subst1 or 'i2.2.0_1' not in subst1 or 'i2.2.0' not in subst1 or 'i2.2_1' not in subst1 or 'i2.2.1.0_1' not in subst1 or cons_f28(a=subst1["i2.2.0"], b=subst1["i2.2.1.0_1"], c=subst1["i2.2.0_1"], d=subst1["i2.2.1.0_2"], n=subst1["i2.2_1"], x=subst1["i2"]):
                                        pass
                                        # State 2724
                                        subst2 = Substitution(subst1)
                                        try:
                                            subst2.try_add_variable('i2.2', 1)
                                        except ValueError:
                                            pass
                                        else:
                                            pass
                                            if 'i2.2' not in subst2 or cons_f20(m=subst2["i2.2"]):
                                                pass
                                                # State 2725
                                                if len(subjects40) == 0:
                                                    pass
                                                    # State 2726
                                                    if len(subjects) == 0:
                                                        pass
                                                        # 19: (a + v*a)**m /; (cons_f2) and (cons_f3) and (cons_f27) and (cons_f20) and (cons_f28)
                                                        yield 19, subst2
                                        if len(subjects40) >= 1:
                                            tmp69 = []
                                            tmp69.append(subjects40.popleft())
                                            while True:
                                                if len(tmp69) > 1:
                                                    tmp70 = create_operation_expression(associative1, tmp69)
                                                elif len(tmp69) == 1:
                                                    tmp70 = tmp69[0]
                                                else:
                                                    assert False, "Unreachable"
                                                subst2 = Substitution(subst1)
                                                try:
                                                    subst2.try_add_variable('i2.2', tmp70)
                                                except ValueError:
                                                    pass
                                                else:
                                                    pass
                                                    if 'i2.2' not in subst2 or cons_f20(m=subst2["i2.2"]):
                                                        pass
                                                        # State 2725
                                                        if len(subjects40) == 0:
                                                            pass
                                                            # State 2726
                                                            if len(subjects) == 0:
                                                                pass
                                                                # 19: (a + v*a)**m /; (cons_f2) and (cons_f3) and (cons_f27) and (cons_f20) and (cons_f28)
                                                                yield 19, subst2
                                                if len(subjects40) == 0:
                                                    break
                                                tmp69.append(subjects40.popleft())
                                            subjects40.extendleft(reversed(tmp69))
                    if pattern_index == 7:
                        pass
                        if 'i2.2.1.0_2' not in subst1 or 'i2.2.1.0_1' not in subst1 or 'i2.2.0' not in subst1 or 'i2.2.0_1' not in subst1 or cons_f27(a=subst1["i2.2.0"], b=subst1["i2.2.1.0_1"], c=subst1["i2.2.0_1"], d=subst1["i2.2.1.0_2"]):
                            pass
                            if 'i2' not in subst1 or 'i2.2.1.0_2' not in subst1 or 'i2.2.0_1' not in subst1 or 'i2.2.0' not in subst1 or 'i2.2_1' not in subst1 or 'i2.2.1.0_1' not in subst1 or cons_f28(a=subst1["i2.2.0"], b=subst1["i2.2.1.0_1"], c=subst1["i2.2.0_1"], d=subst1["i2.2.1.0_2"], n=subst1["i2.2_1"], x=subst1["i2"]):
                                pass
                                if 'i2' not in subst1 or 'i2.2.0_1' not in subst1 or cons_f8(c=subst1["i2.2.0_1"], x=subst1["i2"]):
                                    pass
                                    if 'i2.2.1.0_2' not in subst1 or 'i2' not in subst1 or cons_f29(d=subst1["i2.2.1.0_2"], x=subst1["i2"]):
                                        pass
                                        # State 2735
                                        subst2 = Substitution(subst1)
                                        try:
                                            subst2.try_add_variable('i2.2_1', 1)
                                        except ValueError:
                                            pass
                                        else:
                                            pass
                                            if 'i2.2_1' not in subst2 or 'i2' not in subst2 or cons_f4(n=subst2["i2.2_1"], x=subst2["i2"]):
                                                pass
                                                if 'i2' not in subst2 or 'i2.2.1.0_2' not in subst2 or 'i2.2.0_1' not in subst2 or 'i2.2.0' not in subst2 or 'i2.2_1' not in subst2 or 'i2.2.1.0_1' not in subst2 or cons_f28(a=subst2["i2.2.0"], b=subst2["i2.2.1.0_1"], c=subst2["i2.2.0_1"], d=subst2["i2.2.1.0_2"], n=subst2["i2.2_1"], x=subst2["i2"]):
                                                    pass
                                                    # State 2736
                                                    if len(subjects40) == 0:
                                                        pass
                                                        # State 2737
                                                        if len(subjects) == 0:
                                                            pass
                                                            # 20: (c + v*b)**n /; (cons_f8) and (cons_f29) and (cons_f4) and (cons_f27) and (cons_f28)
                                                            yield 20, subst2
                                        if len(subjects40) >= 1:
                                            tmp73 = []
                                            tmp73.append(subjects40.popleft())
                                            while True:
                                                if len(tmp73) > 1:
                                                    tmp74 = create_operation_expression(associative1, tmp73)
                                                elif len(tmp73) == 1:
                                                    tmp74 = tmp73[0]
                                                else:
                                                    assert False, "Unreachable"
                                                subst2 = Substitution(subst1)
                                                try:
                                                    subst2.try_add_variable('i2.2_1', tmp74)
                                                except ValueError:
                                                    pass
                                                else:
                                                    pass
                                                    if 'i2.2_1' not in subst2 or 'i2' not in subst2 or cons_f4(n=subst2["i2.2_1"], x=subst2["i2"]):
                                                        pass
                                                        if 'i2' not in subst2 or 'i2.2.1.0_2' not in subst2 or 'i2.2.0_1' not in subst2 or 'i2.2.0' not in subst2 or 'i2.2_1' not in subst2 or 'i2.2.1.0_1' not in subst2 or cons_f28(a=subst2["i2.2.0"], b=subst2["i2.2.1.0_1"], c=subst2["i2.2.0_1"], d=subst2["i2.2.1.0_2"], n=subst2["i2.2_1"], x=subst2["i2"]):
                                                            pass
                                                            # State 2736
                                                            if len(subjects40) == 0:
                                                                pass
                                                                # State 2737
                                                                if len(subjects) == 0:
                                                                    pass
                                                                    # 20: (c + v*b)**n /; (cons_f8) and (cons_f29) and (cons_f4) and (cons_f27) and (cons_f28)
                                                                    yield 20, subst2
                                                if len(subjects40) == 0:
                                                    break
                                                tmp73.append(subjects40.popleft())
                                            subjects40.extendleft(reversed(tmp73))
                    if pattern_index == 8:
                        pass
                        if 'i2' not in subst1 or 'i2.2.0' not in subst1 or cons_f2(a=subst1["i2.2.0"], x=subst1["i2"]):
                            pass
                            if 'i2' not in subst1 or 'i2.2.1.0_1' not in subst1 or cons_f3(b=subst1["i2.2.1.0_1"], x=subst1["i2"]):
                                pass
                                if 'i2.2.1.0_2' not in subst1 or 'i2.2.1.0_1' not in subst1 or 'i2.2.0' not in subst1 or 'i2.2.0_1' not in subst1 or cons_f27(a=subst1["i2.2.0"], b=subst1["i2.2.1.0_1"], c=subst1["i2.2.0_1"], d=subst1["i2.2.1.0_2"]):
                                    pass
                                    if 'i2.2.1.0_2' not in subst1 or 'i2.2.1.0_1' not in subst1 or cons_f30(b=subst1["i2.2.1.0_1"], d=subst1["i2.2.1.0_2"]):
                                        pass
                                        # State 2741
                                        if len(subjects40) >= 1:
                                            tmp76 = []
                                            tmp76.append(subjects40.popleft())
                                            while True:
                                                if len(tmp76) > 1:
                                                    tmp77 = create_operation_expression(associative1, tmp76)
                                                elif len(tmp76) == 1:
                                                    tmp77 = tmp76[0]
                                                else:
                                                    assert False, "Unreachable"
                                                subst2 = Substitution(subst1)
                                                try:
                                                    subst2.try_add_variable('i2.2', tmp77)
                                                except ValueError:
                                                    pass
                                                else:
                                                    pass
                                                    if 'i2' not in subst2 or 'i2.2' not in subst2 or cons_f19(m=subst2["i2.2"], x=subst2["i2"]):
                                                        pass
                                                        if 'i2.2_1' not in subst2 or 'i2.2' not in subst2 or cons_f31(m=subst2["i2.2"], n=subst2["i2.2_1"]):
                                                            pass
                                                            # State 2742
                                                            if len(subjects40) == 0:
                                                                pass
                                                                # State 2743
                                                                if len(subjects) == 0:
                                                                    pass
                                                                    # 21: (a + v*a)**m /; (cons_f2) and (cons_f3) and (cons_f19) and (cons_f27) and (cons_f30) and (cons_f31)
                                                                    yield 21, subst2
                                                if len(subjects40) == 0:
                                                    break
                                                tmp76.append(subjects40.popleft())
                                            subjects40.extendleft(reversed(tmp76))
                    if pattern_index == 9:
                        pass
                        if 'i2.2.1.0_2' not in subst1 or 'i2.2.1.0_1' not in subst1 or 'i2.2.0' not in subst1 or 'i2.2.0_1' not in subst1 or cons_f27(a=subst1["i2.2.0"], b=subst1["i2.2.1.0_1"], c=subst1["i2.2.0_1"], d=subst1["i2.2.1.0_2"]):
                            pass
                            if 'i2' not in subst1 or 'i2.2.0_1' not in subst1 or cons_f8(c=subst1["i2.2.0_1"], x=subst1["i2"]):
                                pass
                                if 'i2.2.1.0_2' not in subst1 or 'i2' not in subst1 or cons_f29(d=subst1["i2.2.1.0_2"], x=subst1["i2"]):
                                    pass
                                    if 'i2.2.1.0_2' not in subst1 or 'i2.2.1.0_1' not in subst1 or cons_f30(b=subst1["i2.2.1.0_1"], d=subst1["i2.2.1.0_2"]):
                                        pass
                                        # State 2744
                                        if len(subjects40) >= 1:
                                            tmp79 = []
                                            tmp79.append(subjects40.popleft())
                                            while True:
                                                if len(tmp79) > 1:
                                                    tmp80 = create_operation_expression(associative1, tmp79)
                                                elif len(tmp79) == 1:
                                                    tmp80 = tmp79[0]
                                                else:
                                                    assert False, "Unreachable"
                                                subst2 = Substitution(subst1)
                                                try:
                                                    subst2.try_add_variable('i2.2_1', tmp80)
                                                except ValueError:
                                                    pass
                                                else:
                                                    pass
                                                    if 'i2.2_1' not in subst2 or 'i2' not in subst2 or cons_f4(n=subst2["i2.2_1"], x=subst2["i2"]):
                                                        pass
                                                        if 'i2.2_1' not in subst2 or 'i2.2' not in subst2 or cons_f31(m=subst2["i2.2"], n=subst2["i2.2_1"]):
                                                            pass
                                                            # State 2745
                                                            if len(subjects40) == 0:
                                                                pass
                                                                # State 2746
                                                                if len(subjects) == 0:
                                                                    pass
                                                                    # 22: (c + v*b)**n /; (cons_f8) and (cons_f29) and (cons_f4) and (cons_f27) and (cons_f30) and (cons_f31)
                                                                    yield 22, subst2
                                                if len(subjects40) == 0:
                                                    break
                                                tmp79.append(subjects40.popleft())
                                            subjects40.extendleft(reversed(tmp79))
                    if pattern_index == 10:
                        pass
                        if 'i2' not in subst1 or 'i2.2.0' not in subst1 or cons_f2(a=subst1["i2.2.0"], x=subst1["i2"]):
                            pass
                            if 'i2' not in subst1 or 'i2.2.1.0_1' not in subst1 or cons_f3(b=subst1["i2.2.1.0_1"], x=subst1["i2"]):
                                pass
                                if 'i2.2.1.0_2' not in subst1 or 'i2.2.1.0_1' not in subst1 or 'i2.2.0' not in subst1 or 'i2.2.0_1' not in subst1 or cons_f27(a=subst1["i2.2.0"], b=subst1["i2.2.1.0_1"], c=subst1["i2.2.0_1"], d=subst1["i2.2.1.0_2"]):
                                    pass
                                    if 'i2.2_1' not in subst1 or 'i2.2.1.0_2' not in subst1 or 'i2.2.1.0_1' not in subst1 or 'i2.2' not in subst1 or cons_f32(b=subst1["i2.2.1.0_1"], d=subst1["i2.2.1.0_2"], m=subst1["i2.2"], n=subst1["i2.2_1"]):
                                        pass
                                        # State 2750
                                        if len(subjects40) >= 1:
                                            tmp82 = []
                                            tmp82.append(subjects40.popleft())
                                            while True:
                                                if len(tmp82) > 1:
                                                    tmp83 = create_operation_expression(associative1, tmp82)
                                                elif len(tmp82) == 1:
                                                    tmp83 = tmp82[0]
                                                else:
                                                    assert False, "Unreachable"
                                                subst2 = Substitution(subst1)
                                                try:
                                                    subst2.try_add_variable('i2.2', tmp83)
                                                except ValueError:
                                                    pass
                                                else:
                                                    pass
                                                    if 'i2' not in subst2 or 'i2.2' not in subst2 or cons_f19(m=subst2["i2.2"], x=subst2["i2"]):
                                                        pass
                                                        if 'i2.2_1' not in subst2 or 'i2.2.1.0_2' not in subst2 or 'i2.2.1.0_1' not in subst2 or 'i2.2' not in subst2 or cons_f32(b=subst2["i2.2.1.0_1"], d=subst2["i2.2.1.0_2"], m=subst2["i2.2"], n=subst2["i2.2_1"]):
                                                            pass
                                                            # State 2751
                                                            if len(subjects40) == 0:
                                                                pass
                                                                # State 2752
                                                                if len(subjects) == 0:
                                                                    pass
                                                                    # 23: (a + v*a)**m /; (cons_f2) and (cons_f3) and (cons_f19) and (cons_f27) and (cons_f32)
                                                                    yield 23, subst2
                                                if len(subjects40) == 0:
                                                    break
                                                tmp82.append(subjects40.popleft())
                                            subjects40.extendleft(reversed(tmp82))
                    if pattern_index == 11:
                        pass
                        if 'i2.2.1.0_2' not in subst1 or 'i2.2.1.0_1' not in subst1 or 'i2.2.0' not in subst1 or 'i2.2.0_1' not in subst1 or cons_f27(a=subst1["i2.2.0"], b=subst1["i2.2.1.0_1"], c=subst1["i2.2.0_1"], d=subst1["i2.2.1.0_2"]):
                            pass
                            if 'i2' not in subst1 or 'i2.2.0_1' not in subst1 or cons_f8(c=subst1["i2.2.0_1"], x=subst1["i2"]):
                                pass
                                if 'i2.2.1.0_2' not in subst1 or 'i2' not in subst1 or cons_f29(d=subst1["i2.2.1.0_2"], x=subst1["i2"]):
                                    pass
                                    if 'i2.2_1' not in subst1 or 'i2.2.1.0_2' not in subst1 or 'i2.2.1.0_1' not in subst1 or 'i2.2' not in subst1 or cons_f32(b=subst1["i2.2.1.0_1"], d=subst1["i2.2.1.0_2"], m=subst1["i2.2"], n=subst1["i2.2_1"]):
                                        pass
                                        # State 2753
                                        if len(subjects40) >= 1:
                                            tmp85 = []
                                            tmp85.append(subjects40.popleft())
                                            while True:
                                                if len(tmp85) > 1:
                                                    tmp86 = create_operation_expression(associative1, tmp85)
                                                elif len(tmp85) == 1:
                                                    tmp86 = tmp85[0]
                                                else:
                                                    assert False, "Unreachable"
                                                subst2 = Substitution(subst1)
                                                try:
                                                    subst2.try_add_variable('i2.2_1', tmp86)
                                                except ValueError:
                                                    pass
                                                else:
                                                    pass
                                                    if 'i2.2_1' not in subst2 or 'i2' not in subst2 or cons_f4(n=subst2["i2.2_1"], x=subst2["i2"]):
                                                        pass
                                                        if 'i2.2_1' not in subst2 or 'i2.2.1.0_2' not in subst2 or 'i2.2.1.0_1' not in subst2 or 'i2.2' not in subst2 or cons_f32(b=subst2["i2.2.1.0_1"], d=subst2["i2.2.1.0_2"], m=subst2["i2.2"], n=subst2["i2.2_1"]):
                                                            pass
                                                            # State 2754
                                                            if len(subjects40) == 0:
                                                                pass
                                                                # State 2755
                                                                if len(subjects) == 0:
                                                                    pass
                                                                    # 24: (c + v*b)**n /; (cons_f8) and (cons_f29) and (cons_f4) and (cons_f27) and (cons_f32)
                                                                    yield 24, subst2
                                                if len(subjects40) == 0:
                                                    break
                                                tmp85.append(subjects40.popleft())
                                            subjects40.extendleft(reversed(tmp85))
                    if pattern_index == 12:
                        pass
                        if 'i2' not in subst1 or 'i2.2.0' not in subst1 or cons_f2(a=subst1["i2.2.0"], x=subst1["i2"]):
                            pass
                            if 'i2' not in subst1 or 'i2.2.1.0_1' not in subst1 or cons_f3(b=subst1["i2.2.1.0_1"], x=subst1["i2"]):
                                pass
                                if 'i2.1.0' not in subst1 or 'i2.2.0' not in subst1 or 'i2.1.1.0_1' not in subst1 or 'i2.1.1.0' not in subst1 or 'i2.2.1.0_1' not in subst1 or cons_f35(A=subst1["i2.1.0"], B=subst1["i2.1.1.0_1"], C=subst1["i2.1.1.0"], a=subst1["i2.2.0"], b=subst1["i2.2.1.0_1"]):
                                    pass
                                    # State 2775
                                    if len(subjects40) >= 1:
                                        tmp88 = []
                                        tmp88.append(subjects40.popleft())
                                        while True:
                                            if len(tmp88) > 1:
                                                tmp89 = create_operation_expression(associative1, tmp88)
                                            elif len(tmp88) == 1:
                                                tmp89 = tmp88[0]
                                            else:
                                                assert False, "Unreachable"
                                            subst2 = Substitution(subst1)
                                            try:
                                                subst2.try_add_variable('i2.2', tmp89)
                                            except ValueError:
                                                pass
                                            else:
                                                pass
                                                if 'i2.2' not in subst2 or cons_f33(m=subst2["i2.2"]):
                                                    pass
                                                    if 'i2.2' not in subst2 or cons_f34(m=subst2["i2.2"]):
                                                        pass
                                                        # State 2776
                                                        if len(subjects40) == 0:
                                                            pass
                                                            # State 2777
                                                            if len(subjects) == 0:
                                                                pass
                                                                # 27: (a + v*a)**m /; (cons_f2) and (cons_f3) and (cons_f35) and (cons_f33) and (cons_f34)
                                                                yield 27, subst2
                                            if len(subjects40) == 0:
                                                break
                                            tmp88.append(subjects40.popleft())
                                        subjects40.extendleft(reversed(tmp88))
                    if pattern_index == 13:
                        pass
                        if 'i2.2.0' not in subst1 or 'i2.2.1.1' not in subst1 or cons_f2(a=subst1["i2.2.0"], x=subst1["i2.2.1.1"]):
                            pass
                            if 'i2.2.1.0' not in subst1 or 'i2.2.1.1' not in subst1 or cons_f3(b=subst1["i2.2.1.0"], x=subst1["i2.2.1.1"]):
                                pass
                                if 'i2.2.1.2' not in subst1 or 'i2.2.1.1' not in subst1 or cons_f4(n=subst1["i2.2.1.2"], x=subst1["i2.2.1.1"]):
                                    pass
                                    if 'i2.2.0_1' not in subst1 or 'i2.2.1.1' not in subst1 or cons_f8(c=subst1["i2.2.0_1"], x=subst1["i2.2.1.1"]):
                                        pass
                                        if 'i2.2.1.0_1' not in subst1 or 'i2.2.1.1' not in subst1 or cons_f29(d=subst1["i2.2.1.0_1"], x=subst1["i2.2.1.1"]):
                                            pass
                                            if 'i2.2' not in subst1 or 'i2.2.1.1' not in subst1 or cons_f19(m=subst1["i2.2"], x=subst1["i2.2.1.1"]):
                                                pass
                                                if 'i2.2.1.2' not in subst1 or 'i2.2.1.2_1' not in subst1 or cons_f39(n=subst1["i2.2.1.2"], q=subst1["i2.2.1.2_1"]):
                                                    pass
                                                    if 'i2.2.1.0_1' not in subst1 or 'i2.2.1.0' not in subst1 or 'i2.2.0' not in subst1 or 'i2.2.0_1' not in subst1 or cons_f41(a=subst1["i2.2.0"], b=subst1["i2.2.1.0"], c=subst1["i2.2.0_1"], d=subst1["i2.2.1.0_1"]):
                                                        pass
                                                        if 'i2.2.1.2' not in subst1 or 'i2.2' not in subst1 or cons_f42(m=subst1["i2.2"], n=subst1["i2.2.1.2"]):
                                                            pass
                                                            # State 2794
                                                            subst2 = Substitution(subst1)
                                                            try:
                                                                subst2.try_add_variable('i2.2', 1)
                                                            except ValueError:
                                                                pass
                                                            else:
                                                                pass
                                                                if 'i2.2' not in subst2 or 'i2.2.1.1' not in subst2 or cons_f19(m=subst2["i2.2"], x=subst2["i2.2.1.1"]):
                                                                    pass
                                                                    if 'i2.2.1.2' not in subst2 or 'i2.2' not in subst2 or cons_f42(m=subst2["i2.2"], n=subst2["i2.2.1.2"]):
                                                                        pass
                                                                        # State 2795
                                                                        if len(subjects40) == 0:
                                                                            pass
                                                                            # State 2796
                                                                            if len(subjects) == 0:
                                                                                pass
                                                                                # 29: (a + a*v**m)**p /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f19) and (cons_f4) and (cons_f39) and (cons_f41) and (cons_f42)
                                                                                yield 29, subst2
                                                            if len(subjects40) >= 1:
                                                                tmp92 = []
                                                                tmp92.append(subjects40.popleft())
                                                                while True:
                                                                    if len(tmp92) > 1:
                                                                        tmp93 = create_operation_expression(associative1, tmp92)
                                                                    elif len(tmp92) == 1:
                                                                        tmp93 = tmp92[0]
                                                                    else:
                                                                        assert False, "Unreachable"
                                                                    subst2 = Substitution(subst1)
                                                                    try:
                                                                        subst2.try_add_variable('i2.2', tmp93)
                                                                    except ValueError:
                                                                        pass
                                                                    else:
                                                                        pass
                                                                        if 'i2.2' not in subst2 or 'i2.2.1.1' not in subst2 or cons_f19(m=subst2["i2.2"], x=subst2["i2.2.1.1"]):
                                                                            pass
                                                                            if 'i2.2.1.2' not in subst2 or 'i2.2' not in subst2 or cons_f42(m=subst2["i2.2"], n=subst2["i2.2.1.2"]):
                                                                                pass
                                                                                # State 2795
                                                                                if len(subjects40) == 0:
                                                                                    pass
                                                                                    # State 2796
                                                                                    if len(subjects) == 0:
                                                                                        pass
                                                                                        # 29: (a + a*v**m)**p /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f19) and (cons_f4) and (cons_f39) and (cons_f41) and (cons_f42)
                                                                                        yield 29, subst2
                                                                    if len(subjects40) == 0:
                                                                        break
                                                                    tmp92.append(subjects40.popleft())
                                                                subjects40.extendleft(reversed(tmp92))
                    if pattern_index == 14:
                        pass
                        if 'i2.2.0' not in subst1 or 'i2.2.1.1' not in subst1 or cons_f2(a=subst1["i2.2.0"], x=subst1["i2.2.1.1"]):
                            pass
                            if 'i2.2.1.0' not in subst1 or 'i2.2.1.1' not in subst1 or cons_f3(b=subst1["i2.2.1.0"], x=subst1["i2.2.1.1"]):
                                pass
                                if 'i2.2.1.2' not in subst1 or 'i2.2.1.1' not in subst1 or cons_f4(n=subst1["i2.2.1.2"], x=subst1["i2.2.1.1"]):
                                    pass
                                    if 'i2.2.0_1' not in subst1 or 'i2.2.1.1' not in subst1 or cons_f8(c=subst1["i2.2.0_1"], x=subst1["i2.2.1.1"]):
                                        pass
                                        if 'i2.2.1.0_1' not in subst1 or 'i2.2.1.1' not in subst1 or cons_f29(d=subst1["i2.2.1.0_1"], x=subst1["i2.2.1.1"]):
                                            pass
                                            if 'i2.2' not in subst1 or 'i2.2.1.1' not in subst1 or cons_f19(m=subst1["i2.2"], x=subst1["i2.2.1.1"]):
                                                pass
                                                if 'i2.2.1.2' not in subst1 or 'i2.2.1.2_1' not in subst1 or cons_f39(n=subst1["i2.2.1.2"], q=subst1["i2.2.1.2_1"]):
                                                    pass
                                                    if 'i2.2.1.0_1' not in subst1 or 'i2.2.1.0' not in subst1 or 'i2.2.0' not in subst1 or 'i2.2.0_1' not in subst1 or cons_f41(a=subst1["i2.2.0"], b=subst1["i2.2.1.0"], c=subst1["i2.2.0_1"], d=subst1["i2.2.1.0_1"]):
                                                        pass
                                                        # State 2813
                                                        subst2 = Substitution(subst1)
                                                        try:
                                                            subst2.try_add_variable('i2.2_1', 1)
                                                        except ValueError:
                                                            pass
                                                        else:
                                                            pass
                                                            if 'i2.2_1' not in subst2 or cons_f40(p=subst2["i2.2_1"]):
                                                                pass
                                                                # State 2814
                                                                if len(subjects40) == 0:
                                                                    pass
                                                                    # State 2815
                                                                    if len(subjects) == 0:
                                                                        pass
                                                                        # 30: (c + b*v**n)**p /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f19) and (cons_f4) and (cons_f39) and (cons_f40) and (cons_f41)
                                                                        yield 30, subst2
                                                        if len(subjects40) >= 1:
                                                            tmp96 = []
                                                            tmp96.append(subjects40.popleft())
                                                            while True:
                                                                if len(tmp96) > 1:
                                                                    tmp97 = create_operation_expression(associative1, tmp96)
                                                                elif len(tmp96) == 1:
                                                                    tmp97 = tmp96[0]
                                                                else:
                                                                    assert False, "Unreachable"
                                                                subst2 = Substitution(subst1)
                                                                try:
                                                                    subst2.try_add_variable('i2.2_1', tmp97)
                                                                except ValueError:
                                                                    pass
                                                                else:
                                                                    pass
                                                                    if 'i2.2_1' not in subst2 or cons_f40(p=subst2["i2.2_1"]):
                                                                        pass
                                                                        # State 2814
                                                                        if len(subjects40) == 0:
                                                                            pass
                                                                            # State 2815
                                                                            if len(subjects) == 0:
                                                                                pass
                                                                                # 30: (c + b*v**n)**p /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f19) and (cons_f4) and (cons_f39) and (cons_f40) and (cons_f41)
                                                                                yield 30, subst2
                                                                if len(subjects40) == 0:
                                                                    break
                                                                tmp96.append(subjects40.popleft())
                                                            subjects40.extendleft(reversed(tmp96))
                    if pattern_index == 15:
                        pass
                        if 'i2.2' not in subst1 or 'i2.2.1.1' not in subst1 or cons_f5(p=subst1["i2.2"], x=subst1["i2.2.1.1"]):
                            pass
                            if 'i2.2.1.0_1' not in subst1 or 'i2.2.1.1' not in subst1 or cons_f3(b=subst1["i2.2.1.0_1"], x=subst1["i2.2.1.1"]):
                                pass
                                if 'i2.2.1.2_1' not in subst1 or 'i2.2.1.1' not in subst1 or cons_f4(n=subst1["i2.2.1.2_1"], x=subst1["i2.2.1.1"]):
                                    pass
                                    if 'i2.2.1.2' not in subst1 or 'i2.2.1.2_1' not in subst1 or cons_f7(j=subst1["i2.2.1.2"], n=subst1["i2.2.1.2_1"]):
                                        pass
                                        if 'i2.2.0_1' not in subst1 or 'i2.2.1.1' not in subst1 or cons_f2(a=subst1["i2.2.0_1"], x=subst1["i2.2.1.1"]):
                                            pass
                                            if 'i2.2.0' not in subst1 or 'i2.2.1.1' not in subst1 or cons_f8(c=subst1["i2.2.0"], x=subst1["i2.2.1.1"]):
                                                pass
                                                if 'i2.2.1.0' not in subst1 or 'i2.2.1.1' not in subst1 or cons_f29(d=subst1["i2.2.1.0"], x=subst1["i2.2.1.1"]):
                                                    pass
                                                    if 'i2.2_1' not in subst1 or 'i2.2.1.1' not in subst1 or cons_f19(m=subst1["i2.2_1"], x=subst1["i2.2.1.1"]):
                                                        pass
                                                        if 'i2.2.0' not in subst1 or 'i2.2.0_1' not in subst1 or 'i2.2.1.0_1' not in subst1 or 'i2.2.1.0' not in subst1 or cons_f44(a=subst1["i2.2.0_1"], b=subst1["i2.2.1.0_1"], c=subst1["i2.2.0"], d=subst1["i2.2.1.0"]):
                                                            pass
                                                            if 'i2.2.0_1' not in subst1 or cons_f45(a=subst1["i2.2.0_1"]):
                                                                pass
                                                                # State 2822
                                                                subst2 = Substitution(subst1)
                                                                try:
                                                                    subst2.try_add_variable('i2.2_1', 1)
                                                                except ValueError:
                                                                    pass
                                                                else:
                                                                    pass
                                                                    if 'i2.2_1' not in subst2 or 'i2.2.1.1' not in subst2 or cons_f19(m=subst2["i2.2_1"], x=subst2["i2.2.1.1"]):
                                                                        pass
                                                                        if 'i2.2_1' not in subst2 or 'i2.2' not in subst2 or cons_f43(m=subst2["i2.2_1"], p=subst2["i2.2"]):
                                                                            pass
                                                                            # State 2823
                                                                            if len(subjects40) == 0:
                                                                                pass
                                                                                # State 2824
                                                                                if len(subjects) == 0:
                                                                                    pass
                                                                                    # 31: (c + b*v**n)**p /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f19) and (cons_f4) and (cons_f5) and (cons_f7) and (cons_f43) and (cons_f44) and (cons_f45)
                                                                                    yield 31, subst2
                                                                if len(subjects40) >= 1:
                                                                    tmp100 = []
                                                                    tmp100.append(subjects40.popleft())
                                                                    while True:
                                                                        if len(tmp100) > 1:
                                                                            tmp101 = create_operation_expression(associative1, tmp100)
                                                                        elif len(tmp100) == 1:
                                                                            tmp101 = tmp100[0]
                                                                        else:
                                                                            assert False, "Unreachable"
                                                                        subst2 = Substitution(subst1)
                                                                        try:
                                                                            subst2.try_add_variable('i2.2_1', tmp101)
                                                                        except ValueError:
                                                                            pass
                                                                        else:
                                                                            pass
                                                                            if 'i2.2_1' not in subst2 or 'i2.2.1.1' not in subst2 or cons_f19(m=subst2["i2.2_1"], x=subst2["i2.2.1.1"]):
                                                                                pass
                                                                                if 'i2.2_1' not in subst2 or 'i2.2' not in subst2 or cons_f43(m=subst2["i2.2_1"], p=subst2["i2.2"]):
                                                                                    pass
                                                                                    # State 2823
                                                                                    if len(subjects40) == 0:
                                                                                        pass
                                                                                        # State 2824
                                                                                        if len(subjects) == 0:
                                                                                            pass
                                                                                            # 31: (c + b*v**n)**p /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f19) and (cons_f4) and (cons_f5) and (cons_f7) and (cons_f43) and (cons_f44) and (cons_f45)
                                                                                            yield 31, subst2
                                                                        if len(subjects40) == 0:
                                                                            break
                                                                        tmp100.append(subjects40.popleft())
                                                                    subjects40.extendleft(reversed(tmp100))
                    if pattern_index == 16:
                        pass
                        if 'i2.2' not in subst1 or 'i2.2.1.1' not in subst1 or cons_f5(p=subst1["i2.2"], x=subst1["i2.2.1.1"]):
                            pass
                            if 'i2.2.1.0_1' not in subst1 or 'i2.2.1.1' not in subst1 or cons_f3(b=subst1["i2.2.1.0_1"], x=subst1["i2.2.1.1"]):
                                pass
                                if 'i2.2.1.2_1' not in subst1 or 'i2.2.1.1' not in subst1 or cons_f4(n=subst1["i2.2.1.2_1"], x=subst1["i2.2.1.1"]):
                                    pass
                                    if 'i2.2.1.2' not in subst1 or 'i2.2.1.2_1' not in subst1 or cons_f7(j=subst1["i2.2.1.2"], n=subst1["i2.2.1.2_1"]):
                                        pass
                                        if 'i2.2.0_1' not in subst1 or 'i2.2.1.1' not in subst1 or cons_f2(a=subst1["i2.2.0_1"], x=subst1["i2.2.1.1"]):
                                            pass
                                            if 'i2.2.0' not in subst1 or 'i2.2.1.1' not in subst1 or cons_f8(c=subst1["i2.2.0"], x=subst1["i2.2.1.1"]):
                                                pass
                                                if 'i2.2.1.0' not in subst1 or 'i2.2.1.1' not in subst1 or cons_f29(d=subst1["i2.2.1.0"], x=subst1["i2.2.1.1"]):
                                                    pass
                                                    if 'i2.2_1' not in subst1 or 'i2.2.1.1' not in subst1 or cons_f19(m=subst1["i2.2_1"], x=subst1["i2.2.1.1"]):
                                                        pass
                                                        if 'i2.2.0' not in subst1 or 'i2.2.0_1' not in subst1 or 'i2.2.1.0_1' not in subst1 or 'i2.2.1.0' not in subst1 or cons_f44(a=subst1["i2.2.0_1"], b=subst1["i2.2.1.0_1"], c=subst1["i2.2.0"], d=subst1["i2.2.1.0"]):
                                                            pass
                                                            if 'i2.2.1.0' not in subst1 or cons_f46(d=subst1["i2.2.1.0"]):
                                                                pass
                                                                # State 2836
                                                                subst2 = Substitution(subst1)
                                                                try:
                                                                    subst2.try_add_variable('i2.2', 1)
                                                                except ValueError:
                                                                    pass
                                                                else:
                                                                    pass
                                                                    if 'i2.2' not in subst2 or 'i2.2.1.1' not in subst2 or cons_f5(p=subst2["i2.2"], x=subst2["i2.2.1.1"]):
                                                                        pass
                                                                        if 'i2.2_1' not in subst2 or 'i2.2' not in subst2 or cons_f43(m=subst2["i2.2_1"], p=subst2["i2.2"]):
                                                                            pass
                                                                            # State 2837
                                                                            if len(subjects40) == 0:
                                                                                pass
                                                                                # State 2838
                                                                                if len(subjects) == 0:
                                                                                    pass
                                                                                    # 32: (c + d*x**j)**p /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f19) and (cons_f4) and (cons_f5) and (cons_f7) and (cons_f43) and (cons_f44) and (cons_f46)
                                                                                    yield 32, subst2
                                                                if len(subjects40) >= 1:
                                                                    tmp104 = []
                                                                    tmp104.append(subjects40.popleft())
                                                                    while True:
                                                                        if len(tmp104) > 1:
                                                                            tmp105 = create_operation_expression(associative1, tmp104)
                                                                        elif len(tmp104) == 1:
                                                                            tmp105 = tmp104[0]
                                                                        else:
                                                                            assert False, "Unreachable"
                                                                        subst2 = Substitution(subst1)
                                                                        try:
                                                                            subst2.try_add_variable('i2.2', tmp105)
                                                                        except ValueError:
                                                                            pass
                                                                        else:
                                                                            pass
                                                                            if 'i2.2' not in subst2 or 'i2.2.1.1' not in subst2 or cons_f5(p=subst2["i2.2"], x=subst2["i2.2.1.1"]):
                                                                                pass
                                                                                if 'i2.2_1' not in subst2 or 'i2.2' not in subst2 or cons_f43(m=subst2["i2.2_1"], p=subst2["i2.2"]):
                                                                                    pass
                                                                                    # State 2837
                                                                                    if len(subjects40) == 0:
                                                                                        pass
                                                                                        # State 2838
                                                                                        if len(subjects) == 0:
                                                                                            pass
                                                                                            # 32: (c + d*x**j)**p /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f19) and (cons_f4) and (cons_f5) and (cons_f7) and (cons_f43) and (cons_f44) and (cons_f46)
                                                                                            yield 32, subst2
                                                                        if len(subjects40) == 0:
                                                                            break
                                                                        tmp104.append(subjects40.popleft())
                                                                    subjects40.extendleft(reversed(tmp104))
                    if pattern_index == 17:
                        pass
                        if 'i2.2.0' not in subst1 or 'i2.2.1.1' not in subst1 or cons_f2(a=subst1["i2.2.0"], x=subst1["i2.2.1.1"]):
                            pass
                            if 'i2.2.1.0_1' not in subst1 or 'i2.2.1.1' not in subst1 or cons_f3(b=subst1["i2.2.1.0_1"], x=subst1["i2.2.1.1"]):
                                pass
                                if 'i2.2.1.0' not in subst1 or 'i2.2.1.1' not in subst1 or cons_f8(c=subst1["i2.2.1.0"], x=subst1["i2.2.1.1"]):
                                    pass
                                    if 'i2.2.1.0' not in subst1 or 'i2.2.1.0_1' not in subst1 or 'i2.2.0' not in subst1 or cons_f47(a=subst1["i2.2.0"], b=subst1["i2.2.1.0_1"], c=subst1["i2.2.1.0"]):
                                        pass
                                        # State 2879
                                        subst2 = Substitution(subst1)
                                        try:
                                            subst2.try_add_variable('i2.2', 1)
                                        except ValueError:
                                            pass
                                        else:
                                            pass
                                            if 'i2.2' not in subst2 or cons_f40(p=subst2["i2.2"]):
                                                pass
                                                # State 2880
                                                if len(subjects40) == 0:
                                                    pass
                                                    # State 2881
                                                    if len(subjects) == 0:
                                                        pass
                                                        # 33: (a + b*x + c*x**2)**p /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f47) and (cons_f40)
                                                        yield 33, subst2
                                        if len(subjects40) >= 1:
                                            tmp108 = []
                                            tmp108.append(subjects40.popleft())
                                            while True:
                                                if len(tmp108) > 1:
                                                    tmp109 = create_operation_expression(associative1, tmp108)
                                                elif len(tmp108) == 1:
                                                    tmp109 = tmp108[0]
                                                else:
                                                    assert False, "Unreachable"
                                                subst2 = Substitution(subst1)
                                                try:
                                                    subst2.try_add_variable('i2.2', tmp109)
                                                except ValueError:
                                                    pass
                                                else:
                                                    pass
                                                    if 'i2.2' not in subst2 or cons_f40(p=subst2["i2.2"]):
                                                        pass
                                                        # State 2880
                                                        if len(subjects40) == 0:
                                                            pass
                                                            # State 2881
                                                            if len(subjects) == 0:
                                                                pass
                                                                # 33: (a + b*x + c*x**2)**p /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f47) and (cons_f40)
                                                                yield 33, subst2
                                                if len(subjects40) == 0:
                                                    break
                                                tmp108.append(subjects40.popleft())
                                            subjects40.extendleft(reversed(tmp108))
                    if pattern_index == 18:
                        pass
                        if 'i2.2.0' not in subst1 or 'i2.2.1.1' not in subst1 or cons_f2(a=subst1["i2.2.0"], x=subst1["i2.2.1.1"]):
                            pass
                            if 'i2.2.1.0' not in subst1 or 'i2.2.1.1' not in subst1 or cons_f3(b=subst1["i2.2.1.0"], x=subst1["i2.2.1.1"]):
                                pass
                                if 'i2.2.1.2' not in subst1 or 'i2.2.1.1' not in subst1 or cons_f4(n=subst1["i2.2.1.2"], x=subst1["i2.2.1.1"]):
                                    pass
                                    if 'i2.2.1.0_1' not in subst1 or 'i2.2.1.1' not in subst1 or cons_f8(c=subst1["i2.2.1.0_1"], x=subst1["i2.2.1.1"]):
                                        pass
                                        if 'i2.2.1.2' not in subst1 or 'i2.2.1.2_1' not in subst1 or cons_f48(n=subst1["i2.2.1.2"], n2=subst1["i2.2.1.2_1"]):
                                            pass
                                            if 'i2.2.1.0_1' not in subst1 or 'i2.2.1.0' not in subst1 or 'i2.2.0' not in subst1 or cons_f47(a=subst1["i2.2.0"], b=subst1["i2.2.1.0"], c=subst1["i2.2.1.0_1"]):
                                                pass
                                                # State 2910
                                                subst2 = Substitution(subst1)
                                                try:
                                                    subst2.try_add_variable('i2.2', 1)
                                                except ValueError:
                                                    pass
                                                else:
                                                    pass
                                                    if 'i2.2' not in subst2 or cons_f40(p=subst2["i2.2"]):
                                                        pass
                                                        # State 2911
                                                        if len(subjects40) == 0:
                                                            pass
                                                            # State 2912
                                                            if len(subjects) == 0:
                                                                pass
                                                                # 34: (a + b*v**n + d*x**j)**p /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f4) and (cons_f48) and (cons_f47) and (cons_f40)
                                                                yield 34, subst2
                                                if len(subjects40) >= 1:
                                                    tmp112 = []
                                                    tmp112.append(subjects40.popleft())
                                                    while True:
                                                        if len(tmp112) > 1:
                                                            tmp113 = create_operation_expression(associative1, tmp112)
                                                        elif len(tmp112) == 1:
                                                            tmp113 = tmp112[0]
                                                        else:
                                                            assert False, "Unreachable"
                                                        subst2 = Substitution(subst1)
                                                        try:
                                                            subst2.try_add_variable('i2.2', tmp113)
                                                        except ValueError:
                                                            pass
                                                        else:
                                                            pass
                                                            if 'i2.2' not in subst2 or cons_f40(p=subst2["i2.2"]):
                                                                pass
                                                                # State 2911
                                                                if len(subjects40) == 0:
                                                                    pass
                                                                    # State 2912
                                                                    if len(subjects) == 0:
                                                                        pass
                                                                        # 34: (a + b*v**n + d*x**j)**p /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f4) and (cons_f48) and (cons_f47) and (cons_f40)
                                                                        yield 34, subst2
                                                        if len(subjects40) == 0:
                                                            break
                                                        tmp112.append(subjects40.popleft())
                                                    subjects40.extendleft(reversed(tmp112))
                    if pattern_index == 19:
                        pass
                        if 'i2.2.0' not in subst1 or 'i2.2.1.1' not in subst1 or cons_f2(a=subst1["i2.2.0"], x=subst1["i2.2.1.1"]):
                            pass
                            if 'i2.2' not in subst1 or 'i2.2.1.1' not in subst1 or cons_f5(p=subst1["i2.2"], x=subst1["i2.2.1.1"]):
                                pass
                                if 'i2.2.1.0_1' not in subst1 or 'i2.2.1.1' not in subst1 or cons_f3(b=subst1["i2.2.1.0_1"], x=subst1["i2.2.1.1"]):
                                    pass
                                    if 'i2.2.1.0' not in subst1 or 'i2.2.1.1' not in subst1 or cons_f8(c=subst1["i2.2.1.0"], x=subst1["i2.2.1.1"]):
                                        pass
                                        if 'i2.1.0' not in subst1 or 'i2.2.1.1' not in subst1 or cons_f29(d=subst1["i2.1.0"], x=subst1["i2.2.1.1"]):
                                            pass
                                            if 'i2.1.1.0' not in subst1 or 'i2.2.1.1' not in subst1 or cons_f50(e=subst1["i2.1.1.0"], x=subst1["i2.2.1.1"]):
                                                pass
                                                if 'i2.2.1.0' not in subst1 or 'i2.2.1.0_1' not in subst1 or 'i2.1.0' not in subst1 or 'i2.1.1.0' not in subst1 or cons_f49(b=subst1["i2.2.1.0_1"], c=subst1["i2.2.1.0"], d=subst1["i2.1.0"], e=subst1["i2.1.1.0"]):
                                                    pass
                                                    # State 2919
                                                    subst2 = Substitution(subst1)
                                                    try:
                                                        subst2.try_add_variable('i2.2', 1)
                                                    except ValueError:
                                                        pass
                                                    else:
                                                        pass
                                                        if 'i2.2' not in subst2 or 'i2.2.1.1' not in subst2 or cons_f5(p=subst2["i2.2"], x=subst2["i2.2.1.1"]):
                                                            pass
                                                            # State 2920
                                                            if len(subjects40) == 0:
                                                                pass
                                                                # State 2921
                                                                if len(subjects) == 0:
                                                                    pass
                                                                    # 35: (a + b*x + c*x**2)**p /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f50) and (cons_f5) and (cons_f49)
                                                                    yield 35, subst2
                                                    if len(subjects40) >= 1:
                                                        tmp116 = []
                                                        tmp116.append(subjects40.popleft())
                                                        while True:
                                                            if len(tmp116) > 1:
                                                                tmp117 = create_operation_expression(associative1, tmp116)
                                                            elif len(tmp116) == 1:
                                                                tmp117 = tmp116[0]
                                                            else:
                                                                assert False, "Unreachable"
                                                            subst2 = Substitution(subst1)
                                                            try:
                                                                subst2.try_add_variable('i2.2', tmp117)
                                                            except ValueError:
                                                                pass
                                                            else:
                                                                pass
                                                                if 'i2.2' not in subst2 or 'i2.2.1.1' not in subst2 or cons_f5(p=subst2["i2.2"], x=subst2["i2.2.1.1"]):
                                                                    pass
                                                                    # State 2920
                                                                    if len(subjects40) == 0:
                                                                        pass
                                                                        # State 2921
                                                                        if len(subjects) == 0:
                                                                            pass
                                                                            # 35: (a + b*x + c*x**2)**p /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f50) and (cons_f5) and (cons_f49)
                                                                            yield 35, subst2
                                                            if len(subjects40) == 0:
                                                                break
                                                            tmp116.append(subjects40.popleft())
                                                        subjects40.extendleft(reversed(tmp116))
                    if pattern_index == 20:
                        pass
                        if 'i2.2.1.0_1' not in subst1 or 'i2.2.1.1' not in subst1 or cons_f3(b=subst1["i2.2.1.0_1"], x=subst1["i2.2.1.1"]):
                            pass
                            if 'i2.2.1.0' not in subst1 or 'i2.2.1.1' not in subst1 or cons_f2(a=subst1["i2.2.1.0"], x=subst1["i2.2.1.1"]):
                                pass
                                if 'i2.2.1.2' not in subst1 or 'i2.2.1.1' not in subst1 or cons_f5(p=subst1["i2.2.1.2"], x=subst1["i2.2.1.1"]):
                                    pass
                                    if 'i2.2.1.2_1' not in subst1 or 'i2.2.1.1' not in subst1 or cons_f52(q=subst1["i2.2.1.2_1"], x=subst1["i2.2.1.1"]):
                                        pass
                                        if 'i2.2.1.2' not in subst1 or 'i2.2.1.2_1' not in subst1 or cons_f51(p=subst1["i2.2.1.2"], q=subst1["i2.2.1.2_1"]):
                                            pass
                                            # State 2945
                                            subst2 = Substitution(subst1)
                                            try:
                                                subst2.try_add_variable('i2.2', 1)
                                            except ValueError:
                                                pass
                                            else:
                                                pass
                                                if 'i2.2' not in subst2 or cons_f20(m=subst2["i2.2"]):
                                                    pass
                                                    # State 2946
                                                    if len(subjects40) == 0:
                                                        pass
                                                        # State 2947
                                                        if len(subjects) == 0:
                                                            pass
                                                            # 37: (b*v**n + a*v**m)**m /; (cons_f2) and (cons_f3) and (cons_f5) and (cons_f52) and (cons_f20) and (cons_f51)
                                                            yield 37, subst2
                                            if len(subjects40) >= 1:
                                                tmp120 = []
                                                tmp120.append(subjects40.popleft())
                                                while True:
                                                    if len(tmp120) > 1:
                                                        tmp121 = create_operation_expression(associative1, tmp120)
                                                    elif len(tmp120) == 1:
                                                        tmp121 = tmp120[0]
                                                    else:
                                                        assert False, "Unreachable"
                                                    subst2 = Substitution(subst1)
                                                    try:
                                                        subst2.try_add_variable('i2.2', tmp121)
                                                    except ValueError:
                                                        pass
                                                    else:
                                                        pass
                                                        if 'i2.2' not in subst2 or cons_f20(m=subst2["i2.2"]):
                                                            pass
                                                            # State 2946
                                                            if len(subjects40) == 0:
                                                                pass
                                                                # State 2947
                                                                if len(subjects) == 0:
                                                                    pass
                                                                    # 37: (b*v**n + a*v**m)**m /; (cons_f2) and (cons_f3) and (cons_f5) and (cons_f52) and (cons_f20) and (cons_f51)
                                                                    yield 37, subst2
                                                    if len(subjects40) == 0:
                                                        break
                                                    tmp120.append(subjects40.popleft())
                                                subjects40.extendleft(reversed(tmp120))
                    if pattern_index == 21:
                        pass
                        if 'i2.2.1.0_1' not in subst1 or 'i2.2.1.1' not in subst1 or cons_f3(b=subst1["i2.2.1.0_1"], x=subst1["i2.2.1.1"]):
                            pass
                            if 'i2.2.1.0' not in subst1 or 'i2.2.1.1' not in subst1 or cons_f2(a=subst1["i2.2.1.0"], x=subst1["i2.2.1.1"]):
                                pass
                                if 'i2.2.1.2' not in subst1 or 'i2.2.1.1' not in subst1 or cons_f5(p=subst1["i2.2.1.2"], x=subst1["i2.2.1.1"]):
                                    pass
                                    if 'i2.2.1.2_1' not in subst1 or 'i2.2.1.1' not in subst1 or cons_f52(q=subst1["i2.2.1.2_1"], x=subst1["i2.2.1.1"]):
                                        pass
                                        if 'i2.2.1.2' not in subst1 or 'i2.2.1.2_1' not in subst1 or cons_f51(p=subst1["i2.2.1.2"], q=subst1["i2.2.1.2_1"]):
                                            pass
                                            if 'i2.2.1.0_2' not in subst1 or 'i2.2.1.1' not in subst1 or cons_f8(c=subst1["i2.2.1.0_2"], x=subst1["i2.2.1.1"]):
                                                pass
                                                if 'i2.2.1.2_2' not in subst1 or 'i2.2.1.1' not in subst1 or cons_f54(r=subst1["i2.2.1.2_2"], x=subst1["i2.2.1.1"]):
                                                    pass
                                                    if 'i2.2.1.2' not in subst1 or 'i2.2.1.2_2' not in subst1 or cons_f53(p=subst1["i2.2.1.2"], r=subst1["i2.2.1.2_2"]):
                                                        pass
                                                        # State 3012
                                                        subst2 = Substitution(subst1)
                                                        try:
                                                            subst2.try_add_variable('i2.2', 1)
                                                        except ValueError:
                                                            pass
                                                        else:
                                                            pass
                                                            if 'i2.2' not in subst2 or cons_f20(m=subst2["i2.2"]):
                                                                pass
                                                                # State 3013
                                                                if len(subjects40) == 0:
                                                                    pass
                                                                    # State 3014
                                                                    if len(subjects) == 0:
                                                                        pass
                                                                        # 38: (b*v**n + c*x**r + a*v**m)**m /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f5) and (cons_f52) and (cons_f54) and (cons_f20) and (cons_f51) and (cons_f53)
                                                                        yield 38, subst2
                                                        if len(subjects40) >= 1:
                                                            tmp124 = []
                                                            tmp124.append(subjects40.popleft())
                                                            while True:
                                                                if len(tmp124) > 1:
                                                                    tmp125 = create_operation_expression(associative1, tmp124)
                                                                elif len(tmp124) == 1:
                                                                    tmp125 = tmp124[0]
                                                                else:
                                                                    assert False, "Unreachable"
                                                                subst2 = Substitution(subst1)
                                                                try:
                                                                    subst2.try_add_variable('i2.2', tmp125)
                                                                except ValueError:
                                                                    pass
                                                                else:
                                                                    pass
                                                                    if 'i2.2' not in subst2 or cons_f20(m=subst2["i2.2"]):
                                                                        pass
                                                                        # State 3013
                                                                        if len(subjects40) == 0:
                                                                            pass
                                                                            # State 3014
                                                                            if len(subjects) == 0:
                                                                                pass
                                                                                # 38: (b*v**n + c*x**r + a*v**m)**m /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f5) and (cons_f52) and (cons_f54) and (cons_f20) and (cons_f51) and (cons_f53)
                                                                                yield 38, subst2
                                                                if len(subjects40) == 0:
                                                                    break
                                                                tmp124.append(subjects40.popleft())
                                                            subjects40.extendleft(reversed(tmp124))
                    if pattern_index == 22:
                        pass
                        if 'i2.2.0' not in subst1 or 'i2.2.1.1' not in subst1 or cons_f2(a=subst1["i2.2.0"], x=subst1["i2.2.1.1"]):
                            pass
                            if 'i2.2.1.0' not in subst1 or 'i2.2.1.1' not in subst1 or cons_f3(b=subst1["i2.2.1.0"], x=subst1["i2.2.1.1"]):
                                pass
                                if 'i2.2.1.2' not in subst1 or 'i2.2.1.1' not in subst1 or cons_f4(n=subst1["i2.2.1.2"], x=subst1["i2.2.1.1"]):
                                    pass
                                    if 'i2.2' not in subst1 or 'i2.2.1.1' not in subst1 or cons_f19(m=subst1["i2.2"], x=subst1["i2.2.1.1"]):
                                        pass
                                        if 'i2.2.1.2' not in subst1 or 'i2.2' not in subst1 or cons_f55(m=subst1["i2.2"], n=subst1["i2.2.1.2"]):
                                            pass
                                            # State 3019
                                            if len(subjects40) >= 1 and subjects40[0] == Integer(-1):
                                                tmp127 = subjects40.popleft()
                                                # State 3020
                                                if len(subjects40) == 0:
                                                    pass
                                                    # State 3021
                                                    if len(subjects) == 0:
                                                        pass
                                                        # 39: 1/(c + d*x**j) /; (cons_f2) and (cons_f3) and (cons_f19) and (cons_f4) and (cons_f55)
                                                        yield 39, subst1
                                                subjects40.appendleft(tmp127)
                    if pattern_index == 23:
                        pass
                        if 'i2.2.0' not in subst1 or 'i2.2.1.1' not in subst1 or cons_f2(a=subst1["i2.2.0"], x=subst1["i2.2.1.1"]):
                            pass
                            if 'i2.2.1.0' not in subst1 or 'i2.2.1.1' not in subst1 or cons_f3(b=subst1["i2.2.1.0"], x=subst1["i2.2.1.1"]):
                                pass
                                if 'i2.2.1.2' not in subst1 or 'i2.2.1.1' not in subst1 or cons_f4(n=subst1["i2.2.1.2"], x=subst1["i2.2.1.1"]):
                                    pass
                                    if 'i2.2' not in subst1 or 'i2.2.1.1' not in subst1 or cons_f5(p=subst1["i2.2"], x=subst1["i2.2.1.1"]):
                                        pass
                                        if 'i2.2_1' not in subst1 or 'i2.2.1.1' not in subst1 or cons_f19(m=subst1["i2.2_1"], x=subst1["i2.2.1.1"]):
                                            pass
                                            if 'i2.2.1.2' not in subst1 or 'i2.2_1' not in subst1 or cons_f55(m=subst1["i2.2_1"], n=subst1["i2.2.1.2"]):
                                                pass
                                                # State 3030
                                                if len(subjects40) >= 1:
                                                    tmp128 = []
                                                    tmp128.append(subjects40.popleft())
                                                    while True:
                                                        if len(tmp128) > 1:
                                                            tmp129 = create_operation_expression(associative1, tmp128)
                                                        elif len(tmp128) == 1:
                                                            tmp129 = tmp128[0]
                                                        else:
                                                            assert False, "Unreachable"
                                                        subst2 = Substitution(subst1)
                                                        try:
                                                            subst2.try_add_variable('i2.2', tmp129)
                                                        except ValueError:
                                                            pass
                                                        else:
                                                            pass
                                                            if 'i2.2' not in subst2 or 'i2.2.1.1' not in subst2 or cons_f5(p=subst2["i2.2"], x=subst2["i2.2.1.1"]):
                                                                pass
                                                                if 'i2.2' not in subst2 or cons_f56(p=subst2["i2.2"]):
                                                                    pass
                                                                    # State 3031
                                                                    if len(subjects40) == 0:
                                                                        pass
                                                                        # State 3032
                                                                        if len(subjects) == 0:
                                                                            pass
                                                                            # 41: (c + d*x**j)**p /; (cons_f2) and (cons_f3) and (cons_f19) and (cons_f4) and (cons_f5) and (cons_f55) and (cons_f56)
                                                                            yield 41, subst2
                                                        if len(subjects40) == 0:
                                                            break
                                                        tmp128.append(subjects40.popleft())
                                                    subjects40.extendleft(reversed(tmp128))
                    if pattern_index == 24:
                        pass
                        if 'i2.2.1.2' not in subst1 or 'i2.2.1.1' not in subst1 or cons_f4(n=subst1["i2.2.1.2"], x=subst1["i2.2.1.1"]):
                            pass
                            if 'i2.2' not in subst1 or 'i2.2.1.1' not in subst1 or cons_f5(p=subst1["i2.2"], x=subst1["i2.2.1.1"]):
                                pass
                                if 'i2.2_1' not in subst1 or 'i2.2.1.1' not in subst1 or cons_f19(m=subst1["i2.2_1"], x=subst1["i2.2.1.1"]):
                                    pass
                                    if 'i2.2.0' not in subst1 or 'i2.2.1.1' not in subst1 or cons_f59(a1=subst1["i2.2.0"], x=subst1["i2.2.1.1"]):
                                        pass
                                        if 'i2.2.1.0' not in subst1 or 'i2.2.1.1' not in subst1 or cons_f60(b1=subst1["i2.2.1.0"], x=subst1["i2.2.1.1"]):
                                            pass
                                            if 'i2.2.0_1' not in subst1 or 'i2.2.1.1' not in subst1 or cons_f61(a2=subst1["i2.2.0_1"], x=subst1["i2.2.1.1"]):
                                                pass
                                                if 'i2.2.1.0_1' not in subst1 or 'i2.2.1.1' not in subst1 or cons_f62(b2=subst1["i2.2.1.0_1"], x=subst1["i2.2.1.1"]):
                                                    pass
                                                    if 'i2.2.1.0_1' not in subst1 or 'i2.2.1.0' not in subst1 or 'i2.2.0_1' not in subst1 or 'i2.2.0' not in subst1 or cons_f57(a1=subst1["i2.2.0"], a2=subst1["i2.2.0_1"], b1=subst1["i2.2.1.0"], b2=subst1["i2.2.1.0_1"]):
                                                        pass
                                                        if 'i2.2.1.2' not in subst1 or 'i2.2_1' not in subst1 or cons_f58(m=subst1["i2.2_1"], n=subst1["i2.2.1.2"]):
                                                            pass
                                                            # State 3040
                                                            if len(subjects40) >= 1:
                                                                tmp131 = []
                                                                tmp131.append(subjects40.popleft())
                                                                while True:
                                                                    if len(tmp131) > 1:
                                                                        tmp132 = create_operation_expression(associative1, tmp131)
                                                                    elif len(tmp131) == 1:
                                                                        tmp132 = tmp131[0]
                                                                    else:
                                                                        assert False, "Unreachable"
                                                                    subst2 = Substitution(subst1)
                                                                    try:
                                                                        subst2.try_add_variable('i2.2', tmp132)
                                                                    except ValueError:
                                                                        pass
                                                                    else:
                                                                        pass
                                                                        if 'i2.2' not in subst2 or 'i2.2.1.1' not in subst2 or cons_f5(p=subst2["i2.2"], x=subst2["i2.2.1.1"]):
                                                                            pass
                                                                            if 'i2.2' not in subst2 or cons_f56(p=subst2["i2.2"]):
                                                                                pass
                                                                                # State 3041
                                                                                if len(subjects40) == 0:
                                                                                    pass
                                                                                    # State 3042
                                                                                    if len(subjects) == 0:
                                                                                        pass
                                                                                        # 43: (a + a*v**m)**p /; (cons_f59) and (cons_f60) and (cons_f61) and (cons_f62) and (cons_f19) and (cons_f4) and (cons_f5) and (cons_f57) and (cons_f58) and (cons_f56)
                                                                                        yield 43, subst2
                                                                    if len(subjects40) == 0:
                                                                        break
                                                                    tmp131.append(subjects40.popleft())
                                                                subjects40.extendleft(reversed(tmp131))
                    if pattern_index == 25:
                        pass
                        if 'i2.2.1.2' not in subst1 or 'i2.2.1.1' not in subst1 or cons_f4(n=subst1["i2.2.1.2"], x=subst1["i2.2.1.1"]):
                            pass
                            if 'i2.2' not in subst1 or 'i2.2.1.1' not in subst1 or cons_f5(p=subst1["i2.2"], x=subst1["i2.2.1.1"]):
                                pass
                                if 'i2.2_1' not in subst1 or 'i2.2.1.1' not in subst1 or cons_f19(m=subst1["i2.2_1"], x=subst1["i2.2.1.1"]):
                                    pass
                                    if 'i2.2.0' not in subst1 or 'i2.2.1.1' not in subst1 or cons_f59(a1=subst1["i2.2.0"], x=subst1["i2.2.1.1"]):
                                        pass
                                        if 'i2.2.1.0' not in subst1 or 'i2.2.1.1' not in subst1 or cons_f60(b1=subst1["i2.2.1.0"], x=subst1["i2.2.1.1"]):
                                            pass
                                            if 'i2.2.0_1' not in subst1 or 'i2.2.1.1' not in subst1 or cons_f61(a2=subst1["i2.2.0_1"], x=subst1["i2.2.1.1"]):
                                                pass
                                                if 'i2.2.1.0_1' not in subst1 or 'i2.2.1.1' not in subst1 or cons_f62(b2=subst1["i2.2.1.0_1"], x=subst1["i2.2.1.1"]):
                                                    pass
                                                    if 'i2.2.1.0_1' not in subst1 or 'i2.2.1.0' not in subst1 or 'i2.2.0_1' not in subst1 or 'i2.2.0' not in subst1 or cons_f57(a1=subst1["i2.2.0"], a2=subst1["i2.2.0_1"], b1=subst1["i2.2.1.0"], b2=subst1["i2.2.1.0_1"]):
                                                        pass
                                                        if 'i2.2.1.2' not in subst1 or 'i2.2_1' not in subst1 or cons_f58(m=subst1["i2.2_1"], n=subst1["i2.2.1.2"]):
                                                            pass
                                                            # State 3048
                                                            if len(subjects40) >= 1:
                                                                tmp134 = []
                                                                tmp134.append(subjects40.popleft())
                                                                while True:
                                                                    if len(tmp134) > 1:
                                                                        tmp135 = create_operation_expression(associative1, tmp134)
                                                                    elif len(tmp134) == 1:
                                                                        tmp135 = tmp134[0]
                                                                    else:
                                                                        assert False, "Unreachable"
                                                                    subst2 = Substitution(subst1)
                                                                    try:
                                                                        subst2.try_add_variable('i2.2', tmp135)
                                                                    except ValueError:
                                                                        pass
                                                                    else:
                                                                        pass
                                                                        if 'i2.2' not in subst2 or 'i2.2.1.1' not in subst2 or cons_f5(p=subst2["i2.2"], x=subst2["i2.2.1.1"]):
                                                                            pass
                                                                            if 'i2.2' not in subst2 or cons_f56(p=subst2["i2.2"]):
                                                                                pass
                                                                                # State 3049
                                                                                if len(subjects40) == 0:
                                                                                    pass
                                                                                    # State 3050
                                                                                    if len(subjects) == 0:
                                                                                        pass
                                                                                        # 44: (a2 + b2*v**m)**p /; (cons_f59) and (cons_f60) and (cons_f61) and (cons_f62) and (cons_f19) and (cons_f4) and (cons_f5) and (cons_f57) and (cons_f58) and (cons_f56)
                                                                                        yield 44, subst2
                                                                    if len(subjects40) == 0:
                                                                        break
                                                                    tmp134.append(subjects40.popleft())
                                                                subjects40.extendleft(reversed(tmp134))
                    if pattern_index == 26:
                        pass
                        if 'i2' not in subst1 or 'i2.2.0' not in subst1 or cons_f2(a=subst1["i2.2.0"], x=subst1["i2"]):
                            pass
                            if 'i2' not in subst1 or 'i2.2.1.0' not in subst1 or cons_f3(b=subst1["i2.2.1.0"], x=subst1["i2"]):
                                pass
                                if 'i2.2.1.2' not in subst1 or 'i2' not in subst1 or cons_f4(n=subst1["i2.2.1.2"], x=subst1["i2"]):
                                    pass
                                    if 'i2' not in subst1 or 'i2.2.1.1' not in subst1 or cons_f11(Pm=subst1["i2.2.1.1"], x=subst1["i2"]):
                                        pass
                                        if 'i2' not in subst1 or 'i2.2.1.1' not in subst1 or 'i2.2.1.0' not in subst1 or 'i2.2.0' not in subst1 or 'i2.0' not in subst1 or 'i2.2' not in subst1 or 'i2.2.1.2' not in subst1 or With35(Pm=subst1["i2.2.1.1"], Qm=subst1["i2.0"], a=subst1["i2.2.0"], b=subst1["i2.2.1.0"], n=subst1["i2.2.1.2"], p=subst1["i2.2"], x=subst1["i2"]):
                                            pass
                                            # State 3061
                                            subst2 = Substitution(subst1)
                                            try:
                                                subst2.try_add_variable('i2.2', 1)
                                            except ValueError:
                                                pass
                                            else:
                                                pass
                                                if 'i2' not in subst2 or 'i2.2' not in subst2 or cons_f5(p=subst2["i2.2"], x=subst2["i2"]):
                                                    pass
                                                    if 'i2' not in subst2 or 'i2.2.1.1' not in subst2 or 'i2.2.1.0' not in subst2 or 'i2.2.0' not in subst2 or 'i2.0' not in subst2 or 'i2.2' not in subst2 or 'i2.2.1.2' not in subst2 or With35(Pm=subst2["i2.2.1.1"], Qm=subst2["i2.0"], a=subst2["i2.2.0"], b=subst2["i2.2.1.0"], n=subst2["i2.2.1.2"], p=subst2["i2.2"], x=subst2["i2"]):
                                                        pass
                                                        # State 3062
                                                        if len(subjects40) == 0:
                                                            pass
                                                            # State 3063
                                                            if len(subjects) == 0:
                                                                pass
                                                                # 46: (a + a*v**m)**p /; (cons_f2) and (cons_f3) and (cons_f4) and (cons_f5) and (cons_f11) and (With35)
                                                                yield 46, subst2
                                            if len(subjects40) >= 1:
                                                tmp138 = []
                                                tmp138.append(subjects40.popleft())
                                                while True:
                                                    if len(tmp138) > 1:
                                                        tmp139 = create_operation_expression(associative1, tmp138)
                                                    elif len(tmp138) == 1:
                                                        tmp139 = tmp138[0]
                                                    else:
                                                        assert False, "Unreachable"
                                                    subst2 = Substitution(subst1)
                                                    try:
                                                        subst2.try_add_variable('i2.2', tmp139)
                                                    except ValueError:
                                                        pass
                                                    else:
                                                        pass
                                                        if 'i2' not in subst2 or 'i2.2' not in subst2 or cons_f5(p=subst2["i2.2"], x=subst2["i2"]):
                                                            pass
                                                            if 'i2' not in subst2 or 'i2.2.1.1' not in subst2 or 'i2.2.1.0' not in subst2 or 'i2.2.0' not in subst2 or 'i2.0' not in subst2 or 'i2.2' not in subst2 or 'i2.2.1.2' not in subst2 or With35(Pm=subst2["i2.2.1.1"], Qm=subst2["i2.0"], a=subst2["i2.2.0"], b=subst2["i2.2.1.0"], n=subst2["i2.2.1.2"], p=subst2["i2.2"], x=subst2["i2"]):
                                                                pass
                                                                # State 3062
                                                                if len(subjects40) == 0:
                                                                    pass
                                                                    # State 3063
                                                                    if len(subjects) == 0:
                                                                        pass
                                                                        # 46: (a + a*v**m)**p /; (cons_f2) and (cons_f3) and (cons_f4) and (cons_f5) and (cons_f11) and (With35)
                                                                        yield 46, subst2
                                                    if len(subjects40) == 0:
                                                        break
                                                    tmp138.append(subjects40.popleft())
                                                subjects40.extendleft(reversed(tmp138))
                    if pattern_index == 27:
                        pass
                        if 'i2' not in subst1 or 'i2.2.0' not in subst1 or cons_f2(a=subst1["i2.2.0"], x=subst1["i2"]):
                            pass
                            if 'i2.2.1.2' not in subst1 or 'i2.2.1.2_1' not in subst1 or cons_f48(n=subst1["i2.2.1.2"], n2=subst1["i2.2.1.2_1"]):
                                pass
                                if 'i2' not in subst1 or 'i2.2.1.0' not in subst1 or cons_f3(b=subst1["i2.2.1.0"], x=subst1["i2"]):
                                    pass
                                    if 'i2.2.1.2' not in subst1 or 'i2' not in subst1 or cons_f4(n=subst1["i2.2.1.2"], x=subst1["i2"]):
                                        pass
                                        if 'i2' not in subst1 or 'i2.2.1.1' not in subst1 or cons_f11(Pm=subst1["i2.2.1.1"], x=subst1["i2"]):
                                            pass
                                            if 'i2' not in subst1 or 'i2.2.1.0_1' not in subst1 or cons_f8(c=subst1["i2.2.1.0_1"], x=subst1["i2"]):
                                                pass
                                                if 'i2' not in subst1 or 'i2.2.1.1' not in subst1 or 'i2.2.1.0' not in subst1 or 'i2.2.0' not in subst1 or 'i2.0' not in subst1 or 'i2.2.1.2_1' not in subst1 or 'i2.2.1.2' not in subst1 or 'i2.2' not in subst1 or 'i2.2.1.0_1' not in subst1 or With36(Pm=subst1["i2.2.1.1"], Qm=subst1["i2.0"], a=subst1["i2.2.0"], b=subst1["i2.2.1.0"], c=subst1["i2.2.1.0_1"], n=subst1["i2.2.1.2"], n2=subst1["i2.2.1.2_1"], p=subst1["i2.2"], x=subst1["i2"]):
                                                    pass
                                                    # State 3072
                                                    subst2 = Substitution(subst1)
                                                    try:
                                                        subst2.try_add_variable('i2.2', 1)
                                                    except ValueError:
                                                        pass
                                                    else:
                                                        pass
                                                        if 'i2' not in subst2 or 'i2.2' not in subst2 or cons_f5(p=subst2["i2.2"], x=subst2["i2"]):
                                                            pass
                                                            if 'i2' not in subst2 or 'i2.2.1.1' not in subst2 or 'i2.2.1.0' not in subst2 or 'i2.2.0' not in subst2 or 'i2.0' not in subst2 or 'i2.2.1.2_1' not in subst2 or 'i2.2.1.2' not in subst2 or 'i2.2' not in subst2 or 'i2.2.1.0_1' not in subst2 or With36(Pm=subst2["i2.2.1.1"], Qm=subst2["i2.0"], a=subst2["i2.2.0"], b=subst2["i2.2.1.0"], c=subst2["i2.2.1.0_1"], n=subst2["i2.2.1.2"], n2=subst2["i2.2.1.2_1"], p=subst2["i2.2"], x=subst2["i2"]):
                                                                pass
                                                                # State 3073
                                                                if len(subjects40) == 0:
                                                                    pass
                                                                    # State 3074
                                                                    if len(subjects) == 0:
                                                                        pass
                                                                        # 47: (a + b*v**n + a*v**m)**p /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f4) and (cons_f5) and (cons_f48) and (cons_f11) and (With36)
                                                                        yield 47, subst2
                                                    if len(subjects40) >= 1:
                                                        tmp142 = []
                                                        tmp142.append(subjects40.popleft())
                                                        while True:
                                                            if len(tmp142) > 1:
                                                                tmp143 = create_operation_expression(associative1, tmp142)
                                                            elif len(tmp142) == 1:
                                                                tmp143 = tmp142[0]
                                                            else:
                                                                assert False, "Unreachable"
                                                            subst2 = Substitution(subst1)
                                                            try:
                                                                subst2.try_add_variable('i2.2', tmp143)
                                                            except ValueError:
                                                                pass
                                                            else:
                                                                pass
                                                                if 'i2' not in subst2 or 'i2.2' not in subst2 or cons_f5(p=subst2["i2.2"], x=subst2["i2"]):
                                                                    pass
                                                                    if 'i2' not in subst2 or 'i2.2.1.1' not in subst2 or 'i2.2.1.0' not in subst2 or 'i2.2.0' not in subst2 or 'i2.0' not in subst2 or 'i2.2.1.2_1' not in subst2 or 'i2.2.1.2' not in subst2 or 'i2.2' not in subst2 or 'i2.2.1.0_1' not in subst2 or With36(Pm=subst2["i2.2.1.1"], Qm=subst2["i2.0"], a=subst2["i2.2.0"], b=subst2["i2.2.1.0"], c=subst2["i2.2.1.0_1"], n=subst2["i2.2.1.2"], n2=subst2["i2.2.1.2_1"], p=subst2["i2.2"], x=subst2["i2"]):
                                                                        pass
                                                                        # State 3073
                                                                        if len(subjects40) == 0:
                                                                            pass
                                                                            # State 3074
                                                                            if len(subjects) == 0:
                                                                                pass
                                                                                # 47: (a + b*v**n + a*v**m)**p /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f4) and (cons_f5) and (cons_f48) and (cons_f11) and (With36)
                                                                                yield 47, subst2
                                                            if len(subjects40) == 0:
                                                                break
                                                            tmp142.append(subjects40.popleft())
                                                        subjects40.extendleft(reversed(tmp142))
                subjects40.appendleft(tmp41)
            subst1 = Substitution(subst0)
            try:
                subst1.try_add_variable('i2.2.0', S(0))
            except ValueError:
                pass
            else:
                pass
                # State 2475
                subst2 = Substitution(subst1)
                try:
                    subst2.try_add_variable('i2.2.1.0', S(1))
                except ValueError:
                    pass
                else:
                    pass
                    # State 2476
                    subst3 = Substitution(subst2)
                    try:
                        subst3.try_add_variable('i2.2.1.2', S(1))
                    except ValueError:
                        pass
                    else:
                        pass
                        # State 2477
                        if len(subjects40) >= 1:
                            tmp148 = subjects40.popleft()
                            subst4 = Substitution(subst3)
                            try:
                                subst4.try_add_variable('i2.2.1.1', tmp148)
                            except ValueError:
                                pass
                            else:
                                pass
                                if 'i2.2.0' not in subst4 or 'i2.2.1.1' not in subst4 or cons_f2(a=subst4["i2.2.0"], x=subst4["i2.2.1.1"]):
                                    pass
                                    if 'i2.2.1.0' not in subst4 or 'i2.2.1.1' not in subst4 or cons_f3(b=subst4["i2.2.1.0"], x=subst4["i2.2.1.1"]):
                                        pass
                                        if 'i2.2.1.2' not in subst4 or 'i2.2.1.1' not in subst4 or cons_f4(n=subst4["i2.2.1.2"], x=subst4["i2.2.1.1"]):
                                            pass
                                            if 'i2.2' not in subst4 or 'i2.2.1.1' not in subst4 or cons_f5(p=subst4["i2.2"], x=subst4["i2.2.1.1"]):
                                                pass
                                                # State 2478
                                                subst5 = Substitution(subst4)
                                                try:
                                                    subst5.try_add_variable('i2.2', 1)
                                                except ValueError:
                                                    pass
                                                else:
                                                    pass
                                                    if 'i2.2' not in subst5 or 'i2.2.1.1' not in subst5 or cons_f5(p=subst5["i2.2"], x=subst5["i2.2.1.1"]):
                                                        pass
                                                        # State 2479
                                                        if len(subjects40) == 0:
                                                            pass
                                                            # State 2480
                                                            if len(subjects) == 0:
                                                                pass
                                                                # 1: (a + a*v**m)**p /; (cons_f2) and (cons_f3) and (cons_f4) and (cons_f5) and (cons_f6)
                                                                yield 1, subst5
                                                if len(subjects40) >= 1:
                                                    tmp151 = subjects40.popleft()
                                                    subst5 = Substitution(subst4)
                                                    try:
                                                        subst5.try_add_variable('i2.2', tmp151)
                                                    except ValueError:
                                                        pass
                                                    else:
                                                        pass
                                                        if 'i2.2' not in subst5 or 'i2.2.1.1' not in subst5 or cons_f5(p=subst5["i2.2"], x=subst5["i2.2.1.1"]):
                                                            pass
                                                            # State 2479
                                                            if len(subjects40) == 0:
                                                                pass
                                                                # State 2480
                                                                if len(subjects) == 0:
                                                                    pass
                                                                    # 1: (a + a*v**m)**p /; (cons_f2) and (cons_f3) and (cons_f4) and (cons_f5) and (cons_f6)
                                                                    yield 1, subst5
                                                    subjects40.appendleft(tmp151)
                                if 'i2' not in subst4 or 'i2.2.1.1' not in subst4 or cons_f11(Pm=subst4["i2.2.1.1"], x=subst4["i2"]):
                                    pass
                                    if 'i2' not in subst4 or 'i2.2.1.1' not in subst4 or 'i2.2.1.0' not in subst4 or 'i2.2.0' not in subst4 or 'i2.0' not in subst4 or 'i2.2' not in subst4 or 'i2.2.1.2' not in subst4 or With35(Pm=subst4["i2.2.1.1"], Qm=subst4["i2.0"], a=subst4["i2.2.0"], b=subst4["i2.2.1.0"], n=subst4["i2.2.1.2"], p=subst4["i2.2"], x=subst4["i2"]):
                                        pass
                                        # State 2478
                                        subst5 = Substitution(subst4)
                                        try:
                                            subst5.try_add_variable('i2.2', 1)
                                        except ValueError:
                                            pass
                                        else:
                                            pass
                                            if 'i2' not in subst5 or 'i2.2' not in subst5 or cons_f5(p=subst5["i2.2"], x=subst5["i2"]):
                                                pass
                                                if 'i2' not in subst5 or 'i2.2.1.1' not in subst5 or 'i2.2.1.0' not in subst5 or 'i2.2.0' not in subst5 or 'i2.0' not in subst5 or 'i2.2' not in subst5 or 'i2.2.1.2' not in subst5 or With35(Pm=subst5["i2.2.1.1"], Qm=subst5["i2.0"], a=subst5["i2.2.0"], b=subst5["i2.2.1.0"], n=subst5["i2.2.1.2"], p=subst5["i2.2"], x=subst5["i2"]):
                                                    pass
                                                    # State 2479
                                                    if len(subjects40) == 0:
                                                        pass
                                                        # State 2480
                                                        if len(subjects) == 0:
                                                            pass
                                                            # 46: (a + a*v**m)**p /; (cons_f2) and (cons_f3) and (cons_f4) and (cons_f5) and (cons_f11) and (With35)
                                                            yield 46, subst5
                                        if len(subjects40) >= 1:
                                            tmp154 = subjects40.popleft()
                                            subst5 = Substitution(subst4)
                                            try:
                                                subst5.try_add_variable('i2.2', tmp154)
                                            except ValueError:
                                                pass
                                            else:
                                                pass
                                                if 'i2' not in subst5 or 'i2.2' not in subst5 or cons_f5(p=subst5["i2.2"], x=subst5["i2"]):
                                                    pass
                                                    if 'i2' not in subst5 or 'i2.2.1.1' not in subst5 or 'i2.2.1.0' not in subst5 or 'i2.2.0' not in subst5 or 'i2.0' not in subst5 or 'i2.2' not in subst5 or 'i2.2.1.2' not in subst5 or With35(Pm=subst5["i2.2.1.1"], Qm=subst5["i2.0"], a=subst5["i2.2.0"], b=subst5["i2.2.1.0"], n=subst5["i2.2.1.2"], p=subst5["i2.2"], x=subst5["i2"]):
                                                        pass
                                                        # State 2479
                                                        if len(subjects40) == 0:
                                                            pass
                                                            # State 2480
                                                            if len(subjects) == 0:
                                                                pass
                                                                # 46: (a + a*v**m)**p /; (cons_f2) and (cons_f3) and (cons_f4) and (cons_f5) and (cons_f11) and (With35)
                                                                yield 46, subst5
                                            subjects40.appendleft(tmp154)
                            subjects40.appendleft(tmp148)
                    if len(subjects40) >= 1 and isinstance(subjects40[0], Pow):
                        tmp156 = subjects40.popleft()
                        subjects157 = deque(tmp156._args)
                        # State 2481
                        if len(subjects157) >= 1:
                            tmp158 = subjects157.popleft()
                            subst3 = Substitution(subst2)
                            try:
                                subst3.try_add_variable('i2.2.1.1', tmp158)
                            except ValueError:
                                pass
                            else:
                                pass
                                if 'i2.2.0' not in subst3 or 'i2.2.1.1' not in subst3 or cons_f2(a=subst3["i2.2.0"], x=subst3["i2.2.1.1"]):
                                    pass
                                    if 'i2.2.1.0' not in subst3 or 'i2.2.1.1' not in subst3 or cons_f3(b=subst3["i2.2.1.0"], x=subst3["i2.2.1.1"]):
                                        pass
                                        if 'i2.2.1.2' not in subst3 or 'i2.2.1.1' not in subst3 or cons_f4(n=subst3["i2.2.1.2"], x=subst3["i2.2.1.1"]):
                                            pass
                                            if 'i2.2' not in subst3 or 'i2.2.1.1' not in subst3 or cons_f5(p=subst3["i2.2"], x=subst3["i2.2.1.1"]):
                                                pass
                                                # State 2482
                                                subst4 = Substitution(subst3)
                                                try:
                                                    subst4.try_add_variable('i2.2.1.2', 1)
                                                except ValueError:
                                                    pass
                                                else:
                                                    pass
                                                    if 'i2.2.1.2' not in subst4 or 'i2.2.1.1' not in subst4 or cons_f4(n=subst4["i2.2.1.2"], x=subst4["i2.2.1.1"]):
                                                        pass
                                                        # State 2483
                                                        if len(subjects157) == 0:
                                                            pass
                                                            # State 2484
                                                            subst5 = Substitution(subst4)
                                                            try:
                                                                subst5.try_add_variable('i2.2', 1)
                                                            except ValueError:
                                                                pass
                                                            else:
                                                                pass
                                                                if 'i2.2' not in subst5 or 'i2.2.1.1' not in subst5 or cons_f5(p=subst5["i2.2"], x=subst5["i2.2.1.1"]):
                                                                    pass
                                                                    # State 2485
                                                                    if len(subjects40) == 0:
                                                                        pass
                                                                        # State 2486
                                                                        if len(subjects) == 0:
                                                                            pass
                                                                            # 1: (a + a*v**m)**p /; (cons_f2) and (cons_f3) and (cons_f4) and (cons_f5) and (cons_f6)
                                                                            yield 1, subst5
                                                            if len(subjects40) >= 1:
                                                                tmp162 = subjects40.popleft()
                                                                subst5 = Substitution(subst4)
                                                                try:
                                                                    subst5.try_add_variable('i2.2', tmp162)
                                                                except ValueError:
                                                                    pass
                                                                else:
                                                                    pass
                                                                    if 'i2.2' not in subst5 or 'i2.2.1.1' not in subst5 or cons_f5(p=subst5["i2.2"], x=subst5["i2.2.1.1"]):
                                                                        pass
                                                                        # State 2485
                                                                        if len(subjects40) == 0:
                                                                            pass
                                                                            # State 2486
                                                                            if len(subjects) == 0:
                                                                                pass
                                                                                # 1: (a + a*v**m)**p /; (cons_f2) and (cons_f3) and (cons_f4) and (cons_f5) and (cons_f6)
                                                                                yield 1, subst5
                                                                subjects40.appendleft(tmp162)
                                                if len(subjects157) >= 1:
                                                    tmp164 = subjects157.popleft()
                                                    subst4 = Substitution(subst3)
                                                    try:
                                                        subst4.try_add_variable('i2.2.1.2', tmp164)
                                                    except ValueError:
                                                        pass
                                                    else:
                                                        pass
                                                        if 'i2.2.1.2' not in subst4 or 'i2.2.1.1' not in subst4 or cons_f4(n=subst4["i2.2.1.2"], x=subst4["i2.2.1.1"]):
                                                            pass
                                                            # State 2483
                                                            if len(subjects157) == 0:
                                                                pass
                                                                # State 2484
                                                                subst5 = Substitution(subst4)
                                                                try:
                                                                    subst5.try_add_variable('i2.2', 1)
                                                                except ValueError:
                                                                    pass
                                                                else:
                                                                    pass
                                                                    if 'i2.2' not in subst5 or 'i2.2.1.1' not in subst5 or cons_f5(p=subst5["i2.2"], x=subst5["i2.2.1.1"]):
                                                                        pass
                                                                        # State 2485
                                                                        if len(subjects40) == 0:
                                                                            pass
                                                                            # State 2486
                                                                            if len(subjects) == 0:
                                                                                pass
                                                                                # 1: (a + a*v**m)**p /; (cons_f2) and (cons_f3) and (cons_f4) and (cons_f5) and (cons_f6)
                                                                                yield 1, subst5
                                                                if len(subjects40) >= 1:
                                                                    tmp167 = subjects40.popleft()
                                                                    subst5 = Substitution(subst4)
                                                                    try:
                                                                        subst5.try_add_variable('i2.2', tmp167)
                                                                    except ValueError:
                                                                        pass
                                                                    else:
                                                                        pass
                                                                        if 'i2.2' not in subst5 or 'i2.2.1.1' not in subst5 or cons_f5(p=subst5["i2.2"], x=subst5["i2.2.1.1"]):
                                                                            pass
                                                                            # State 2485
                                                                            if len(subjects40) == 0:
                                                                                pass
                                                                                # State 2486
                                                                                if len(subjects) == 0:
                                                                                    pass
                                                                                    # 1: (a + a*v**m)**p /; (cons_f2) and (cons_f3) and (cons_f4) and (cons_f5) and (cons_f6)
                                                                                    yield 1, subst5
                                                                    subjects40.appendleft(tmp167)
                                                    subjects157.appendleft(tmp164)
                                if 'i2' not in subst3 or 'i2.2.1.1' not in subst3 or cons_f11(Pm=subst3["i2.2.1.1"], x=subst3["i2"]):
                                    pass
                                    if 'i2' not in subst3 or 'i2.2.1.1' not in subst3 or 'i2.2.1.0' not in subst3 or 'i2.2.0' not in subst3 or 'i2.0' not in subst3 or 'i2.2' not in subst3 or 'i2.2.1.2' not in subst3 or With35(Pm=subst3["i2.2.1.1"], Qm=subst3["i2.0"], a=subst3["i2.2.0"], b=subst3["i2.2.1.0"], n=subst3["i2.2.1.2"], p=subst3["i2.2"], x=subst3["i2"]):
                                        pass
                                        # State 2482
                                        subst4 = Substitution(subst3)
                                        try:
                                            subst4.try_add_variable('i2.2.1.2', 1)
                                        except ValueError:
                                            pass
                                        else:
                                            pass
                                            if 'i2.2.1.2' not in subst4 or 'i2' not in subst4 or cons_f4(n=subst4["i2.2.1.2"], x=subst4["i2"]):
                                                pass
                                                if 'i2' not in subst4 or 'i2.2.1.1' not in subst4 or 'i2.2.1.0' not in subst4 or 'i2.2.0' not in subst4 or 'i2.0' not in subst4 or 'i2.2' not in subst4 or 'i2.2.1.2' not in subst4 or With35(Pm=subst4["i2.2.1.1"], Qm=subst4["i2.0"], a=subst4["i2.2.0"], b=subst4["i2.2.1.0"], n=subst4["i2.2.1.2"], p=subst4["i2.2"], x=subst4["i2"]):
                                                    pass
                                                    # State 2483
                                                    if len(subjects157) == 0:
                                                        pass
                                                        # State 2484
                                                        subst5 = Substitution(subst4)
                                                        try:
                                                            subst5.try_add_variable('i2.2', 1)
                                                        except ValueError:
                                                            pass
                                                        else:
                                                            pass
                                                            if 'i2' not in subst5 or 'i2.2' not in subst5 or cons_f5(p=subst5["i2.2"], x=subst5["i2"]):
                                                                pass
                                                                if 'i2' not in subst5 or 'i2.2.1.1' not in subst5 or 'i2.2.1.0' not in subst5 or 'i2.2.0' not in subst5 or 'i2.0' not in subst5 or 'i2.2' not in subst5 or 'i2.2.1.2' not in subst5 or With35(Pm=subst5["i2.2.1.1"], Qm=subst5["i2.0"], a=subst5["i2.2.0"], b=subst5["i2.2.1.0"], n=subst5["i2.2.1.2"], p=subst5["i2.2"], x=subst5["i2"]):
                                                                    pass
                                                                    # State 2485
                                                                    if len(subjects40) == 0:
                                                                        pass
                                                                        # State 2486
                                                                        if len(subjects) == 0:
                                                                            pass
                                                                            # 46: (a + a*v**m)**p /; (cons_f2) and (cons_f3) and (cons_f4) and (cons_f5) and (cons_f11) and (With35)
                                                                            yield 46, subst5
                                                        if len(subjects40) >= 1:
                                                            tmp171 = subjects40.popleft()
                                                            subst5 = Substitution(subst4)
                                                            try:
                                                                subst5.try_add_variable('i2.2', tmp171)
                                                            except ValueError:
                                                                pass
                                                            else:
                                                                pass
                                                                if 'i2' not in subst5 or 'i2.2' not in subst5 or cons_f5(p=subst5["i2.2"], x=subst5["i2"]):
                                                                    pass
                                                                    if 'i2' not in subst5 or 'i2.2.1.1' not in subst5 or 'i2.2.1.0' not in subst5 or 'i2.2.0' not in subst5 or 'i2.0' not in subst5 or 'i2.2' not in subst5 or 'i2.2.1.2' not in subst5 or With35(Pm=subst5["i2.2.1.1"], Qm=subst5["i2.0"], a=subst5["i2.2.0"], b=subst5["i2.2.1.0"], n=subst5["i2.2.1.2"], p=subst5["i2.2"], x=subst5["i2"]):
                                                                        pass
                                                                        # State 2485
                                                                        if len(subjects40) == 0:
                                                                            pass
                                                                            # State 2486
                                                                            if len(subjects) == 0:
                                                                                pass
                                                                                # 46: (a + a*v**m)**p /; (cons_f2) and (cons_f3) and (cons_f4) and (cons_f5) and (cons_f11) and (With35)
                                                                                yield 46, subst5
                                                            subjects40.appendleft(tmp171)
                                        if len(subjects157) >= 1:
                                            tmp173 = subjects157.popleft()
                                            subst4 = Substitution(subst3)
                                            try:
                                                subst4.try_add_variable('i2.2.1.2', tmp173)
                                            except ValueError:
                                                pass
                                            else:
                                                pass
                                                if 'i2.2.1.2' not in subst4 or 'i2' not in subst4 or cons_f4(n=subst4["i2.2.1.2"], x=subst4["i2"]):
                                                    pass
                                                    if 'i2' not in subst4 or 'i2.2.1.1' not in subst4 or 'i2.2.1.0' not in subst4 or 'i2.2.0' not in subst4 or 'i2.0' not in subst4 or 'i2.2' not in subst4 or 'i2.2.1.2' not in subst4 or With35(Pm=subst4["i2.2.1.1"], Qm=subst4["i2.0"], a=subst4["i2.2.0"], b=subst4["i2.2.1.0"], n=subst4["i2.2.1.2"], p=subst4["i2.2"], x=subst4["i2"]):
                                                        pass
                                                        # State 2483
                                                        if len(subjects157) == 0:
                                                            pass
                                                            # State 2484
                                                            subst5 = Substitution(subst4)
                                                            try:
                                                                subst5.try_add_variable('i2.2', 1)
                                                            except ValueError:
                                                                pass
                                                            else:
                                                                pass
                                                                if 'i2' not in subst5 or 'i2.2' not in subst5 or cons_f5(p=subst5["i2.2"], x=subst5["i2"]):
                                                                    pass
                                                                    if 'i2' not in subst5 or 'i2.2.1.1' not in subst5 or 'i2.2.1.0' not in subst5 or 'i2.2.0' not in subst5 or 'i2.0' not in subst5 or 'i2.2' not in subst5 or 'i2.2.1.2' not in subst5 or With35(Pm=subst5["i2.2.1.1"], Qm=subst5["i2.0"], a=subst5["i2.2.0"], b=subst5["i2.2.1.0"], n=subst5["i2.2.1.2"], p=subst5["i2.2"], x=subst5["i2"]):
                                                                        pass
                                                                        # State 2485
                                                                        if len(subjects40) == 0:
                                                                            pass
                                                                            # State 2486
                                                                            if len(subjects) == 0:
                                                                                pass
                                                                                # 46: (a + a*v**m)**p /; (cons_f2) and (cons_f3) and (cons_f4) and (cons_f5) and (cons_f11) and (With35)
                                                                                yield 46, subst5
                                                            if len(subjects40) >= 1:
                                                                tmp176 = subjects40.popleft()
                                                                subst5 = Substitution(subst4)
                                                                try:
                                                                    subst5.try_add_variable('i2.2', tmp176)
                                                                except ValueError:
                                                                    pass
                                                                else:
                                                                    pass
                                                                    if 'i2' not in subst5 or 'i2.2' not in subst5 or cons_f5(p=subst5["i2.2"], x=subst5["i2"]):
                                                                        pass
                                                                        if 'i2' not in subst5 or 'i2.2.1.1' not in subst5 or 'i2.2.1.0' not in subst5 or 'i2.2.0' not in subst5 or 'i2.0' not in subst5 or 'i2.2' not in subst5 or 'i2.2.1.2' not in subst5 or With35(Pm=subst5["i2.2.1.1"], Qm=subst5["i2.0"], a=subst5["i2.2.0"], b=subst5["i2.2.1.0"], n=subst5["i2.2.1.2"], p=subst5["i2.2"], x=subst5["i2"]):
                                                                            pass
                                                                            # State 2485
                                                                            if len(subjects40) == 0:
                                                                                pass
                                                                                # State 2486
                                                                                if len(subjects) == 0:
                                                                                    pass
                                                                                    # 46: (a + a*v**m)**p /; (cons_f2) and (cons_f3) and (cons_f4) and (cons_f5) and (cons_f11) and (With35)
                                                                                    yield 46, subst5
                                                                subjects40.appendleft(tmp176)
                                            subjects157.appendleft(tmp173)
                            subjects157.appendleft(tmp158)
                        subjects40.appendleft(tmp156)
                if len(subjects40) >= 1 and isinstance(subjects40[0], Mul):
                    tmp178 = subjects40.popleft()
                    associative1 = tmp178
                    associative_type1 = type(tmp178)
                    subjects179 = deque(tmp178._args)
                    matcher = CommutativeMatcher2488.get()
                    tmp180 = subjects179
                    subjects179 = []
                    for s in tmp180:
                        matcher.add_subject(s)
                    for pattern_index, subst2 in matcher.match(tmp180, subst1):
                        pass
                        if pattern_index == 0:
                            pass
                            if 'i2.2.0' not in subst2 or 'i2.2.1.1' not in subst2 or cons_f2(a=subst2["i2.2.0"], x=subst2["i2.2.1.1"]):
                                pass
                                if 'i2.2.1.0' not in subst2 or 'i2.2.1.1' not in subst2 or cons_f3(b=subst2["i2.2.1.0"], x=subst2["i2.2.1.1"]):
                                    pass
                                    if 'i2.2.1.2' not in subst2 or 'i2.2.1.1' not in subst2 or cons_f4(n=subst2["i2.2.1.2"], x=subst2["i2.2.1.1"]):
                                        pass
                                        if 'i2.2' not in subst2 or 'i2.2.1.1' not in subst2 or cons_f5(p=subst2["i2.2"], x=subst2["i2.2.1.1"]):
                                            pass
                                            if 'i2.2.1.0' not in subst2 or cons_f6(b=subst2["i2.2.1.0"]):
                                                pass
                                                # State 2495
                                                subst3 = Substitution(subst2)
                                                try:
                                                    subst3.try_add_variable('i2.2', 1)
                                                except ValueError:
                                                    pass
                                                else:
                                                    pass
                                                    if 'i2.2' not in subst3 or 'i2.2.1.1' not in subst3 or cons_f5(p=subst3["i2.2"], x=subst3["i2.2.1.1"]):
                                                        pass
                                                        # State 2496
                                                        if len(subjects40) == 0:
                                                            pass
                                                            # State 2497
                                                            if len(subjects) == 0:
                                                                pass
                                                                # 1: (a + a*v**m)**p /; (cons_f2) and (cons_f3) and (cons_f4) and (cons_f5) and (cons_f6)
                                                                yield 1, subst3
                                                if len(subjects40) >= 1:
                                                    tmp182 = []
                                                    tmp182.append(subjects40.popleft())
                                                    while True:
                                                        if len(tmp182) > 1:
                                                            tmp183 = create_operation_expression(associative1, tmp182)
                                                        elif len(tmp182) == 1:
                                                            tmp183 = tmp182[0]
                                                        else:
                                                            assert False, "Unreachable"
                                                        subst3 = Substitution(subst2)
                                                        try:
                                                            subst3.try_add_variable('i2.2', tmp183)
                                                        except ValueError:
                                                            pass
                                                        else:
                                                            pass
                                                            if 'i2.2' not in subst3 or 'i2.2.1.1' not in subst3 or cons_f5(p=subst3["i2.2"], x=subst3["i2.2.1.1"]):
                                                                pass
                                                                # State 2496
                                                                if len(subjects40) == 0:
                                                                    pass
                                                                    # State 2497
                                                                    if len(subjects) == 0:
                                                                        pass
                                                                        # 1: (a + a*v**m)**p /; (cons_f2) and (cons_f3) and (cons_f4) and (cons_f5) and (cons_f6)
                                                                        yield 1, subst3
                                                        if len(subjects40) == 0:
                                                            break
                                                        tmp182.append(subjects40.popleft())
                                                    subjects40.extendleft(reversed(tmp182))
                        if pattern_index == 1:
                            pass
                            if 'i2' not in subst2 or 'i2.2.1.0' not in subst2 or cons_f3(b=subst2["i2.2.1.0"], x=subst2["i2"]):
                                pass
                                if 'i2.2.1.2' not in subst2 or 'i2' not in subst2 or cons_f4(n=subst2["i2.2.1.2"], x=subst2["i2"]):
                                    pass
                                    if 'i2' not in subst2 or 'i2.2.1.1' not in subst2 or cons_f11(Pm=subst2["i2.2.1.1"], x=subst2["i2"]):
                                        pass
                                        if 'i2' not in subst2 or 'i2.2.1.1' not in subst2 or 'i2.2.1.0' not in subst2 or 'i2.2.0' not in subst2 or 'i2.0' not in subst2 or 'i2.2' not in subst2 or 'i2.2.1.2' not in subst2 or With35(Pm=subst2["i2.2.1.1"], Qm=subst2["i2.0"], a=subst2["i2.2.0"], b=subst2["i2.2.1.0"], n=subst2["i2.2.1.2"], p=subst2["i2.2"], x=subst2["i2"]):
                                            pass
                                            # State 3057
                                            subst3 = Substitution(subst2)
                                            try:
                                                subst3.try_add_variable('i2.2', 1)
                                            except ValueError:
                                                pass
                                            else:
                                                pass
                                                if 'i2' not in subst3 or 'i2.2' not in subst3 or cons_f5(p=subst3["i2.2"], x=subst3["i2"]):
                                                    pass
                                                    if 'i2' not in subst3 or 'i2.2.1.1' not in subst3 or 'i2.2.1.0' not in subst3 or 'i2.2.0' not in subst3 or 'i2.0' not in subst3 or 'i2.2' not in subst3 or 'i2.2.1.2' not in subst3 or With35(Pm=subst3["i2.2.1.1"], Qm=subst3["i2.0"], a=subst3["i2.2.0"], b=subst3["i2.2.1.0"], n=subst3["i2.2.1.2"], p=subst3["i2.2"], x=subst3["i2"]):
                                                        pass
                                                        # State 3058
                                                        if len(subjects40) == 0:
                                                            pass
                                                            # State 3059
                                                            if len(subjects) == 0:
                                                                pass
                                                                # 46: (a + a*v**m)**p /; (cons_f2) and (cons_f3) and (cons_f4) and (cons_f5) and (cons_f11) and (With35)
                                                                yield 46, subst3
                                            if len(subjects40) >= 1:
                                                tmp186 = []
                                                tmp186.append(subjects40.popleft())
                                                while True:
                                                    if len(tmp186) > 1:
                                                        tmp187 = create_operation_expression(associative1, tmp186)
                                                    elif len(tmp186) == 1:
                                                        tmp187 = tmp186[0]
                                                    else:
                                                        assert False, "Unreachable"
                                                    subst3 = Substitution(subst2)
                                                    try:
                                                        subst3.try_add_variable('i2.2', tmp187)
                                                    except ValueError:
                                                        pass
                                                    else:
                                                        pass
                                                        if 'i2' not in subst3 or 'i2.2' not in subst3 or cons_f5(p=subst3["i2.2"], x=subst3["i2"]):
                                                            pass
                                                            if 'i2' not in subst3 or 'i2.2.1.1' not in subst3 or 'i2.2.1.0' not in subst3 or 'i2.2.0' not in subst3 or 'i2.0' not in subst3 or 'i2.2' not in subst3 or 'i2.2.1.2' not in subst3 or With35(Pm=subst3["i2.2.1.1"], Qm=subst3["i2.0"], a=subst3["i2.2.0"], b=subst3["i2.2.1.0"], n=subst3["i2.2.1.2"], p=subst3["i2.2"], x=subst3["i2"]):
                                                                pass
                                                                # State 3058
                                                                if len(subjects40) == 0:
                                                                    pass
                                                                    # State 3059
                                                                    if len(subjects) == 0:
                                                                        pass
                                                                        # 46: (a + a*v**m)**p /; (cons_f2) and (cons_f3) and (cons_f4) and (cons_f5) and (cons_f11) and (With35)
                                                                        yield 46, subst3
                                                    if len(subjects40) == 0:
                                                        break
                                                    tmp186.append(subjects40.popleft())
                                                subjects40.extendleft(reversed(tmp186))
                    subjects40.appendleft(tmp178)
            if len(subjects40) >= 1:
                tmp189 = subjects40.popleft()
                subst1 = Substitution(subst0)
                try:
                    subst1.try_add_variable('i2.1', tmp189)
                except ValueError:
                    pass
                else:
                    pass
                    if 'i2.1' not in subst1 or 'i2' not in subst1 or cons_f11(Pm=subst1["i2.1"], x=subst1["i2"]):
                        pass
                        # State 2641
                        if len(subjects40) >= 1:
                            tmp191 = subjects40.popleft()
                            subst2 = Substitution(subst1)
                            try:
                                subst2.try_add_variable('i2.2', tmp191)
                            except ValueError:
                                pass
                            else:
                                pass
                                if 'i2.2' not in subst2 or cons_f12(p=subst2["i2.2"]):
                                    pass
                                    if 'i2.2' not in subst2 or cons_f13(p=subst2["i2.2"]):
                                        pass
                                        # State 2642
                                        if len(subjects40) == 0:
                                            pass
                                            # State 2643
                                            if len(subjects) == 0:
                                                pass
                                                # 6: Pm**p /; (cons_f11) and (cons_f12) and (cons_f13)
                                                yield 6, subst2
                            subjects40.appendleft(tmp191)
                    if 'i2.1' not in subst1 or 'i2' not in subst1 or cons_f66(Pq=subst1["i2.1"], x=subst1["i2"]):
                        pass
                        if 'i2' not in subst1 or 'i2.1' not in subst1 or 'i2.0' not in subst1 or 'i2.2' not in subst1 or 'i2.1_1' not in subst1 or 'i2.2_1' not in subst1 or With37(Pq=subst1["i2.1"], Qr=subst1["i2.1_1"], m=subst1["i2.2"], p=subst1["i2.2_1"], u=subst1["i2.0"], x=subst1["i2"]):
                            pass
                            # State 2641
                            if len(subjects40) >= 1:
                                tmp193 = subjects40.popleft()
                                subst2 = Substitution(subst1)
                                try:
                                    subst2.try_add_variable('i2.2', tmp193)
                                except ValueError:
                                    pass
                                else:
                                    pass
                                    if 'i2.2' not in subst2 or cons_f64(m=subst2["i2.2"]):
                                        pass
                                        if 'i2' not in subst2 or 'i2.1' not in subst2 or 'i2.0' not in subst2 or 'i2.2' not in subst2 or 'i2.1_1' not in subst2 or 'i2.2_1' not in subst2 or With37(Pq=subst2["i2.1"], Qr=subst2["i2.1_1"], m=subst2["i2.2"], p=subst2["i2.2_1"], u=subst2["i2.0"], x=subst2["i2"]):
                                            pass
                                            # State 2642
                                            if len(subjects40) == 0:
                                                pass
                                                # State 2643
                                                if len(subjects) == 0:
                                                    pass
                                                    # 48: Pm**p /; (cons_f64) and (cons_f66) and (With37)
                                                    yield 48, subst2
                                subjects40.appendleft(tmp193)
                    if 'i2.1' not in subst1 or 'i2' not in subst1 or cons_f67(Qr=subst1["i2.1"], x=subst1["i2"]):
                        pass
                        if 'i2' not in subst1 or 'i2.1' not in subst1 or 'i2.0_1' not in subst1 or 'i2.2' not in subst1 or 'i2.0' not in subst1 or With38(Pq=subst1["i2.0"], Qr=subst1["i2.1"], p=subst1["i2.2"], u=subst1["i2.0_1"], x=subst1["i2"]):
                            pass
                            # State 2641
                            if len(subjects40) >= 1:
                                tmp195 = subjects40.popleft()
                                subst2 = Substitution(subst1)
                                try:
                                    subst2.try_add_variable('i2.2', tmp195)
                                except ValueError:
                                    pass
                                else:
                                    pass
                                    if 'i2.2' not in subst2 or cons_f65(p=subst2["i2.2"]):
                                        pass
                                        if 'i2' not in subst2 or 'i2.1' not in subst2 or 'i2.0_1' not in subst2 or 'i2.2' not in subst2 or 'i2.0' not in subst2 or With38(Pq=subst2["i2.0"], Qr=subst2["i2.1"], p=subst2["i2.2"], u=subst2["i2.0_1"], x=subst2["i2"]):
                                            pass
                                            # State 2642
                                            if len(subjects40) == 0:
                                                pass
                                                # State 2643
                                                if len(subjects) == 0:
                                                    pass
                                                    # 50: Pm**p /; (cons_f65) and (cons_f67) and (With38)
                                                    yield 50, subst2
                                subjects40.appendleft(tmp195)
                subjects40.appendleft(tmp189)
            subst1 = Substitution(subst0)
            try:
                subst1.try_add_variable('i2.2.0_1', S(1))
            except ValueError:
                pass
            else:
                pass
                # State 2677
                if len(subjects40) >= 1:
                    tmp198 = subjects40.popleft()
                    subst2 = Substitution(subst1)
                    try:
                        subst2.try_add_variable('i2.2.0', tmp198)
                    except ValueError:
                        pass
                    else:
                        pass
                        if 'i2.2.0_1' not in subst2 or 'i2.2.0' not in subst2 or cons_f8(c=subst2["i2.2.0_1"], x=subst2["i2.2.0"]):
                            pass
                            if 'i2.2.0' not in subst2 or 'i2.2' not in subst2 or cons_f19(m=subst2["i2.2"], x=subst2["i2.2.0"]):
                                pass
                                if 'i2.2.0' not in subst2 or 'i2.0' not in subst2 or cons_f18(u=subst2["i2.0"], x=subst2["i2.2.0"]):
                                    pass
                                    # State 2678
                                    subst3 = Substitution(subst2)
                                    try:
                                        subst3.try_add_variable('i2.2', 1)
                                    except ValueError:
                                        pass
                                    else:
                                        pass
                                        if 'i2.2.0' not in subst3 or 'i2.2' not in subst3 or cons_f19(m=subst3["i2.2"], x=subst3["i2.2.0"]):
                                            pass
                                            # State 2679
                                            if len(subjects40) == 0:
                                                pass
                                                # State 2680
                                                if len(subjects) == 0:
                                                    pass
                                                    # 10: (x*c)**m /; (cons_f8) and (cons_f19) and (cons_f18)
                                                    yield 10, subst3
                                    if len(subjects40) >= 1:
                                        tmp201 = subjects40.popleft()
                                        subst3 = Substitution(subst2)
                                        try:
                                            subst3.try_add_variable('i2.2', tmp201)
                                        except ValueError:
                                            pass
                                        else:
                                            pass
                                            if 'i2.2.0' not in subst3 or 'i2.2' not in subst3 or cons_f19(m=subst3["i2.2"], x=subst3["i2.2.0"]):
                                                pass
                                                # State 2679
                                                if len(subjects40) == 0:
                                                    pass
                                                    # State 2680
                                                    if len(subjects) == 0:
                                                        pass
                                                        # 10: (x*c)**m /; (cons_f8) and (cons_f19) and (cons_f18)
                                                        yield 10, subst3
                                        subjects40.appendleft(tmp201)
                                    if len(subjects40) >= 1:
                                        tmp203 = subjects40.popleft()
                                        subst3 = Substitution(subst2)
                                        try:
                                            subst3.try_add_variable('i2.2', tmp203)
                                        except ValueError:
                                            pass
                                        else:
                                            pass
                                        subjects40.appendleft(tmp203)
                        # State 2678
                        subst3 = Substitution(subst2)
                        try:
                            subst3.try_add_variable('i2.2', 1)
                        except ValueError:
                            pass
                        else:
                            pass
                        if len(subjects40) >= 1:
                            tmp206 = subjects40.popleft()
                            subst3 = Substitution(subst2)
                            try:
                                subst3.try_add_variable('i2.2', tmp206)
                            except ValueError:
                                pass
                            else:
                                pass
                            subjects40.appendleft(tmp206)
                        if len(subjects40) >= 1:
                            tmp208 = subjects40.popleft()
                            subst3 = Substitution(subst2)
                            try:
                                subst3.try_add_variable('i2.2', tmp208)
                            except ValueError:
                                pass
                            else:
                                pass
                                if 'i2.2_1' not in subst3 or 'i2.2' not in subst3 or cons_f23(m=subst3["i2.2"], n=subst3["i2.2_1"]):
                                    pass
                                    if 'i2' not in subst3 or 'i2.2' not in subst3 or cons_f19(m=subst3["i2.2"], x=subst3["i2"]):
                                        pass
                                        if 'i2.2' not in subst3 or cons_f21(m=subst3["i2.2"]):
                                            pass
                                            # State 2707
                                            if len(subjects40) == 0:
                                                pass
                                                # State 2708
                                                if len(subjects) == 0:
                                                    pass
                                                    # 14: (x*c)**m /; (cons_f2) and (cons_f19) and (cons_f21) and (cons_f23)
                                                    yield 14, subst3
                                if 'i2' not in subst3 or 'i2.2' not in subst3 or cons_f19(m=subst3["i2.2"], x=subst3["i2"]):
                                    pass
                                    if 'i2.2' not in subst3 or cons_f21(m=subst3["i2.2"]):
                                        pass
                                        if 'i2.2_1' not in subst3 or 'i2.2' not in subst3 or cons_f26(m=subst3["i2.2"], n=subst3["i2.2_1"]):
                                            pass
                                            # State 2707
                                            if len(subjects40) == 0:
                                                pass
                                                # State 2708
                                                if len(subjects) == 0:
                                                    pass
                                                    # 18: (x*c)**m /; (cons_f2) and (cons_f19) and (cons_f21) and (cons_f26)
                                                    yield 18, subst3
                                if 'i2.2' not in subst3 or cons_f33(m=subst3["i2.2"]):
                                    pass
                                    if 'i2.2' not in subst3 or cons_f34(m=subst3["i2.2"]):
                                        pass
                                        # State 2707
                                        if len(subjects40) == 0:
                                            pass
                                            # State 2708
                                            if len(subjects) == 0:
                                                pass
                                                # 25: (x*c)**m /; (cons_f2) and (cons_f33) and (cons_f34)
                                                yield 25, subst3
                            subjects40.appendleft(tmp208)
                    subjects40.appendleft(tmp198)
            if len(subjects40) >= 1:
                tmp210 = subjects40.popleft()
                subst1 = Substitution(subst0)
                try:
                    subst1.try_add_variable('i2.2.0_1', tmp210)
                except ValueError:
                    pass
                else:
                    pass
                    # State 2694
                    subst2 = Substitution(subst1)
                    try:
                        subst2.try_add_variable('i2.2_1', 1)
                    except ValueError:
                        pass
                    else:
                        pass
                        if 'i2.2_1' not in subst2 or cons_f20(m=subst2["i2.2_1"]):
                            pass
                            # State 2695
                            if len(subjects40) == 0:
                                pass
                                # State 2696
                                if len(subjects) == 0:
                                    pass
                                    # 12: v**m /; (cons_f20)
                                    yield 12, subst2
                    if len(subjects40) >= 1:
                        tmp213 = subjects40.popleft()
                        subst2 = Substitution(subst1)
                        try:
                            subst2.try_add_variable('i2.2_1', tmp213)
                        except ValueError:
                            pass
                        else:
                            pass
                            if 'i2.2_1' not in subst2 or cons_f20(m=subst2["i2.2_1"]):
                                pass
                                # State 2695
                                if len(subjects40) == 0:
                                    pass
                                    # State 2696
                                    if len(subjects) == 0:
                                        pass
                                        # 12: v**m /; (cons_f20)
                                        yield 12, subst2
                        subjects40.appendleft(tmp213)
                subjects40.appendleft(tmp210)
            subst1 = Substitution(subst0)
            try:
                subst1.try_add_variable('i2.2.0_2', S(1))
            except ValueError:
                pass
            else:
                pass
                # State 2700
                if len(subjects40) >= 1:
                    tmp216 = subjects40.popleft()
                    subst2 = Substitution(subst1)
                    try:
                        subst2.try_add_variable('i2.2.0', tmp216)
                    except ValueError:
                        pass
                    else:
                        pass
                        # State 2701
                        if len(subjects40) >= 1:
                            tmp218 = subjects40.popleft()
                            subst3 = Substitution(subst2)
                            try:
                                subst3.try_add_variable('i2.2_1', tmp218)
                            except ValueError:
                                pass
                            else:
                                pass
                                if 'i2.2_1' not in subst3 or cons_f22(n=subst3["i2.2_1"]):
                                    pass
                                    if 'i2.2_1' not in subst3 or 'i2.2' not in subst3 or cons_f23(m=subst3["i2.2"], n=subst3["i2.2_1"]):
                                        pass
                                        # State 2702
                                        if len(subjects40) == 0:
                                            pass
                                            # State 2703
                                            if len(subjects) == 0:
                                                pass
                                                # 13: (v*b)**n /; (cons_f3) and (cons_f22) and (cons_f23)
                                                yield 13, subst3
                                if 'i2.2_1' not in subst3 or 'i2.2' not in subst3 or cons_f23(m=subst3["i2.2"], n=subst3["i2.2_1"]):
                                    pass
                                    if 'i2.2_1' not in subst3 or cons_f24(n=subst3["i2.2_1"]):
                                        pass
                                        # State 2702
                                        if len(subjects40) == 0:
                                            pass
                                            # State 2703
                                            if len(subjects) == 0:
                                                pass
                                                # 15: (v*b)**n /; (cons_f3) and (cons_f24) and (cons_f23)
                                                yield 15, subst3
                                    if 'i2.2_1' not in subst3 or 'i2' not in subst3 or cons_f4(n=subst3["i2.2_1"], x=subst3["i2"]):
                                        pass
                                        if 'i2.2_1' not in subst3 or cons_f25(n=subst3["i2.2_1"]):
                                            pass
                                            # State 2702
                                            if len(subjects40) == 0:
                                                pass
                                                # State 2703
                                                if len(subjects) == 0:
                                                    pass
                                                    # 16: (v*b)**n /; (cons_f3) and (cons_f4) and (cons_f25) and (cons_f23)
                                                    yield 16, subst3
                                if 'i2.2_1' not in subst3 or 'i2' not in subst3 or cons_f4(n=subst3["i2.2_1"], x=subst3["i2"]):
                                    pass
                                    if 'i2.2_1' not in subst3 or cons_f25(n=subst3["i2.2_1"]):
                                        pass
                                        if 'i2.2_1' not in subst3 or 'i2.2' not in subst3 or cons_f26(m=subst3["i2.2"], n=subst3["i2.2_1"]):
                                            pass
                                            # State 2702
                                            if len(subjects40) == 0:
                                                pass
                                                # State 2703
                                                if len(subjects) == 0:
                                                    pass
                                                    # 17: (v*b)**n /; (cons_f3) and (cons_f4) and (cons_f25) and (cons_f26)
                                                    yield 17, subst3
                            subjects40.appendleft(tmp218)
                    subjects40.appendleft(tmp216)
            if len(subjects40) >= 1:
                tmp220 = subjects40.popleft()
                subst1 = Substitution(subst0)
                try:
                    subst1.try_add_variable('i2.2.1.1', tmp220)
                except ValueError:
                    pass
                else:
                    pass
                    if 'i2.2.0' not in subst1 or 'i2.2.1.1' not in subst1 or cons_f2(a=subst1["i2.2.0"], x=subst1["i2.2.1.1"]):
                        pass
                        if 'i2.2.1.0' not in subst1 or 'i2.2.1.1' not in subst1 or cons_f3(b=subst1["i2.2.1.0"], x=subst1["i2.2.1.1"]):
                            pass
                            if 'i2.2.1.2' not in subst1 or 'i2.2.1.1' not in subst1 or cons_f4(n=subst1["i2.2.1.2"], x=subst1["i2.2.1.1"]):
                                pass
                                if 'i2.2' not in subst1 or 'i2.2.1.1' not in subst1 or cons_f5(p=subst1["i2.2"], x=subst1["i2.2.1.1"]):
                                    pass
                                    if 'i2.2_1' not in subst1 or 'i2.2.1.1' not in subst1 or cons_f19(m=subst1["i2.2_1"], x=subst1["i2.2.1.1"]):
                                        pass
                                        # State 3023
                                        subst2 = Substitution(subst1)
                                        try:
                                            subst2.try_add_variable('i2.2', 1)
                                        except ValueError:
                                            pass
                                        else:
                                            pass
                                        if len(subjects40) >= 1:
                                            tmp223 = subjects40.popleft()
                                            subst2 = Substitution(subst1)
                                            try:
                                                subst2.try_add_variable('i2.2', tmp223)
                                            except ValueError:
                                                pass
                                            else:
                                                pass
                                            subjects40.appendleft(tmp223)
                                        subst2 = Substitution(subst1)
                                        try:
                                            subst2.try_add_variable('i2.2_1', 1)
                                        except ValueError:
                                            pass
                                        else:
                                            pass
                                            if 'i2.2_1' not in subst2 or 'i2.2.1.1' not in subst2 or cons_f19(m=subst2["i2.2_1"], x=subst2["i2.2.1.1"]):
                                                pass
                                                if 'i2.2.1.2' not in subst2 or 'i2.2_1' not in subst2 or cons_f55(m=subst2["i2.2_1"], n=subst2["i2.2.1.2"]):
                                                    pass
                                                    # State 3034
                                                    if len(subjects40) == 0:
                                                        pass
                                                        # State 3035
                                                        if len(subjects) == 0:
                                                            pass
                                                            # 42: x**m /; (cons_f2) and (cons_f3) and (cons_f19) and (cons_f4) and (cons_f5) and (cons_f55)
                                                            yield 42, subst2
                                        if len(subjects40) >= 1:
                                            tmp226 = subjects40.popleft()
                                            subst2 = Substitution(subst1)
                                            try:
                                                subst2.try_add_variable('i2.2_1', tmp226)
                                            except ValueError:
                                                pass
                                            else:
                                                pass
                                                if 'i2.2_1' not in subst2 or 'i2.2.1.1' not in subst2 or cons_f19(m=subst2["i2.2_1"], x=subst2["i2.2.1.1"]):
                                                    pass
                                                    if 'i2.2.1.2' not in subst2 or 'i2.2_1' not in subst2 or cons_f55(m=subst2["i2.2_1"], n=subst2["i2.2.1.2"]):
                                                        pass
                                                        # State 3034
                                                        if len(subjects40) == 0:
                                                            pass
                                                            # State 3035
                                                            if len(subjects) == 0:
                                                                pass
                                                                # 42: x**m /; (cons_f2) and (cons_f3) and (cons_f19) and (cons_f4) and (cons_f5) and (cons_f55)
                                                                yield 42, subst2
                                            subjects40.appendleft(tmp226)
                                if 'i2.2' not in subst1 or 'i2.2.1.1' not in subst1 or cons_f19(m=subst1["i2.2"], x=subst1["i2.2.1.1"]):
                                    pass
                                    # State 3023
                                    subst2 = Substitution(subst1)
                                    try:
                                        subst2.try_add_variable('i2.2', 1)
                                    except ValueError:
                                        pass
                                    else:
                                        pass
                                        if 'i2.2' not in subst2 or 'i2.2.1.1' not in subst2 or cons_f19(m=subst2["i2.2"], x=subst2["i2.2.1.1"]):
                                            pass
                                            if 'i2.2.1.2' not in subst2 or 'i2.2' not in subst2 or cons_f55(m=subst2["i2.2"], n=subst2["i2.2.1.2"]):
                                                pass
                                                # State 3024
                                                if len(subjects40) == 0:
                                                    pass
                                                    # State 3025
                                                    if len(subjects) == 0:
                                                        pass
                                                        # 40: x**m /; (cons_f2) and (cons_f3) and (cons_f19) and (cons_f4) and (cons_f55)
                                                        yield 40, subst2
                                    if len(subjects40) >= 1:
                                        tmp229 = subjects40.popleft()
                                        subst2 = Substitution(subst1)
                                        try:
                                            subst2.try_add_variable('i2.2', tmp229)
                                        except ValueError:
                                            pass
                                        else:
                                            pass
                                            if 'i2.2' not in subst2 or 'i2.2.1.1' not in subst2 or cons_f19(m=subst2["i2.2"], x=subst2["i2.2.1.1"]):
                                                pass
                                                if 'i2.2.1.2' not in subst2 or 'i2.2' not in subst2 or cons_f55(m=subst2["i2.2"], n=subst2["i2.2.1.2"]):
                                                    pass
                                                    # State 3024
                                                    if len(subjects40) == 0:
                                                        pass
                                                        # State 3025
                                                        if len(subjects) == 0:
                                                            pass
                                                            # 40: x**m /; (cons_f2) and (cons_f3) and (cons_f19) and (cons_f4) and (cons_f55)
                                                            yield 40, subst2
                                        subjects40.appendleft(tmp229)
                                    subst2 = Substitution(subst1)
                                    try:
                                        subst2.try_add_variable('i2.2_1', 1)
                                    except ValueError:
                                        pass
                                    else:
                                        pass
                                    if len(subjects40) >= 1:
                                        tmp232 = subjects40.popleft()
                                        subst2 = Substitution(subst1)
                                        try:
                                            subst2.try_add_variable('i2.2_1', tmp232)
                                        except ValueError:
                                            pass
                                        else:
                                            pass
                                        subjects40.appendleft(tmp232)
                    if 'i2.2.1.2' not in subst1 or 'i2.2.1.1' not in subst1 or cons_f4(n=subst1["i2.2.1.2"], x=subst1["i2.2.1.1"]):
                        pass
                        if 'i2.2' not in subst1 or 'i2.2.1.1' not in subst1 or cons_f5(p=subst1["i2.2"], x=subst1["i2.2.1.1"]):
                            pass
                            if 'i2.2_1' not in subst1 or 'i2.2.1.1' not in subst1 or cons_f19(m=subst1["i2.2_1"], x=subst1["i2.2.1.1"]):
                                pass
                                if 'i2.2.0' not in subst1 or 'i2.2.1.1' not in subst1 or cons_f59(a1=subst1["i2.2.0"], x=subst1["i2.2.1.1"]):
                                    pass
                                    if 'i2.2.1.0' not in subst1 or 'i2.2.1.1' not in subst1 or cons_f60(b1=subst1["i2.2.1.0"], x=subst1["i2.2.1.1"]):
                                        pass
                                        if 'i2.2.0_1' not in subst1 or 'i2.2.1.1' not in subst1 or cons_f61(a2=subst1["i2.2.0_1"], x=subst1["i2.2.1.1"]):
                                            pass
                                            if 'i2.2.1.0_1' not in subst1 or 'i2.2.1.1' not in subst1 or cons_f62(b2=subst1["i2.2.1.0_1"], x=subst1["i2.2.1.1"]):
                                                pass
                                                # State 3023
                                                subst2 = Substitution(subst1)
                                                try:
                                                    subst2.try_add_variable('i2.2', 1)
                                                except ValueError:
                                                    pass
                                                else:
                                                    pass
                                                if len(subjects40) >= 1:
                                                    tmp235 = subjects40.popleft()
                                                    subst2 = Substitution(subst1)
                                                    try:
                                                        subst2.try_add_variable('i2.2', tmp235)
                                                    except ValueError:
                                                        pass
                                                    else:
                                                        pass
                                                    subjects40.appendleft(tmp235)
                                                subst2 = Substitution(subst1)
                                                try:
                                                    subst2.try_add_variable('i2.2_1', 1)
                                                except ValueError:
                                                    pass
                                                else:
                                                    pass
                                                    if 'i2.2_1' not in subst2 or 'i2.2.1.1' not in subst2 or cons_f19(m=subst2["i2.2_1"], x=subst2["i2.2.1.1"]):
                                                        pass
                                                        if 'i2.2.1.2' not in subst2 or 'i2.2_1' not in subst2 or cons_f58(m=subst2["i2.2_1"], n=subst2["i2.2.1.2"]):
                                                            pass
                                                            # State 3034
                                                            if len(subjects40) == 0:
                                                                pass
                                                                # State 3035
                                                                if len(subjects) == 0:
                                                                    pass
                                                                    # 45: x**m /; (cons_f59) and (cons_f60) and (cons_f61) and (cons_f62) and (cons_f19) and (cons_f4) and (cons_f5) and (cons_f58)
                                                                    yield 45, subst2
                                                if len(subjects40) >= 1:
                                                    tmp238 = subjects40.popleft()
                                                    subst2 = Substitution(subst1)
                                                    try:
                                                        subst2.try_add_variable('i2.2_1', tmp238)
                                                    except ValueError:
                                                        pass
                                                    else:
                                                        pass
                                                        if 'i2.2_1' not in subst2 or 'i2.2.1.1' not in subst2 or cons_f19(m=subst2["i2.2_1"], x=subst2["i2.2.1.1"]):
                                                            pass
                                                            if 'i2.2.1.2' not in subst2 or 'i2.2_1' not in subst2 or cons_f58(m=subst2["i2.2_1"], n=subst2["i2.2.1.2"]):
                                                                pass
                                                                # State 3034
                                                                if len(subjects40) == 0:
                                                                    pass
                                                                    # State 3035
                                                                    if len(subjects) == 0:
                                                                        pass
                                                                        # 45: x**m /; (cons_f59) and (cons_f60) and (cons_f61) and (cons_f62) and (cons_f19) and (cons_f4) and (cons_f5) and (cons_f58)
                                                                        yield 45, subst2
                                                    subjects40.appendleft(tmp238)
                subjects40.appendleft(tmp220)
            if len(subjects40) >= 1:
                tmp240 = subjects40.popleft()
                subst1 = Substitution(subst0)
                try:
                    subst1.try_add_variable('i2.1_1', tmp240)
                except ValueError:
                    pass
                else:
                    pass
                    if 'i2' not in subst1 or 'i2.1' not in subst1 or 'i2.0' not in subst1 or 'i2.2' not in subst1 or 'i2.1_1' not in subst1 or 'i2.2_1' not in subst1 or With37(Pq=subst1["i2.1"], Qr=subst1["i2.1_1"], m=subst1["i2.2"], p=subst1["i2.2_1"], u=subst1["i2.0"], x=subst1["i2"]):
                        pass
                        if 'i2.1_1' not in subst1 or 'i2' not in subst1 or cons_f67(Qr=subst1["i2.1_1"], x=subst1["i2"]):
                            pass
                            # State 3078
                            if len(subjects40) >= 1:
                                tmp242 = subjects40.popleft()
                                subst2 = Substitution(subst1)
                                try:
                                    subst2.try_add_variable('i2.2_1', tmp242)
                                except ValueError:
                                    pass
                                else:
                                    pass
                                    if 'i2' not in subst2 or 'i2.1' not in subst2 or 'i2.0' not in subst2 or 'i2.2' not in subst2 or 'i2.1_1' not in subst2 or 'i2.2_1' not in subst2 or With37(Pq=subst2["i2.1"], Qr=subst2["i2.1_1"], m=subst2["i2.2"], p=subst2["i2.2_1"], u=subst2["i2.0"], x=subst2["i2"]):
                                        pass
                                        if 'i2.2_1' not in subst2 or cons_f65(p=subst2["i2.2_1"]):
                                            pass
                                            # State 3079
                                            if len(subjects40) == 0:
                                                pass
                                                # State 3080
                                                if len(subjects) == 0:
                                                    pass
                                                    # 49: Qr**p /; (cons_f65) and (cons_f67) and (With37)
                                                    yield 49, subst2
                                subjects40.appendleft(tmp242)
                subjects40.appendleft(tmp240)
            if len(subjects40) >= 1 and isinstance(subjects40[0], Mul):
                tmp244 = subjects40.popleft()
                associative1 = tmp244
                associative_type1 = type(tmp244)
                subjects245 = deque(tmp244._args)
                matcher = CommutativeMatcher2682.get()
                tmp246 = subjects245
                subjects245 = []
                for s in tmp246:
                    matcher.add_subject(s)
                for pattern_index, subst1 in matcher.match(tmp246, subst0):
                    pass
                    if pattern_index == 0:
                        pass
                        if 'i2.2.0_1' not in subst1 or 'i2.2.0' not in subst1 or cons_f8(c=subst1["i2.2.0_1"], x=subst1["i2.2.0"]):
                            pass
                            if 'i2.2.0' not in subst1 or 'i2.2' not in subst1 or cons_f19(m=subst1["i2.2"], x=subst1["i2.2.0"]):
                                pass
                                if 'i2.2.0' not in subst1 or 'i2.0' not in subst1 or cons_f18(u=subst1["i2.0"], x=subst1["i2.2.0"]):
                                    pass
                                    # State 2683
                                    subst2 = Substitution(subst1)
                                    try:
                                        subst2.try_add_variable('i2.2', 1)
                                    except ValueError:
                                        pass
                                    else:
                                        pass
                                        if 'i2.2.0' not in subst2 or 'i2.2' not in subst2 or cons_f19(m=subst2["i2.2"], x=subst2["i2.2.0"]):
                                            pass
                                            # State 2684
                                            if len(subjects40) == 0:
                                                pass
                                                # State 2685
                                                if len(subjects) == 0:
                                                    pass
                                                    # 10: (x*c)**m /; (cons_f8) and (cons_f19) and (cons_f18)
                                                    yield 10, subst2
                                    if len(subjects40) >= 1:
                                        tmp248 = []
                                        tmp248.append(subjects40.popleft())
                                        while True:
                                            if len(tmp248) > 1:
                                                tmp249 = create_operation_expression(associative1, tmp248)
                                            elif len(tmp248) == 1:
                                                tmp249 = tmp248[0]
                                            else:
                                                assert False, "Unreachable"
                                            subst2 = Substitution(subst1)
                                            try:
                                                subst2.try_add_variable('i2.2', tmp249)
                                            except ValueError:
                                                pass
                                            else:
                                                pass
                                                if 'i2.2.0' not in subst2 or 'i2.2' not in subst2 or cons_f19(m=subst2["i2.2"], x=subst2["i2.2.0"]):
                                                    pass
                                                    # State 2684
                                                    if len(subjects40) == 0:
                                                        pass
                                                        # State 2685
                                                        if len(subjects) == 0:
                                                            pass
                                                            # 10: (x*c)**m /; (cons_f8) and (cons_f19) and (cons_f18)
                                                            yield 10, subst2
                                            if len(subjects40) == 0:
                                                break
                                            tmp248.append(subjects40.popleft())
                                        subjects40.extendleft(reversed(tmp248))
                                    if len(subjects40) >= 1:
                                        tmp251 = []
                                        tmp251.append(subjects40.popleft())
                                        while True:
                                            if len(tmp251) > 1:
                                                tmp252 = create_operation_expression(associative1, tmp251)
                                            elif len(tmp251) == 1:
                                                tmp252 = tmp251[0]
                                            else:
                                                assert False, "Unreachable"
                                            subst2 = Substitution(subst1)
                                            try:
                                                subst2.try_add_variable('i2.2', tmp252)
                                            except ValueError:
                                                pass
                                            else:
                                                pass
                                            if len(subjects40) == 0:
                                                break
                                            tmp251.append(subjects40.popleft())
                                        subjects40.extendleft(reversed(tmp251))
                        if 'i2' not in subst1 or 'i2.2.0_1' not in subst1 or cons_f2(a=subst1["i2.2.0_1"], x=subst1["i2"]):
                            pass
                            # State 2683
                            subst2 = Substitution(subst1)
                            try:
                                subst2.try_add_variable('i2.2', 1)
                            except ValueError:
                                pass
                            else:
                                pass
                            if len(subjects40) >= 1:
                                tmp255 = []
                                tmp255.append(subjects40.popleft())
                                while True:
                                    if len(tmp255) > 1:
                                        tmp256 = create_operation_expression(associative1, tmp255)
                                    elif len(tmp255) == 1:
                                        tmp256 = tmp255[0]
                                    else:
                                        assert False, "Unreachable"
                                    subst2 = Substitution(subst1)
                                    try:
                                        subst2.try_add_variable('i2.2', tmp256)
                                    except ValueError:
                                        pass
                                    else:
                                        pass
                                    if len(subjects40) == 0:
                                        break
                                    tmp255.append(subjects40.popleft())
                                subjects40.extendleft(reversed(tmp255))
                            if len(subjects40) >= 1:
                                tmp258 = []
                                tmp258.append(subjects40.popleft())
                                while True:
                                    if len(tmp258) > 1:
                                        tmp259 = create_operation_expression(associative1, tmp258)
                                    elif len(tmp258) == 1:
                                        tmp259 = tmp258[0]
                                    else:
                                        assert False, "Unreachable"
                                    subst2 = Substitution(subst1)
                                    try:
                                        subst2.try_add_variable('i2.2', tmp259)
                                    except ValueError:
                                        pass
                                    else:
                                        pass
                                        if 'i2.2_1' not in subst2 or 'i2.2' not in subst2 or cons_f23(m=subst2["i2.2"], n=subst2["i2.2_1"]):
                                            pass
                                            if 'i2' not in subst2 or 'i2.2' not in subst2 or cons_f19(m=subst2["i2.2"], x=subst2["i2"]):
                                                pass
                                                if 'i2.2' not in subst2 or cons_f21(m=subst2["i2.2"]):
                                                    pass
                                                    # State 2709
                                                    if len(subjects40) == 0:
                                                        pass
                                                        # State 2710
                                                        if len(subjects) == 0:
                                                            pass
                                                            # 14: (x*c)**m /; (cons_f2) and (cons_f19) and (cons_f21) and (cons_f23)
                                                            yield 14, subst2
                                        if 'i2' not in subst2 or 'i2.2' not in subst2 or cons_f19(m=subst2["i2.2"], x=subst2["i2"]):
                                            pass
                                            if 'i2.2' not in subst2 or cons_f21(m=subst2["i2.2"]):
                                                pass
                                                if 'i2.2_1' not in subst2 or 'i2.2' not in subst2 or cons_f26(m=subst2["i2.2"], n=subst2["i2.2_1"]):
                                                    pass
                                                    # State 2709
                                                    if len(subjects40) == 0:
                                                        pass
                                                        # State 2710
                                                        if len(subjects) == 0:
                                                            pass
                                                            # 18: (x*c)**m /; (cons_f2) and (cons_f19) and (cons_f21) and (cons_f26)
                                                            yield 18, subst2
                                        if 'i2.2' not in subst2 or cons_f33(m=subst2["i2.2"]):
                                            pass
                                            if 'i2.2' not in subst2 or cons_f34(m=subst2["i2.2"]):
                                                pass
                                                # State 2709
                                                if len(subjects40) == 0:
                                                    pass
                                                    # State 2710
                                                    if len(subjects) == 0:
                                                        pass
                                                        # 25: (x*c)**m /; (cons_f2) and (cons_f33) and (cons_f34)
                                                        yield 25, subst2
                                    if len(subjects40) == 0:
                                        break
                                    tmp258.append(subjects40.popleft())
                                subjects40.extendleft(reversed(tmp258))
                    if pattern_index == 1:
                        pass
                        if 'i2' not in subst1 or 'i2.2.0' not in subst1 or cons_f3(b=subst1["i2.2.0"], x=subst1["i2"]):
                            pass
                            # State 2689
                            if len(subjects40) >= 1:
                                tmp261 = []
                                tmp261.append(subjects40.popleft())
                                while True:
                                    if len(tmp261) > 1:
                                        tmp262 = create_operation_expression(associative1, tmp261)
                                    elif len(tmp261) == 1:
                                        tmp262 = tmp261[0]
                                    else:
                                        assert False, "Unreachable"
                                    subst2 = Substitution(subst1)
                                    try:
                                        subst2.try_add_variable('i2.2', tmp262)
                                    except ValueError:
                                        pass
                                    else:
                                        pass
                                        if 'i2' not in subst2 or 'i2.2' not in subst2 or cons_f4(n=subst2["i2.2"], x=subst2["i2"]):
                                            pass
                                            # State 2690
                                            if len(subjects40) == 0:
                                                pass
                                                # State 2691
                                                if len(subjects) == 0:
                                                    pass
                                                    # 11: (b*v)**n /; (cons_f3) and (cons_f4)
                                                    yield 11, subst2
                                    if len(subjects40) == 0:
                                        break
                                    tmp261.append(subjects40.popleft())
                                subjects40.extendleft(reversed(tmp261))
                    if pattern_index == 2:
                        pass
                        if 'i2.2.0_2' not in subst1 or 'i2' not in subst1 or cons_f3(b=subst1["i2.2.0_2"], x=subst1["i2"]):
                            pass
                            # State 2704
                            if len(subjects40) >= 1:
                                tmp264 = []
                                tmp264.append(subjects40.popleft())
                                while True:
                                    if len(tmp264) > 1:
                                        tmp265 = create_operation_expression(associative1, tmp264)
                                    elif len(tmp264) == 1:
                                        tmp265 = tmp264[0]
                                    else:
                                        assert False, "Unreachable"
                                    subst2 = Substitution(subst1)
                                    try:
                                        subst2.try_add_variable('i2.2_1', tmp265)
                                    except ValueError:
                                        pass
                                    else:
                                        pass
                                        if 'i2.2_1' not in subst2 or cons_f22(n=subst2["i2.2_1"]):
                                            pass
                                            if 'i2.2_1' not in subst2 or 'i2.2' not in subst2 or cons_f23(m=subst2["i2.2"], n=subst2["i2.2_1"]):
                                                pass
                                                # State 2705
                                                if len(subjects40) == 0:
                                                    pass
                                                    # State 2706
                                                    if len(subjects) == 0:
                                                        pass
                                                        # 13: (v*b)**n /; (cons_f3) and (cons_f22) and (cons_f23)
                                                        yield 13, subst2
                                        if 'i2.2_1' not in subst2 or 'i2.2' not in subst2 or cons_f23(m=subst2["i2.2"], n=subst2["i2.2_1"]):
                                            pass
                                            if 'i2.2_1' not in subst2 or cons_f24(n=subst2["i2.2_1"]):
                                                pass
                                                # State 2705
                                                if len(subjects40) == 0:
                                                    pass
                                                    # State 2706
                                                    if len(subjects) == 0:
                                                        pass
                                                        # 15: (v*b)**n /; (cons_f3) and (cons_f24) and (cons_f23)
                                                        yield 15, subst2
                                            if 'i2.2_1' not in subst2 or 'i2' not in subst2 or cons_f4(n=subst2["i2.2_1"], x=subst2["i2"]):
                                                pass
                                                if 'i2.2_1' not in subst2 or cons_f25(n=subst2["i2.2_1"]):
                                                    pass
                                                    # State 2705
                                                    if len(subjects40) == 0:
                                                        pass
                                                        # State 2706
                                                        if len(subjects) == 0:
                                                            pass
                                                            # 16: (v*b)**n /; (cons_f3) and (cons_f4) and (cons_f25) and (cons_f23)
                                                            yield 16, subst2
                                        if 'i2.2_1' not in subst2 or 'i2' not in subst2 or cons_f4(n=subst2["i2.2_1"], x=subst2["i2"]):
                                            pass
                                            if 'i2.2_1' not in subst2 or cons_f25(n=subst2["i2.2_1"]):
                                                pass
                                                if 'i2.2_1' not in subst2 or 'i2.2' not in subst2 or cons_f26(m=subst2["i2.2"], n=subst2["i2.2_1"]):
                                                    pass
                                                    # State 2705
                                                    if len(subjects40) == 0:
                                                        pass
                                                        # State 2706
                                                        if len(subjects) == 0:
                                                            pass
                                                            # 17: (v*b)**n /; (cons_f3) and (cons_f4) and (cons_f25) and (cons_f26)
                                                            yield 17, subst2
                                    if len(subjects40) == 0:
                                        break
                                    tmp264.append(subjects40.popleft())
                                subjects40.extendleft(reversed(tmp264))
                subjects40.appendleft(tmp244)
            subjects.appendleft(tmp39)
        if len(subjects) >= 1 and isinstance(subjects[0], Add):
            tmp267 = subjects.popleft()
            associative1 = tmp267
            associative_type1 = type(tmp267)
            subjects268 = deque(tmp267._args)
            matcher = CommutativeMatcher2651.get()
            tmp269 = subjects268
            subjects268 = []
            for s in tmp269:
                matcher.add_subject(s)
            for pattern_index, subst1 in matcher.match(tmp269, subst0):
                pass
                if pattern_index == 0:
                    pass
                    if 'i2.1.1.0' not in subst1 or 'i2.0' not in subst1 or cons_f2(a=subst1["i2.0"], x=subst1["i2.1.1.0"]):
                        pass
                        if 'i2.1.1.0' not in subst1 or 'i2.1.0' not in subst1 or cons_f3(b=subst1["i2.1.0"], x=subst1["i2.1.1.0"]):
                            pass
                            if 'i2.1.1.0_1' not in subst1 or 'i2.1.1.0' not in subst1 or cons_f8(c=subst1["i2.1.1.0_1"], x=subst1["i2.1.1.0"]):
                                pass
                                if 'i2.1.0' not in subst1 or 'i2.1.1.0_1' not in subst1 or 'i2.1.1.0' not in subst1 or 'i2.0' not in subst1 or cons_f14(a=subst1["i2.0"], b=subst1["i2.1.0"], c=subst1["i2.1.1.0_1"], x=subst1["i2.1.1.0"]):
                                    pass
                                    # State 2657
                                    if len(subjects) == 0:
                                        pass
                                        # 7: b + x*c /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f14)
                                        yield 7, subst1
                if pattern_index == 1:
                    pass
                    if 'i2.1.1.0_1' not in subst1 or 'i2' not in subst1 or cons_f3(b=subst1["i2.1.1.0_1"], x=subst1["i2"]):
                        pass
                        if 'i2' not in subst1 or 'i2.1.1.0' not in subst1 or cons_f8(c=subst1["i2.1.1.0"], x=subst1["i2"]):
                            pass
                            # State 2771
                            if len(subjects) == 0:
                                pass
                                # 26: b*v + c*v**2 /; (cons_f3) and (cons_f8)
                                yield 26, subst1
                if pattern_index == 2:
                    pass
                    if 'i2.1.0' not in subst1 or 'i2.2.0' not in subst1 or 'i2.1.1.0_1' not in subst1 or 'i2.1.1.0' not in subst1 or 'i2.2.1.0_1' not in subst1 or cons_f35(A=subst1["i2.1.0"], B=subst1["i2.1.1.0_1"], C=subst1["i2.1.1.0"], a=subst1["i2.2.0"], b=subst1["i2.2.1.0_1"]):
                        pass
                        if 'i2' not in subst1 or 'i2.1.0' not in subst1 or cons_f36(A=subst1["i2.1.0"], x=subst1["i2"]):
                            pass
                            if 'i2.1.1.0_1' not in subst1 or 'i2' not in subst1 or cons_f37(B=subst1["i2.1.1.0_1"], x=subst1["i2"]):
                                pass
                                if 'i2' not in subst1 or 'i2.1.1.0' not in subst1 or cons_f38(C=subst1["i2.1.1.0"], x=subst1["i2"]):
                                    pass
                                    # State 2787
                                    if len(subjects) == 0:
                                        pass
                                        # 28: A + B*v + C*v**2 /; (cons_f36) and (cons_f37) and (cons_f38) and (cons_f35)
                                        yield 28, subst1
                if pattern_index == 3:
                    pass
                    if 'i2.2.0' not in subst1 or 'i2.2.1.1' not in subst1 or cons_f2(a=subst1["i2.2.0"], x=subst1["i2.2.1.1"]):
                        pass
                        if 'i2.2' not in subst1 or 'i2.2.1.1' not in subst1 or cons_f5(p=subst1["i2.2"], x=subst1["i2.2.1.1"]):
                            pass
                            if 'i2.2.1.0_1' not in subst1 or 'i2.2.1.1' not in subst1 or cons_f3(b=subst1["i2.2.1.0_1"], x=subst1["i2.2.1.1"]):
                                pass
                                if 'i2.2.1.0' not in subst1 or 'i2.2.1.1' not in subst1 or cons_f8(c=subst1["i2.2.1.0"], x=subst1["i2.2.1.1"]):
                                    pass
                                    if 'i2.1.0' not in subst1 or 'i2.2.1.1' not in subst1 or cons_f29(d=subst1["i2.1.0"], x=subst1["i2.2.1.1"]):
                                        pass
                                        if 'i2.1.1.0' not in subst1 or 'i2.2.1.1' not in subst1 or cons_f50(e=subst1["i2.1.1.0"], x=subst1["i2.2.1.1"]):
                                            pass
                                            if 'i2.2.1.0' not in subst1 or 'i2.2.1.0_1' not in subst1 or 'i2.1.0' not in subst1 or 'i2.1.1.0' not in subst1 or cons_f49(b=subst1["i2.2.1.0_1"], c=subst1["i2.2.1.0"], d=subst1["i2.1.0"], e=subst1["i2.1.1.0"]):
                                                pass
                                                # State 2924
                                                if len(subjects) == 0:
                                                    pass
                                                    # 36: d + e*x /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f50) and (cons_f5) and (cons_f49)
                                                    yield 36, subst1
            subjects.appendleft(tmp267)
        if len(subjects) >= 1 and subjects[0] == Integer(-1):
            tmp270 = subjects.popleft()
            # State 2661
            if len(subjects) == 0:
                pass
                # 8: -1
                yield 8, subst0
            subjects.appendleft(tmp270)
        if len(subjects) >= 1 and subjects[0] == I:
            tmp271 = subjects.popleft()
            # State 2665
            if len(subjects) == 0:
                pass
                # 9: I
                yield 9, subst0
            subjects.appendleft(tmp271)
        return
        yield


from matchpy.matching.many_to_one import CommutativeMatcher
from .generated_part000017 import *
from .generated_part000010 import *
from .generated_part000014 import *
from .generated_part000016 import *
from .generated_part000008 import *
from matchpy.utils import VariableWithCount
from multiset import Multiset
from collections import deque
from .generated_part000018 import *
from .generated_part000012 import *
from .generated_part000011 import *