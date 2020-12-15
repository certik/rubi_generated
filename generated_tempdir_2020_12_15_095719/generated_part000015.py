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


class CommutativeMatcher2383(CommutativeMatcher):
    _instance = None
    patterns = {
    0: (0, Multiset({0: 1}), [
      (VariableWithCount('i2.2.1.0', 1, 1, S(1)), Mul)
]),
    1: (1, Multiset({1: 1}), [
      (VariableWithCount('i2.2.1.0', 1, 1, S(1)), Mul)
]),
    2: (2, Multiset({2: 1}), [
      (VariableWithCount('i2.2.1.0_1', 1, 1, S(1)), Mul)
]),
    3: (3, Multiset({}), [
      (VariableWithCount('i2.2.1.0', 1, 1, None), Mul),
      (VariableWithCount('i2.2.1.0_1', 1, 1, S(1)), Mul)
]),
    4: (4, Multiset({}), [
      (VariableWithCount('i2.2.1.0', 1, 1, None), Mul),
      (VariableWithCount('i2.2.1.0_2', 1, 1, S(1)), Mul)
]),
    5: (5, Multiset({3: 1}), [
      (VariableWithCount('i2.2.1.0', 1, 1, S(1)), Mul)
]),
    6: (6, Multiset({4: 1}), [
      (VariableWithCount('i2.2.1.0_1', 1, 1, S(1)), Mul)
]),
    7: (7, Multiset({5: 1}), [
      (VariableWithCount('i2.2.1.0_1', 1, 1, S(1)), Mul)
]),
    8: (8, Multiset({6: 1}), [
      (VariableWithCount('i2.2.1.0', 1, 1, S(1)), Mul)
]),
    9: (9, Multiset({7: 1}), [
      (VariableWithCount('i2.2.1.0', 1, 1, S(1)), Mul)
]),
    10: (10, Multiset({}), [
      (VariableWithCount('i2.2.1.0_1', 1, 1, S(1)), Mul),
      (VariableWithCount('i2.2.1.1', 1, 1, None), Mul)
]),
    11: (11, Multiset({8: 1}), [
      (VariableWithCount('i2.2.1.0_1', 1, 1, S(1)), Mul)
]),
    12: (12, Multiset({9: 1}), [
      (VariableWithCount('i2.2.1.0', 1, 1, S(1)), Mul)
]),
    13: (13, Multiset({10: 1}), [
      (VariableWithCount('i2.2.1.0', 1, 1, S(1)), Mul)
]),
    14: (14, Multiset({11: 1}), [
      (VariableWithCount('i2.2.1.0', 1, 1, S(1)), Mul)
]),
    15: (15, Multiset({12: 1}), [
      (VariableWithCount('i2.2.1.0_1', 1, 1, S(1)), Mul)
]),
    16: (16, Multiset({13: 1}), [
      (VariableWithCount('i2.2.1.0', 1, 1, S(1)), Mul)
]),
    17: (17, Multiset({14: 1}), [
      (VariableWithCount('i2.2.1.0_1', 1, 1, S(1)), Mul)
]),
    18: (18, Multiset({15: 1}), [
      (VariableWithCount('i2.2.1.0_2', 1, 1, S(1)), Mul)
]),
    19: (19, Multiset({16: 1}), [
      (VariableWithCount('i2.2.1.0', 1, 1, S(1)), Mul)
]),
    20: (20, Multiset({17: 1}), [
      (VariableWithCount('i2.2.1.0', 1, 1, S(1)), Mul)
]),
    21: (21, Multiset({18: 1}), [
      (VariableWithCount('i2.2.1.0', 1, 1, S(1)), Mul)
]),
    22: (22, Multiset({18: 1}), [
      (VariableWithCount('i2.2.1.0_1', 1, 1, S(1)), Mul)
]),
    23: (23, Multiset({19: 1}), [
      (VariableWithCount('i2.2.1.0', 1, 1, S(1)), Mul)
]),
    24: (24, Multiset({20: 1}), [
      (VariableWithCount('i2.2.1.0', 1, 1, S(1)), Mul)
]),
    25: (25, Multiset({21: 1}), [
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
        if CommutativeMatcher2383._instance is None:
            CommutativeMatcher2383._instance = CommutativeMatcher2383()
        return CommutativeMatcher2383._instance

    @staticmethod
    def get_match_iter(subject):
        subjects = deque([subject]) if subject is not None else deque()
        subst0 = Substitution()
        # State 2382
        subst1 = Substitution(subst0)
        try:
            subst1.try_add_variable('i2.2.1.2', S(1))
        except ValueError:
            pass
        else:
            pass
            # State 2384
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
                            if 'i2.2.1.2' not in subst2 or 'i2.2.1.1' not in subst2 or cons_f4(n=subst2["i2.2.1.2"], x=subst2["i2.2.1.1"]):
                                pass
                                if 'i2.2' not in subst2 or 'i2.2.1.1' not in subst2 or cons_f5(p=subst2["i2.2"], x=subst2["i2.2.1.1"]):
                                    pass
                                    # State 2385
                                    if len(subjects) == 0:
                                        pass
                                        # 0: v**m /; (cons_f2) and (cons_f3) and (cons_f4) and (cons_f5)
                                        yield 0, subst2
                                if 'i2.2.0_1' not in subst2 or 'i2.2.1.1' not in subst2 or cons_f8(c=subst2["i2.2.0_1"], x=subst2["i2.2.1.1"]):
                                    pass
                                    if 'i2.2.1.0_1' not in subst2 or 'i2.2.1.1' not in subst2 or cons_f29(d=subst2["i2.2.1.0_1"], x=subst2["i2.2.1.1"]):
                                        pass
                                        if 'i2.2' not in subst2 or 'i2.2.1.1' not in subst2 or cons_f19(m=subst2["i2.2"], x=subst2["i2.2.1.1"]):
                                            pass
                                            # State 2385
                                            if len(subjects) == 0:
                                                pass
                                                # 3: v**m /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f19) and (cons_f4) and (cons_f39) and (cons_f42)
                                                yield 3, subst2
                        if 'i2.2' not in subst2 or 'i2.2.1.1' not in subst2 or cons_f5(p=subst2["i2.2"], x=subst2["i2.2.1.1"]):
                            pass
                            if 'i2.2.1.0_1' not in subst2 or 'i2.2.1.1' not in subst2 or cons_f3(b=subst2["i2.2.1.0_1"], x=subst2["i2.2.1.1"]):
                                pass
                                if 'i2.2.1.0' not in subst2 or 'i2.2.1.1' not in subst2 or cons_f8(c=subst2["i2.2.1.0"], x=subst2["i2.2.1.1"]):
                                    pass
                                    if 'i2.2.1.2_1' not in subst2 or 'i2.2.1.1' not in subst2 or cons_f4(n=subst2["i2.2.1.2_1"], x=subst2["i2.2.1.1"]):
                                        pass
                                        # State 2385
                                        if len(subjects) == 0:
                                            pass
                                            # 1: v**m /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f4) and (cons_f5) and (cons_f7)
                                            yield 1, subst2
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
                                                # State 2385
                                                if len(subjects) == 0:
                                                    pass
                                                    # 18: v**m /; (cons_f59) and (cons_f60) and (cons_f61) and (cons_f62) and (cons_f19) and (cons_f4) and (cons_f5) and (cons_f58)
                                                    yield 18, subst2
                    if 'i2.2.1.0_1' not in subst2 or 'i2.2.1.1' not in subst2 or cons_f3(b=subst2["i2.2.1.0_1"], x=subst2["i2.2.1.1"]):
                        pass
                        if 'i2.2.1.0' not in subst2 or 'i2.2.1.1' not in subst2 or cons_f2(a=subst2["i2.2.1.0"], x=subst2["i2.2.1.1"]):
                            pass
                            if 'i2.2.1.2' not in subst2 or 'i2.2.1.1' not in subst2 or cons_f5(p=subst2["i2.2.1.2"], x=subst2["i2.2.1.1"]):
                                pass
                                if 'i2.2.1.2_1' not in subst2 or 'i2.2.1.1' not in subst2 or cons_f52(q=subst2["i2.2.1.2_1"], x=subst2["i2.2.1.1"]):
                                    pass
                                    if 'i2.2.1.0_2' not in subst2 or 'i2.2.1.1' not in subst2 or cons_f8(c=subst2["i2.2.1.0_2"], x=subst2["i2.2.1.1"]):
                                        pass
                                        if 'i2.2.1.2_2' not in subst2 or 'i2.2.1.1' not in subst2 or cons_f54(r=subst2["i2.2.1.2_2"], x=subst2["i2.2.1.1"]):
                                            pass
                                            # State 2385
                                            if len(subjects) == 0:
                                                pass
                                                # 13: v**m /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f5) and (cons_f52) and (cons_f54) and (cons_f51) and (cons_f53)
                                                yield 13, subst2
                                    # State 2385
                                    if len(subjects) == 0:
                                        pass
                                        # 11: v**m /; (cons_f2) and (cons_f3) and (cons_f5) and (cons_f52) and (cons_f51)
                                        yield 11, subst2
                    if 'i2' not in subst2 or 'i2.2.1.1' not in subst2 or cons_f11(Pm=subst2["i2.2.1.1"], x=subst2["i2"]):
                        pass
                        if 'i2' not in subst2 or 'i2.2.1.1' not in subst2 or 'i2.2.1.0' not in subst2 or 'i2.2.0' not in subst2 or 'i2.0' not in subst2 or 'i2.2' not in subst2 or 'i2.2.1.2' not in subst2 or With35(Pm=subst2["i2.2.1.1"], Qm=subst2["i2.0"], a=subst2["i2.2.0"], b=subst2["i2.2.1.0"], n=subst2["i2.2.1.2"], p=subst2["i2.2"], x=subst2["i2"]):
                            pass
                            # State 2385
                            if len(subjects) == 0:
                                pass
                                # 19: v**m /; (cons_f4) and (cons_f11) and (With35)
                                yield 19, subst2
                        if 'i2' not in subst2 or 'i2.2.1.1' not in subst2 or 'i2.2.1.0' not in subst2 or 'i2.2.0' not in subst2 or 'i2.0' not in subst2 or 'i2.2.1.2_1' not in subst2 or 'i2.2.1.2' not in subst2 or 'i2.2' not in subst2 or 'i2.2.1.0_1' not in subst2 or With36(Pm=subst2["i2.2.1.1"], Qm=subst2["i2.0"], a=subst2["i2.2.0"], b=subst2["i2.2.1.0"], c=subst2["i2.2.1.0_1"], n=subst2["i2.2.1.2"], n2=subst2["i2.2.1.2_1"], p=subst2["i2.2"], x=subst2["i2"]):
                            pass
                            # State 2385
                            if len(subjects) == 0:
                                pass
                                # 20: v**m /; (cons_f4) and (cons_f48) and (cons_f11) and (With36)
                                yield 20, subst2
                subjects.appendleft(tmp2)
        subst1 = Substitution(subst0)
        try:
            subst1.try_add_variable('i2.2.1.2_1', S(1))
        except ValueError:
            pass
        else:
            pass
            # State 2560
            if len(subjects) >= 1:
                tmp5 = subjects.popleft()
                subst2 = Substitution(subst1)
                try:
                    subst2.try_add_variable('i2.2.1.1', tmp5)
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
                                if 'i2.2.0_1' not in subst2 or 'i2.2.1.1' not in subst2 or cons_f8(c=subst2["i2.2.0_1"], x=subst2["i2.2.1.1"]):
                                    pass
                                    if 'i2.2.1.0_1' not in subst2 or 'i2.2.1.1' not in subst2 or cons_f29(d=subst2["i2.2.1.0_1"], x=subst2["i2.2.1.1"]):
                                        pass
                                        if 'i2.2' not in subst2 or 'i2.2.1.1' not in subst2 or cons_f19(m=subst2["i2.2"], x=subst2["i2.2.1.1"]):
                                            pass
                                            # State 2561
                                            if len(subjects) == 0:
                                                pass
                                                # 4: v**n /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f19) and (cons_f4) and (cons_f39)
                                                yield 4, subst2
                                if 'i2.2.1.0_1' not in subst2 or 'i2.2.1.1' not in subst2 or cons_f8(c=subst2["i2.2.1.0_1"], x=subst2["i2.2.1.1"]):
                                    pass
                                    # State 2561
                                    if len(subjects) == 0:
                                        pass
                                        # 8: v**n /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f4) and (cons_f48)
                                        yield 8, subst2
                        if 'i2.2' not in subst2 or 'i2.2.1.1' not in subst2 or cons_f5(p=subst2["i2.2"], x=subst2["i2.2.1.1"]):
                            pass
                            if 'i2.2.1.0_1' not in subst2 or 'i2.2.1.1' not in subst2 or cons_f3(b=subst2["i2.2.1.0_1"], x=subst2["i2.2.1.1"]):
                                pass
                                if 'i2.2.1.0' not in subst2 or 'i2.2.1.1' not in subst2 or cons_f8(c=subst2["i2.2.1.0"], x=subst2["i2.2.1.1"]):
                                    pass
                                    if 'i2.2.1.2_1' not in subst2 or 'i2.2.1.1' not in subst2 or cons_f4(n=subst2["i2.2.1.2_1"], x=subst2["i2.2.1.1"]):
                                        pass
                                        # State 2561
                                        if len(subjects) == 0:
                                            pass
                                            # 2: v**n /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f4) and (cons_f5) and (cons_f7)
                                            yield 2, subst2
                    if 'i2.2' not in subst2 or 'i2.2.1.1' not in subst2 or cons_f5(p=subst2["i2.2"], x=subst2["i2.2.1.1"]):
                        pass
                        if 'i2.2.1.0_1' not in subst2 or 'i2.2.1.1' not in subst2 or cons_f3(b=subst2["i2.2.1.0_1"], x=subst2["i2.2.1.1"]):
                            pass
                            if 'i2.2.1.2_1' not in subst2 or 'i2.2.1.1' not in subst2 or cons_f4(n=subst2["i2.2.1.2_1"], x=subst2["i2.2.1.1"]):
                                pass
                                if 'i2.2.0_1' not in subst2 or 'i2.2.1.1' not in subst2 or cons_f2(a=subst2["i2.2.0_1"], x=subst2["i2.2.1.1"]):
                                    pass
                                    if 'i2.2.0' not in subst2 or 'i2.2.1.1' not in subst2 or cons_f8(c=subst2["i2.2.0"], x=subst2["i2.2.1.1"]):
                                        pass
                                        if 'i2.2.1.0' not in subst2 or 'i2.2.1.1' not in subst2 or cons_f29(d=subst2["i2.2.1.0"], x=subst2["i2.2.1.1"]):
                                            pass
                                            if 'i2.2_1' not in subst2 or 'i2.2.1.1' not in subst2 or cons_f19(m=subst2["i2.2_1"], x=subst2["i2.2.1.1"]):
                                                pass
                                                # State 2561
                                                if len(subjects) == 0:
                                                    pass
                                                    # 5: v**n /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f19) and (cons_f4) and (cons_f5) and (cons_f7)
                                                    yield 5, subst2
                    if 'i2.2.1.0_1' not in subst2 or 'i2.2.1.1' not in subst2 or cons_f3(b=subst2["i2.2.1.0_1"], x=subst2["i2.2.1.1"]):
                        pass
                        if 'i2.2.1.0' not in subst2 or 'i2.2.1.1' not in subst2 or cons_f2(a=subst2["i2.2.1.0"], x=subst2["i2.2.1.1"]):
                            pass
                            if 'i2.2.1.2' not in subst2 or 'i2.2.1.1' not in subst2 or cons_f5(p=subst2["i2.2.1.2"], x=subst2["i2.2.1.1"]):
                                pass
                                if 'i2.2.1.2_1' not in subst2 or 'i2.2.1.1' not in subst2 or cons_f52(q=subst2["i2.2.1.2_1"], x=subst2["i2.2.1.1"]):
                                    pass
                                    if 'i2.2.1.0_2' not in subst2 or 'i2.2.1.1' not in subst2 or cons_f8(c=subst2["i2.2.1.0_2"], x=subst2["i2.2.1.1"]):
                                        pass
                                        if 'i2.2.1.2_2' not in subst2 or 'i2.2.1.1' not in subst2 or cons_f54(r=subst2["i2.2.1.2_2"], x=subst2["i2.2.1.1"]):
                                            pass
                                            # State 2561
                                            if len(subjects) == 0:
                                                pass
                                                # 14: v**n /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f5) and (cons_f52) and (cons_f54) and (cons_f51)
                                                yield 14, subst2
                                    # State 2561
                                    if len(subjects) == 0:
                                        pass
                                        # 12: v**n /; (cons_f2) and (cons_f3) and (cons_f5) and (cons_f52) and (cons_f51)
                                        yield 12, subst2
                    if 'i2' not in subst2 or 'i2.2.1.1' not in subst2 or cons_f11(Pm=subst2["i2.2.1.1"], x=subst2["i2"]):
                        pass
                        if 'i2' not in subst2 or 'i2.2.1.1' not in subst2 or 'i2.2.1.0' not in subst2 or 'i2.2.0' not in subst2 or 'i2.0' not in subst2 or 'i2.2.1.2_1' not in subst2 or 'i2.2.1.2' not in subst2 or 'i2.2' not in subst2 or 'i2.2.1.0_1' not in subst2 or With36(Pm=subst2["i2.2.1.1"], Qm=subst2["i2.0"], a=subst2["i2.2.0"], b=subst2["i2.2.1.0"], c=subst2["i2.2.1.0_1"], n=subst2["i2.2.1.2"], n2=subst2["i2.2.1.2_1"], p=subst2["i2.2"], x=subst2["i2"]):
                            pass
                            # State 2561
                            if len(subjects) == 0:
                                pass
                                # 21: v**n /; (cons_f48) and (cons_f11) and (With36)
                                yield 21, subst2
                subjects.appendleft(tmp5)
        subst1 = Substitution(subst0)
        try:
            subst1.try_add_variable('i2.2.1.2_2', S(1))
        except ValueError:
            pass
        else:
            pass
            # State 3007
            if len(subjects) >= 1:
                tmp8 = subjects.popleft()
                subst2 = Substitution(subst1)
                try:
                    subst2.try_add_variable('i2.2.1.1', tmp8)
                except ValueError:
                    pass
                else:
                    pass
                    if 'i2.2.1.0_1' not in subst2 or 'i2.2.1.1' not in subst2 or cons_f3(b=subst2["i2.2.1.0_1"], x=subst2["i2.2.1.1"]):
                        pass
                        if 'i2.2.1.0' not in subst2 or 'i2.2.1.1' not in subst2 or cons_f2(a=subst2["i2.2.1.0"], x=subst2["i2.2.1.1"]):
                            pass
                            if 'i2.2.1.2' not in subst2 or 'i2.2.1.1' not in subst2 or cons_f5(p=subst2["i2.2.1.2"], x=subst2["i2.2.1.1"]):
                                pass
                                if 'i2.2.1.2_1' not in subst2 or 'i2.2.1.1' not in subst2 or cons_f52(q=subst2["i2.2.1.2_1"], x=subst2["i2.2.1.1"]):
                                    pass
                                    if 'i2.2.1.0_2' not in subst2 or 'i2.2.1.1' not in subst2 or cons_f8(c=subst2["i2.2.1.0_2"], x=subst2["i2.2.1.1"]):
                                        pass
                                        if 'i2.2.1.2_2' not in subst2 or 'i2.2.1.1' not in subst2 or cons_f54(r=subst2["i2.2.1.2_2"], x=subst2["i2.2.1.1"]):
                                            pass
                                            # State 3008
                                            if len(subjects) == 0:
                                                pass
                                                # 15: x**r /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f5) and (cons_f52) and (cons_f54) and (cons_f53)
                                                yield 15, subst2
                subjects.appendleft(tmp8)
        if len(subjects) >= 1 and isinstance(subjects[0], Pow):
            tmp10 = subjects.popleft()
            subjects11 = deque(tmp10._args)
            # State 2386
            if len(subjects11) >= 1:
                tmp12 = subjects11.popleft()
                subst1 = Substitution(subst0)
                try:
                    subst1.try_add_variable('i2.2.1.1', tmp12)
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
                                        # State 2387
                                        subst2 = Substitution(subst1)
                                        try:
                                            subst2.try_add_variable('i2.2.1.2', 1)
                                        except ValueError:
                                            pass
                                        else:
                                            pass
                                        if len(subjects11) >= 1:
                                            tmp15 = subjects11.popleft()
                                            subst2 = Substitution(subst1)
                                            try:
                                                subst2.try_add_variable('i2.2.1.2', tmp15)
                                            except ValueError:
                                                pass
                                            else:
                                                pass
                                            subjects11.appendleft(tmp15)
                                        subst2 = Substitution(subst1)
                                        try:
                                            subst2.try_add_variable('i2.2.1.2_1', 1)
                                        except ValueError:
                                            pass
                                        else:
                                            pass
                                        if len(subjects11) >= 1:
                                            tmp18 = subjects11.popleft()
                                            subst2 = Substitution(subst1)
                                            try:
                                                subst2.try_add_variable('i2.2.1.2_1', tmp18)
                                            except ValueError:
                                                pass
                                            else:
                                                pass
                                            subjects11.appendleft(tmp18)
                                        if len(subjects11) >= 1:
                                            tmp20 = subjects11.popleft()
                                            subst2 = Substitution(subst1)
                                            try:
                                                subst2.try_add_variable('i2.2.1.2', tmp20)
                                            except ValueError:
                                                pass
                                            else:
                                                pass
                                                if 'i2.2.1.2' not in subst2 or 'i2.2.1.1' not in subst2 or cons_f4(n=subst2["i2.2.1.2"], x=subst2["i2.2.1.1"]):
                                                    pass
                                                    if 'i2.2.1.2' not in subst2 or 'i2.2_1' not in subst2 or cons_f55(m=subst2["i2.2_1"], n=subst2["i2.2.1.2"]):
                                                        pass
                                                        # State 2833
                                                        if len(subjects11) == 0:
                                                            pass
                                                            # State 2834
                                                            if len(subjects) == 0:
                                                                pass
                                                                # 17: x**j /; (cons_f2) and (cons_f3) and (cons_f19) and (cons_f4) and (cons_f5) and (cons_f55)
                                                                yield 17, subst2
                                            subjects11.appendleft(tmp20)
                                        subst2 = Substitution(subst1)
                                        try:
                                            subst2.try_add_variable('i2.2.1.2_2', 1)
                                        except ValueError:
                                            pass
                                        else:
                                            pass
                                        if len(subjects11) >= 1:
                                            tmp23 = subjects11.popleft()
                                            subst2 = Substitution(subst1)
                                            try:
                                                subst2.try_add_variable('i2.2.1.2_2', tmp23)
                                            except ValueError:
                                                pass
                                            else:
                                                pass
                                            subjects11.appendleft(tmp23)
                                        if len(subjects11) >= 1 and subjects11[0] == Integer(2):
                                            tmp25 = subjects11.popleft()
                                            # State 2874
                                            if len(subjects11) == 0:
                                                pass
                                                # State 2875
                                                if len(subjects) == 0:
                                                    pass
                                            subjects11.appendleft(tmp25)
                                    # State 2387
                                    subst2 = Substitution(subst1)
                                    try:
                                        subst2.try_add_variable('i2.2.1.2', 1)
                                    except ValueError:
                                        pass
                                    else:
                                        pass
                                        if 'i2.2.1.2' not in subst2 or 'i2.2.1.1' not in subst2 or cons_f4(n=subst2["i2.2.1.2"], x=subst2["i2.2.1.1"]):
                                            pass
                                            # State 2388
                                            if len(subjects11) == 0:
                                                pass
                                                # State 2389
                                                if len(subjects) == 0:
                                                    pass
                                                    # 0: v**m /; (cons_f2) and (cons_f3) and (cons_f4) and (cons_f5)
                                                    yield 0, subst2
                                    if len(subjects11) >= 1:
                                        tmp27 = subjects11.popleft()
                                        subst2 = Substitution(subst1)
                                        try:
                                            subst2.try_add_variable('i2.2.1.2', tmp27)
                                        except ValueError:
                                            pass
                                        else:
                                            pass
                                            if 'i2.2.1.2' not in subst2 or 'i2.2.1.1' not in subst2 or cons_f4(n=subst2["i2.2.1.2"], x=subst2["i2.2.1.1"]):
                                                pass
                                                # State 2388
                                                if len(subjects11) == 0:
                                                    pass
                                                    # State 2389
                                                    if len(subjects) == 0:
                                                        pass
                                                        # 0: v**m /; (cons_f2) and (cons_f3) and (cons_f4) and (cons_f5)
                                                        yield 0, subst2
                                        subjects11.appendleft(tmp27)
                                    subst2 = Substitution(subst1)
                                    try:
                                        subst2.try_add_variable('i2.2.1.2_1', 1)
                                    except ValueError:
                                        pass
                                    else:
                                        pass
                                    if len(subjects11) >= 1:
                                        tmp30 = subjects11.popleft()
                                        subst2 = Substitution(subst1)
                                        try:
                                            subst2.try_add_variable('i2.2.1.2_1', tmp30)
                                        except ValueError:
                                            pass
                                        else:
                                            pass
                                        subjects11.appendleft(tmp30)
                                    if len(subjects11) >= 1:
                                        tmp32 = subjects11.popleft()
                                        subst2 = Substitution(subst1)
                                        try:
                                            subst2.try_add_variable('i2.2.1.2', tmp32)
                                        except ValueError:
                                            pass
                                        else:
                                            pass
                                        subjects11.appendleft(tmp32)
                                    subst2 = Substitution(subst1)
                                    try:
                                        subst2.try_add_variable('i2.2.1.2_2', 1)
                                    except ValueError:
                                        pass
                                    else:
                                        pass
                                    if len(subjects11) >= 1:
                                        tmp35 = subjects11.popleft()
                                        subst2 = Substitution(subst1)
                                        try:
                                            subst2.try_add_variable('i2.2.1.2_2', tmp35)
                                        except ValueError:
                                            pass
                                        else:
                                            pass
                                        subjects11.appendleft(tmp35)
                                    if len(subjects11) >= 1 and subjects11[0] == Integer(2):
                                        tmp37 = subjects11.popleft()
                                        # State 2874
                                        if len(subjects11) == 0:
                                            pass
                                            # State 2875
                                            if len(subjects) == 0:
                                                pass
                                        subjects11.appendleft(tmp37)
                                if 'i2.2.0_1' not in subst1 or 'i2.2.1.1' not in subst1 or cons_f8(c=subst1["i2.2.0_1"], x=subst1["i2.2.1.1"]):
                                    pass
                                    if 'i2.2.1.0_1' not in subst1 or 'i2.2.1.1' not in subst1 or cons_f29(d=subst1["i2.2.1.0_1"], x=subst1["i2.2.1.1"]):
                                        pass
                                        if 'i2.2' not in subst1 or 'i2.2.1.1' not in subst1 or cons_f19(m=subst1["i2.2"], x=subst1["i2.2.1.1"]):
                                            pass
                                            # State 2387
                                            subst2 = Substitution(subst1)
                                            try:
                                                subst2.try_add_variable('i2.2.1.2', 1)
                                            except ValueError:
                                                pass
                                            else:
                                                pass
                                                if 'i2.2.1.2' not in subst2 or 'i2.2.1.1' not in subst2 or cons_f4(n=subst2["i2.2.1.2"], x=subst2["i2.2.1.1"]):
                                                    pass
                                                    if 'i2.2.1.2' not in subst2 or 'i2.2.1.2_1' not in subst2 or cons_f39(n=subst2["i2.2.1.2"], q=subst2["i2.2.1.2_1"]):
                                                        pass
                                                        if 'i2.2.1.2' not in subst2 or 'i2.2' not in subst2 or cons_f42(m=subst2["i2.2"], n=subst2["i2.2.1.2"]):
                                                            pass
                                                            # State 2388
                                                            if len(subjects11) == 0:
                                                                pass
                                                                # State 2389
                                                                if len(subjects) == 0:
                                                                    pass
                                                                    # 3: v**m /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f19) and (cons_f4) and (cons_f39) and (cons_f42)
                                                                    yield 3, subst2
                                            if len(subjects11) >= 1:
                                                tmp39 = subjects11.popleft()
                                                subst2 = Substitution(subst1)
                                                try:
                                                    subst2.try_add_variable('i2.2.1.2', tmp39)
                                                except ValueError:
                                                    pass
                                                else:
                                                    pass
                                                    if 'i2.2.1.2' not in subst2 or 'i2.2.1.1' not in subst2 or cons_f4(n=subst2["i2.2.1.2"], x=subst2["i2.2.1.1"]):
                                                        pass
                                                        if 'i2.2.1.2' not in subst2 or 'i2.2.1.2_1' not in subst2 or cons_f39(n=subst2["i2.2.1.2"], q=subst2["i2.2.1.2_1"]):
                                                            pass
                                                            if 'i2.2.1.2' not in subst2 or 'i2.2' not in subst2 or cons_f42(m=subst2["i2.2"], n=subst2["i2.2.1.2"]):
                                                                pass
                                                                # State 2388
                                                                if len(subjects11) == 0:
                                                                    pass
                                                                    # State 2389
                                                                    if len(subjects) == 0:
                                                                        pass
                                                                        # 3: v**m /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f19) and (cons_f4) and (cons_f39) and (cons_f42)
                                                                        yield 3, subst2
                                                subjects11.appendleft(tmp39)
                                            subst2 = Substitution(subst1)
                                            try:
                                                subst2.try_add_variable('i2.2.1.2_1', 1)
                                            except ValueError:
                                                pass
                                            else:
                                                pass
                                                if 'i2.2.1.2' not in subst2 or 'i2.2.1.2_1' not in subst2 or cons_f39(n=subst2["i2.2.1.2"], q=subst2["i2.2.1.2_1"]):
                                                    pass
                                                    # State 2562
                                                    if len(subjects11) == 0:
                                                        pass
                                                        # State 2563
                                                        if len(subjects) == 0:
                                                            pass
                                                            # 4: v**n /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f19) and (cons_f4) and (cons_f39)
                                                            yield 4, subst2
                                            if len(subjects11) >= 1:
                                                tmp42 = subjects11.popleft()
                                                subst2 = Substitution(subst1)
                                                try:
                                                    subst2.try_add_variable('i2.2.1.2_1', tmp42)
                                                except ValueError:
                                                    pass
                                                else:
                                                    pass
                                                    if 'i2.2.1.2' not in subst2 or 'i2.2.1.2_1' not in subst2 or cons_f39(n=subst2["i2.2.1.2"], q=subst2["i2.2.1.2_1"]):
                                                        pass
                                                        # State 2562
                                                        if len(subjects11) == 0:
                                                            pass
                                                            # State 2563
                                                            if len(subjects) == 0:
                                                                pass
                                                                # 4: v**n /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f19) and (cons_f4) and (cons_f39)
                                                                yield 4, subst2
                                                subjects11.appendleft(tmp42)
                                            if len(subjects11) >= 1:
                                                tmp44 = subjects11.popleft()
                                                subst2 = Substitution(subst1)
                                                try:
                                                    subst2.try_add_variable('i2.2.1.2', tmp44)
                                                except ValueError:
                                                    pass
                                                else:
                                                    pass
                                                subjects11.appendleft(tmp44)
                                            subst2 = Substitution(subst1)
                                            try:
                                                subst2.try_add_variable('i2.2.1.2_2', 1)
                                            except ValueError:
                                                pass
                                            else:
                                                pass
                                            if len(subjects11) >= 1:
                                                tmp47 = subjects11.popleft()
                                                subst2 = Substitution(subst1)
                                                try:
                                                    subst2.try_add_variable('i2.2.1.2_2', tmp47)
                                                except ValueError:
                                                    pass
                                                else:
                                                    pass
                                                subjects11.appendleft(tmp47)
                                            if len(subjects11) >= 1 and subjects11[0] == Integer(2):
                                                tmp49 = subjects11.popleft()
                                                # State 2874
                                                if len(subjects11) == 0:
                                                    pass
                                                    # State 2875
                                                    if len(subjects) == 0:
                                                        pass
                                                subjects11.appendleft(tmp49)
                                if 'i2.2' not in subst1 or 'i2.2.1.1' not in subst1 or cons_f19(m=subst1["i2.2"], x=subst1["i2.2.1.1"]):
                                    pass
                                    # State 2387
                                    subst2 = Substitution(subst1)
                                    try:
                                        subst2.try_add_variable('i2.2.1.2', 1)
                                    except ValueError:
                                        pass
                                    else:
                                        pass
                                    if len(subjects11) >= 1:
                                        tmp51 = subjects11.popleft()
                                        subst2 = Substitution(subst1)
                                        try:
                                            subst2.try_add_variable('i2.2.1.2', tmp51)
                                        except ValueError:
                                            pass
                                        else:
                                            pass
                                        subjects11.appendleft(tmp51)
                                    subst2 = Substitution(subst1)
                                    try:
                                        subst2.try_add_variable('i2.2.1.2_1', 1)
                                    except ValueError:
                                        pass
                                    else:
                                        pass
                                    if len(subjects11) >= 1:
                                        tmp54 = subjects11.popleft()
                                        subst2 = Substitution(subst1)
                                        try:
                                            subst2.try_add_variable('i2.2.1.2_1', tmp54)
                                        except ValueError:
                                            pass
                                        else:
                                            pass
                                        subjects11.appendleft(tmp54)
                                    if len(subjects11) >= 1:
                                        tmp56 = subjects11.popleft()
                                        subst2 = Substitution(subst1)
                                        try:
                                            subst2.try_add_variable('i2.2.1.2', tmp56)
                                        except ValueError:
                                            pass
                                        else:
                                            pass
                                            if 'i2.2.1.2' not in subst2 or 'i2.2.1.1' not in subst2 or cons_f4(n=subst2["i2.2.1.2"], x=subst2["i2.2.1.1"]):
                                                pass
                                                if 'i2.2.1.2' not in subst2 or 'i2.2' not in subst2 or cons_f55(m=subst2["i2.2"], n=subst2["i2.2.1.2"]):
                                                    pass
                                                    # State 2833
                                                    if len(subjects11) == 0:
                                                        pass
                                                        # State 2834
                                                        if len(subjects) == 0:
                                                            pass
                                                            # 16: x**j /; (cons_f2) and (cons_f3) and (cons_f19) and (cons_f4) and (cons_f55)
                                                            yield 16, subst2
                                        subjects11.appendleft(tmp56)
                                    subst2 = Substitution(subst1)
                                    try:
                                        subst2.try_add_variable('i2.2.1.2_2', 1)
                                    except ValueError:
                                        pass
                                    else:
                                        pass
                                    if len(subjects11) >= 1:
                                        tmp59 = subjects11.popleft()
                                        subst2 = Substitution(subst1)
                                        try:
                                            subst2.try_add_variable('i2.2.1.2_2', tmp59)
                                        except ValueError:
                                            pass
                                        else:
                                            pass
                                        subjects11.appendleft(tmp59)
                                    if len(subjects11) >= 1 and subjects11[0] == Integer(2):
                                        tmp61 = subjects11.popleft()
                                        # State 2874
                                        if len(subjects11) == 0:
                                            pass
                                            # State 2875
                                            if len(subjects) == 0:
                                                pass
                                        subjects11.appendleft(tmp61)
                                if 'i2.2.1.0_1' not in subst1 or 'i2.2.1.1' not in subst1 or cons_f8(c=subst1["i2.2.1.0_1"], x=subst1["i2.2.1.1"]):
                                    pass
                                    # State 2387
                                    subst2 = Substitution(subst1)
                                    try:
                                        subst2.try_add_variable('i2.2.1.2', 1)
                                    except ValueError:
                                        pass
                                    else:
                                        pass
                                    if len(subjects11) >= 1:
                                        tmp63 = subjects11.popleft()
                                        subst2 = Substitution(subst1)
                                        try:
                                            subst2.try_add_variable('i2.2.1.2', tmp63)
                                        except ValueError:
                                            pass
                                        else:
                                            pass
                                        subjects11.appendleft(tmp63)
                                    subst2 = Substitution(subst1)
                                    try:
                                        subst2.try_add_variable('i2.2.1.2_1', 1)
                                    except ValueError:
                                        pass
                                    else:
                                        pass
                                        if 'i2.2.1.2' not in subst2 or 'i2.2.1.2_1' not in subst2 or cons_f48(n=subst2["i2.2.1.2"], n2=subst2["i2.2.1.2_1"]):
                                            pass
                                            # State 2562
                                            if len(subjects11) == 0:
                                                pass
                                                # State 2563
                                                if len(subjects) == 0:
                                                    pass
                                                    # 8: v**n /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f4) and (cons_f48)
                                                    yield 8, subst2
                                    if len(subjects11) >= 1:
                                        tmp66 = subjects11.popleft()
                                        subst2 = Substitution(subst1)
                                        try:
                                            subst2.try_add_variable('i2.2.1.2_1', tmp66)
                                        except ValueError:
                                            pass
                                        else:
                                            pass
                                            if 'i2.2.1.2' not in subst2 or 'i2.2.1.2_1' not in subst2 or cons_f48(n=subst2["i2.2.1.2"], n2=subst2["i2.2.1.2_1"]):
                                                pass
                                                # State 2562
                                                if len(subjects11) == 0:
                                                    pass
                                                    # State 2563
                                                    if len(subjects) == 0:
                                                        pass
                                                        # 8: v**n /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f4) and (cons_f48)
                                                        yield 8, subst2
                                        subjects11.appendleft(tmp66)
                                    if len(subjects11) >= 1:
                                        tmp68 = subjects11.popleft()
                                        subst2 = Substitution(subst1)
                                        try:
                                            subst2.try_add_variable('i2.2.1.2', tmp68)
                                        except ValueError:
                                            pass
                                        else:
                                            pass
                                            if 'i2.2.1.2' not in subst2 or 'i2.2.1.1' not in subst2 or cons_f4(n=subst2["i2.2.1.2"], x=subst2["i2.2.1.1"]):
                                                pass
                                                if 'i2.2.1.2' not in subst2 or 'i2.2.1.2_1' not in subst2 or cons_f48(n=subst2["i2.2.1.2"], n2=subst2["i2.2.1.2_1"]):
                                                    pass
                                                    # State 2833
                                                    if len(subjects11) == 0:
                                                        pass
                                                        # State 2834
                                                        if len(subjects) == 0:
                                                            pass
                                                            # 9: x**j /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f4) and (cons_f48)
                                                            yield 9, subst2
                                        subjects11.appendleft(tmp68)
                                    subst2 = Substitution(subst1)
                                    try:
                                        subst2.try_add_variable('i2.2.1.2_2', 1)
                                    except ValueError:
                                        pass
                                    else:
                                        pass
                                    if len(subjects11) >= 1:
                                        tmp71 = subjects11.popleft()
                                        subst2 = Substitution(subst1)
                                        try:
                                            subst2.try_add_variable('i2.2.1.2_2', tmp71)
                                        except ValueError:
                                            pass
                                        else:
                                            pass
                                        subjects11.appendleft(tmp71)
                                    if len(subjects11) >= 1 and subjects11[0] == Integer(2):
                                        tmp73 = subjects11.popleft()
                                        # State 2874
                                        if len(subjects11) == 0:
                                            pass
                                            # State 2875
                                            if len(subjects) == 0:
                                                pass
                                        subjects11.appendleft(tmp73)
                        if 'i2.2' not in subst1 or 'i2.2.1.1' not in subst1 or cons_f5(p=subst1["i2.2"], x=subst1["i2.2.1.1"]):
                            pass
                            if 'i2.2.1.0_1' not in subst1 or 'i2.2.1.1' not in subst1 or cons_f3(b=subst1["i2.2.1.0_1"], x=subst1["i2.2.1.1"]):
                                pass
                                if 'i2.2.1.0' not in subst1 or 'i2.2.1.1' not in subst1 or cons_f8(c=subst1["i2.2.1.0"], x=subst1["i2.2.1.1"]):
                                    pass
                                    if 'i2.2.1.2_1' not in subst1 or 'i2.2.1.1' not in subst1 or cons_f4(n=subst1["i2.2.1.2_1"], x=subst1["i2.2.1.1"]):
                                        pass
                                        # State 2387
                                        subst2 = Substitution(subst1)
                                        try:
                                            subst2.try_add_variable('i2.2.1.2', 1)
                                        except ValueError:
                                            pass
                                        else:
                                            pass
                                            if 'i2.2.1.2' not in subst2 or 'i2.2.1.2_1' not in subst2 or cons_f7(j=subst2["i2.2.1.2"], n=subst2["i2.2.1.2_1"]):
                                                pass
                                                # State 2388
                                                if len(subjects11) == 0:
                                                    pass
                                                    # State 2389
                                                    if len(subjects) == 0:
                                                        pass
                                                        # 1: v**m /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f4) and (cons_f5) and (cons_f7)
                                                        yield 1, subst2
                                        if len(subjects11) >= 1:
                                            tmp75 = subjects11.popleft()
                                            subst2 = Substitution(subst1)
                                            try:
                                                subst2.try_add_variable('i2.2.1.2', tmp75)
                                            except ValueError:
                                                pass
                                            else:
                                                pass
                                                if 'i2.2.1.2' not in subst2 or 'i2.2.1.2_1' not in subst2 or cons_f7(j=subst2["i2.2.1.2"], n=subst2["i2.2.1.2_1"]):
                                                    pass
                                                    # State 2388
                                                    if len(subjects11) == 0:
                                                        pass
                                                        # State 2389
                                                        if len(subjects) == 0:
                                                            pass
                                                            # 1: v**m /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f4) and (cons_f5) and (cons_f7)
                                                            yield 1, subst2
                                            subjects11.appendleft(tmp75)
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
                                                    # State 2562
                                                    if len(subjects11) == 0:
                                                        pass
                                                        # State 2563
                                                        if len(subjects) == 0:
                                                            pass
                                                            # 2: v**n /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f4) and (cons_f5) and (cons_f7)
                                                            yield 2, subst2
                                        if len(subjects11) >= 1:
                                            tmp78 = subjects11.popleft()
                                            subst2 = Substitution(subst1)
                                            try:
                                                subst2.try_add_variable('i2.2.1.2_1', tmp78)
                                            except ValueError:
                                                pass
                                            else:
                                                pass
                                                if 'i2.2.1.2_1' not in subst2 or 'i2.2.1.1' not in subst2 or cons_f4(n=subst2["i2.2.1.2_1"], x=subst2["i2.2.1.1"]):
                                                    pass
                                                    if 'i2.2.1.2' not in subst2 or 'i2.2.1.2_1' not in subst2 or cons_f7(j=subst2["i2.2.1.2"], n=subst2["i2.2.1.2_1"]):
                                                        pass
                                                        # State 2562
                                                        if len(subjects11) == 0:
                                                            pass
                                                            # State 2563
                                                            if len(subjects) == 0:
                                                                pass
                                                                # 2: v**n /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f4) and (cons_f5) and (cons_f7)
                                                                yield 2, subst2
                                            subjects11.appendleft(tmp78)
                                        if len(subjects11) >= 1:
                                            tmp80 = subjects11.popleft()
                                            subst2 = Substitution(subst1)
                                            try:
                                                subst2.try_add_variable('i2.2.1.2', tmp80)
                                            except ValueError:
                                                pass
                                            else:
                                                pass
                                            subjects11.appendleft(tmp80)
                                        subst2 = Substitution(subst1)
                                        try:
                                            subst2.try_add_variable('i2.2.1.2_2', 1)
                                        except ValueError:
                                            pass
                                        else:
                                            pass
                                        if len(subjects11) >= 1:
                                            tmp83 = subjects11.popleft()
                                            subst2 = Substitution(subst1)
                                            try:
                                                subst2.try_add_variable('i2.2.1.2_2', tmp83)
                                            except ValueError:
                                                pass
                                            else:
                                                pass
                                            subjects11.appendleft(tmp83)
                                        if len(subjects11) >= 1 and subjects11[0] == Integer(2):
                                            tmp85 = subjects11.popleft()
                                            # State 2874
                                            if len(subjects11) == 0:
                                                pass
                                                # State 2875
                                                if len(subjects) == 0:
                                                    pass
                                            subjects11.appendleft(tmp85)
                                    if 'i2.1.0' not in subst1 or 'i2.2.1.1' not in subst1 or cons_f29(d=subst1["i2.1.0"], x=subst1["i2.2.1.1"]):
                                        pass
                                        if 'i2.1.1.0' not in subst1 or 'i2.2.1.1' not in subst1 or cons_f50(e=subst1["i2.1.1.0"], x=subst1["i2.2.1.1"]):
                                            pass
                                            # State 2387
                                            subst2 = Substitution(subst1)
                                            try:
                                                subst2.try_add_variable('i2.2.1.2', 1)
                                            except ValueError:
                                                pass
                                            else:
                                                pass
                                            if len(subjects11) >= 1:
                                                tmp87 = subjects11.popleft()
                                                subst2 = Substitution(subst1)
                                                try:
                                                    subst2.try_add_variable('i2.2.1.2', tmp87)
                                                except ValueError:
                                                    pass
                                                else:
                                                    pass
                                                subjects11.appendleft(tmp87)
                                            subst2 = Substitution(subst1)
                                            try:
                                                subst2.try_add_variable('i2.2.1.2_1', 1)
                                            except ValueError:
                                                pass
                                            else:
                                                pass
                                            if len(subjects11) >= 1:
                                                tmp90 = subjects11.popleft()
                                                subst2 = Substitution(subst1)
                                                try:
                                                    subst2.try_add_variable('i2.2.1.2_1', tmp90)
                                                except ValueError:
                                                    pass
                                                else:
                                                    pass
                                                subjects11.appendleft(tmp90)
                                            if len(subjects11) >= 1:
                                                tmp92 = subjects11.popleft()
                                                subst2 = Substitution(subst1)
                                                try:
                                                    subst2.try_add_variable('i2.2.1.2', tmp92)
                                                except ValueError:
                                                    pass
                                                else:
                                                    pass
                                                subjects11.appendleft(tmp92)
                                            subst2 = Substitution(subst1)
                                            try:
                                                subst2.try_add_variable('i2.2.1.2_2', 1)
                                            except ValueError:
                                                pass
                                            else:
                                                pass
                                            if len(subjects11) >= 1:
                                                tmp95 = subjects11.popleft()
                                                subst2 = Substitution(subst1)
                                                try:
                                                    subst2.try_add_variable('i2.2.1.2_2', tmp95)
                                                except ValueError:
                                                    pass
                                                else:
                                                    pass
                                                subjects11.appendleft(tmp95)
                                            if len(subjects11) >= 1 and subjects11[0] == Integer(2):
                                                tmp97 = subjects11.popleft()
                                                # State 2874
                                                if len(subjects11) == 0:
                                                    pass
                                                    # State 2875
                                                    if len(subjects) == 0:
                                                        pass
                                                        # 10: x**2 /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f50) and (cons_f5)
                                                        yield 10, subst1
                                                subjects11.appendleft(tmp97)
                        if 'i2.2.1.0_1' not in subst1 or 'i2.2.1.1' not in subst1 or cons_f3(b=subst1["i2.2.1.0_1"], x=subst1["i2.2.1.1"]):
                            pass
                            if 'i2.2.1.0' not in subst1 or 'i2.2.1.1' not in subst1 or cons_f8(c=subst1["i2.2.1.0"], x=subst1["i2.2.1.1"]):
                                pass
                                # State 2387
                                subst2 = Substitution(subst1)
                                try:
                                    subst2.try_add_variable('i2.2.1.2', 1)
                                except ValueError:
                                    pass
                                else:
                                    pass
                                if len(subjects11) >= 1:
                                    tmp99 = subjects11.popleft()
                                    subst2 = Substitution(subst1)
                                    try:
                                        subst2.try_add_variable('i2.2.1.2', tmp99)
                                    except ValueError:
                                        pass
                                    else:
                                        pass
                                    subjects11.appendleft(tmp99)
                                subst2 = Substitution(subst1)
                                try:
                                    subst2.try_add_variable('i2.2.1.2_1', 1)
                                except ValueError:
                                    pass
                                else:
                                    pass
                                if len(subjects11) >= 1:
                                    tmp102 = subjects11.popleft()
                                    subst2 = Substitution(subst1)
                                    try:
                                        subst2.try_add_variable('i2.2.1.2_1', tmp102)
                                    except ValueError:
                                        pass
                                    else:
                                        pass
                                    subjects11.appendleft(tmp102)
                                if len(subjects11) >= 1:
                                    tmp104 = subjects11.popleft()
                                    subst2 = Substitution(subst1)
                                    try:
                                        subst2.try_add_variable('i2.2.1.2', tmp104)
                                    except ValueError:
                                        pass
                                    else:
                                        pass
                                    subjects11.appendleft(tmp104)
                                subst2 = Substitution(subst1)
                                try:
                                    subst2.try_add_variable('i2.2.1.2_2', 1)
                                except ValueError:
                                    pass
                                else:
                                    pass
                                if len(subjects11) >= 1:
                                    tmp107 = subjects11.popleft()
                                    subst2 = Substitution(subst1)
                                    try:
                                        subst2.try_add_variable('i2.2.1.2_2', tmp107)
                                    except ValueError:
                                        pass
                                    else:
                                        pass
                                    subjects11.appendleft(tmp107)
                                if len(subjects11) >= 1 and subjects11[0] == Integer(2):
                                    tmp109 = subjects11.popleft()
                                    # State 2874
                                    if len(subjects11) == 0:
                                        pass
                                        # State 2875
                                        if len(subjects) == 0:
                                            pass
                                            # 7: x**2 /; (cons_f2) and (cons_f3) and (cons_f8)
                                            yield 7, subst1
                                    subjects11.appendleft(tmp109)
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
                                                # State 2387
                                                subst2 = Substitution(subst1)
                                                try:
                                                    subst2.try_add_variable('i2.2.1.2', 1)
                                                except ValueError:
                                                    pass
                                                else:
                                                    pass
                                                    if 'i2.2.1.2' not in subst2 or 'i2.2.1.1' not in subst2 or cons_f4(n=subst2["i2.2.1.2"], x=subst2["i2.2.1.1"]):
                                                        pass
                                                        if 'i2.2.1.2' not in subst2 or 'i2.2_1' not in subst2 or cons_f58(m=subst2["i2.2_1"], n=subst2["i2.2.1.2"]):
                                                            pass
                                                            # State 2388
                                                            if len(subjects11) == 0:
                                                                pass
                                                                # State 2389
                                                                if len(subjects) == 0:
                                                                    pass
                                                                    # 18: v**m /; (cons_f59) and (cons_f60) and (cons_f61) and (cons_f62) and (cons_f19) and (cons_f4) and (cons_f5) and (cons_f58)
                                                                    yield 18, subst2
                                                if len(subjects11) >= 1:
                                                    tmp111 = subjects11.popleft()
                                                    subst2 = Substitution(subst1)
                                                    try:
                                                        subst2.try_add_variable('i2.2.1.2', tmp111)
                                                    except ValueError:
                                                        pass
                                                    else:
                                                        pass
                                                        if 'i2.2.1.2' not in subst2 or 'i2.2.1.1' not in subst2 or cons_f4(n=subst2["i2.2.1.2"], x=subst2["i2.2.1.1"]):
                                                            pass
                                                            if 'i2.2.1.2' not in subst2 or 'i2.2_1' not in subst2 or cons_f58(m=subst2["i2.2_1"], n=subst2["i2.2.1.2"]):
                                                                pass
                                                                # State 2388
                                                                if len(subjects11) == 0:
                                                                    pass
                                                                    # State 2389
                                                                    if len(subjects) == 0:
                                                                        pass
                                                                        # 18: v**m /; (cons_f59) and (cons_f60) and (cons_f61) and (cons_f62) and (cons_f19) and (cons_f4) and (cons_f5) and (cons_f58)
                                                                        yield 18, subst2
                                                    subjects11.appendleft(tmp111)
                                                subst2 = Substitution(subst1)
                                                try:
                                                    subst2.try_add_variable('i2.2.1.2_1', 1)
                                                except ValueError:
                                                    pass
                                                else:
                                                    pass
                                                if len(subjects11) >= 1:
                                                    tmp114 = subjects11.popleft()
                                                    subst2 = Substitution(subst1)
                                                    try:
                                                        subst2.try_add_variable('i2.2.1.2_1', tmp114)
                                                    except ValueError:
                                                        pass
                                                    else:
                                                        pass
                                                    subjects11.appendleft(tmp114)
                                                if len(subjects11) >= 1:
                                                    tmp116 = subjects11.popleft()
                                                    subst2 = Substitution(subst1)
                                                    try:
                                                        subst2.try_add_variable('i2.2.1.2', tmp116)
                                                    except ValueError:
                                                        pass
                                                    else:
                                                        pass
                                                    subjects11.appendleft(tmp116)
                                                subst2 = Substitution(subst1)
                                                try:
                                                    subst2.try_add_variable('i2.2.1.2_2', 1)
                                                except ValueError:
                                                    pass
                                                else:
                                                    pass
                                                if len(subjects11) >= 1:
                                                    tmp119 = subjects11.popleft()
                                                    subst2 = Substitution(subst1)
                                                    try:
                                                        subst2.try_add_variable('i2.2.1.2_2', tmp119)
                                                    except ValueError:
                                                        pass
                                                    else:
                                                        pass
                                                    subjects11.appendleft(tmp119)
                                                if len(subjects11) >= 1 and subjects11[0] == Integer(2):
                                                    tmp121 = subjects11.popleft()
                                                    # State 2874
                                                    if len(subjects11) == 0:
                                                        pass
                                                        # State 2875
                                                        if len(subjects) == 0:
                                                            pass
                                                    subjects11.appendleft(tmp121)
                    if 'i2.2' not in subst1 or 'i2.2.1.1' not in subst1 or cons_f5(p=subst1["i2.2"], x=subst1["i2.2.1.1"]):
                        pass
                        if 'i2.2.1.0_1' not in subst1 or 'i2.2.1.1' not in subst1 or cons_f3(b=subst1["i2.2.1.0_1"], x=subst1["i2.2.1.1"]):
                            pass
                            if 'i2.2.1.2_1' not in subst1 or 'i2.2.1.1' not in subst1 or cons_f4(n=subst1["i2.2.1.2_1"], x=subst1["i2.2.1.1"]):
                                pass
                                if 'i2.2.0_1' not in subst1 or 'i2.2.1.1' not in subst1 or cons_f2(a=subst1["i2.2.0_1"], x=subst1["i2.2.1.1"]):
                                    pass
                                    if 'i2.2.0' not in subst1 or 'i2.2.1.1' not in subst1 or cons_f8(c=subst1["i2.2.0"], x=subst1["i2.2.1.1"]):
                                        pass
                                        if 'i2.2.1.0' not in subst1 or 'i2.2.1.1' not in subst1 or cons_f29(d=subst1["i2.2.1.0"], x=subst1["i2.2.1.1"]):
                                            pass
                                            if 'i2.2_1' not in subst1 or 'i2.2.1.1' not in subst1 or cons_f19(m=subst1["i2.2_1"], x=subst1["i2.2.1.1"]):
                                                pass
                                                # State 2387
                                                subst2 = Substitution(subst1)
                                                try:
                                                    subst2.try_add_variable('i2.2.1.2', 1)
                                                except ValueError:
                                                    pass
                                                else:
                                                    pass
                                                if len(subjects11) >= 1:
                                                    tmp123 = subjects11.popleft()
                                                    subst2 = Substitution(subst1)
                                                    try:
                                                        subst2.try_add_variable('i2.2.1.2', tmp123)
                                                    except ValueError:
                                                        pass
                                                    else:
                                                        pass
                                                    subjects11.appendleft(tmp123)
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
                                                            # State 2562
                                                            if len(subjects11) == 0:
                                                                pass
                                                                # State 2563
                                                                if len(subjects) == 0:
                                                                    pass
                                                                    # 5: v**n /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f19) and (cons_f4) and (cons_f5) and (cons_f7)
                                                                    yield 5, subst2
                                                if len(subjects11) >= 1:
                                                    tmp126 = subjects11.popleft()
                                                    subst2 = Substitution(subst1)
                                                    try:
                                                        subst2.try_add_variable('i2.2.1.2_1', tmp126)
                                                    except ValueError:
                                                        pass
                                                    else:
                                                        pass
                                                        if 'i2.2.1.2_1' not in subst2 or 'i2.2.1.1' not in subst2 or cons_f4(n=subst2["i2.2.1.2_1"], x=subst2["i2.2.1.1"]):
                                                            pass
                                                            if 'i2.2.1.2' not in subst2 or 'i2.2.1.2_1' not in subst2 or cons_f7(j=subst2["i2.2.1.2"], n=subst2["i2.2.1.2_1"]):
                                                                pass
                                                                # State 2562
                                                                if len(subjects11) == 0:
                                                                    pass
                                                                    # State 2563
                                                                    if len(subjects) == 0:
                                                                        pass
                                                                        # 5: v**n /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f19) and (cons_f4) and (cons_f5) and (cons_f7)
                                                                        yield 5, subst2
                                                    subjects11.appendleft(tmp126)
                                                if len(subjects11) >= 1:
                                                    tmp128 = subjects11.popleft()
                                                    subst2 = Substitution(subst1)
                                                    try:
                                                        subst2.try_add_variable('i2.2.1.2', tmp128)
                                                    except ValueError:
                                                        pass
                                                    else:
                                                        pass
                                                        if 'i2.2.1.2' not in subst2 or 'i2.2.1.2_1' not in subst2 or cons_f7(j=subst2["i2.2.1.2"], n=subst2["i2.2.1.2_1"]):
                                                            pass
                                                            # State 2833
                                                            if len(subjects11) == 0:
                                                                pass
                                                                # State 2834
                                                                if len(subjects) == 0:
                                                                    pass
                                                                    # 6: x**j /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f19) and (cons_f4) and (cons_f5) and (cons_f7)
                                                                    yield 6, subst2
                                                    subjects11.appendleft(tmp128)
                                                subst2 = Substitution(subst1)
                                                try:
                                                    subst2.try_add_variable('i2.2.1.2_2', 1)
                                                except ValueError:
                                                    pass
                                                else:
                                                    pass
                                                if len(subjects11) >= 1:
                                                    tmp131 = subjects11.popleft()
                                                    subst2 = Substitution(subst1)
                                                    try:
                                                        subst2.try_add_variable('i2.2.1.2_2', tmp131)
                                                    except ValueError:
                                                        pass
                                                    else:
                                                        pass
                                                    subjects11.appendleft(tmp131)
                                                if len(subjects11) >= 1 and subjects11[0] == Integer(2):
                                                    tmp133 = subjects11.popleft()
                                                    # State 2874
                                                    if len(subjects11) == 0:
                                                        pass
                                                        # State 2875
                                                        if len(subjects) == 0:
                                                            pass
                                                    subjects11.appendleft(tmp133)
                    if 'i2.2.1.0_1' not in subst1 or 'i2.2.1.1' not in subst1 or cons_f3(b=subst1["i2.2.1.0_1"], x=subst1["i2.2.1.1"]):
                        pass
                        if 'i2.2.1.0' not in subst1 or 'i2.2.1.1' not in subst1 or cons_f2(a=subst1["i2.2.1.0"], x=subst1["i2.2.1.1"]):
                            pass
                            if 'i2.2.1.2' not in subst1 or 'i2.2.1.1' not in subst1 or cons_f5(p=subst1["i2.2.1.2"], x=subst1["i2.2.1.1"]):
                                pass
                                if 'i2.2.1.2_1' not in subst1 or 'i2.2.1.1' not in subst1 or cons_f52(q=subst1["i2.2.1.2_1"], x=subst1["i2.2.1.1"]):
                                    pass
                                    if 'i2.2.1.0_2' not in subst1 or 'i2.2.1.1' not in subst1 or cons_f8(c=subst1["i2.2.1.0_2"], x=subst1["i2.2.1.1"]):
                                        pass
                                        if 'i2.2.1.2_2' not in subst1 or 'i2.2.1.1' not in subst1 or cons_f54(r=subst1["i2.2.1.2_2"], x=subst1["i2.2.1.1"]):
                                            pass
                                            # State 2387
                                            subst2 = Substitution(subst1)
                                            try:
                                                subst2.try_add_variable('i2.2.1.2', 1)
                                            except ValueError:
                                                pass
                                            else:
                                                pass
                                                if 'i2.2.1.2' not in subst2 or 'i2.2.1.1' not in subst2 or cons_f5(p=subst2["i2.2.1.2"], x=subst2["i2.2.1.1"]):
                                                    pass
                                                    if 'i2.2.1.2' not in subst2 or 'i2.2.1.2_1' not in subst2 or cons_f51(p=subst2["i2.2.1.2"], q=subst2["i2.2.1.2_1"]):
                                                        pass
                                                        if 'i2.2.1.2' not in subst2 or 'i2.2.1.2_2' not in subst2 or cons_f53(p=subst2["i2.2.1.2"], r=subst2["i2.2.1.2_2"]):
                                                            pass
                                                            # State 2388
                                                            if len(subjects11) == 0:
                                                                pass
                                                                # State 2389
                                                                if len(subjects) == 0:
                                                                    pass
                                                                    # 13: v**m /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f5) and (cons_f52) and (cons_f54) and (cons_f51) and (cons_f53)
                                                                    yield 13, subst2
                                            if len(subjects11) >= 1:
                                                tmp135 = subjects11.popleft()
                                                subst2 = Substitution(subst1)
                                                try:
                                                    subst2.try_add_variable('i2.2.1.2', tmp135)
                                                except ValueError:
                                                    pass
                                                else:
                                                    pass
                                                    if 'i2.2.1.2' not in subst2 or 'i2.2.1.1' not in subst2 or cons_f5(p=subst2["i2.2.1.2"], x=subst2["i2.2.1.1"]):
                                                        pass
                                                        if 'i2.2.1.2' not in subst2 or 'i2.2.1.2_1' not in subst2 or cons_f51(p=subst2["i2.2.1.2"], q=subst2["i2.2.1.2_1"]):
                                                            pass
                                                            if 'i2.2.1.2' not in subst2 or 'i2.2.1.2_2' not in subst2 or cons_f53(p=subst2["i2.2.1.2"], r=subst2["i2.2.1.2_2"]):
                                                                pass
                                                                # State 2388
                                                                if len(subjects11) == 0:
                                                                    pass
                                                                    # State 2389
                                                                    if len(subjects) == 0:
                                                                        pass
                                                                        # 13: v**m /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f5) and (cons_f52) and (cons_f54) and (cons_f51) and (cons_f53)
                                                                        yield 13, subst2
                                                subjects11.appendleft(tmp135)
                                            subst2 = Substitution(subst1)
                                            try:
                                                subst2.try_add_variable('i2.2.1.2_1', 1)
                                            except ValueError:
                                                pass
                                            else:
                                                pass
                                                if 'i2.2.1.2_1' not in subst2 or 'i2.2.1.1' not in subst2 or cons_f52(q=subst2["i2.2.1.2_1"], x=subst2["i2.2.1.1"]):
                                                    pass
                                                    if 'i2.2.1.2' not in subst2 or 'i2.2.1.2_1' not in subst2 or cons_f51(p=subst2["i2.2.1.2"], q=subst2["i2.2.1.2_1"]):
                                                        pass
                                                        # State 2562
                                                        if len(subjects11) == 0:
                                                            pass
                                                            # State 2563
                                                            if len(subjects) == 0:
                                                                pass
                                                                # 14: v**n /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f5) and (cons_f52) and (cons_f54) and (cons_f51)
                                                                yield 14, subst2
                                            if len(subjects11) >= 1:
                                                tmp138 = subjects11.popleft()
                                                subst2 = Substitution(subst1)
                                                try:
                                                    subst2.try_add_variable('i2.2.1.2_1', tmp138)
                                                except ValueError:
                                                    pass
                                                else:
                                                    pass
                                                    if 'i2.2.1.2_1' not in subst2 or 'i2.2.1.1' not in subst2 or cons_f52(q=subst2["i2.2.1.2_1"], x=subst2["i2.2.1.1"]):
                                                        pass
                                                        if 'i2.2.1.2' not in subst2 or 'i2.2.1.2_1' not in subst2 or cons_f51(p=subst2["i2.2.1.2"], q=subst2["i2.2.1.2_1"]):
                                                            pass
                                                            # State 2562
                                                            if len(subjects11) == 0:
                                                                pass
                                                                # State 2563
                                                                if len(subjects) == 0:
                                                                    pass
                                                                    # 14: v**n /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f5) and (cons_f52) and (cons_f54) and (cons_f51)
                                                                    yield 14, subst2
                                                subjects11.appendleft(tmp138)
                                            if len(subjects11) >= 1:
                                                tmp140 = subjects11.popleft()
                                                subst2 = Substitution(subst1)
                                                try:
                                                    subst2.try_add_variable('i2.2.1.2', tmp140)
                                                except ValueError:
                                                    pass
                                                else:
                                                    pass
                                                subjects11.appendleft(tmp140)
                                            subst2 = Substitution(subst1)
                                            try:
                                                subst2.try_add_variable('i2.2.1.2_2', 1)
                                            except ValueError:
                                                pass
                                            else:
                                                pass
                                                if 'i2.2.1.2_2' not in subst2 or 'i2.2.1.1' not in subst2 or cons_f54(r=subst2["i2.2.1.2_2"], x=subst2["i2.2.1.1"]):
                                                    pass
                                                    if 'i2.2.1.2' not in subst2 or 'i2.2.1.2_2' not in subst2 or cons_f53(p=subst2["i2.2.1.2"], r=subst2["i2.2.1.2_2"]):
                                                        pass
                                                        # State 3009
                                                        if len(subjects11) == 0:
                                                            pass
                                                            # State 3010
                                                            if len(subjects) == 0:
                                                                pass
                                                                # 15: x**r /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f5) and (cons_f52) and (cons_f54) and (cons_f53)
                                                                yield 15, subst2
                                            if len(subjects11) >= 1:
                                                tmp143 = subjects11.popleft()
                                                subst2 = Substitution(subst1)
                                                try:
                                                    subst2.try_add_variable('i2.2.1.2_2', tmp143)
                                                except ValueError:
                                                    pass
                                                else:
                                                    pass
                                                    if 'i2.2.1.2_2' not in subst2 or 'i2.2.1.1' not in subst2 or cons_f54(r=subst2["i2.2.1.2_2"], x=subst2["i2.2.1.1"]):
                                                        pass
                                                        if 'i2.2.1.2' not in subst2 or 'i2.2.1.2_2' not in subst2 or cons_f53(p=subst2["i2.2.1.2"], r=subst2["i2.2.1.2_2"]):
                                                            pass
                                                            # State 3009
                                                            if len(subjects11) == 0:
                                                                pass
                                                                # State 3010
                                                                if len(subjects) == 0:
                                                                    pass
                                                                    # 15: x**r /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f5) and (cons_f52) and (cons_f54) and (cons_f53)
                                                                    yield 15, subst2
                                                subjects11.appendleft(tmp143)
                                            if len(subjects11) >= 1 and subjects11[0] == Integer(2):
                                                tmp145 = subjects11.popleft()
                                                # State 2874
                                                if len(subjects11) == 0:
                                                    pass
                                                    # State 2875
                                                    if len(subjects) == 0:
                                                        pass
                                                subjects11.appendleft(tmp145)
                                    # State 2387
                                    subst2 = Substitution(subst1)
                                    try:
                                        subst2.try_add_variable('i2.2.1.2', 1)
                                    except ValueError:
                                        pass
                                    else:
                                        pass
                                        if 'i2.2.1.2' not in subst2 or 'i2.2.1.1' not in subst2 or cons_f5(p=subst2["i2.2.1.2"], x=subst2["i2.2.1.1"]):
                                            pass
                                            if 'i2.2.1.2' not in subst2 or 'i2.2.1.2_1' not in subst2 or cons_f51(p=subst2["i2.2.1.2"], q=subst2["i2.2.1.2_1"]):
                                                pass
                                                # State 2388
                                                if len(subjects11) == 0:
                                                    pass
                                                    # State 2389
                                                    if len(subjects) == 0:
                                                        pass
                                                        # 11: v**m /; (cons_f2) and (cons_f3) and (cons_f5) and (cons_f52) and (cons_f51)
                                                        yield 11, subst2
                                    if len(subjects11) >= 1:
                                        tmp147 = subjects11.popleft()
                                        subst2 = Substitution(subst1)
                                        try:
                                            subst2.try_add_variable('i2.2.1.2', tmp147)
                                        except ValueError:
                                            pass
                                        else:
                                            pass
                                            if 'i2.2.1.2' not in subst2 or 'i2.2.1.1' not in subst2 or cons_f5(p=subst2["i2.2.1.2"], x=subst2["i2.2.1.1"]):
                                                pass
                                                if 'i2.2.1.2' not in subst2 or 'i2.2.1.2_1' not in subst2 or cons_f51(p=subst2["i2.2.1.2"], q=subst2["i2.2.1.2_1"]):
                                                    pass
                                                    # State 2388
                                                    if len(subjects11) == 0:
                                                        pass
                                                        # State 2389
                                                        if len(subjects) == 0:
                                                            pass
                                                            # 11: v**m /; (cons_f2) and (cons_f3) and (cons_f5) and (cons_f52) and (cons_f51)
                                                            yield 11, subst2
                                        subjects11.appendleft(tmp147)
                                    subst2 = Substitution(subst1)
                                    try:
                                        subst2.try_add_variable('i2.2.1.2_1', 1)
                                    except ValueError:
                                        pass
                                    else:
                                        pass
                                        if 'i2.2.1.2_1' not in subst2 or 'i2.2.1.1' not in subst2 or cons_f52(q=subst2["i2.2.1.2_1"], x=subst2["i2.2.1.1"]):
                                            pass
                                            if 'i2.2.1.2' not in subst2 or 'i2.2.1.2_1' not in subst2 or cons_f51(p=subst2["i2.2.1.2"], q=subst2["i2.2.1.2_1"]):
                                                pass
                                                # State 2562
                                                if len(subjects11) == 0:
                                                    pass
                                                    # State 2563
                                                    if len(subjects) == 0:
                                                        pass
                                                        # 12: v**n /; (cons_f2) and (cons_f3) and (cons_f5) and (cons_f52) and (cons_f51)
                                                        yield 12, subst2
                                    if len(subjects11) >= 1:
                                        tmp150 = subjects11.popleft()
                                        subst2 = Substitution(subst1)
                                        try:
                                            subst2.try_add_variable('i2.2.1.2_1', tmp150)
                                        except ValueError:
                                            pass
                                        else:
                                            pass
                                            if 'i2.2.1.2_1' not in subst2 or 'i2.2.1.1' not in subst2 or cons_f52(q=subst2["i2.2.1.2_1"], x=subst2["i2.2.1.1"]):
                                                pass
                                                if 'i2.2.1.2' not in subst2 or 'i2.2.1.2_1' not in subst2 or cons_f51(p=subst2["i2.2.1.2"], q=subst2["i2.2.1.2_1"]):
                                                    pass
                                                    # State 2562
                                                    if len(subjects11) == 0:
                                                        pass
                                                        # State 2563
                                                        if len(subjects) == 0:
                                                            pass
                                                            # 12: v**n /; (cons_f2) and (cons_f3) and (cons_f5) and (cons_f52) and (cons_f51)
                                                            yield 12, subst2
                                        subjects11.appendleft(tmp150)
                                    if len(subjects11) >= 1:
                                        tmp152 = subjects11.popleft()
                                        subst2 = Substitution(subst1)
                                        try:
                                            subst2.try_add_variable('i2.2.1.2', tmp152)
                                        except ValueError:
                                            pass
                                        else:
                                            pass
                                        subjects11.appendleft(tmp152)
                                    subst2 = Substitution(subst1)
                                    try:
                                        subst2.try_add_variable('i2.2.1.2_2', 1)
                                    except ValueError:
                                        pass
                                    else:
                                        pass
                                    if len(subjects11) >= 1:
                                        tmp155 = subjects11.popleft()
                                        subst2 = Substitution(subst1)
                                        try:
                                            subst2.try_add_variable('i2.2.1.2_2', tmp155)
                                        except ValueError:
                                            pass
                                        else:
                                            pass
                                        subjects11.appendleft(tmp155)
                                    if len(subjects11) >= 1 and subjects11[0] == Integer(2):
                                        tmp157 = subjects11.popleft()
                                        # State 2874
                                        if len(subjects11) == 0:
                                            pass
                                            # State 2875
                                            if len(subjects) == 0:
                                                pass
                                        subjects11.appendleft(tmp157)
                    if 'i2' not in subst1 or 'i2.2.1.1' not in subst1 or cons_f11(Pm=subst1["i2.2.1.1"], x=subst1["i2"]):
                        pass
                        if 'i2' not in subst1 or 'i2.2.1.1' not in subst1 or 'i2.2.1.0' not in subst1 or 'i2.2.0' not in subst1 or 'i2.0' not in subst1 or 'i2.2' not in subst1 or 'i2.2.1.2' not in subst1 or With35(Pm=subst1["i2.2.1.1"], Qm=subst1["i2.0"], a=subst1["i2.2.0"], b=subst1["i2.2.1.0"], n=subst1["i2.2.1.2"], p=subst1["i2.2"], x=subst1["i2"]):
                            pass
                            # State 2387
                            subst2 = Substitution(subst1)
                            try:
                                subst2.try_add_variable('i2.2.1.2', 1)
                            except ValueError:
                                pass
                            else:
                                pass
                                if 'i2.2.1.2' not in subst2 or 'i2' not in subst2 or cons_f4(n=subst2["i2.2.1.2"], x=subst2["i2"]):
                                    pass
                                    if 'i2' not in subst2 or 'i2.2.1.1' not in subst2 or 'i2.2.1.0' not in subst2 or 'i2.2.0' not in subst2 or 'i2.0' not in subst2 or 'i2.2' not in subst2 or 'i2.2.1.2' not in subst2 or With35(Pm=subst2["i2.2.1.1"], Qm=subst2["i2.0"], a=subst2["i2.2.0"], b=subst2["i2.2.1.0"], n=subst2["i2.2.1.2"], p=subst2["i2.2"], x=subst2["i2"]):
                                        pass
                                        # State 2388
                                        if len(subjects11) == 0:
                                            pass
                                            # State 2389
                                            if len(subjects) == 0:
                                                pass
                                                # 19: v**m /; (cons_f4) and (cons_f11) and (With35)
                                                yield 19, subst2
                            if len(subjects11) >= 1:
                                tmp159 = subjects11.popleft()
                                subst2 = Substitution(subst1)
                                try:
                                    subst2.try_add_variable('i2.2.1.2', tmp159)
                                except ValueError:
                                    pass
                                else:
                                    pass
                                    if 'i2.2.1.2' not in subst2 or 'i2' not in subst2 or cons_f4(n=subst2["i2.2.1.2"], x=subst2["i2"]):
                                        pass
                                        if 'i2' not in subst2 or 'i2.2.1.1' not in subst2 or 'i2.2.1.0' not in subst2 or 'i2.2.0' not in subst2 or 'i2.0' not in subst2 or 'i2.2' not in subst2 or 'i2.2.1.2' not in subst2 or With35(Pm=subst2["i2.2.1.1"], Qm=subst2["i2.0"], a=subst2["i2.2.0"], b=subst2["i2.2.1.0"], n=subst2["i2.2.1.2"], p=subst2["i2.2"], x=subst2["i2"]):
                                            pass
                                            # State 2388
                                            if len(subjects11) == 0:
                                                pass
                                                # State 2389
                                                if len(subjects) == 0:
                                                    pass
                                                    # 19: v**m /; (cons_f4) and (cons_f11) and (With35)
                                                    yield 19, subst2
                                subjects11.appendleft(tmp159)
                            subst2 = Substitution(subst1)
                            try:
                                subst2.try_add_variable('i2.2.1.2_1', 1)
                            except ValueError:
                                pass
                            else:
                                pass
                            if len(subjects11) >= 1:
                                tmp162 = subjects11.popleft()
                                subst2 = Substitution(subst1)
                                try:
                                    subst2.try_add_variable('i2.2.1.2_1', tmp162)
                                except ValueError:
                                    pass
                                else:
                                    pass
                                subjects11.appendleft(tmp162)
                            if len(subjects11) >= 1:
                                tmp164 = subjects11.popleft()
                                subst2 = Substitution(subst1)
                                try:
                                    subst2.try_add_variable('i2.2.1.2', tmp164)
                                except ValueError:
                                    pass
                                else:
                                    pass
                                subjects11.appendleft(tmp164)
                            subst2 = Substitution(subst1)
                            try:
                                subst2.try_add_variable('i2.2.1.2_2', 1)
                            except ValueError:
                                pass
                            else:
                                pass
                            if len(subjects11) >= 1:
                                tmp167 = subjects11.popleft()
                                subst2 = Substitution(subst1)
                                try:
                                    subst2.try_add_variable('i2.2.1.2_2', tmp167)
                                except ValueError:
                                    pass
                                else:
                                    pass
                                subjects11.appendleft(tmp167)
                            if len(subjects11) >= 1 and subjects11[0] == Integer(2):
                                tmp169 = subjects11.popleft()
                                # State 2874
                                if len(subjects11) == 0:
                                    pass
                                    # State 2875
                                    if len(subjects) == 0:
                                        pass
                                subjects11.appendleft(tmp169)
                        if 'i2' not in subst1 or 'i2.2.1.1' not in subst1 or 'i2.2.1.0' not in subst1 or 'i2.2.0' not in subst1 or 'i2.0' not in subst1 or 'i2.2.1.2_1' not in subst1 or 'i2.2.1.2' not in subst1 or 'i2.2' not in subst1 or 'i2.2.1.0_1' not in subst1 or With36(Pm=subst1["i2.2.1.1"], Qm=subst1["i2.0"], a=subst1["i2.2.0"], b=subst1["i2.2.1.0"], c=subst1["i2.2.1.0_1"], n=subst1["i2.2.1.2"], n2=subst1["i2.2.1.2_1"], p=subst1["i2.2"], x=subst1["i2"]):
                            pass
                            # State 2387
                            subst2 = Substitution(subst1)
                            try:
                                subst2.try_add_variable('i2.2.1.2', 1)
                            except ValueError:
                                pass
                            else:
                                pass
                                if 'i2.2.1.2' not in subst2 or 'i2.2.1.2_1' not in subst2 or cons_f48(n=subst2["i2.2.1.2"], n2=subst2["i2.2.1.2_1"]):
                                    pass
                                    if 'i2.2.1.2' not in subst2 or 'i2' not in subst2 or cons_f4(n=subst2["i2.2.1.2"], x=subst2["i2"]):
                                        pass
                                        if 'i2' not in subst2 or 'i2.2.1.1' not in subst2 or 'i2.2.1.0' not in subst2 or 'i2.2.0' not in subst2 or 'i2.0' not in subst2 or 'i2.2.1.2_1' not in subst2 or 'i2.2.1.2' not in subst2 or 'i2.2' not in subst2 or 'i2.2.1.0_1' not in subst2 or With36(Pm=subst2["i2.2.1.1"], Qm=subst2["i2.0"], a=subst2["i2.2.0"], b=subst2["i2.2.1.0"], c=subst2["i2.2.1.0_1"], n=subst2["i2.2.1.2"], n2=subst2["i2.2.1.2_1"], p=subst2["i2.2"], x=subst2["i2"]):
                                            pass
                                            # State 2388
                                            if len(subjects11) == 0:
                                                pass
                                                # State 2389
                                                if len(subjects) == 0:
                                                    pass
                                                    # 20: v**m /; (cons_f4) and (cons_f48) and (cons_f11) and (With36)
                                                    yield 20, subst2
                            if len(subjects11) >= 1:
                                tmp171 = subjects11.popleft()
                                subst2 = Substitution(subst1)
                                try:
                                    subst2.try_add_variable('i2.2.1.2', tmp171)
                                except ValueError:
                                    pass
                                else:
                                    pass
                                    if 'i2.2.1.2' not in subst2 or 'i2.2.1.2_1' not in subst2 or cons_f48(n=subst2["i2.2.1.2"], n2=subst2["i2.2.1.2_1"]):
                                        pass
                                        if 'i2.2.1.2' not in subst2 or 'i2' not in subst2 or cons_f4(n=subst2["i2.2.1.2"], x=subst2["i2"]):
                                            pass
                                            if 'i2' not in subst2 or 'i2.2.1.1' not in subst2 or 'i2.2.1.0' not in subst2 or 'i2.2.0' not in subst2 or 'i2.0' not in subst2 or 'i2.2.1.2_1' not in subst2 or 'i2.2.1.2' not in subst2 or 'i2.2' not in subst2 or 'i2.2.1.0_1' not in subst2 or With36(Pm=subst2["i2.2.1.1"], Qm=subst2["i2.0"], a=subst2["i2.2.0"], b=subst2["i2.2.1.0"], c=subst2["i2.2.1.0_1"], n=subst2["i2.2.1.2"], n2=subst2["i2.2.1.2_1"], p=subst2["i2.2"], x=subst2["i2"]):
                                                pass
                                                # State 2388
                                                if len(subjects11) == 0:
                                                    pass
                                                    # State 2389
                                                    if len(subjects) == 0:
                                                        pass
                                                        # 20: v**m /; (cons_f4) and (cons_f48) and (cons_f11) and (With36)
                                                        yield 20, subst2
                                subjects11.appendleft(tmp171)
                            subst2 = Substitution(subst1)
                            try:
                                subst2.try_add_variable('i2.2.1.2_1', 1)
                            except ValueError:
                                pass
                            else:
                                pass
                                if 'i2.2.1.2' not in subst2 or 'i2.2.1.2_1' not in subst2 or cons_f48(n=subst2["i2.2.1.2"], n2=subst2["i2.2.1.2_1"]):
                                    pass
                                    if 'i2' not in subst2 or 'i2.2.1.1' not in subst2 or 'i2.2.1.0' not in subst2 or 'i2.2.0' not in subst2 or 'i2.0' not in subst2 or 'i2.2.1.2_1' not in subst2 or 'i2.2.1.2' not in subst2 or 'i2.2' not in subst2 or 'i2.2.1.0_1' not in subst2 or With36(Pm=subst2["i2.2.1.1"], Qm=subst2["i2.0"], a=subst2["i2.2.0"], b=subst2["i2.2.1.0"], c=subst2["i2.2.1.0_1"], n=subst2["i2.2.1.2"], n2=subst2["i2.2.1.2_1"], p=subst2["i2.2"], x=subst2["i2"]):
                                        pass
                                        # State 2562
                                        if len(subjects11) == 0:
                                            pass
                                            # State 2563
                                            if len(subjects) == 0:
                                                pass
                                                # 21: v**n /; (cons_f48) and (cons_f11) and (With36)
                                                yield 21, subst2
                            if len(subjects11) >= 1:
                                tmp174 = subjects11.popleft()
                                subst2 = Substitution(subst1)
                                try:
                                    subst2.try_add_variable('i2.2.1.2_1', tmp174)
                                except ValueError:
                                    pass
                                else:
                                    pass
                                    if 'i2.2.1.2' not in subst2 or 'i2.2.1.2_1' not in subst2 or cons_f48(n=subst2["i2.2.1.2"], n2=subst2["i2.2.1.2_1"]):
                                        pass
                                        if 'i2' not in subst2 or 'i2.2.1.1' not in subst2 or 'i2.2.1.0' not in subst2 or 'i2.2.0' not in subst2 or 'i2.0' not in subst2 or 'i2.2.1.2_1' not in subst2 or 'i2.2.1.2' not in subst2 or 'i2.2' not in subst2 or 'i2.2.1.0_1' not in subst2 or With36(Pm=subst2["i2.2.1.1"], Qm=subst2["i2.0"], a=subst2["i2.2.0"], b=subst2["i2.2.1.0"], c=subst2["i2.2.1.0_1"], n=subst2["i2.2.1.2"], n2=subst2["i2.2.1.2_1"], p=subst2["i2.2"], x=subst2["i2"]):
                                            pass
                                            # State 2562
                                            if len(subjects11) == 0:
                                                pass
                                                # State 2563
                                                if len(subjects) == 0:
                                                    pass
                                                    # 21: v**n /; (cons_f48) and (cons_f11) and (With36)
                                                    yield 21, subst2
                                subjects11.appendleft(tmp174)
                            if len(subjects11) >= 1:
                                tmp176 = subjects11.popleft()
                                subst2 = Substitution(subst1)
                                try:
                                    subst2.try_add_variable('i2.2.1.2', tmp176)
                                except ValueError:
                                    pass
                                else:
                                    pass
                                subjects11.appendleft(tmp176)
                            subst2 = Substitution(subst1)
                            try:
                                subst2.try_add_variable('i2.2.1.2_2', 1)
                            except ValueError:
                                pass
                            else:
                                pass
                            if len(subjects11) >= 1:
                                tmp179 = subjects11.popleft()
                                subst2 = Substitution(subst1)
                                try:
                                    subst2.try_add_variable('i2.2.1.2_2', tmp179)
                                except ValueError:
                                    pass
                                else:
                                    pass
                                subjects11.appendleft(tmp179)
                            if len(subjects11) >= 1 and subjects11[0] == Integer(2):
                                tmp181 = subjects11.popleft()
                                # State 2874
                                if len(subjects11) == 0:
                                    pass
                                    # State 2875
                                    if len(subjects) == 0:
                                        pass
                                subjects11.appendleft(tmp181)
                subjects11.appendleft(tmp12)
            subjects.appendleft(tmp10)
        return
        yield


from collections import deque