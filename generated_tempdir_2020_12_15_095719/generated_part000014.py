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


class CommutativeMatcher2374(CommutativeMatcher):
    _instance = None
    patterns = {
    0: (0, Multiset({0: 1}), [
      (VariableWithCount('i2.2.0', 1, 1, None), Add)
]),
    1: (1, Multiset({1: 1}), [
      (VariableWithCount('i2.2.0', 1, 1, S(0)), Add)
]),
    2: (2, Multiset({2: 1, 3: 1}), [
      (VariableWithCount('i2.2.0', 1, 1, None), Add)
]),
    3: (3, Multiset({2: 1, 4: 1}), [
      (VariableWithCount('i2.2.0', 1, 1, S(0)), Add)
]),
    4: (4, Multiset({5: 1, 3: 1}), [
      (VariableWithCount('i2.2.0', 1, 1, S(0)), Add)
]),
    5: (5, Multiset({6: 1, 7: 1}), [
      (VariableWithCount('i2.2.0', 1, 1, S(0)), Add)
]),
    6: (6, Multiset({8: 1}), [
      (VariableWithCount('i2.2.0', 1, 1, None), Add)
]),
    7: (7, Multiset({9: 1}), [
      (VariableWithCount('i2.2.0_1', 1, 1, None), Add)
]),
    8: (8, Multiset({10: 1}), [
      (VariableWithCount('i2.2.0', 1, 1, None), Add)
]),
    9: (9, Multiset({11: 1}), [
      (VariableWithCount('i2.2.0_1', 1, 1, None), Add)
]),
    10: (10, Multiset({12: 1}), [
      (VariableWithCount('i2.2.0', 1, 1, None), Add)
]),
    11: (11, Multiset({13: 1}), [
      (VariableWithCount('i2.2.0_1', 1, 1, None), Add)
]),
    12: (12, Multiset({14: 1}), [
      (VariableWithCount('i2.2.0', 1, 1, None), Add)
]),
    13: (13, Multiset({15: 1}), [
      (VariableWithCount('i2.2.0', 1, 1, None), Add)
]),
    14: (14, Multiset({16: 1}), [
      (VariableWithCount('i2.2.0_1', 1, 1, None), Add)
]),
    15: (15, Multiset({17: 1}), [
      (VariableWithCount('i2.2.0_1', 1, 1, None), Add)
]),
    16: (16, Multiset({18: 1}), [
      (VariableWithCount('i2.2.0', 1, 1, None), Add)
]),
    17: (17, Multiset({19: 1, 20: 1}), [
      (VariableWithCount('i2.2.0', 1, 1, None), Add)
]),
    18: (18, Multiset({21: 1, 22: 1}), [
      (VariableWithCount('i2.2.0', 1, 1, None), Add)
]),
    19: (19, Multiset({23: 1, 24: 1}), [
      (VariableWithCount('i2.2.0', 1, 1, S(0)), Add)
]),
    20: (20, Multiset({25: 1, 26: 1}), [
      
]),
    21: (21, Multiset({27: 1, 28: 1, 29: 1}), [
      
]),
    22: (22, Multiset({30: 1}), [
      (VariableWithCount('i2.2.0', 1, 1, None), Add)
]),
    23: (23, Multiset({31: 1}), [
      (VariableWithCount('i2.2.0', 1, 1, None), Add)
]),
    24: (24, Multiset({32: 1}), [
      (VariableWithCount('i2.2.0', 1, 1, None), Add)
]),
    25: (25, Multiset({33: 1}), [
      (VariableWithCount('i2.2.0_1', 1, 1, None), Add)
]),
    26: (26, Multiset({34: 1}), [
      (VariableWithCount('i2.2.0', 1, 1, S(0)), Add)
]),
    27: (27, Multiset({35: 1, 36: 1}), [
      (VariableWithCount('i2.2.0', 1, 1, S(0)), Add)
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
        if CommutativeMatcher2374._instance is None:
            CommutativeMatcher2374._instance = CommutativeMatcher2374()
        return CommutativeMatcher2374._instance

    @staticmethod
    def get_match_iter(subject):
        subjects = deque([subject]) if subject is not None else deque()
        subst0 = Substitution()
        # State 2373
        subst1 = Substitution(subst0)
        try:
            subst1.try_add_variable('i2.2.1.0', S(1))
        except ValueError:
            pass
        else:
            pass
            # State 2375
            subst2 = Substitution(subst1)
            try:
                subst2.try_add_variable('i2.2.1.2', S(1))
            except ValueError:
                pass
            else:
                pass
                # State 2376
                if len(subjects) >= 1:
                    tmp3 = subjects.popleft()
                    subst3 = Substitution(subst2)
                    try:
                        subst3.try_add_variable('i2.2.1.1', tmp3)
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
                                        # State 2377
                                        if len(subjects) == 0:
                                            pass
                                            # 0: a*v**m /; (cons_f2) and (cons_f3) and (cons_f4) and (cons_f5)
                                            yield 0, subst3
                                            # 1: a*v**m /; (cons_f2) and (cons_f3) and (cons_f4) and (cons_f5) and (cons_f6)
                                            yield 1, subst3
                                    if 'i2.2.0_1' not in subst3 or 'i2.2.1.1' not in subst3 or cons_f8(c=subst3["i2.2.0_1"], x=subst3["i2.2.1.1"]):
                                        pass
                                        if 'i2.2.1.0_1' not in subst3 or 'i2.2.1.1' not in subst3 or cons_f29(d=subst3["i2.2.1.0_1"], x=subst3["i2.2.1.1"]):
                                            pass
                                            if 'i2.2' not in subst3 or 'i2.2.1.1' not in subst3 or cons_f19(m=subst3["i2.2"], x=subst3["i2.2.1.1"]):
                                                pass
                                                # State 2377
                                                if len(subjects) == 0:
                                                    pass
                                                    # 15: a*v**m /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f19) and (cons_f4) and (cons_f39) and (cons_f41) and (cons_f42)
                                                    yield 15, subst3
                            if 'i2.2' not in subst3 or 'i2.2.1.1' not in subst3 or cons_f5(p=subst3["i2.2"], x=subst3["i2.2.1.1"]):
                                pass
                                if 'i2.2.1.0_1' not in subst3 or 'i2.2.1.1' not in subst3 or cons_f3(b=subst3["i2.2.1.0_1"], x=subst3["i2.2.1.1"]):
                                    pass
                                    if 'i2.2.1.0' not in subst3 or 'i2.2.1.1' not in subst3 or cons_f8(c=subst3["i2.2.1.0"], x=subst3["i2.2.1.1"]):
                                        pass
                                        if 'i2.2.1.2_1' not in subst3 or 'i2.2.1.1' not in subst3 or cons_f4(n=subst3["i2.2.1.2_1"], x=subst3["i2.2.1.1"]):
                                            pass
                                            # State 2377
                                            if len(subjects) == 0:
                                                pass
                                                # 2: a*v**m /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f4) and (cons_f5) and (cons_f7)
                                                yield 2, subst3
                                                # 5: a*v**m /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f4) and (cons_f5) and (cons_f7) and (cons_f9)
                                                yield 5, subst3
                        if 'i2.2.1.2' not in subst3 or 'i2.2.1.1' not in subst3 or cons_f4(n=subst3["i2.2.1.2"], x=subst3["i2.2.1.1"]):
                            pass
                            if 'i2.2' not in subst3 or 'i2.2.1.1' not in subst3 or cons_f5(p=subst3["i2.2"], x=subst3["i2.2.1.1"]):
                                pass
                                if 'i2.2_1' not in subst3 or 'i2.2.1.1' not in subst3 or cons_f19(m=subst3["i2.2_1"], x=subst3["i2.2.1.1"]):
                                    pass
                                    if 'i2.2.0' not in subst3 or 'i2.2.1.1' not in subst3 or cons_f59(a1=subst3["i2.2.0"], x=subst3["i2.2.1.1"]):
                                        pass
                                        if 'i2.2.1.0' not in subst3 or 'i2.2.1.1' not in subst3 or cons_f60(b1=subst3["i2.2.1.0"], x=subst3["i2.2.1.1"]):
                                            pass
                                            if 'i2.2.0_1' not in subst3 or 'i2.2.1.1' not in subst3 or cons_f61(a2=subst3["i2.2.0_1"], x=subst3["i2.2.1.1"]):
                                                pass
                                                if 'i2.2.1.0_1' not in subst3 or 'i2.2.1.1' not in subst3 or cons_f62(b2=subst3["i2.2.1.0_1"], x=subst3["i2.2.1.1"]):
                                                    pass
                                                    # State 2377
                                                    if len(subjects) == 0:
                                                        pass
                                                        # 32: a*v**m /; (cons_f59) and (cons_f60) and (cons_f61) and (cons_f62) and (cons_f19) and (cons_f4) and (cons_f5) and (cons_f57) and (cons_f58)
                                                        yield 32, subst3
                        if 'i2.2.1.0_1' not in subst3 or 'i2.2.1.1' not in subst3 or cons_f3(b=subst3["i2.2.1.0_1"], x=subst3["i2.2.1.1"]):
                            pass
                            if 'i2.2.1.0' not in subst3 or 'i2.2.1.1' not in subst3 or cons_f2(a=subst3["i2.2.1.0"], x=subst3["i2.2.1.1"]):
                                pass
                                if 'i2.2.1.2' not in subst3 or 'i2.2.1.1' not in subst3 or cons_f5(p=subst3["i2.2.1.2"], x=subst3["i2.2.1.1"]):
                                    pass
                                    if 'i2.2.1.2_1' not in subst3 or 'i2.2.1.1' not in subst3 or cons_f52(q=subst3["i2.2.1.2_1"], x=subst3["i2.2.1.1"]):
                                        pass
                                        if 'i2.2.1.0_2' not in subst3 or 'i2.2.1.1' not in subst3 or cons_f8(c=subst3["i2.2.1.0_2"], x=subst3["i2.2.1.1"]):
                                            pass
                                            if 'i2.2.1.2_2' not in subst3 or 'i2.2.1.1' not in subst3 or cons_f54(r=subst3["i2.2.1.2_2"], x=subst3["i2.2.1.1"]):
                                                pass
                                                # State 2377
                                                if len(subjects) == 0:
                                                    pass
                                                    # 27: a*v**m /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f5) and (cons_f52) and (cons_f54) and (cons_f51) and (cons_f53)
                                                    yield 27, subst3
                                        # State 2377
                                        if len(subjects) == 0:
                                            pass
                                            # 25: a*v**m /; (cons_f2) and (cons_f3) and (cons_f5) and (cons_f52) and (cons_f51)
                                            yield 25, subst3
                        if 'i2' not in subst3 or 'i2.2.1.1' not in subst3 or cons_f11(Pm=subst3["i2.2.1.1"], x=subst3["i2"]):
                            pass
                            if 'i2' not in subst3 or 'i2.2.1.1' not in subst3 or 'i2.2.1.0' not in subst3 or 'i2.2.0' not in subst3 or 'i2.0' not in subst3 or 'i2.2' not in subst3 or 'i2.2.1.2' not in subst3 or With35(Pm=subst3["i2.2.1.1"], Qm=subst3["i2.0"], a=subst3["i2.2.0"], b=subst3["i2.2.1.0"], n=subst3["i2.2.1.2"], p=subst3["i2.2"], x=subst3["i2"]):
                                pass
                                # State 2377
                                if len(subjects) == 0:
                                    pass
                                    # 34: a*v**m /; (cons_f3) and (cons_f4) and (cons_f11) and (With35)
                                    yield 34, subst3
                            if 'i2' not in subst3 or 'i2.2.1.1' not in subst3 or 'i2.2.1.0' not in subst3 or 'i2.2.0' not in subst3 or 'i2.0' not in subst3 or 'i2.2.1.2_1' not in subst3 or 'i2.2.1.2' not in subst3 or 'i2.2' not in subst3 or 'i2.2.1.0_1' not in subst3 or With36(Pm=subst3["i2.2.1.1"], Qm=subst3["i2.0"], a=subst3["i2.2.0"], b=subst3["i2.2.1.0"], c=subst3["i2.2.1.0_1"], n=subst3["i2.2.1.2"], n2=subst3["i2.2.1.2_1"], p=subst3["i2.2"], x=subst3["i2"]):
                                pass
                                # State 2377
                                if len(subjects) == 0:
                                    pass
                                    # 35: a*v**m /; (cons_f3) and (cons_f4) and (cons_f48) and (cons_f11) and (With36)
                                    yield 35, subst3
                    subjects.appendleft(tmp3)
            if len(subjects) >= 1 and isinstance(subjects[0], Pow):
                tmp5 = subjects.popleft()
                subjects6 = deque(tmp5._args)
                # State 2378
                if len(subjects6) >= 1:
                    tmp7 = subjects6.popleft()
                    subst2 = Substitution(subst1)
                    try:
                        subst2.try_add_variable('i2.2.1.1', tmp7)
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
                                            # State 2379
                                            subst3 = Substitution(subst2)
                                            try:
                                                subst3.try_add_variable('i2.2.1.2', 1)
                                            except ValueError:
                                                pass
                                            else:
                                                pass
                                            if len(subjects6) >= 1:
                                                tmp10 = subjects6.popleft()
                                                subst3 = Substitution(subst2)
                                                try:
                                                    subst3.try_add_variable('i2.2.1.2', tmp10)
                                                except ValueError:
                                                    pass
                                                else:
                                                    pass
                                                subjects6.appendleft(tmp10)
                                            if len(subjects6) >= 1:
                                                tmp12 = subjects6.popleft()
                                                subst3 = Substitution(subst2)
                                                try:
                                                    subst3.try_add_variable('i2.2.1.2', tmp12)
                                                except ValueError:
                                                    pass
                                                else:
                                                    pass
                                                    if 'i2.2.1.2' not in subst3 or 'i2.2.1.1' not in subst3 or cons_f4(n=subst3["i2.2.1.2"], x=subst3["i2.2.1.1"]):
                                                        pass
                                                        if 'i2.2.1.2' not in subst3 or 'i2.2_1' not in subst3 or cons_f55(m=subst3["i2.2_1"], n=subst3["i2.2.1.2"]):
                                                            pass
                                                            # State 2831
                                                            if len(subjects6) == 0:
                                                                pass
                                                                # State 2832
                                                                if len(subjects) == 0:
                                                                    pass
                                                                    # 31: d*x**j /; (cons_f2) and (cons_f3) and (cons_f19) and (cons_f4) and (cons_f5) and (cons_f55)
                                                                    yield 31, subst3
                                                subjects6.appendleft(tmp12)
                                            if len(subjects6) >= 1 and subjects6[0] == Integer(2):
                                                tmp14 = subjects6.popleft()
                                                # State 2872
                                                if len(subjects6) == 0:
                                                    pass
                                                    # State 2873
                                                    if len(subjects) == 0:
                                                        pass
                                                subjects6.appendleft(tmp14)
                                        # State 2379
                                        subst3 = Substitution(subst2)
                                        try:
                                            subst3.try_add_variable('i2.2.1.2', 1)
                                        except ValueError:
                                            pass
                                        else:
                                            pass
                                            if 'i2.2.1.2' not in subst3 or 'i2.2.1.1' not in subst3 or cons_f4(n=subst3["i2.2.1.2"], x=subst3["i2.2.1.1"]):
                                                pass
                                                # State 2380
                                                if len(subjects6) == 0:
                                                    pass
                                                    # State 2381
                                                    if len(subjects) == 0:
                                                        pass
                                                        # 0: a*v**m /; (cons_f2) and (cons_f3) and (cons_f4) and (cons_f5)
                                                        yield 0, subst3
                                                        # 1: a*v**m /; (cons_f2) and (cons_f3) and (cons_f4) and (cons_f5) and (cons_f6)
                                                        yield 1, subst3
                                        if len(subjects6) >= 1:
                                            tmp16 = subjects6.popleft()
                                            subst3 = Substitution(subst2)
                                            try:
                                                subst3.try_add_variable('i2.2.1.2', tmp16)
                                            except ValueError:
                                                pass
                                            else:
                                                pass
                                                if 'i2.2.1.2' not in subst3 or 'i2.2.1.1' not in subst3 or cons_f4(n=subst3["i2.2.1.2"], x=subst3["i2.2.1.1"]):
                                                    pass
                                                    # State 2380
                                                    if len(subjects6) == 0:
                                                        pass
                                                        # State 2381
                                                        if len(subjects) == 0:
                                                            pass
                                                            # 0: a*v**m /; (cons_f2) and (cons_f3) and (cons_f4) and (cons_f5)
                                                            yield 0, subst3
                                                            # 1: a*v**m /; (cons_f2) and (cons_f3) and (cons_f4) and (cons_f5) and (cons_f6)
                                                            yield 1, subst3
                                            subjects6.appendleft(tmp16)
                                        if len(subjects6) >= 1:
                                            tmp18 = subjects6.popleft()
                                            subst3 = Substitution(subst2)
                                            try:
                                                subst3.try_add_variable('i2.2.1.2', tmp18)
                                            except ValueError:
                                                pass
                                            else:
                                                pass
                                            subjects6.appendleft(tmp18)
                                        if len(subjects6) >= 1 and subjects6[0] == Integer(2):
                                            tmp20 = subjects6.popleft()
                                            # State 2872
                                            if len(subjects6) == 0:
                                                pass
                                                # State 2873
                                                if len(subjects) == 0:
                                                    pass
                                            subjects6.appendleft(tmp20)
                                    if 'i2.2.0_1' not in subst2 or 'i2.2.1.1' not in subst2 or cons_f8(c=subst2["i2.2.0_1"], x=subst2["i2.2.1.1"]):
                                        pass
                                        if 'i2.2.1.0_1' not in subst2 or 'i2.2.1.1' not in subst2 or cons_f29(d=subst2["i2.2.1.0_1"], x=subst2["i2.2.1.1"]):
                                            pass
                                            if 'i2.2' not in subst2 or 'i2.2.1.1' not in subst2 or cons_f19(m=subst2["i2.2"], x=subst2["i2.2.1.1"]):
                                                pass
                                                # State 2379
                                                subst3 = Substitution(subst2)
                                                try:
                                                    subst3.try_add_variable('i2.2.1.2', 1)
                                                except ValueError:
                                                    pass
                                                else:
                                                    pass
                                                    if 'i2.2.1.2' not in subst3 or 'i2.2.1.1' not in subst3 or cons_f4(n=subst3["i2.2.1.2"], x=subst3["i2.2.1.1"]):
                                                        pass
                                                        if 'i2.2.1.2' not in subst3 or 'i2.2.1.2_1' not in subst3 or cons_f39(n=subst3["i2.2.1.2"], q=subst3["i2.2.1.2_1"]):
                                                            pass
                                                            if 'i2.2.1.2' not in subst3 or 'i2.2' not in subst3 or cons_f42(m=subst3["i2.2"], n=subst3["i2.2.1.2"]):
                                                                pass
                                                                # State 2380
                                                                if len(subjects6) == 0:
                                                                    pass
                                                                    # State 2381
                                                                    if len(subjects) == 0:
                                                                        pass
                                                                        # 15: a*v**m /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f19) and (cons_f4) and (cons_f39) and (cons_f41) and (cons_f42)
                                                                        yield 15, subst3
                                                if len(subjects6) >= 1:
                                                    tmp22 = subjects6.popleft()
                                                    subst3 = Substitution(subst2)
                                                    try:
                                                        subst3.try_add_variable('i2.2.1.2', tmp22)
                                                    except ValueError:
                                                        pass
                                                    else:
                                                        pass
                                                        if 'i2.2.1.2' not in subst3 or 'i2.2.1.1' not in subst3 or cons_f4(n=subst3["i2.2.1.2"], x=subst3["i2.2.1.1"]):
                                                            pass
                                                            if 'i2.2.1.2' not in subst3 or 'i2.2.1.2_1' not in subst3 or cons_f39(n=subst3["i2.2.1.2"], q=subst3["i2.2.1.2_1"]):
                                                                pass
                                                                if 'i2.2.1.2' not in subst3 or 'i2.2' not in subst3 or cons_f42(m=subst3["i2.2"], n=subst3["i2.2.1.2"]):
                                                                    pass
                                                                    # State 2380
                                                                    if len(subjects6) == 0:
                                                                        pass
                                                                        # State 2381
                                                                        if len(subjects) == 0:
                                                                            pass
                                                                            # 15: a*v**m /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f19) and (cons_f4) and (cons_f39) and (cons_f41) and (cons_f42)
                                                                            yield 15, subst3
                                                    subjects6.appendleft(tmp22)
                                                if len(subjects6) >= 1:
                                                    tmp24 = subjects6.popleft()
                                                    subst3 = Substitution(subst2)
                                                    try:
                                                        subst3.try_add_variable('i2.2.1.2', tmp24)
                                                    except ValueError:
                                                        pass
                                                    else:
                                                        pass
                                                    subjects6.appendleft(tmp24)
                                                if len(subjects6) >= 1 and subjects6[0] == Integer(2):
                                                    tmp26 = subjects6.popleft()
                                                    # State 2872
                                                    if len(subjects6) == 0:
                                                        pass
                                                        # State 2873
                                                        if len(subjects) == 0:
                                                            pass
                                                    subjects6.appendleft(tmp26)
                                    if 'i2.2' not in subst2 or 'i2.2.1.1' not in subst2 or cons_f19(m=subst2["i2.2"], x=subst2["i2.2.1.1"]):
                                        pass
                                        # State 2379
                                        subst3 = Substitution(subst2)
                                        try:
                                            subst3.try_add_variable('i2.2.1.2', 1)
                                        except ValueError:
                                            pass
                                        else:
                                            pass
                                        if len(subjects6) >= 1:
                                            tmp28 = subjects6.popleft()
                                            subst3 = Substitution(subst2)
                                            try:
                                                subst3.try_add_variable('i2.2.1.2', tmp28)
                                            except ValueError:
                                                pass
                                            else:
                                                pass
                                            subjects6.appendleft(tmp28)
                                        if len(subjects6) >= 1:
                                            tmp30 = subjects6.popleft()
                                            subst3 = Substitution(subst2)
                                            try:
                                                subst3.try_add_variable('i2.2.1.2', tmp30)
                                            except ValueError:
                                                pass
                                            else:
                                                pass
                                                if 'i2.2.1.2' not in subst3 or 'i2.2.1.1' not in subst3 or cons_f4(n=subst3["i2.2.1.2"], x=subst3["i2.2.1.1"]):
                                                    pass
                                                    if 'i2.2.1.2' not in subst3 or 'i2.2' not in subst3 or cons_f55(m=subst3["i2.2"], n=subst3["i2.2.1.2"]):
                                                        pass
                                                        # State 2831
                                                        if len(subjects6) == 0:
                                                            pass
                                                            # State 2832
                                                            if len(subjects) == 0:
                                                                pass
                                                                # 30: d*x**j /; (cons_f2) and (cons_f3) and (cons_f19) and (cons_f4) and (cons_f55)
                                                                yield 30, subst3
                                            subjects6.appendleft(tmp30)
                                        if len(subjects6) >= 1 and subjects6[0] == Integer(2):
                                            tmp32 = subjects6.popleft()
                                            # State 2872
                                            if len(subjects6) == 0:
                                                pass
                                                # State 2873
                                                if len(subjects) == 0:
                                                    pass
                                            subjects6.appendleft(tmp32)
                                    if 'i2.2.1.0_1' not in subst2 or 'i2.2.1.1' not in subst2 or cons_f8(c=subst2["i2.2.1.0_1"], x=subst2["i2.2.1.1"]):
                                        pass
                                        # State 2379
                                        subst3 = Substitution(subst2)
                                        try:
                                            subst3.try_add_variable('i2.2.1.2', 1)
                                        except ValueError:
                                            pass
                                        else:
                                            pass
                                        if len(subjects6) >= 1:
                                            tmp34 = subjects6.popleft()
                                            subst3 = Substitution(subst2)
                                            try:
                                                subst3.try_add_variable('i2.2.1.2', tmp34)
                                            except ValueError:
                                                pass
                                            else:
                                                pass
                                            subjects6.appendleft(tmp34)
                                        if len(subjects6) >= 1:
                                            tmp36 = subjects6.popleft()
                                            subst3 = Substitution(subst2)
                                            try:
                                                subst3.try_add_variable('i2.2.1.2', tmp36)
                                            except ValueError:
                                                pass
                                            else:
                                                pass
                                                if 'i2.2.1.2' not in subst3 or 'i2.2.1.1' not in subst3 or cons_f4(n=subst3["i2.2.1.2"], x=subst3["i2.2.1.1"]):
                                                    pass
                                                    if 'i2.2.1.2' not in subst3 or 'i2.2.1.2_1' not in subst3 or cons_f48(n=subst3["i2.2.1.2"], n2=subst3["i2.2.1.2_1"]):
                                                        pass
                                                        # State 2831
                                                        if len(subjects6) == 0:
                                                            pass
                                                            # State 2832
                                                            if len(subjects) == 0:
                                                                pass
                                                                # 22: d*x**j /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f4) and (cons_f48) and (cons_f47)
                                                                yield 22, subst3
                                            subjects6.appendleft(tmp36)
                                        if len(subjects6) >= 1 and subjects6[0] == Integer(2):
                                            tmp38 = subjects6.popleft()
                                            # State 2872
                                            if len(subjects6) == 0:
                                                pass
                                                # State 2873
                                                if len(subjects) == 0:
                                                    pass
                                            subjects6.appendleft(tmp38)
                            if 'i2.2' not in subst2 or 'i2.2.1.1' not in subst2 or cons_f5(p=subst2["i2.2"], x=subst2["i2.2.1.1"]):
                                pass
                                if 'i2.2.1.0_1' not in subst2 or 'i2.2.1.1' not in subst2 or cons_f3(b=subst2["i2.2.1.0_1"], x=subst2["i2.2.1.1"]):
                                    pass
                                    if 'i2.2.1.0' not in subst2 or 'i2.2.1.1' not in subst2 or cons_f8(c=subst2["i2.2.1.0"], x=subst2["i2.2.1.1"]):
                                        pass
                                        if 'i2.2.1.2_1' not in subst2 or 'i2.2.1.1' not in subst2 or cons_f4(n=subst2["i2.2.1.2_1"], x=subst2["i2.2.1.1"]):
                                            pass
                                            # State 2379
                                            subst3 = Substitution(subst2)
                                            try:
                                                subst3.try_add_variable('i2.2.1.2', 1)
                                            except ValueError:
                                                pass
                                            else:
                                                pass
                                                if 'i2.2.1.2' not in subst3 or 'i2.2.1.2_1' not in subst3 or cons_f7(j=subst3["i2.2.1.2"], n=subst3["i2.2.1.2_1"]):
                                                    pass
                                                    # State 2380
                                                    if len(subjects6) == 0:
                                                        pass
                                                        # State 2381
                                                        if len(subjects) == 0:
                                                            pass
                                                            # 2: a*v**m /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f4) and (cons_f5) and (cons_f7)
                                                            yield 2, subst3
                                                            # 5: a*v**m /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f4) and (cons_f5) and (cons_f7) and (cons_f9)
                                                            yield 5, subst3
                                            if len(subjects6) >= 1:
                                                tmp40 = subjects6.popleft()
                                                subst3 = Substitution(subst2)
                                                try:
                                                    subst3.try_add_variable('i2.2.1.2', tmp40)
                                                except ValueError:
                                                    pass
                                                else:
                                                    pass
                                                    if 'i2.2.1.2' not in subst3 or 'i2.2.1.2_1' not in subst3 or cons_f7(j=subst3["i2.2.1.2"], n=subst3["i2.2.1.2_1"]):
                                                        pass
                                                        # State 2380
                                                        if len(subjects6) == 0:
                                                            pass
                                                            # State 2381
                                                            if len(subjects) == 0:
                                                                pass
                                                                # 2: a*v**m /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f4) and (cons_f5) and (cons_f7)
                                                                yield 2, subst3
                                                                # 5: a*v**m /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f4) and (cons_f5) and (cons_f7) and (cons_f9)
                                                                yield 5, subst3
                                                subjects6.appendleft(tmp40)
                                            if len(subjects6) >= 1:
                                                tmp42 = subjects6.popleft()
                                                subst3 = Substitution(subst2)
                                                try:
                                                    subst3.try_add_variable('i2.2.1.2', tmp42)
                                                except ValueError:
                                                    pass
                                                else:
                                                    pass
                                                subjects6.appendleft(tmp42)
                                            if len(subjects6) >= 1 and subjects6[0] == Integer(2):
                                                tmp44 = subjects6.popleft()
                                                # State 2872
                                                if len(subjects6) == 0:
                                                    pass
                                                    # State 2873
                                                    if len(subjects) == 0:
                                                        pass
                                                subjects6.appendleft(tmp44)
                                        if 'i2.1.0' not in subst2 or 'i2.2.1.1' not in subst2 or cons_f29(d=subst2["i2.1.0"], x=subst2["i2.2.1.1"]):
                                            pass
                                            if 'i2.1.1.0' not in subst2 or 'i2.2.1.1' not in subst2 or cons_f50(e=subst2["i2.1.1.0"], x=subst2["i2.2.1.1"]):
                                                pass
                                                # State 2379
                                                subst3 = Substitution(subst2)
                                                try:
                                                    subst3.try_add_variable('i2.2.1.2', 1)
                                                except ValueError:
                                                    pass
                                                else:
                                                    pass
                                                if len(subjects6) >= 1:
                                                    tmp46 = subjects6.popleft()
                                                    subst3 = Substitution(subst2)
                                                    try:
                                                        subst3.try_add_variable('i2.2.1.2', tmp46)
                                                    except ValueError:
                                                        pass
                                                    else:
                                                        pass
                                                    subjects6.appendleft(tmp46)
                                                if len(subjects6) >= 1:
                                                    tmp48 = subjects6.popleft()
                                                    subst3 = Substitution(subst2)
                                                    try:
                                                        subst3.try_add_variable('i2.2.1.2', tmp48)
                                                    except ValueError:
                                                        pass
                                                    else:
                                                        pass
                                                    subjects6.appendleft(tmp48)
                                                if len(subjects6) >= 1 and subjects6[0] == Integer(2):
                                                    tmp50 = subjects6.popleft()
                                                    # State 2872
                                                    if len(subjects6) == 0:
                                                        pass
                                                        # State 2873
                                                        if len(subjects) == 0:
                                                            pass
                                                            # 23: c*x**2 /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f50) and (cons_f5) and (cons_f49)
                                                            yield 23, subst2
                                                    subjects6.appendleft(tmp50)
                            if 'i2.2.1.0_1' not in subst2 or 'i2.2.1.1' not in subst2 or cons_f3(b=subst2["i2.2.1.0_1"], x=subst2["i2.2.1.1"]):
                                pass
                                if 'i2.2.1.0' not in subst2 or 'i2.2.1.1' not in subst2 or cons_f8(c=subst2["i2.2.1.0"], x=subst2["i2.2.1.1"]):
                                    pass
                                    # State 2379
                                    subst3 = Substitution(subst2)
                                    try:
                                        subst3.try_add_variable('i2.2.1.2', 1)
                                    except ValueError:
                                        pass
                                    else:
                                        pass
                                    if len(subjects6) >= 1:
                                        tmp52 = subjects6.popleft()
                                        subst3 = Substitution(subst2)
                                        try:
                                            subst3.try_add_variable('i2.2.1.2', tmp52)
                                        except ValueError:
                                            pass
                                        else:
                                            pass
                                        subjects6.appendleft(tmp52)
                                    if len(subjects6) >= 1:
                                        tmp54 = subjects6.popleft()
                                        subst3 = Substitution(subst2)
                                        try:
                                            subst3.try_add_variable('i2.2.1.2', tmp54)
                                        except ValueError:
                                            pass
                                        else:
                                            pass
                                        subjects6.appendleft(tmp54)
                                    if len(subjects6) >= 1 and subjects6[0] == Integer(2):
                                        tmp56 = subjects6.popleft()
                                        # State 2872
                                        if len(subjects6) == 0:
                                            pass
                                            # State 2873
                                            if len(subjects) == 0:
                                                pass
                                                # 19: c*x**2 /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f47)
                                                yield 19, subst2
                                        subjects6.appendleft(tmp56)
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
                                                    # State 2379
                                                    subst3 = Substitution(subst2)
                                                    try:
                                                        subst3.try_add_variable('i2.2.1.2', 1)
                                                    except ValueError:
                                                        pass
                                                    else:
                                                        pass
                                                        if 'i2.2.1.2' not in subst3 or 'i2.2.1.1' not in subst3 or cons_f4(n=subst3["i2.2.1.2"], x=subst3["i2.2.1.1"]):
                                                            pass
                                                            if 'i2.2.1.2' not in subst3 or 'i2.2_1' not in subst3 or cons_f58(m=subst3["i2.2_1"], n=subst3["i2.2.1.2"]):
                                                                pass
                                                                # State 2380
                                                                if len(subjects6) == 0:
                                                                    pass
                                                                    # State 2381
                                                                    if len(subjects) == 0:
                                                                        pass
                                                                        # 32: a*v**m /; (cons_f59) and (cons_f60) and (cons_f61) and (cons_f62) and (cons_f19) and (cons_f4) and (cons_f5) and (cons_f57) and (cons_f58)
                                                                        yield 32, subst3
                                                    if len(subjects6) >= 1:
                                                        tmp58 = subjects6.popleft()
                                                        subst3 = Substitution(subst2)
                                                        try:
                                                            subst3.try_add_variable('i2.2.1.2', tmp58)
                                                        except ValueError:
                                                            pass
                                                        else:
                                                            pass
                                                            if 'i2.2.1.2' not in subst3 or 'i2.2.1.1' not in subst3 or cons_f4(n=subst3["i2.2.1.2"], x=subst3["i2.2.1.1"]):
                                                                pass
                                                                if 'i2.2.1.2' not in subst3 or 'i2.2_1' not in subst3 or cons_f58(m=subst3["i2.2_1"], n=subst3["i2.2.1.2"]):
                                                                    pass
                                                                    # State 2380
                                                                    if len(subjects6) == 0:
                                                                        pass
                                                                        # State 2381
                                                                        if len(subjects) == 0:
                                                                            pass
                                                                            # 32: a*v**m /; (cons_f59) and (cons_f60) and (cons_f61) and (cons_f62) and (cons_f19) and (cons_f4) and (cons_f5) and (cons_f57) and (cons_f58)
                                                                            yield 32, subst3
                                                        subjects6.appendleft(tmp58)
                                                    if len(subjects6) >= 1:
                                                        tmp60 = subjects6.popleft()
                                                        subst3 = Substitution(subst2)
                                                        try:
                                                            subst3.try_add_variable('i2.2.1.2', tmp60)
                                                        except ValueError:
                                                            pass
                                                        else:
                                                            pass
                                                        subjects6.appendleft(tmp60)
                                                    if len(subjects6) >= 1 and subjects6[0] == Integer(2):
                                                        tmp62 = subjects6.popleft()
                                                        # State 2872
                                                        if len(subjects6) == 0:
                                                            pass
                                                            # State 2873
                                                            if len(subjects) == 0:
                                                                pass
                                                        subjects6.appendleft(tmp62)
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
                                                    # State 2379
                                                    subst3 = Substitution(subst2)
                                                    try:
                                                        subst3.try_add_variable('i2.2.1.2', 1)
                                                    except ValueError:
                                                        pass
                                                    else:
                                                        pass
                                                    if len(subjects6) >= 1:
                                                        tmp64 = subjects6.popleft()
                                                        subst3 = Substitution(subst2)
                                                        try:
                                                            subst3.try_add_variable('i2.2.1.2', tmp64)
                                                        except ValueError:
                                                            pass
                                                        else:
                                                            pass
                                                        subjects6.appendleft(tmp64)
                                                    if len(subjects6) >= 1:
                                                        tmp66 = subjects6.popleft()
                                                        subst3 = Substitution(subst2)
                                                        try:
                                                            subst3.try_add_variable('i2.2.1.2', tmp66)
                                                        except ValueError:
                                                            pass
                                                        else:
                                                            pass
                                                            if 'i2.2.1.2' not in subst3 or 'i2.2.1.2_1' not in subst3 or cons_f7(j=subst3["i2.2.1.2"], n=subst3["i2.2.1.2_1"]):
                                                                pass
                                                                # State 2831
                                                                if len(subjects6) == 0:
                                                                    pass
                                                                    # State 2832
                                                                    if len(subjects) == 0:
                                                                        pass
                                                                        # 18: d*x**j /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f19) and (cons_f4) and (cons_f5) and (cons_f7) and (cons_f44) and (cons_f46)
                                                                        yield 18, subst3
                                                        subjects6.appendleft(tmp66)
                                                    if len(subjects6) >= 1 and subjects6[0] == Integer(2):
                                                        tmp68 = subjects6.popleft()
                                                        # State 2872
                                                        if len(subjects6) == 0:
                                                            pass
                                                            # State 2873
                                                            if len(subjects) == 0:
                                                                pass
                                                        subjects6.appendleft(tmp68)
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
                                                # State 2379
                                                subst3 = Substitution(subst2)
                                                try:
                                                    subst3.try_add_variable('i2.2.1.2', 1)
                                                except ValueError:
                                                    pass
                                                else:
                                                    pass
                                                    if 'i2.2.1.2' not in subst3 or 'i2.2.1.1' not in subst3 or cons_f5(p=subst3["i2.2.1.2"], x=subst3["i2.2.1.1"]):
                                                        pass
                                                        if 'i2.2.1.2' not in subst3 or 'i2.2.1.2_1' not in subst3 or cons_f51(p=subst3["i2.2.1.2"], q=subst3["i2.2.1.2_1"]):
                                                            pass
                                                            if 'i2.2.1.2' not in subst3 or 'i2.2.1.2_2' not in subst3 or cons_f53(p=subst3["i2.2.1.2"], r=subst3["i2.2.1.2_2"]):
                                                                pass
                                                                # State 2380
                                                                if len(subjects6) == 0:
                                                                    pass
                                                                    # State 2381
                                                                    if len(subjects) == 0:
                                                                        pass
                                                                        # 27: a*v**m /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f5) and (cons_f52) and (cons_f54) and (cons_f51) and (cons_f53)
                                                                        yield 27, subst3
                                                if len(subjects6) >= 1:
                                                    tmp70 = subjects6.popleft()
                                                    subst3 = Substitution(subst2)
                                                    try:
                                                        subst3.try_add_variable('i2.2.1.2', tmp70)
                                                    except ValueError:
                                                        pass
                                                    else:
                                                        pass
                                                        if 'i2.2.1.2' not in subst3 or 'i2.2.1.1' not in subst3 or cons_f5(p=subst3["i2.2.1.2"], x=subst3["i2.2.1.1"]):
                                                            pass
                                                            if 'i2.2.1.2' not in subst3 or 'i2.2.1.2_1' not in subst3 or cons_f51(p=subst3["i2.2.1.2"], q=subst3["i2.2.1.2_1"]):
                                                                pass
                                                                if 'i2.2.1.2' not in subst3 or 'i2.2.1.2_2' not in subst3 or cons_f53(p=subst3["i2.2.1.2"], r=subst3["i2.2.1.2_2"]):
                                                                    pass
                                                                    # State 2380
                                                                    if len(subjects6) == 0:
                                                                        pass
                                                                        # State 2381
                                                                        if len(subjects) == 0:
                                                                            pass
                                                                            # 27: a*v**m /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f5) and (cons_f52) and (cons_f54) and (cons_f51) and (cons_f53)
                                                                            yield 27, subst3
                                                    subjects6.appendleft(tmp70)
                                                if len(subjects6) >= 1:
                                                    tmp72 = subjects6.popleft()
                                                    subst3 = Substitution(subst2)
                                                    try:
                                                        subst3.try_add_variable('i2.2.1.2', tmp72)
                                                    except ValueError:
                                                        pass
                                                    else:
                                                        pass
                                                    subjects6.appendleft(tmp72)
                                                if len(subjects6) >= 1 and subjects6[0] == Integer(2):
                                                    tmp74 = subjects6.popleft()
                                                    # State 2872
                                                    if len(subjects6) == 0:
                                                        pass
                                                        # State 2873
                                                        if len(subjects) == 0:
                                                            pass
                                                    subjects6.appendleft(tmp74)
                                        # State 2379
                                        subst3 = Substitution(subst2)
                                        try:
                                            subst3.try_add_variable('i2.2.1.2', 1)
                                        except ValueError:
                                            pass
                                        else:
                                            pass
                                            if 'i2.2.1.2' not in subst3 or 'i2.2.1.1' not in subst3 or cons_f5(p=subst3["i2.2.1.2"], x=subst3["i2.2.1.1"]):
                                                pass
                                                if 'i2.2.1.2' not in subst3 or 'i2.2.1.2_1' not in subst3 or cons_f51(p=subst3["i2.2.1.2"], q=subst3["i2.2.1.2_1"]):
                                                    pass
                                                    # State 2380
                                                    if len(subjects6) == 0:
                                                        pass
                                                        # State 2381
                                                        if len(subjects) == 0:
                                                            pass
                                                            # 25: a*v**m /; (cons_f2) and (cons_f3) and (cons_f5) and (cons_f52) and (cons_f51)
                                                            yield 25, subst3
                                        if len(subjects6) >= 1:
                                            tmp76 = subjects6.popleft()
                                            subst3 = Substitution(subst2)
                                            try:
                                                subst3.try_add_variable('i2.2.1.2', tmp76)
                                            except ValueError:
                                                pass
                                            else:
                                                pass
                                                if 'i2.2.1.2' not in subst3 or 'i2.2.1.1' not in subst3 or cons_f5(p=subst3["i2.2.1.2"], x=subst3["i2.2.1.1"]):
                                                    pass
                                                    if 'i2.2.1.2' not in subst3 or 'i2.2.1.2_1' not in subst3 or cons_f51(p=subst3["i2.2.1.2"], q=subst3["i2.2.1.2_1"]):
                                                        pass
                                                        # State 2380
                                                        if len(subjects6) == 0:
                                                            pass
                                                            # State 2381
                                                            if len(subjects) == 0:
                                                                pass
                                                                # 25: a*v**m /; (cons_f2) and (cons_f3) and (cons_f5) and (cons_f52) and (cons_f51)
                                                                yield 25, subst3
                                            subjects6.appendleft(tmp76)
                                        if len(subjects6) >= 1:
                                            tmp78 = subjects6.popleft()
                                            subst3 = Substitution(subst2)
                                            try:
                                                subst3.try_add_variable('i2.2.1.2', tmp78)
                                            except ValueError:
                                                pass
                                            else:
                                                pass
                                            subjects6.appendleft(tmp78)
                                        if len(subjects6) >= 1 and subjects6[0] == Integer(2):
                                            tmp80 = subjects6.popleft()
                                            # State 2872
                                            if len(subjects6) == 0:
                                                pass
                                                # State 2873
                                                if len(subjects) == 0:
                                                    pass
                                            subjects6.appendleft(tmp80)
                        if 'i2' not in subst2 or 'i2.2.1.1' not in subst2 or cons_f11(Pm=subst2["i2.2.1.1"], x=subst2["i2"]):
                            pass
                            if 'i2' not in subst2 or 'i2.2.1.1' not in subst2 or 'i2.2.1.0' not in subst2 or 'i2.2.0' not in subst2 or 'i2.0' not in subst2 or 'i2.2' not in subst2 or 'i2.2.1.2' not in subst2 or With35(Pm=subst2["i2.2.1.1"], Qm=subst2["i2.0"], a=subst2["i2.2.0"], b=subst2["i2.2.1.0"], n=subst2["i2.2.1.2"], p=subst2["i2.2"], x=subst2["i2"]):
                                pass
                                # State 2379
                                subst3 = Substitution(subst2)
                                try:
                                    subst3.try_add_variable('i2.2.1.2', 1)
                                except ValueError:
                                    pass
                                else:
                                    pass
                                    if 'i2.2.1.2' not in subst3 or 'i2' not in subst3 or cons_f4(n=subst3["i2.2.1.2"], x=subst3["i2"]):
                                        pass
                                        if 'i2' not in subst3 or 'i2.2.1.1' not in subst3 or 'i2.2.1.0' not in subst3 or 'i2.2.0' not in subst3 or 'i2.0' not in subst3 or 'i2.2' not in subst3 or 'i2.2.1.2' not in subst3 or With35(Pm=subst3["i2.2.1.1"], Qm=subst3["i2.0"], a=subst3["i2.2.0"], b=subst3["i2.2.1.0"], n=subst3["i2.2.1.2"], p=subst3["i2.2"], x=subst3["i2"]):
                                            pass
                                            # State 2380
                                            if len(subjects6) == 0:
                                                pass
                                                # State 2381
                                                if len(subjects) == 0:
                                                    pass
                                                    # 34: a*v**m /; (cons_f3) and (cons_f4) and (cons_f11) and (With35)
                                                    yield 34, subst3
                                if len(subjects6) >= 1:
                                    tmp82 = subjects6.popleft()
                                    subst3 = Substitution(subst2)
                                    try:
                                        subst3.try_add_variable('i2.2.1.2', tmp82)
                                    except ValueError:
                                        pass
                                    else:
                                        pass
                                        if 'i2.2.1.2' not in subst3 or 'i2' not in subst3 or cons_f4(n=subst3["i2.2.1.2"], x=subst3["i2"]):
                                            pass
                                            if 'i2' not in subst3 or 'i2.2.1.1' not in subst3 or 'i2.2.1.0' not in subst3 or 'i2.2.0' not in subst3 or 'i2.0' not in subst3 or 'i2.2' not in subst3 or 'i2.2.1.2' not in subst3 or With35(Pm=subst3["i2.2.1.1"], Qm=subst3["i2.0"], a=subst3["i2.2.0"], b=subst3["i2.2.1.0"], n=subst3["i2.2.1.2"], p=subst3["i2.2"], x=subst3["i2"]):
                                                pass
                                                # State 2380
                                                if len(subjects6) == 0:
                                                    pass
                                                    # State 2381
                                                    if len(subjects) == 0:
                                                        pass
                                                        # 34: a*v**m /; (cons_f3) and (cons_f4) and (cons_f11) and (With35)
                                                        yield 34, subst3
                                    subjects6.appendleft(tmp82)
                                if len(subjects6) >= 1:
                                    tmp84 = subjects6.popleft()
                                    subst3 = Substitution(subst2)
                                    try:
                                        subst3.try_add_variable('i2.2.1.2', tmp84)
                                    except ValueError:
                                        pass
                                    else:
                                        pass
                                    subjects6.appendleft(tmp84)
                                if len(subjects6) >= 1 and subjects6[0] == Integer(2):
                                    tmp86 = subjects6.popleft()
                                    # State 2872
                                    if len(subjects6) == 0:
                                        pass
                                        # State 2873
                                        if len(subjects) == 0:
                                            pass
                                    subjects6.appendleft(tmp86)
                            if 'i2' not in subst2 or 'i2.2.1.1' not in subst2 or 'i2.2.1.0' not in subst2 or 'i2.2.0' not in subst2 or 'i2.0' not in subst2 or 'i2.2.1.2_1' not in subst2 or 'i2.2.1.2' not in subst2 or 'i2.2' not in subst2 or 'i2.2.1.0_1' not in subst2 or With36(Pm=subst2["i2.2.1.1"], Qm=subst2["i2.0"], a=subst2["i2.2.0"], b=subst2["i2.2.1.0"], c=subst2["i2.2.1.0_1"], n=subst2["i2.2.1.2"], n2=subst2["i2.2.1.2_1"], p=subst2["i2.2"], x=subst2["i2"]):
                                pass
                                # State 2379
                                subst3 = Substitution(subst2)
                                try:
                                    subst3.try_add_variable('i2.2.1.2', 1)
                                except ValueError:
                                    pass
                                else:
                                    pass
                                    if 'i2.2.1.2' not in subst3 or 'i2.2.1.2_1' not in subst3 or cons_f48(n=subst3["i2.2.1.2"], n2=subst3["i2.2.1.2_1"]):
                                        pass
                                        if 'i2.2.1.2' not in subst3 or 'i2' not in subst3 or cons_f4(n=subst3["i2.2.1.2"], x=subst3["i2"]):
                                            pass
                                            if 'i2' not in subst3 or 'i2.2.1.1' not in subst3 or 'i2.2.1.0' not in subst3 or 'i2.2.0' not in subst3 or 'i2.0' not in subst3 or 'i2.2.1.2_1' not in subst3 or 'i2.2.1.2' not in subst3 or 'i2.2' not in subst3 or 'i2.2.1.0_1' not in subst3 or With36(Pm=subst3["i2.2.1.1"], Qm=subst3["i2.0"], a=subst3["i2.2.0"], b=subst3["i2.2.1.0"], c=subst3["i2.2.1.0_1"], n=subst3["i2.2.1.2"], n2=subst3["i2.2.1.2_1"], p=subst3["i2.2"], x=subst3["i2"]):
                                                pass
                                                # State 2380
                                                if len(subjects6) == 0:
                                                    pass
                                                    # State 2381
                                                    if len(subjects) == 0:
                                                        pass
                                                        # 35: a*v**m /; (cons_f3) and (cons_f4) and (cons_f48) and (cons_f11) and (With36)
                                                        yield 35, subst3
                                if len(subjects6) >= 1:
                                    tmp88 = subjects6.popleft()
                                    subst3 = Substitution(subst2)
                                    try:
                                        subst3.try_add_variable('i2.2.1.2', tmp88)
                                    except ValueError:
                                        pass
                                    else:
                                        pass
                                        if 'i2.2.1.2' not in subst3 or 'i2.2.1.2_1' not in subst3 or cons_f48(n=subst3["i2.2.1.2"], n2=subst3["i2.2.1.2_1"]):
                                            pass
                                            if 'i2.2.1.2' not in subst3 or 'i2' not in subst3 or cons_f4(n=subst3["i2.2.1.2"], x=subst3["i2"]):
                                                pass
                                                if 'i2' not in subst3 or 'i2.2.1.1' not in subst3 or 'i2.2.1.0' not in subst3 or 'i2.2.0' not in subst3 or 'i2.0' not in subst3 or 'i2.2.1.2_1' not in subst3 or 'i2.2.1.2' not in subst3 or 'i2.2' not in subst3 or 'i2.2.1.0_1' not in subst3 or With36(Pm=subst3["i2.2.1.1"], Qm=subst3["i2.0"], a=subst3["i2.2.0"], b=subst3["i2.2.1.0"], c=subst3["i2.2.1.0_1"], n=subst3["i2.2.1.2"], n2=subst3["i2.2.1.2_1"], p=subst3["i2.2"], x=subst3["i2"]):
                                                    pass
                                                    # State 2380
                                                    if len(subjects6) == 0:
                                                        pass
                                                        # State 2381
                                                        if len(subjects) == 0:
                                                            pass
                                                            # 35: a*v**m /; (cons_f3) and (cons_f4) and (cons_f48) and (cons_f11) and (With36)
                                                            yield 35, subst3
                                    subjects6.appendleft(tmp88)
                                if len(subjects6) >= 1:
                                    tmp90 = subjects6.popleft()
                                    subst3 = Substitution(subst2)
                                    try:
                                        subst3.try_add_variable('i2.2.1.2', tmp90)
                                    except ValueError:
                                        pass
                                    else:
                                        pass
                                    subjects6.appendleft(tmp90)
                                if len(subjects6) >= 1 and subjects6[0] == Integer(2):
                                    tmp92 = subjects6.popleft()
                                    # State 2872
                                    if len(subjects6) == 0:
                                        pass
                                        # State 2873
                                        if len(subjects) == 0:
                                            pass
                                    subjects6.appendleft(tmp92)
                    subjects6.appendleft(tmp7)
                subjects.appendleft(tmp5)
        subst1 = Substitution(subst0)
        try:
            subst1.try_add_variable('i2.2.1.0_1', S(1))
        except ValueError:
            pass
        else:
            pass
            # State 2553
            subst2 = Substitution(subst1)
            try:
                subst2.try_add_variable('i2.2.1.2_1', S(1))
            except ValueError:
                pass
            else:
                pass
                # State 2554
                if len(subjects) >= 1:
                    tmp95 = subjects.popleft()
                    subst3 = Substitution(subst2)
                    try:
                        subst3.try_add_variable('i2.2.1.1', tmp95)
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
                                    if 'i2.2.0_1' not in subst3 or 'i2.2.1.1' not in subst3 or cons_f8(c=subst3["i2.2.0_1"], x=subst3["i2.2.1.1"]):
                                        pass
                                        if 'i2.2.1.0_1' not in subst3 or 'i2.2.1.1' not in subst3 or cons_f29(d=subst3["i2.2.1.0_1"], x=subst3["i2.2.1.1"]):
                                            pass
                                            if 'i2.2' not in subst3 or 'i2.2.1.1' not in subst3 or cons_f19(m=subst3["i2.2"], x=subst3["i2.2.1.1"]):
                                                pass
                                                # State 2555
                                                if len(subjects) == 0:
                                                    pass
                                                    # 16: b*v**n /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f19) and (cons_f4) and (cons_f39) and (cons_f41)
                                                    yield 16, subst3
                                    if 'i2.2.1.0_1' not in subst3 or 'i2.2.1.1' not in subst3 or cons_f8(c=subst3["i2.2.1.0_1"], x=subst3["i2.2.1.1"]):
                                        pass
                                        # State 2555
                                        if len(subjects) == 0:
                                            pass
                                            # 21: b*v**n /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f4) and (cons_f48) and (cons_f47)
                                            yield 21, subst3
                            if 'i2.2' not in subst3 or 'i2.2.1.1' not in subst3 or cons_f5(p=subst3["i2.2"], x=subst3["i2.2.1.1"]):
                                pass
                                if 'i2.2.1.0_1' not in subst3 or 'i2.2.1.1' not in subst3 or cons_f3(b=subst3["i2.2.1.0_1"], x=subst3["i2.2.1.1"]):
                                    pass
                                    if 'i2.2.1.0' not in subst3 or 'i2.2.1.1' not in subst3 or cons_f8(c=subst3["i2.2.1.0"], x=subst3["i2.2.1.1"]):
                                        pass
                                        if 'i2.2.1.2_1' not in subst3 or 'i2.2.1.1' not in subst3 or cons_f4(n=subst3["i2.2.1.2_1"], x=subst3["i2.2.1.1"]):
                                            pass
                                            # State 2555
                                            if len(subjects) == 0:
                                                pass
                                                # 3: b*v**n /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f4) and (cons_f5) and (cons_f7)
                                                yield 3, subst3
                                                # 4: b*v**n /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f4) and (cons_f5) and (cons_f7) and (cons_f6)
                                                yield 4, subst3
                        if 'i2.2' not in subst3 or 'i2.2.1.1' not in subst3 or cons_f5(p=subst3["i2.2"], x=subst3["i2.2.1.1"]):
                            pass
                            if 'i2.2.1.0_1' not in subst3 or 'i2.2.1.1' not in subst3 or cons_f3(b=subst3["i2.2.1.0_1"], x=subst3["i2.2.1.1"]):
                                pass
                                if 'i2.2.1.2_1' not in subst3 or 'i2.2.1.1' not in subst3 or cons_f4(n=subst3["i2.2.1.2_1"], x=subst3["i2.2.1.1"]):
                                    pass
                                    if 'i2.2.0_1' not in subst3 or 'i2.2.1.1' not in subst3 or cons_f2(a=subst3["i2.2.0_1"], x=subst3["i2.2.1.1"]):
                                        pass
                                        if 'i2.2.0' not in subst3 or 'i2.2.1.1' not in subst3 or cons_f8(c=subst3["i2.2.0"], x=subst3["i2.2.1.1"]):
                                            pass
                                            if 'i2.2.1.0' not in subst3 or 'i2.2.1.1' not in subst3 or cons_f29(d=subst3["i2.2.1.0"], x=subst3["i2.2.1.1"]):
                                                pass
                                                if 'i2.2_1' not in subst3 or 'i2.2.1.1' not in subst3 or cons_f19(m=subst3["i2.2_1"], x=subst3["i2.2.1.1"]):
                                                    pass
                                                    # State 2555
                                                    if len(subjects) == 0:
                                                        pass
                                                        # 17: b*v**n /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f19) and (cons_f4) and (cons_f5) and (cons_f7) and (cons_f44)
                                                        yield 17, subst3
                        if 'i2.2.1.0_1' not in subst3 or 'i2.2.1.1' not in subst3 or cons_f3(b=subst3["i2.2.1.0_1"], x=subst3["i2.2.1.1"]):
                            pass
                            if 'i2.2.1.0' not in subst3 or 'i2.2.1.1' not in subst3 or cons_f2(a=subst3["i2.2.1.0"], x=subst3["i2.2.1.1"]):
                                pass
                                if 'i2.2.1.2' not in subst3 or 'i2.2.1.1' not in subst3 or cons_f5(p=subst3["i2.2.1.2"], x=subst3["i2.2.1.1"]):
                                    pass
                                    if 'i2.2.1.2_1' not in subst3 or 'i2.2.1.1' not in subst3 or cons_f52(q=subst3["i2.2.1.2_1"], x=subst3["i2.2.1.1"]):
                                        pass
                                        if 'i2.2.1.0_2' not in subst3 or 'i2.2.1.1' not in subst3 or cons_f8(c=subst3["i2.2.1.0_2"], x=subst3["i2.2.1.1"]):
                                            pass
                                            if 'i2.2.1.2_2' not in subst3 or 'i2.2.1.1' not in subst3 or cons_f54(r=subst3["i2.2.1.2_2"], x=subst3["i2.2.1.1"]):
                                                pass
                                                # State 2555
                                                if len(subjects) == 0:
                                                    pass
                                                    # 28: b*v**n /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f5) and (cons_f52) and (cons_f54) and (cons_f51)
                                                    yield 28, subst3
                                        # State 2555
                                        if len(subjects) == 0:
                                            pass
                                            # 26: b*v**n /; (cons_f2) and (cons_f3) and (cons_f5) and (cons_f52) and (cons_f51)
                                            yield 26, subst3
                        if 'i2' not in subst3 or 'i2.2.1.1' not in subst3 or cons_f11(Pm=subst3["i2.2.1.1"], x=subst3["i2"]):
                            pass
                            if 'i2' not in subst3 or 'i2.2.1.1' not in subst3 or 'i2.2.1.0' not in subst3 or 'i2.2.0' not in subst3 or 'i2.0' not in subst3 or 'i2.2.1.2_1' not in subst3 or 'i2.2.1.2' not in subst3 or 'i2.2' not in subst3 or 'i2.2.1.0_1' not in subst3 or With36(Pm=subst3["i2.2.1.1"], Qm=subst3["i2.0"], a=subst3["i2.2.0"], b=subst3["i2.2.1.0"], c=subst3["i2.2.1.0_1"], n=subst3["i2.2.1.2"], n2=subst3["i2.2.1.2_1"], p=subst3["i2.2"], x=subst3["i2"]):
                                pass
                                # State 2555
                                if len(subjects) == 0:
                                    pass
                                    # 36: b*v**n /; (cons_f8) and (cons_f48) and (cons_f11) and (With36)
                                    yield 36, subst3
                    subjects.appendleft(tmp95)
            if len(subjects) >= 1:
                tmp97 = subjects.popleft()
                subst2 = Substitution(subst1)
                try:
                    subst2.try_add_variable('i2.2.1.0', tmp97)
                except ValueError:
                    pass
                else:
                    pass
                    if 'i2' not in subst2 or 'i2.2.1.0' not in subst2 or cons_f10(v=subst2["i2.2.1.0"], x=subst2["i2"]):
                        pass
                        # State 2625
                        if len(subjects) == 0:
                            pass
                            # 6: v*a /; (cons_f2) and (cons_f10)
                            yield 6, subst2
                    # State 2625
                    if len(subjects) == 0:
                        pass
                        # 8: v*a /; (cons_f3) and (cons_f27) and (cons_f28)
                        yield 8, subst2
                        # 10: v*a /; (cons_f3) and (cons_f27) and (cons_f30)
                        yield 10, subst2
                        # 12: v*a /; (cons_f3) and (cons_f27) and (cons_f32)
                        yield 12, subst2
                        # 14: v*a /; (cons_f3) and (cons_f35)
                        yield 14, subst2
                subjects.appendleft(tmp97)
            if len(subjects) >= 1:
                tmp99 = subjects.popleft()
                subst2 = Substitution(subst1)
                try:
                    subst2.try_add_variable('i2.2.1.1', tmp99)
                except ValueError:
                    pass
                else:
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
                                            # State 2877
                                            if len(subjects) == 0:
                                                pass
                                                # 24: b*x /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f50) and (cons_f5) and (cons_f49)
                                                yield 24, subst2
                        if 'i2.2.1.0_1' not in subst2 or 'i2.2.1.1' not in subst2 or cons_f3(b=subst2["i2.2.1.0_1"], x=subst2["i2.2.1.1"]):
                            pass
                            if 'i2.2.1.0' not in subst2 or 'i2.2.1.1' not in subst2 or cons_f8(c=subst2["i2.2.1.0"], x=subst2["i2.2.1.1"]):
                                pass
                                # State 2877
                                if len(subjects) == 0:
                                    pass
                                    # 20: b*x /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f47)
                                    yield 20, subst2
                subjects.appendleft(tmp99)
            subst2 = Substitution(subst1)
            try:
                subst2.try_add_variable('i2.2.1.2', S(1))
            except ValueError:
                pass
            else:
                pass
                # State 3043
                if len(subjects) >= 1:
                    tmp102 = subjects.popleft()
                    subst3 = Substitution(subst2)
                    try:
                        subst3.try_add_variable('i2.2.1.1', tmp102)
                    except ValueError:
                        pass
                    else:
                        pass
                        if 'i2.2.1.2' not in subst3 or 'i2.2.1.1' not in subst3 or cons_f4(n=subst3["i2.2.1.2"], x=subst3["i2.2.1.1"]):
                            pass
                            if 'i2.2' not in subst3 or 'i2.2.1.1' not in subst3 or cons_f5(p=subst3["i2.2"], x=subst3["i2.2.1.1"]):
                                pass
                                if 'i2.2_1' not in subst3 or 'i2.2.1.1' not in subst3 or cons_f19(m=subst3["i2.2_1"], x=subst3["i2.2.1.1"]):
                                    pass
                                    if 'i2.2.0' not in subst3 or 'i2.2.1.1' not in subst3 or cons_f59(a1=subst3["i2.2.0"], x=subst3["i2.2.1.1"]):
                                        pass
                                        if 'i2.2.1.0' not in subst3 or 'i2.2.1.1' not in subst3 or cons_f60(b1=subst3["i2.2.1.0"], x=subst3["i2.2.1.1"]):
                                            pass
                                            if 'i2.2.0_1' not in subst3 or 'i2.2.1.1' not in subst3 or cons_f61(a2=subst3["i2.2.0_1"], x=subst3["i2.2.1.1"]):
                                                pass
                                                if 'i2.2.1.0_1' not in subst3 or 'i2.2.1.1' not in subst3 or cons_f62(b2=subst3["i2.2.1.0_1"], x=subst3["i2.2.1.1"]):
                                                    pass
                                                    # State 3044
                                                    if len(subjects) == 0:
                                                        pass
                                                        # 33: b2*v**m /; (cons_f59) and (cons_f60) and (cons_f61) and (cons_f62) and (cons_f19) and (cons_f4) and (cons_f5) and (cons_f57) and (cons_f58)
                                                        yield 33, subst3
                    subjects.appendleft(tmp102)
            if len(subjects) >= 1 and isinstance(subjects[0], Pow):
                tmp104 = subjects.popleft()
                subjects105 = deque(tmp104._args)
                # State 2556
                if len(subjects105) >= 1:
                    tmp106 = subjects105.popleft()
                    subst2 = Substitution(subst1)
                    try:
                        subst2.try_add_variable('i2.2.1.1', tmp106)
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
                                                # State 2557
                                                subst3 = Substitution(subst2)
                                                try:
                                                    subst3.try_add_variable('i2.2.1.2_1', 1)
                                                except ValueError:
                                                    pass
                                                else:
                                                    pass
                                                    if 'i2.2.1.2' not in subst3 or 'i2.2.1.2_1' not in subst3 or cons_f39(n=subst3["i2.2.1.2"], q=subst3["i2.2.1.2_1"]):
                                                        pass
                                                        # State 2558
                                                        if len(subjects105) == 0:
                                                            pass
                                                            # State 2559
                                                            if len(subjects) == 0:
                                                                pass
                                                                # 16: b*v**n /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f19) and (cons_f4) and (cons_f39) and (cons_f41)
                                                                yield 16, subst3
                                                if len(subjects105) >= 1:
                                                    tmp109 = subjects105.popleft()
                                                    subst3 = Substitution(subst2)
                                                    try:
                                                        subst3.try_add_variable('i2.2.1.2_1', tmp109)
                                                    except ValueError:
                                                        pass
                                                    else:
                                                        pass
                                                        if 'i2.2.1.2' not in subst3 or 'i2.2.1.2_1' not in subst3 or cons_f39(n=subst3["i2.2.1.2"], q=subst3["i2.2.1.2_1"]):
                                                            pass
                                                            # State 2558
                                                            if len(subjects105) == 0:
                                                                pass
                                                                # State 2559
                                                                if len(subjects) == 0:
                                                                    pass
                                                                    # 16: b*v**n /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f19) and (cons_f4) and (cons_f39) and (cons_f41)
                                                                    yield 16, subst3
                                                    subjects105.appendleft(tmp109)
                                                subst3 = Substitution(subst2)
                                                try:
                                                    subst3.try_add_variable('i2.2.1.2', 1)
                                                except ValueError:
                                                    pass
                                                else:
                                                    pass
                                                if len(subjects105) >= 1:
                                                    tmp112 = subjects105.popleft()
                                                    subst3 = Substitution(subst2)
                                                    try:
                                                        subst3.try_add_variable('i2.2.1.2', tmp112)
                                                    except ValueError:
                                                        pass
                                                    else:
                                                        pass
                                                    subjects105.appendleft(tmp112)
                                    if 'i2.2.1.0_1' not in subst2 or 'i2.2.1.1' not in subst2 or cons_f8(c=subst2["i2.2.1.0_1"], x=subst2["i2.2.1.1"]):
                                        pass
                                        # State 2557
                                        subst3 = Substitution(subst2)
                                        try:
                                            subst3.try_add_variable('i2.2.1.2_1', 1)
                                        except ValueError:
                                            pass
                                        else:
                                            pass
                                            if 'i2.2.1.2' not in subst3 or 'i2.2.1.2_1' not in subst3 or cons_f48(n=subst3["i2.2.1.2"], n2=subst3["i2.2.1.2_1"]):
                                                pass
                                                # State 2558
                                                if len(subjects105) == 0:
                                                    pass
                                                    # State 2559
                                                    if len(subjects) == 0:
                                                        pass
                                                        # 21: b*v**n /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f4) and (cons_f48) and (cons_f47)
                                                        yield 21, subst3
                                        if len(subjects105) >= 1:
                                            tmp115 = subjects105.popleft()
                                            subst3 = Substitution(subst2)
                                            try:
                                                subst3.try_add_variable('i2.2.1.2_1', tmp115)
                                            except ValueError:
                                                pass
                                            else:
                                                pass
                                                if 'i2.2.1.2' not in subst3 or 'i2.2.1.2_1' not in subst3 or cons_f48(n=subst3["i2.2.1.2"], n2=subst3["i2.2.1.2_1"]):
                                                    pass
                                                    # State 2558
                                                    if len(subjects105) == 0:
                                                        pass
                                                        # State 2559
                                                        if len(subjects) == 0:
                                                            pass
                                                            # 21: b*v**n /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f4) and (cons_f48) and (cons_f47)
                                                            yield 21, subst3
                                            subjects105.appendleft(tmp115)
                                        subst3 = Substitution(subst2)
                                        try:
                                            subst3.try_add_variable('i2.2.1.2', 1)
                                        except ValueError:
                                            pass
                                        else:
                                            pass
                                        if len(subjects105) >= 1:
                                            tmp118 = subjects105.popleft()
                                            subst3 = Substitution(subst2)
                                            try:
                                                subst3.try_add_variable('i2.2.1.2', tmp118)
                                            except ValueError:
                                                pass
                                            else:
                                                pass
                                            subjects105.appendleft(tmp118)
                            if 'i2.2' not in subst2 or 'i2.2.1.1' not in subst2 or cons_f5(p=subst2["i2.2"], x=subst2["i2.2.1.1"]):
                                pass
                                if 'i2.2.1.0_1' not in subst2 or 'i2.2.1.1' not in subst2 or cons_f3(b=subst2["i2.2.1.0_1"], x=subst2["i2.2.1.1"]):
                                    pass
                                    if 'i2.2.1.0' not in subst2 or 'i2.2.1.1' not in subst2 or cons_f8(c=subst2["i2.2.1.0"], x=subst2["i2.2.1.1"]):
                                        pass
                                        if 'i2.2.1.2_1' not in subst2 or 'i2.2.1.1' not in subst2 or cons_f4(n=subst2["i2.2.1.2_1"], x=subst2["i2.2.1.1"]):
                                            pass
                                            # State 2557
                                            subst3 = Substitution(subst2)
                                            try:
                                                subst3.try_add_variable('i2.2.1.2_1', 1)
                                            except ValueError:
                                                pass
                                            else:
                                                pass
                                                if 'i2.2.1.2_1' not in subst3 or 'i2.2.1.1' not in subst3 or cons_f4(n=subst3["i2.2.1.2_1"], x=subst3["i2.2.1.1"]):
                                                    pass
                                                    if 'i2.2.1.2' not in subst3 or 'i2.2.1.2_1' not in subst3 or cons_f7(j=subst3["i2.2.1.2"], n=subst3["i2.2.1.2_1"]):
                                                        pass
                                                        # State 2558
                                                        if len(subjects105) == 0:
                                                            pass
                                                            # State 2559
                                                            if len(subjects) == 0:
                                                                pass
                                                                # 3: b*v**n /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f4) and (cons_f5) and (cons_f7)
                                                                yield 3, subst3
                                                                # 4: b*v**n /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f4) and (cons_f5) and (cons_f7) and (cons_f6)
                                                                yield 4, subst3
                                            if len(subjects105) >= 1:
                                                tmp121 = subjects105.popleft()
                                                subst3 = Substitution(subst2)
                                                try:
                                                    subst3.try_add_variable('i2.2.1.2_1', tmp121)
                                                except ValueError:
                                                    pass
                                                else:
                                                    pass
                                                    if 'i2.2.1.2_1' not in subst3 or 'i2.2.1.1' not in subst3 or cons_f4(n=subst3["i2.2.1.2_1"], x=subst3["i2.2.1.1"]):
                                                        pass
                                                        if 'i2.2.1.2' not in subst3 or 'i2.2.1.2_1' not in subst3 or cons_f7(j=subst3["i2.2.1.2"], n=subst3["i2.2.1.2_1"]):
                                                            pass
                                                            # State 2558
                                                            if len(subjects105) == 0:
                                                                pass
                                                                # State 2559
                                                                if len(subjects) == 0:
                                                                    pass
                                                                    # 3: b*v**n /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f4) and (cons_f5) and (cons_f7)
                                                                    yield 3, subst3
                                                                    # 4: b*v**n /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f4) and (cons_f5) and (cons_f7) and (cons_f6)
                                                                    yield 4, subst3
                                                subjects105.appendleft(tmp121)
                                            subst3 = Substitution(subst2)
                                            try:
                                                subst3.try_add_variable('i2.2.1.2', 1)
                                            except ValueError:
                                                pass
                                            else:
                                                pass
                                            if len(subjects105) >= 1:
                                                tmp124 = subjects105.popleft()
                                                subst3 = Substitution(subst2)
                                                try:
                                                    subst3.try_add_variable('i2.2.1.2', tmp124)
                                                except ValueError:
                                                    pass
                                                else:
                                                    pass
                                                subjects105.appendleft(tmp124)
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
                                                    # State 2557
                                                    subst3 = Substitution(subst2)
                                                    try:
                                                        subst3.try_add_variable('i2.2.1.2_1', 1)
                                                    except ValueError:
                                                        pass
                                                    else:
                                                        pass
                                                    if len(subjects105) >= 1:
                                                        tmp127 = subjects105.popleft()
                                                        subst3 = Substitution(subst2)
                                                        try:
                                                            subst3.try_add_variable('i2.2.1.2_1', tmp127)
                                                        except ValueError:
                                                            pass
                                                        else:
                                                            pass
                                                        subjects105.appendleft(tmp127)
                                                    subst3 = Substitution(subst2)
                                                    try:
                                                        subst3.try_add_variable('i2.2.1.2', 1)
                                                    except ValueError:
                                                        pass
                                                    else:
                                                        pass
                                                        if 'i2.2.1.2' not in subst3 or 'i2.2.1.1' not in subst3 or cons_f4(n=subst3["i2.2.1.2"], x=subst3["i2.2.1.1"]):
                                                            pass
                                                            if 'i2.2.1.2' not in subst3 or 'i2.2_1' not in subst3 or cons_f58(m=subst3["i2.2_1"], n=subst3["i2.2.1.2"]):
                                                                pass
                                                                # State 3045
                                                                if len(subjects105) == 0:
                                                                    pass
                                                                    # State 3046
                                                                    if len(subjects) == 0:
                                                                        pass
                                                                        # 33: b2*v**m /; (cons_f59) and (cons_f60) and (cons_f61) and (cons_f62) and (cons_f19) and (cons_f4) and (cons_f5) and (cons_f57) and (cons_f58)
                                                                        yield 33, subst3
                                                    if len(subjects105) >= 1:
                                                        tmp130 = subjects105.popleft()
                                                        subst3 = Substitution(subst2)
                                                        try:
                                                            subst3.try_add_variable('i2.2.1.2', tmp130)
                                                        except ValueError:
                                                            pass
                                                        else:
                                                            pass
                                                            if 'i2.2.1.2' not in subst3 or 'i2.2.1.1' not in subst3 or cons_f4(n=subst3["i2.2.1.2"], x=subst3["i2.2.1.1"]):
                                                                pass
                                                                if 'i2.2.1.2' not in subst3 or 'i2.2_1' not in subst3 or cons_f58(m=subst3["i2.2_1"], n=subst3["i2.2.1.2"]):
                                                                    pass
                                                                    # State 3045
                                                                    if len(subjects105) == 0:
                                                                        pass
                                                                        # State 3046
                                                                        if len(subjects) == 0:
                                                                            pass
                                                                            # 33: b2*v**m /; (cons_f59) and (cons_f60) and (cons_f61) and (cons_f62) and (cons_f19) and (cons_f4) and (cons_f5) and (cons_f57) and (cons_f58)
                                                                            yield 33, subst3
                                                        subjects105.appendleft(tmp130)
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
                                                    # State 2557
                                                    subst3 = Substitution(subst2)
                                                    try:
                                                        subst3.try_add_variable('i2.2.1.2_1', 1)
                                                    except ValueError:
                                                        pass
                                                    else:
                                                        pass
                                                        if 'i2.2.1.2_1' not in subst3 or 'i2.2.1.1' not in subst3 or cons_f4(n=subst3["i2.2.1.2_1"], x=subst3["i2.2.1.1"]):
                                                            pass
                                                            if 'i2.2.1.2' not in subst3 or 'i2.2.1.2_1' not in subst3 or cons_f7(j=subst3["i2.2.1.2"], n=subst3["i2.2.1.2_1"]):
                                                                pass
                                                                # State 2558
                                                                if len(subjects105) == 0:
                                                                    pass
                                                                    # State 2559
                                                                    if len(subjects) == 0:
                                                                        pass
                                                                        # 17: b*v**n /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f19) and (cons_f4) and (cons_f5) and (cons_f7) and (cons_f44)
                                                                        yield 17, subst3
                                                    if len(subjects105) >= 1:
                                                        tmp133 = subjects105.popleft()
                                                        subst3 = Substitution(subst2)
                                                        try:
                                                            subst3.try_add_variable('i2.2.1.2_1', tmp133)
                                                        except ValueError:
                                                            pass
                                                        else:
                                                            pass
                                                            if 'i2.2.1.2_1' not in subst3 or 'i2.2.1.1' not in subst3 or cons_f4(n=subst3["i2.2.1.2_1"], x=subst3["i2.2.1.1"]):
                                                                pass
                                                                if 'i2.2.1.2' not in subst3 or 'i2.2.1.2_1' not in subst3 or cons_f7(j=subst3["i2.2.1.2"], n=subst3["i2.2.1.2_1"]):
                                                                    pass
                                                                    # State 2558
                                                                    if len(subjects105) == 0:
                                                                        pass
                                                                        # State 2559
                                                                        if len(subjects) == 0:
                                                                            pass
                                                                            # 17: b*v**n /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f19) and (cons_f4) and (cons_f5) and (cons_f7) and (cons_f44)
                                                                            yield 17, subst3
                                                        subjects105.appendleft(tmp133)
                                                    subst3 = Substitution(subst2)
                                                    try:
                                                        subst3.try_add_variable('i2.2.1.2', 1)
                                                    except ValueError:
                                                        pass
                                                    else:
                                                        pass
                                                    if len(subjects105) >= 1:
                                                        tmp136 = subjects105.popleft()
                                                        subst3 = Substitution(subst2)
                                                        try:
                                                            subst3.try_add_variable('i2.2.1.2', tmp136)
                                                        except ValueError:
                                                            pass
                                                        else:
                                                            pass
                                                        subjects105.appendleft(tmp136)
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
                                                # State 2557
                                                subst3 = Substitution(subst2)
                                                try:
                                                    subst3.try_add_variable('i2.2.1.2_1', 1)
                                                except ValueError:
                                                    pass
                                                else:
                                                    pass
                                                    if 'i2.2.1.2_1' not in subst3 or 'i2.2.1.1' not in subst3 or cons_f52(q=subst3["i2.2.1.2_1"], x=subst3["i2.2.1.1"]):
                                                        pass
                                                        if 'i2.2.1.2' not in subst3 or 'i2.2.1.2_1' not in subst3 or cons_f51(p=subst3["i2.2.1.2"], q=subst3["i2.2.1.2_1"]):
                                                            pass
                                                            # State 2558
                                                            if len(subjects105) == 0:
                                                                pass
                                                                # State 2559
                                                                if len(subjects) == 0:
                                                                    pass
                                                                    # 28: b*v**n /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f5) and (cons_f52) and (cons_f54) and (cons_f51)
                                                                    yield 28, subst3
                                                if len(subjects105) >= 1:
                                                    tmp139 = subjects105.popleft()
                                                    subst3 = Substitution(subst2)
                                                    try:
                                                        subst3.try_add_variable('i2.2.1.2_1', tmp139)
                                                    except ValueError:
                                                        pass
                                                    else:
                                                        pass
                                                        if 'i2.2.1.2_1' not in subst3 or 'i2.2.1.1' not in subst3 or cons_f52(q=subst3["i2.2.1.2_1"], x=subst3["i2.2.1.1"]):
                                                            pass
                                                            if 'i2.2.1.2' not in subst3 or 'i2.2.1.2_1' not in subst3 or cons_f51(p=subst3["i2.2.1.2"], q=subst3["i2.2.1.2_1"]):
                                                                pass
                                                                # State 2558
                                                                if len(subjects105) == 0:
                                                                    pass
                                                                    # State 2559
                                                                    if len(subjects) == 0:
                                                                        pass
                                                                        # 28: b*v**n /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f5) and (cons_f52) and (cons_f54) and (cons_f51)
                                                                        yield 28, subst3
                                                    subjects105.appendleft(tmp139)
                                                subst3 = Substitution(subst2)
                                                try:
                                                    subst3.try_add_variable('i2.2.1.2', 1)
                                                except ValueError:
                                                    pass
                                                else:
                                                    pass
                                                if len(subjects105) >= 1:
                                                    tmp142 = subjects105.popleft()
                                                    subst3 = Substitution(subst2)
                                                    try:
                                                        subst3.try_add_variable('i2.2.1.2', tmp142)
                                                    except ValueError:
                                                        pass
                                                    else:
                                                        pass
                                                    subjects105.appendleft(tmp142)
                                        # State 2557
                                        subst3 = Substitution(subst2)
                                        try:
                                            subst3.try_add_variable('i2.2.1.2_1', 1)
                                        except ValueError:
                                            pass
                                        else:
                                            pass
                                            if 'i2.2.1.2_1' not in subst3 or 'i2.2.1.1' not in subst3 or cons_f52(q=subst3["i2.2.1.2_1"], x=subst3["i2.2.1.1"]):
                                                pass
                                                if 'i2.2.1.2' not in subst3 or 'i2.2.1.2_1' not in subst3 or cons_f51(p=subst3["i2.2.1.2"], q=subst3["i2.2.1.2_1"]):
                                                    pass
                                                    # State 2558
                                                    if len(subjects105) == 0:
                                                        pass
                                                        # State 2559
                                                        if len(subjects) == 0:
                                                            pass
                                                            # 26: b*v**n /; (cons_f2) and (cons_f3) and (cons_f5) and (cons_f52) and (cons_f51)
                                                            yield 26, subst3
                                        if len(subjects105) >= 1:
                                            tmp145 = subjects105.popleft()
                                            subst3 = Substitution(subst2)
                                            try:
                                                subst3.try_add_variable('i2.2.1.2_1', tmp145)
                                            except ValueError:
                                                pass
                                            else:
                                                pass
                                                if 'i2.2.1.2_1' not in subst3 or 'i2.2.1.1' not in subst3 or cons_f52(q=subst3["i2.2.1.2_1"], x=subst3["i2.2.1.1"]):
                                                    pass
                                                    if 'i2.2.1.2' not in subst3 or 'i2.2.1.2_1' not in subst3 or cons_f51(p=subst3["i2.2.1.2"], q=subst3["i2.2.1.2_1"]):
                                                        pass
                                                        # State 2558
                                                        if len(subjects105) == 0:
                                                            pass
                                                            # State 2559
                                                            if len(subjects) == 0:
                                                                pass
                                                                # 26: b*v**n /; (cons_f2) and (cons_f3) and (cons_f5) and (cons_f52) and (cons_f51)
                                                                yield 26, subst3
                                            subjects105.appendleft(tmp145)
                                        subst3 = Substitution(subst2)
                                        try:
                                            subst3.try_add_variable('i2.2.1.2', 1)
                                        except ValueError:
                                            pass
                                        else:
                                            pass
                                        if len(subjects105) >= 1:
                                            tmp148 = subjects105.popleft()
                                            subst3 = Substitution(subst2)
                                            try:
                                                subst3.try_add_variable('i2.2.1.2', tmp148)
                                            except ValueError:
                                                pass
                                            else:
                                                pass
                                            subjects105.appendleft(tmp148)
                        if 'i2' not in subst2 or 'i2.2.1.1' not in subst2 or cons_f11(Pm=subst2["i2.2.1.1"], x=subst2["i2"]):
                            pass
                            if 'i2' not in subst2 or 'i2.2.1.1' not in subst2 or 'i2.2.1.0' not in subst2 or 'i2.2.0' not in subst2 or 'i2.0' not in subst2 or 'i2.2.1.2_1' not in subst2 or 'i2.2.1.2' not in subst2 or 'i2.2' not in subst2 or 'i2.2.1.0_1' not in subst2 or With36(Pm=subst2["i2.2.1.1"], Qm=subst2["i2.0"], a=subst2["i2.2.0"], b=subst2["i2.2.1.0"], c=subst2["i2.2.1.0_1"], n=subst2["i2.2.1.2"], n2=subst2["i2.2.1.2_1"], p=subst2["i2.2"], x=subst2["i2"]):
                                pass
                                # State 2557
                                subst3 = Substitution(subst2)
                                try:
                                    subst3.try_add_variable('i2.2.1.2_1', 1)
                                except ValueError:
                                    pass
                                else:
                                    pass
                                    if 'i2.2.1.2' not in subst3 or 'i2.2.1.2_1' not in subst3 or cons_f48(n=subst3["i2.2.1.2"], n2=subst3["i2.2.1.2_1"]):
                                        pass
                                        if 'i2' not in subst3 or 'i2.2.1.1' not in subst3 or 'i2.2.1.0' not in subst3 or 'i2.2.0' not in subst3 or 'i2.0' not in subst3 or 'i2.2.1.2_1' not in subst3 or 'i2.2.1.2' not in subst3 or 'i2.2' not in subst3 or 'i2.2.1.0_1' not in subst3 or With36(Pm=subst3["i2.2.1.1"], Qm=subst3["i2.0"], a=subst3["i2.2.0"], b=subst3["i2.2.1.0"], c=subst3["i2.2.1.0_1"], n=subst3["i2.2.1.2"], n2=subst3["i2.2.1.2_1"], p=subst3["i2.2"], x=subst3["i2"]):
                                            pass
                                            # State 2558
                                            if len(subjects105) == 0:
                                                pass
                                                # State 2559
                                                if len(subjects) == 0:
                                                    pass
                                                    # 36: b*v**n /; (cons_f8) and (cons_f48) and (cons_f11) and (With36)
                                                    yield 36, subst3
                                if len(subjects105) >= 1:
                                    tmp151 = subjects105.popleft()
                                    subst3 = Substitution(subst2)
                                    try:
                                        subst3.try_add_variable('i2.2.1.2_1', tmp151)
                                    except ValueError:
                                        pass
                                    else:
                                        pass
                                        if 'i2.2.1.2' not in subst3 or 'i2.2.1.2_1' not in subst3 or cons_f48(n=subst3["i2.2.1.2"], n2=subst3["i2.2.1.2_1"]):
                                            pass
                                            if 'i2' not in subst3 or 'i2.2.1.1' not in subst3 or 'i2.2.1.0' not in subst3 or 'i2.2.0' not in subst3 or 'i2.0' not in subst3 or 'i2.2.1.2_1' not in subst3 or 'i2.2.1.2' not in subst3 or 'i2.2' not in subst3 or 'i2.2.1.0_1' not in subst3 or With36(Pm=subst3["i2.2.1.1"], Qm=subst3["i2.0"], a=subst3["i2.2.0"], b=subst3["i2.2.1.0"], c=subst3["i2.2.1.0_1"], n=subst3["i2.2.1.2"], n2=subst3["i2.2.1.2_1"], p=subst3["i2.2"], x=subst3["i2"]):
                                                pass
                                                # State 2558
                                                if len(subjects105) == 0:
                                                    pass
                                                    # State 2559
                                                    if len(subjects) == 0:
                                                        pass
                                                        # 36: b*v**n /; (cons_f8) and (cons_f48) and (cons_f11) and (With36)
                                                        yield 36, subst3
                                    subjects105.appendleft(tmp151)
                                subst3 = Substitution(subst2)
                                try:
                                    subst3.try_add_variable('i2.2.1.2', 1)
                                except ValueError:
                                    pass
                                else:
                                    pass
                                if len(subjects105) >= 1:
                                    tmp154 = subjects105.popleft()
                                    subst3 = Substitution(subst2)
                                    try:
                                        subst3.try_add_variable('i2.2.1.2', tmp154)
                                    except ValueError:
                                        pass
                                    else:
                                        pass
                                    subjects105.appendleft(tmp154)
                    subjects105.appendleft(tmp106)
                subjects.appendleft(tmp104)
        subst1 = Substitution(subst0)
        try:
            subst1.try_add_variable('i2.2.1.0_2', S(1))
        except ValueError:
            pass
        else:
            pass
            # State 2627
            if len(subjects) >= 1:
                tmp157 = subjects.popleft()
                subst2 = Substitution(subst1)
                try:
                    subst2.try_add_variable('i2.2.1.0', tmp157)
                except ValueError:
                    pass
                else:
                    pass
                    if 'i2' not in subst2 or 'i2.2.1.0' not in subst2 or cons_f10(v=subst2["i2.2.1.0"], x=subst2["i2"]):
                        pass
                        # State 2628
                        if len(subjects) == 0:
                            pass
                            # 7: v*b /; (cons_f3) and (cons_f10)
                            yield 7, subst2
                    # State 2628
                    if len(subjects) == 0:
                        pass
                        # 9: v*b /; (cons_f29) and (cons_f27) and (cons_f28)
                        yield 9, subst2
                        # 11: v*b /; (cons_f29) and (cons_f27) and (cons_f30)
                        yield 11, subst2
                        # 13: v*b /; (cons_f29) and (cons_f27) and (cons_f32)
                        yield 13, subst2
                subjects.appendleft(tmp157)
            subst2 = Substitution(subst1)
            try:
                subst2.try_add_variable('i2.2.1.2_2', S(1))
            except ValueError:
                pass
            else:
                pass
                # State 3001
                if len(subjects) >= 1:
                    tmp160 = subjects.popleft()
                    subst3 = Substitution(subst2)
                    try:
                        subst3.try_add_variable('i2.2.1.1', tmp160)
                    except ValueError:
                        pass
                    else:
                        pass
                        if 'i2.2.1.0_1' not in subst3 or 'i2.2.1.1' not in subst3 or cons_f3(b=subst3["i2.2.1.0_1"], x=subst3["i2.2.1.1"]):
                            pass
                            if 'i2.2.1.0' not in subst3 or 'i2.2.1.1' not in subst3 or cons_f2(a=subst3["i2.2.1.0"], x=subst3["i2.2.1.1"]):
                                pass
                                if 'i2.2.1.2' not in subst3 or 'i2.2.1.1' not in subst3 or cons_f5(p=subst3["i2.2.1.2"], x=subst3["i2.2.1.1"]):
                                    pass
                                    if 'i2.2.1.2_1' not in subst3 or 'i2.2.1.1' not in subst3 or cons_f52(q=subst3["i2.2.1.2_1"], x=subst3["i2.2.1.1"]):
                                        pass
                                        if 'i2.2.1.0_2' not in subst3 or 'i2.2.1.1' not in subst3 or cons_f8(c=subst3["i2.2.1.0_2"], x=subst3["i2.2.1.1"]):
                                            pass
                                            if 'i2.2.1.2_2' not in subst3 or 'i2.2.1.1' not in subst3 or cons_f54(r=subst3["i2.2.1.2_2"], x=subst3["i2.2.1.1"]):
                                                pass
                                                # State 3002
                                                if len(subjects) == 0:
                                                    pass
                                                    # 29: c*x**r /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f5) and (cons_f52) and (cons_f54) and (cons_f53)
                                                    yield 29, subst3
                    subjects.appendleft(tmp160)
            if len(subjects) >= 1 and isinstance(subjects[0], Pow):
                tmp162 = subjects.popleft()
                subjects163 = deque(tmp162._args)
                # State 3003
                if len(subjects163) >= 1:
                    tmp164 = subjects163.popleft()
                    subst2 = Substitution(subst1)
                    try:
                        subst2.try_add_variable('i2.2.1.1', tmp164)
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
                                                # State 3004
                                                subst3 = Substitution(subst2)
                                                try:
                                                    subst3.try_add_variable('i2.2.1.2_2', 1)
                                                except ValueError:
                                                    pass
                                                else:
                                                    pass
                                                    if 'i2.2.1.2_2' not in subst3 or 'i2.2.1.1' not in subst3 or cons_f54(r=subst3["i2.2.1.2_2"], x=subst3["i2.2.1.1"]):
                                                        pass
                                                        if 'i2.2.1.2' not in subst3 or 'i2.2.1.2_2' not in subst3 or cons_f53(p=subst3["i2.2.1.2"], r=subst3["i2.2.1.2_2"]):
                                                            pass
                                                            # State 3005
                                                            if len(subjects163) == 0:
                                                                pass
                                                                # State 3006
                                                                if len(subjects) == 0:
                                                                    pass
                                                                    # 29: c*x**r /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f5) and (cons_f52) and (cons_f54) and (cons_f53)
                                                                    yield 29, subst3
                                                if len(subjects163) >= 1:
                                                    tmp167 = subjects163.popleft()
                                                    subst3 = Substitution(subst2)
                                                    try:
                                                        subst3.try_add_variable('i2.2.1.2_2', tmp167)
                                                    except ValueError:
                                                        pass
                                                    else:
                                                        pass
                                                        if 'i2.2.1.2_2' not in subst3 or 'i2.2.1.1' not in subst3 or cons_f54(r=subst3["i2.2.1.2_2"], x=subst3["i2.2.1.1"]):
                                                            pass
                                                            if 'i2.2.1.2' not in subst3 or 'i2.2.1.2_2' not in subst3 or cons_f53(p=subst3["i2.2.1.2"], r=subst3["i2.2.1.2_2"]):
                                                                pass
                                                                # State 3005
                                                                if len(subjects163) == 0:
                                                                    pass
                                                                    # State 3006
                                                                    if len(subjects) == 0:
                                                                        pass
                                                                        # 29: c*x**r /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f5) and (cons_f52) and (cons_f54) and (cons_f53)
                                                                        yield 29, subst3
                                                    subjects163.appendleft(tmp167)
                    subjects163.appendleft(tmp164)
                subjects.appendleft(tmp162)
        if len(subjects) >= 1 and isinstance(subjects[0], Mul):
            tmp169 = subjects.popleft()
            associative1 = tmp169
            associative_type1 = type(tmp169)
            subjects170 = deque(tmp169._args)
            matcher = CommutativeMatcher2383.get()
            tmp171 = subjects170
            subjects170 = []
            for s in tmp171:
                matcher.add_subject(s)
            for pattern_index, subst1 in matcher.match(tmp171, subst0):
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
                                    if 'i2.2.1.0' not in subst1 or cons_f6(b=subst1["i2.2.1.0"]):
                                        pass
                                        # State 2390
                                        if len(subjects) == 0:
                                            pass
                                            # 1: a*v**m /; (cons_f2) and (cons_f3) and (cons_f4) and (cons_f5) and (cons_f6)
                                            yield 1, subst1
                                    # State 2390
                                    if len(subjects) == 0:
                                        pass
                                        # 0: a*v**m /; (cons_f2) and (cons_f3) and (cons_f4) and (cons_f5)
                                        yield 0, subst1
                if pattern_index == 1:
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
                                                # State 2552
                                                if len(subjects) == 0:
                                                    pass
                                                    # 5: a*v**m /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f4) and (cons_f5) and (cons_f7) and (cons_f9)
                                                    yield 5, subst1
                                            # State 2552
                                            if len(subjects) == 0:
                                                pass
                                                # 2: a*v**m /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f4) and (cons_f5) and (cons_f7)
                                                yield 2, subst1
                if pattern_index == 2:
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
                                                # State 2564
                                                if len(subjects) == 0:
                                                    pass
                                                    # 4: b*v**n /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f4) and (cons_f5) and (cons_f7) and (cons_f6)
                                                    yield 4, subst1
                                            # State 2564
                                            if len(subjects) == 0:
                                                pass
                                                # 3: b*v**n /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f4) and (cons_f5) and (cons_f7)
                                                yield 3, subst1
                if pattern_index == 3:
                    pass
                    if 'i2' not in subst1 or 'i2.2.1.0_1' not in subst1 or cons_f2(a=subst1["i2.2.1.0_1"], x=subst1["i2"]):
                        pass
                        if 'i2' not in subst1 or 'i2.2.1.0' not in subst1 or cons_f10(v=subst1["i2.2.1.0"], x=subst1["i2"]):
                            pass
                            # State 2626
                            if len(subjects) == 0:
                                pass
                                # 6: v*a /; (cons_f2) and (cons_f10)
                                yield 6, subst1
                    if 'i2' not in subst1 or 'i2.2.1.0_1' not in subst1 or cons_f3(b=subst1["i2.2.1.0_1"], x=subst1["i2"]):
                        pass
                        if 'i2.2.1.0_2' not in subst1 or 'i2.2.1.0_1' not in subst1 or 'i2.2.0' not in subst1 or 'i2.2.0_1' not in subst1 or cons_f27(a=subst1["i2.2.0"], b=subst1["i2.2.1.0_1"], c=subst1["i2.2.0_1"], d=subst1["i2.2.1.0_2"]):
                            pass
                            if 'i2' not in subst1 or 'i2.2.1.0_2' not in subst1 or 'i2.2.0_1' not in subst1 or 'i2.2.0' not in subst1 or 'i2.2_1' not in subst1 or 'i2.2.1.0_1' not in subst1 or cons_f28(a=subst1["i2.2.0"], b=subst1["i2.2.1.0_1"], c=subst1["i2.2.0_1"], d=subst1["i2.2.1.0_2"], n=subst1["i2.2_1"], x=subst1["i2"]):
                                pass
                                # State 2626
                                if len(subjects) == 0:
                                    pass
                                    # 8: v*a /; (cons_f3) and (cons_f27) and (cons_f28)
                                    yield 8, subst1
                            if 'i2.2.1.0_2' not in subst1 or 'i2.2.1.0_1' not in subst1 or cons_f30(b=subst1["i2.2.1.0_1"], d=subst1["i2.2.1.0_2"]):
                                pass
                                # State 2626
                                if len(subjects) == 0:
                                    pass
                                    # 10: v*a /; (cons_f3) and (cons_f27) and (cons_f30)
                                    yield 10, subst1
                            if 'i2.2_1' not in subst1 or 'i2.2.1.0_2' not in subst1 or 'i2.2.1.0_1' not in subst1 or 'i2.2' not in subst1 or cons_f32(b=subst1["i2.2.1.0_1"], d=subst1["i2.2.1.0_2"], m=subst1["i2.2"], n=subst1["i2.2_1"]):
                                pass
                                # State 2626
                                if len(subjects) == 0:
                                    pass
                                    # 12: v*a /; (cons_f3) and (cons_f27) and (cons_f32)
                                    yield 12, subst1
                        if 'i2.1.0' not in subst1 or 'i2.2.0' not in subst1 or 'i2.1.1.0_1' not in subst1 or 'i2.1.1.0' not in subst1 or 'i2.2.1.0_1' not in subst1 or cons_f35(A=subst1["i2.1.0"], B=subst1["i2.1.1.0_1"], C=subst1["i2.1.1.0"], a=subst1["i2.2.0"], b=subst1["i2.2.1.0_1"]):
                            pass
                            # State 2626
                            if len(subjects) == 0:
                                pass
                                # 14: v*a /; (cons_f3) and (cons_f35)
                                yield 14, subst1
                if pattern_index == 4:
                    pass
                    if 'i2' not in subst1 or 'i2.2.1.0' not in subst1 or cons_f10(v=subst1["i2.2.1.0"], x=subst1["i2"]):
                        pass
                        if 'i2.2.1.0_2' not in subst1 or 'i2' not in subst1 or cons_f3(b=subst1["i2.2.1.0_2"], x=subst1["i2"]):
                            pass
                            # State 2629
                            if len(subjects) == 0:
                                pass
                                # 7: v*b /; (cons_f3) and (cons_f10)
                                yield 7, subst1
                    if 'i2.2.1.0_2' not in subst1 or 'i2.2.1.0_1' not in subst1 or 'i2.2.0' not in subst1 or 'i2.2.0_1' not in subst1 or cons_f27(a=subst1["i2.2.0"], b=subst1["i2.2.1.0_1"], c=subst1["i2.2.0_1"], d=subst1["i2.2.1.0_2"]):
                        pass
                        if 'i2' not in subst1 or 'i2.2.1.0_2' not in subst1 or 'i2.2.0_1' not in subst1 or 'i2.2.0' not in subst1 or 'i2.2_1' not in subst1 or 'i2.2.1.0_1' not in subst1 or cons_f28(a=subst1["i2.2.0"], b=subst1["i2.2.1.0_1"], c=subst1["i2.2.0_1"], d=subst1["i2.2.1.0_2"], n=subst1["i2.2_1"], x=subst1["i2"]):
                            pass
                            if 'i2.2.1.0_2' not in subst1 or 'i2' not in subst1 or cons_f29(d=subst1["i2.2.1.0_2"], x=subst1["i2"]):
                                pass
                                # State 2629
                                if len(subjects) == 0:
                                    pass
                                    # 9: v*b /; (cons_f29) and (cons_f27) and (cons_f28)
                                    yield 9, subst1
                        if 'i2.2.1.0_2' not in subst1 or 'i2' not in subst1 or cons_f29(d=subst1["i2.2.1.0_2"], x=subst1["i2"]):
                            pass
                            if 'i2.2.1.0_2' not in subst1 or 'i2.2.1.0_1' not in subst1 or cons_f30(b=subst1["i2.2.1.0_1"], d=subst1["i2.2.1.0_2"]):
                                pass
                                # State 2629
                                if len(subjects) == 0:
                                    pass
                                    # 11: v*b /; (cons_f29) and (cons_f27) and (cons_f30)
                                    yield 11, subst1
                            if 'i2.2_1' not in subst1 or 'i2.2.1.0_2' not in subst1 or 'i2.2.1.0_1' not in subst1 or 'i2.2' not in subst1 or cons_f32(b=subst1["i2.2.1.0_1"], d=subst1["i2.2.1.0_2"], m=subst1["i2.2"], n=subst1["i2.2_1"]):
                                pass
                                # State 2629
                                if len(subjects) == 0:
                                    pass
                                    # 13: v*b /; (cons_f29) and (cons_f27) and (cons_f32)
                                    yield 13, subst1
                if pattern_index == 5:
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
                                                        # State 2793
                                                        if len(subjects) == 0:
                                                            pass
                                                            # 15: a*v**m /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f19) and (cons_f4) and (cons_f39) and (cons_f41) and (cons_f42)
                                                            yield 15, subst1
                if pattern_index == 6:
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
                                                    # State 2812
                                                    if len(subjects) == 0:
                                                        pass
                                                        # 16: b*v**n /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f19) and (cons_f4) and (cons_f39) and (cons_f41)
                                                        yield 16, subst1
                if pattern_index == 7:
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
                                                        # State 2821
                                                        if len(subjects) == 0:
                                                            pass
                                                            # 17: b*v**n /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f19) and (cons_f4) and (cons_f5) and (cons_f7) and (cons_f44)
                                                            yield 17, subst1
                if pattern_index == 8:
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
                                                            # State 2835
                                                            if len(subjects) == 0:
                                                                pass
                                                                # 18: d*x**j /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f19) and (cons_f4) and (cons_f5) and (cons_f7) and (cons_f44) and (cons_f46)
                                                                yield 18, subst1
                if pattern_index == 9:
                    pass
                    if 'i2.2.0' not in subst1 or 'i2.2.1.1' not in subst1 or cons_f2(a=subst1["i2.2.0"], x=subst1["i2.2.1.1"]):
                        pass
                        if 'i2.2.1.0_1' not in subst1 or 'i2.2.1.1' not in subst1 or cons_f3(b=subst1["i2.2.1.0_1"], x=subst1["i2.2.1.1"]):
                            pass
                            if 'i2.2.1.0' not in subst1 or 'i2.2.1.1' not in subst1 or cons_f8(c=subst1["i2.2.1.0"], x=subst1["i2.2.1.1"]):
                                pass
                                if 'i2.2.1.0' not in subst1 or 'i2.2.1.0_1' not in subst1 or 'i2.2.0' not in subst1 or cons_f47(a=subst1["i2.2.0"], b=subst1["i2.2.1.0_1"], c=subst1["i2.2.1.0"]):
                                    pass
                                    # State 2876
                                    if len(subjects) == 0:
                                        pass
                                        # 19: c*x**2 /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f47)
                                        yield 19, subst1
                if pattern_index == 10:
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
                                                # State 2878
                                                if len(subjects) == 0:
                                                    pass
                                                    # 24: b*x /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f50) and (cons_f5) and (cons_f49)
                                                    yield 24, subst1
                        if 'i2.2.1.0_1' not in subst1 or 'i2.2.1.1' not in subst1 or cons_f3(b=subst1["i2.2.1.0_1"], x=subst1["i2.2.1.1"]):
                            pass
                            if 'i2.2.1.0' not in subst1 or 'i2.2.1.1' not in subst1 or cons_f8(c=subst1["i2.2.1.0"], x=subst1["i2.2.1.1"]):
                                pass
                                if 'i2.2.1.0' not in subst1 or 'i2.2.1.0_1' not in subst1 or 'i2.2.0' not in subst1 or cons_f47(a=subst1["i2.2.0"], b=subst1["i2.2.1.0_1"], c=subst1["i2.2.1.0"]):
                                    pass
                                    # State 2878
                                    if len(subjects) == 0:
                                        pass
                                        # 20: b*x /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f47)
                                        yield 20, subst1
                if pattern_index == 11:
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
                                            # State 2908
                                            if len(subjects) == 0:
                                                pass
                                                # 21: b*v**n /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f4) and (cons_f48) and (cons_f47)
                                                yield 21, subst1
                if pattern_index == 12:
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
                                            # State 2909
                                            if len(subjects) == 0:
                                                pass
                                                # 22: d*x**j /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f4) and (cons_f48) and (cons_f47)
                                                yield 22, subst1
                if pattern_index == 13:
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
                                                # State 2918
                                                if len(subjects) == 0:
                                                    pass
                                                    # 23: c*x**2 /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f50) and (cons_f5) and (cons_f49)
                                                    yield 23, subst1
                if pattern_index == 14:
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
                                        # State 2943
                                        if len(subjects) == 0:
                                            pass
                                            # 25: a*v**m /; (cons_f2) and (cons_f3) and (cons_f5) and (cons_f52) and (cons_f51)
                                            yield 25, subst1
                if pattern_index == 15:
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
                                        # State 2944
                                        if len(subjects) == 0:
                                            pass
                                            # 26: b*v**n /; (cons_f2) and (cons_f3) and (cons_f5) and (cons_f52) and (cons_f51)
                                            yield 26, subst1
                if pattern_index == 16:
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
                                                    # State 2999
                                                    if len(subjects) == 0:
                                                        pass
                                                        # 27: a*v**m /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f5) and (cons_f52) and (cons_f54) and (cons_f51) and (cons_f53)
                                                        yield 27, subst1
                if pattern_index == 17:
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
                                                # State 3000
                                                if len(subjects) == 0:
                                                    pass
                                                    # 28: b*v**n /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f5) and (cons_f52) and (cons_f54) and (cons_f51)
                                                    yield 28, subst1
                if pattern_index == 18:
                    pass
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
                                            if 'i2.2.1.2' not in subst1 or 'i2.2.1.2_2' not in subst1 or cons_f53(p=subst1["i2.2.1.2"], r=subst1["i2.2.1.2_2"]):
                                                pass
                                                # State 3011
                                                if len(subjects) == 0:
                                                    pass
                                                    # 29: c*x**r /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f5) and (cons_f52) and (cons_f54) and (cons_f53)
                                                    yield 29, subst1
                if pattern_index == 19:
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
                                        # State 3018
                                        if len(subjects) == 0:
                                            pass
                                            # 30: d*x**j /; (cons_f2) and (cons_f3) and (cons_f19) and (cons_f4) and (cons_f55)
                                            yield 30, subst1
                if pattern_index == 20:
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
                                            # State 3029
                                            if len(subjects) == 0:
                                                pass
                                                # 31: d*x**j /; (cons_f2) and (cons_f3) and (cons_f19) and (cons_f4) and (cons_f5) and (cons_f55)
                                                yield 31, subst1
                if pattern_index == 21:
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
                                                        # State 3039
                                                        if len(subjects) == 0:
                                                            pass
                                                            # 32: a*v**m /; (cons_f59) and (cons_f60) and (cons_f61) and (cons_f62) and (cons_f19) and (cons_f4) and (cons_f5) and (cons_f57) and (cons_f58)
                                                            yield 32, subst1
                if pattern_index == 22:
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
                                                        # State 3047
                                                        if len(subjects) == 0:
                                                            pass
                                                            # 33: b2*v**m /; (cons_f59) and (cons_f60) and (cons_f61) and (cons_f62) and (cons_f19) and (cons_f4) and (cons_f5) and (cons_f57) and (cons_f58)
                                                            yield 33, subst1
                if pattern_index == 23:
                    pass
                    if 'i2' not in subst1 or 'i2.2.1.0' not in subst1 or cons_f3(b=subst1["i2.2.1.0"], x=subst1["i2"]):
                        pass
                        if 'i2.2.1.2' not in subst1 or 'i2' not in subst1 or cons_f4(n=subst1["i2.2.1.2"], x=subst1["i2"]):
                            pass
                            if 'i2' not in subst1 or 'i2.2.1.1' not in subst1 or cons_f11(Pm=subst1["i2.2.1.1"], x=subst1["i2"]):
                                pass
                                if 'i2' not in subst1 or 'i2.2.1.1' not in subst1 or 'i2.2.1.0' not in subst1 or 'i2.2.0' not in subst1 or 'i2.0' not in subst1 or 'i2.2' not in subst1 or 'i2.2.1.2' not in subst1 or With35(Pm=subst1["i2.2.1.1"], Qm=subst1["i2.0"], a=subst1["i2.2.0"], b=subst1["i2.2.1.0"], n=subst1["i2.2.1.2"], p=subst1["i2.2"], x=subst1["i2"]):
                                    pass
                                    # State 3060
                                    if len(subjects) == 0:
                                        pass
                                        # 34: a*v**m /; (cons_f3) and (cons_f4) and (cons_f11) and (With35)
                                        yield 34, subst1
                if pattern_index == 24:
                    pass
                    if 'i2.2.1.2' not in subst1 or 'i2.2.1.2_1' not in subst1 or cons_f48(n=subst1["i2.2.1.2"], n2=subst1["i2.2.1.2_1"]):
                        pass
                        if 'i2' not in subst1 or 'i2.2.1.0' not in subst1 or cons_f3(b=subst1["i2.2.1.0"], x=subst1["i2"]):
                            pass
                            if 'i2.2.1.2' not in subst1 or 'i2' not in subst1 or cons_f4(n=subst1["i2.2.1.2"], x=subst1["i2"]):
                                pass
                                if 'i2' not in subst1 or 'i2.2.1.1' not in subst1 or cons_f11(Pm=subst1["i2.2.1.1"], x=subst1["i2"]):
                                    pass
                                    if 'i2' not in subst1 or 'i2.2.1.1' not in subst1 or 'i2.2.1.0' not in subst1 or 'i2.2.0' not in subst1 or 'i2.0' not in subst1 or 'i2.2.1.2_1' not in subst1 or 'i2.2.1.2' not in subst1 or 'i2.2' not in subst1 or 'i2.2.1.0_1' not in subst1 or With36(Pm=subst1["i2.2.1.1"], Qm=subst1["i2.0"], a=subst1["i2.2.0"], b=subst1["i2.2.1.0"], c=subst1["i2.2.1.0_1"], n=subst1["i2.2.1.2"], n2=subst1["i2.2.1.2_1"], p=subst1["i2.2"], x=subst1["i2"]):
                                        pass
                                        # State 3070
                                        if len(subjects) == 0:
                                            pass
                                            # 35: a*v**m /; (cons_f3) and (cons_f4) and (cons_f48) and (cons_f11) and (With36)
                                            yield 35, subst1
                if pattern_index == 25:
                    pass
                    if 'i2.2.1.2' not in subst1 or 'i2.2.1.2_1' not in subst1 or cons_f48(n=subst1["i2.2.1.2"], n2=subst1["i2.2.1.2_1"]):
                        pass
                        if 'i2' not in subst1 or 'i2.2.1.1' not in subst1 or cons_f11(Pm=subst1["i2.2.1.1"], x=subst1["i2"]):
                            pass
                            if 'i2' not in subst1 or 'i2.2.1.1' not in subst1 or 'i2.2.1.0' not in subst1 or 'i2.2.0' not in subst1 or 'i2.0' not in subst1 or 'i2.2.1.2_1' not in subst1 or 'i2.2.1.2' not in subst1 or 'i2.2' not in subst1 or 'i2.2.1.0_1' not in subst1 or With36(Pm=subst1["i2.2.1.1"], Qm=subst1["i2.0"], a=subst1["i2.2.0"], b=subst1["i2.2.1.0"], c=subst1["i2.2.1.0_1"], n=subst1["i2.2.1.2"], n2=subst1["i2.2.1.2_1"], p=subst1["i2.2"], x=subst1["i2"]):
                                pass
                                if 'i2' not in subst1 or 'i2.2.1.0_1' not in subst1 or cons_f8(c=subst1["i2.2.1.0_1"], x=subst1["i2"]):
                                    pass
                                    # State 3071
                                    if len(subjects) == 0:
                                        pass
                                        # 36: b*v**n /; (cons_f8) and (cons_f48) and (cons_f11) and (With36)
                                        yield 36, subst1
            subjects.appendleft(tmp169)
        return
        yield


from matchpy.matching.many_to_one import CommutativeMatcher
from .generated_part000015 import *
from matchpy.utils import VariableWithCount
from multiset import Multiset
from collections import deque