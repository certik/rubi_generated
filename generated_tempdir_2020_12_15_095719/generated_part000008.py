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


class CommutativeMatcher2354(CommutativeMatcher):
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
      (VariableWithCount('i2.2.0', 1, 1, None), Add)
]),
    8: (8, Multiset({10: 1}), [
      (VariableWithCount('i2.2.0', 1, 1, None), Add)
]),
    9: (9, Multiset({11: 1, 12: 1}), [
      (VariableWithCount('i2.2.0', 1, 1, None), Add)
]),
    10: (10, Multiset({13: 1, 14: 1}), [
      (VariableWithCount('i2.2.0', 1, 1, None), Add)
]),
    11: (11, Multiset({15: 1, 16: 1}), [
      (VariableWithCount('i2.2.0', 1, 1, S(0)), Add)
]),
    12: (12, Multiset({17: 1, 18: 1}), [
      
]),
    13: (13, Multiset({19: 1, 20: 1, 21: 1}), [
      
]),
    14: (14, Multiset({22: 1}), [
      (VariableWithCount('i2.2.0', 1, 1, S(0)), Add)
]),
    15: (15, Multiset({23: 1, 24: 1}), [
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
        if CommutativeMatcher2354._instance is None:
            CommutativeMatcher2354._instance = CommutativeMatcher2354()
        return CommutativeMatcher2354._instance

    @staticmethod
    def get_match_iter(subject):
        subjects = deque([subject]) if subject is not None else deque()
        subst0 = Substitution()
        # State 2353
        subst1 = Substitution(subst0)
        try:
            subst1.try_add_variable('i2.2.1.0', S(1))
        except ValueError:
            pass
        else:
            pass
            # State 2355
            subst2 = Substitution(subst1)
            try:
                subst2.try_add_variable('i2.2.1.2', S(1))
            except ValueError:
                pass
            else:
                pass
                # State 2356
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
                                        # State 2357
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
                                                # State 2357
                                                if len(subjects) == 0:
                                                    pass
                                                    # 9: a*v**m /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f19) and (cons_f4) and (cons_f39) and (cons_f41) and (cons_f42)
                                                    yield 9, subst3
                            if 'i2.2' not in subst3 or 'i2.2.1.1' not in subst3 or cons_f5(p=subst3["i2.2"], x=subst3["i2.2.1.1"]):
                                pass
                                if 'i2.2.1.0_1' not in subst3 or 'i2.2.1.1' not in subst3 or cons_f3(b=subst3["i2.2.1.0_1"], x=subst3["i2.2.1.1"]):
                                    pass
                                    if 'i2.2.1.0' not in subst3 or 'i2.2.1.1' not in subst3 or cons_f8(c=subst3["i2.2.1.0"], x=subst3["i2.2.1.1"]):
                                        pass
                                        if 'i2.2.1.2_1' not in subst3 or 'i2.2.1.1' not in subst3 or cons_f4(n=subst3["i2.2.1.2_1"], x=subst3["i2.2.1.1"]):
                                            pass
                                            # State 2357
                                            if len(subjects) == 0:
                                                pass
                                                # 2: a*v**m /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f4) and (cons_f5) and (cons_f7)
                                                yield 2, subst3
                                                # 5: a*v**m /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f4) and (cons_f5) and (cons_f7) and (cons_f9)
                                                yield 5, subst3
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
                                                # State 2357
                                                if len(subjects) == 0:
                                                    pass
                                                    # 19: a*v**m /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f5) and (cons_f52) and (cons_f54) and (cons_f51) and (cons_f53)
                                                    yield 19, subst3
                                        # State 2357
                                        if len(subjects) == 0:
                                            pass
                                            # 17: a*v**m /; (cons_f2) and (cons_f3) and (cons_f5) and (cons_f52) and (cons_f51)
                                            yield 17, subst3
                        if 'i2' not in subst3 or 'i2.2.1.1' not in subst3 or cons_f11(Pm=subst3["i2.2.1.1"], x=subst3["i2"]):
                            pass
                            if 'i2' not in subst3 or 'i2.2.1.1' not in subst3 or 'i2.2.1.0' not in subst3 or 'i2.2.0' not in subst3 or 'i2.0' not in subst3 or 'i2.2' not in subst3 or 'i2.2.1.2' not in subst3 or With35(Pm=subst3["i2.2.1.1"], Qm=subst3["i2.0"], a=subst3["i2.2.0"], b=subst3["i2.2.1.0"], n=subst3["i2.2.1.2"], p=subst3["i2.2"], x=subst3["i2"]):
                                pass
                                # State 2357
                                if len(subjects) == 0:
                                    pass
                                    # 22: a*v**m /; (cons_f3) and (cons_f4) and (cons_f11) and (With35)
                                    yield 22, subst3
                            if 'i2' not in subst3 or 'i2.2.1.1' not in subst3 or 'i2.2.1.0' not in subst3 or 'i2.2.0' not in subst3 or 'i2.0' not in subst3 or 'i2.2.1.2_1' not in subst3 or 'i2.2.1.2' not in subst3 or 'i2.2' not in subst3 or 'i2.2.1.0_1' not in subst3 or With36(Pm=subst3["i2.2.1.1"], Qm=subst3["i2.0"], a=subst3["i2.2.0"], b=subst3["i2.2.1.0"], c=subst3["i2.2.1.0_1"], n=subst3["i2.2.1.2"], n2=subst3["i2.2.1.2_1"], p=subst3["i2.2"], x=subst3["i2"]):
                                pass
                                # State 2357
                                if len(subjects) == 0:
                                    pass
                                    # 23: a*v**m /; (cons_f3) and (cons_f4) and (cons_f48) and (cons_f11) and (With36)
                                    yield 23, subst3
                    subjects.appendleft(tmp3)
            if len(subjects) >= 1 and isinstance(subjects[0], Pow):
                tmp5 = subjects.popleft()
                subjects6 = deque(tmp5._args)
                # State 2358
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
                                        # State 2359
                                        subst3 = Substitution(subst2)
                                        try:
                                            subst3.try_add_variable('i2.2.1.2', 1)
                                        except ValueError:
                                            pass
                                        else:
                                            pass
                                            if 'i2.2.1.2' not in subst3 or 'i2.2.1.1' not in subst3 or cons_f4(n=subst3["i2.2.1.2"], x=subst3["i2.2.1.1"]):
                                                pass
                                                # State 2360
                                                if len(subjects6) == 0:
                                                    pass
                                                    # State 2361
                                                    if len(subjects) == 0:
                                                        pass
                                                        # 0: a*v**m /; (cons_f2) and (cons_f3) and (cons_f4) and (cons_f5)
                                                        yield 0, subst3
                                                        # 1: a*v**m /; (cons_f2) and (cons_f3) and (cons_f4) and (cons_f5) and (cons_f6)
                                                        yield 1, subst3
                                        if len(subjects6) >= 1:
                                            tmp10 = subjects6.popleft()
                                            subst3 = Substitution(subst2)
                                            try:
                                                subst3.try_add_variable('i2.2.1.2', tmp10)
                                            except ValueError:
                                                pass
                                            else:
                                                pass
                                                if 'i2.2.1.2' not in subst3 or 'i2.2.1.1' not in subst3 or cons_f4(n=subst3["i2.2.1.2"], x=subst3["i2.2.1.1"]):
                                                    pass
                                                    # State 2360
                                                    if len(subjects6) == 0:
                                                        pass
                                                        # State 2361
                                                        if len(subjects) == 0:
                                                            pass
                                                            # 0: a*v**m /; (cons_f2) and (cons_f3) and (cons_f4) and (cons_f5)
                                                            yield 0, subst3
                                                            # 1: a*v**m /; (cons_f2) and (cons_f3) and (cons_f4) and (cons_f5) and (cons_f6)
                                                            yield 1, subst3
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
                                            subjects6.appendleft(tmp12)
                                        if len(subjects6) >= 1 and subjects6[0] == Integer(2):
                                            tmp14 = subjects6.popleft()
                                            # State 2864
                                            if len(subjects6) == 0:
                                                pass
                                                # State 2865
                                                if len(subjects) == 0:
                                                    pass
                                            subjects6.appendleft(tmp14)
                                    if 'i2.2.0_1' not in subst2 or 'i2.2.1.1' not in subst2 or cons_f8(c=subst2["i2.2.0_1"], x=subst2["i2.2.1.1"]):
                                        pass
                                        if 'i2.2.1.0_1' not in subst2 or 'i2.2.1.1' not in subst2 or cons_f29(d=subst2["i2.2.1.0_1"], x=subst2["i2.2.1.1"]):
                                            pass
                                            if 'i2.2' not in subst2 or 'i2.2.1.1' not in subst2 or cons_f19(m=subst2["i2.2"], x=subst2["i2.2.1.1"]):
                                                pass
                                                # State 2359
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
                                                                # State 2360
                                                                if len(subjects6) == 0:
                                                                    pass
                                                                    # State 2361
                                                                    if len(subjects) == 0:
                                                                        pass
                                                                        # 9: a*v**m /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f19) and (cons_f4) and (cons_f39) and (cons_f41) and (cons_f42)
                                                                        yield 9, subst3
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
                                                            if 'i2.2.1.2' not in subst3 or 'i2.2.1.2_1' not in subst3 or cons_f39(n=subst3["i2.2.1.2"], q=subst3["i2.2.1.2_1"]):
                                                                pass
                                                                if 'i2.2.1.2' not in subst3 or 'i2.2' not in subst3 or cons_f42(m=subst3["i2.2"], n=subst3["i2.2.1.2"]):
                                                                    pass
                                                                    # State 2360
                                                                    if len(subjects6) == 0:
                                                                        pass
                                                                        # State 2361
                                                                        if len(subjects) == 0:
                                                                            pass
                                                                            # 9: a*v**m /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f19) and (cons_f4) and (cons_f39) and (cons_f41) and (cons_f42)
                                                                            yield 9, subst3
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
                                                    # State 2864
                                                    if len(subjects6) == 0:
                                                        pass
                                                        # State 2865
                                                        if len(subjects) == 0:
                                                            pass
                                                    subjects6.appendleft(tmp20)
                                    if 'i2.2.1.0_1' not in subst2 or 'i2.2.1.1' not in subst2 or cons_f8(c=subst2["i2.2.1.0_1"], x=subst2["i2.2.1.1"]):
                                        pass
                                        # State 2359
                                        subst3 = Substitution(subst2)
                                        try:
                                            subst3.try_add_variable('i2.2.1.2', 1)
                                        except ValueError:
                                            pass
                                        else:
                                            pass
                                        if len(subjects6) >= 1:
                                            tmp22 = subjects6.popleft()
                                            subst3 = Substitution(subst2)
                                            try:
                                                subst3.try_add_variable('i2.2.1.2', tmp22)
                                            except ValueError:
                                                pass
                                            else:
                                                pass
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
                                                if 'i2.2.1.2' not in subst3 or 'i2.2.1.1' not in subst3 or cons_f4(n=subst3["i2.2.1.2"], x=subst3["i2.2.1.1"]):
                                                    pass
                                                    if 'i2.2.1.2' not in subst3 or 'i2.2.1.2_1' not in subst3 or cons_f48(n=subst3["i2.2.1.2"], n2=subst3["i2.2.1.2_1"]):
                                                        pass
                                                        # State 2825
                                                        if len(subjects6) == 0:
                                                            pass
                                                            # State 2826
                                                            if len(subjects) == 0:
                                                                pass
                                                                # 14: d*x**j /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f4) and (cons_f48) and (cons_f47)
                                                                yield 14, subst3
                                            subjects6.appendleft(tmp24)
                                        if len(subjects6) >= 1 and subjects6[0] == Integer(2):
                                            tmp26 = subjects6.popleft()
                                            # State 2864
                                            if len(subjects6) == 0:
                                                pass
                                                # State 2865
                                                if len(subjects) == 0:
                                                    pass
                                            subjects6.appendleft(tmp26)
                            if 'i2.2' not in subst2 or 'i2.2.1.1' not in subst2 or cons_f5(p=subst2["i2.2"], x=subst2["i2.2.1.1"]):
                                pass
                                if 'i2.2.1.0_1' not in subst2 or 'i2.2.1.1' not in subst2 or cons_f3(b=subst2["i2.2.1.0_1"], x=subst2["i2.2.1.1"]):
                                    pass
                                    if 'i2.2.1.0' not in subst2 or 'i2.2.1.1' not in subst2 or cons_f8(c=subst2["i2.2.1.0"], x=subst2["i2.2.1.1"]):
                                        pass
                                        if 'i2.2.1.2_1' not in subst2 or 'i2.2.1.1' not in subst2 or cons_f4(n=subst2["i2.2.1.2_1"], x=subst2["i2.2.1.1"]):
                                            pass
                                            # State 2359
                                            subst3 = Substitution(subst2)
                                            try:
                                                subst3.try_add_variable('i2.2.1.2', 1)
                                            except ValueError:
                                                pass
                                            else:
                                                pass
                                                if 'i2.2.1.2' not in subst3 or 'i2.2.1.2_1' not in subst3 or cons_f7(j=subst3["i2.2.1.2"], n=subst3["i2.2.1.2_1"]):
                                                    pass
                                                    # State 2360
                                                    if len(subjects6) == 0:
                                                        pass
                                                        # State 2361
                                                        if len(subjects) == 0:
                                                            pass
                                                            # 2: a*v**m /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f4) and (cons_f5) and (cons_f7)
                                                            yield 2, subst3
                                                            # 5: a*v**m /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f4) and (cons_f5) and (cons_f7) and (cons_f9)
                                                            yield 5, subst3
                                            if len(subjects6) >= 1:
                                                tmp28 = subjects6.popleft()
                                                subst3 = Substitution(subst2)
                                                try:
                                                    subst3.try_add_variable('i2.2.1.2', tmp28)
                                                except ValueError:
                                                    pass
                                                else:
                                                    pass
                                                    if 'i2.2.1.2' not in subst3 or 'i2.2.1.2_1' not in subst3 or cons_f7(j=subst3["i2.2.1.2"], n=subst3["i2.2.1.2_1"]):
                                                        pass
                                                        # State 2360
                                                        if len(subjects6) == 0:
                                                            pass
                                                            # State 2361
                                                            if len(subjects) == 0:
                                                                pass
                                                                # 2: a*v**m /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f4) and (cons_f5) and (cons_f7)
                                                                yield 2, subst3
                                                                # 5: a*v**m /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f4) and (cons_f5) and (cons_f7) and (cons_f9)
                                                                yield 5, subst3
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
                                                subjects6.appendleft(tmp30)
                                            if len(subjects6) >= 1 and subjects6[0] == Integer(2):
                                                tmp32 = subjects6.popleft()
                                                # State 2864
                                                if len(subjects6) == 0:
                                                    pass
                                                    # State 2865
                                                    if len(subjects) == 0:
                                                        pass
                                                subjects6.appendleft(tmp32)
                                        if 'i2.1.0' not in subst2 or 'i2.2.1.1' not in subst2 or cons_f29(d=subst2["i2.1.0"], x=subst2["i2.2.1.1"]):
                                            pass
                                            if 'i2.1.1.0' not in subst2 or 'i2.2.1.1' not in subst2 or cons_f50(e=subst2["i2.1.1.0"], x=subst2["i2.2.1.1"]):
                                                pass
                                                # State 2359
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
                                                    subjects6.appendleft(tmp36)
                                                if len(subjects6) >= 1 and subjects6[0] == Integer(2):
                                                    tmp38 = subjects6.popleft()
                                                    # State 2864
                                                    if len(subjects6) == 0:
                                                        pass
                                                        # State 2865
                                                        if len(subjects) == 0:
                                                            pass
                                                            # 15: c*x**2 /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f50) and (cons_f5) and (cons_f49)
                                                            yield 15, subst2
                                                    subjects6.appendleft(tmp38)
                            if 'i2.2.1.0_1' not in subst2 or 'i2.2.1.1' not in subst2 or cons_f3(b=subst2["i2.2.1.0_1"], x=subst2["i2.2.1.1"]):
                                pass
                                if 'i2.2.1.0' not in subst2 or 'i2.2.1.1' not in subst2 or cons_f8(c=subst2["i2.2.1.0"], x=subst2["i2.2.1.1"]):
                                    pass
                                    # State 2359
                                    subst3 = Substitution(subst2)
                                    try:
                                        subst3.try_add_variable('i2.2.1.2', 1)
                                    except ValueError:
                                        pass
                                    else:
                                        pass
                                    if len(subjects6) >= 1:
                                        tmp40 = subjects6.popleft()
                                        subst3 = Substitution(subst2)
                                        try:
                                            subst3.try_add_variable('i2.2.1.2', tmp40)
                                        except ValueError:
                                            pass
                                        else:
                                            pass
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
                                        # State 2864
                                        if len(subjects6) == 0:
                                            pass
                                            # State 2865
                                            if len(subjects) == 0:
                                                pass
                                                # 11: c*x**2 /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f47)
                                                yield 11, subst2
                                        subjects6.appendleft(tmp44)
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
                                                    # State 2359
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
                                                            if 'i2.2.1.2' not in subst3 or 'i2.2.1.2_1' not in subst3 or cons_f7(j=subst3["i2.2.1.2"], n=subst3["i2.2.1.2_1"]):
                                                                pass
                                                                # State 2825
                                                                if len(subjects6) == 0:
                                                                    pass
                                                                    # State 2826
                                                                    if len(subjects) == 0:
                                                                        pass
                                                                        # 10: d*x**j /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f19) and (cons_f4) and (cons_f5) and (cons_f7) and (cons_f44) and (cons_f46)
                                                                        yield 10, subst3
                                                        subjects6.appendleft(tmp48)
                                                    if len(subjects6) >= 1 and subjects6[0] == Integer(2):
                                                        tmp50 = subjects6.popleft()
                                                        # State 2864
                                                        if len(subjects6) == 0:
                                                            pass
                                                            # State 2865
                                                            if len(subjects) == 0:
                                                                pass
                                                        subjects6.appendleft(tmp50)
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
                                                # State 2359
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
                                                                # State 2360
                                                                if len(subjects6) == 0:
                                                                    pass
                                                                    # State 2361
                                                                    if len(subjects) == 0:
                                                                        pass
                                                                        # 19: a*v**m /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f5) and (cons_f52) and (cons_f54) and (cons_f51) and (cons_f53)
                                                                        yield 19, subst3
                                                if len(subjects6) >= 1:
                                                    tmp52 = subjects6.popleft()
                                                    subst3 = Substitution(subst2)
                                                    try:
                                                        subst3.try_add_variable('i2.2.1.2', tmp52)
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
                                                                    # State 2360
                                                                    if len(subjects6) == 0:
                                                                        pass
                                                                        # State 2361
                                                                        if len(subjects) == 0:
                                                                            pass
                                                                            # 19: a*v**m /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f5) and (cons_f52) and (cons_f54) and (cons_f51) and (cons_f53)
                                                                            yield 19, subst3
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
                                                    # State 2864
                                                    if len(subjects6) == 0:
                                                        pass
                                                        # State 2865
                                                        if len(subjects) == 0:
                                                            pass
                                                    subjects6.appendleft(tmp56)
                                        # State 2359
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
                                                    # State 2360
                                                    if len(subjects6) == 0:
                                                        pass
                                                        # State 2361
                                                        if len(subjects) == 0:
                                                            pass
                                                            # 17: a*v**m /; (cons_f2) and (cons_f3) and (cons_f5) and (cons_f52) and (cons_f51)
                                                            yield 17, subst3
                                        if len(subjects6) >= 1:
                                            tmp58 = subjects6.popleft()
                                            subst3 = Substitution(subst2)
                                            try:
                                                subst3.try_add_variable('i2.2.1.2', tmp58)
                                            except ValueError:
                                                pass
                                            else:
                                                pass
                                                if 'i2.2.1.2' not in subst3 or 'i2.2.1.1' not in subst3 or cons_f5(p=subst3["i2.2.1.2"], x=subst3["i2.2.1.1"]):
                                                    pass
                                                    if 'i2.2.1.2' not in subst3 or 'i2.2.1.2_1' not in subst3 or cons_f51(p=subst3["i2.2.1.2"], q=subst3["i2.2.1.2_1"]):
                                                        pass
                                                        # State 2360
                                                        if len(subjects6) == 0:
                                                            pass
                                                            # State 2361
                                                            if len(subjects) == 0:
                                                                pass
                                                                # 17: a*v**m /; (cons_f2) and (cons_f3) and (cons_f5) and (cons_f52) and (cons_f51)
                                                                yield 17, subst3
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
                                            # State 2864
                                            if len(subjects6) == 0:
                                                pass
                                                # State 2865
                                                if len(subjects) == 0:
                                                    pass
                                            subjects6.appendleft(tmp62)
                        if 'i2' not in subst2 or 'i2.2.1.1' not in subst2 or cons_f11(Pm=subst2["i2.2.1.1"], x=subst2["i2"]):
                            pass
                            if 'i2' not in subst2 or 'i2.2.1.1' not in subst2 or 'i2.2.1.0' not in subst2 or 'i2.2.0' not in subst2 or 'i2.0' not in subst2 or 'i2.2' not in subst2 or 'i2.2.1.2' not in subst2 or With35(Pm=subst2["i2.2.1.1"], Qm=subst2["i2.0"], a=subst2["i2.2.0"], b=subst2["i2.2.1.0"], n=subst2["i2.2.1.2"], p=subst2["i2.2"], x=subst2["i2"]):
                                pass
                                # State 2359
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
                                            # State 2360
                                            if len(subjects6) == 0:
                                                pass
                                                # State 2361
                                                if len(subjects) == 0:
                                                    pass
                                                    # 22: a*v**m /; (cons_f3) and (cons_f4) and (cons_f11) and (With35)
                                                    yield 22, subst3
                                if len(subjects6) >= 1:
                                    tmp64 = subjects6.popleft()
                                    subst3 = Substitution(subst2)
                                    try:
                                        subst3.try_add_variable('i2.2.1.2', tmp64)
                                    except ValueError:
                                        pass
                                    else:
                                        pass
                                        if 'i2.2.1.2' not in subst3 or 'i2' not in subst3 or cons_f4(n=subst3["i2.2.1.2"], x=subst3["i2"]):
                                            pass
                                            if 'i2' not in subst3 or 'i2.2.1.1' not in subst3 or 'i2.2.1.0' not in subst3 or 'i2.2.0' not in subst3 or 'i2.0' not in subst3 or 'i2.2' not in subst3 or 'i2.2.1.2' not in subst3 or With35(Pm=subst3["i2.2.1.1"], Qm=subst3["i2.0"], a=subst3["i2.2.0"], b=subst3["i2.2.1.0"], n=subst3["i2.2.1.2"], p=subst3["i2.2"], x=subst3["i2"]):
                                                pass
                                                # State 2360
                                                if len(subjects6) == 0:
                                                    pass
                                                    # State 2361
                                                    if len(subjects) == 0:
                                                        pass
                                                        # 22: a*v**m /; (cons_f3) and (cons_f4) and (cons_f11) and (With35)
                                                        yield 22, subst3
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
                                    subjects6.appendleft(tmp66)
                                if len(subjects6) >= 1 and subjects6[0] == Integer(2):
                                    tmp68 = subjects6.popleft()
                                    # State 2864
                                    if len(subjects6) == 0:
                                        pass
                                        # State 2865
                                        if len(subjects) == 0:
                                            pass
                                    subjects6.appendleft(tmp68)
                            if 'i2' not in subst2 or 'i2.2.1.1' not in subst2 or 'i2.2.1.0' not in subst2 or 'i2.2.0' not in subst2 or 'i2.0' not in subst2 or 'i2.2.1.2_1' not in subst2 or 'i2.2.1.2' not in subst2 or 'i2.2' not in subst2 or 'i2.2.1.0_1' not in subst2 or With36(Pm=subst2["i2.2.1.1"], Qm=subst2["i2.0"], a=subst2["i2.2.0"], b=subst2["i2.2.1.0"], c=subst2["i2.2.1.0_1"], n=subst2["i2.2.1.2"], n2=subst2["i2.2.1.2_1"], p=subst2["i2.2"], x=subst2["i2"]):
                                pass
                                # State 2359
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
                                                # State 2360
                                                if len(subjects6) == 0:
                                                    pass
                                                    # State 2361
                                                    if len(subjects) == 0:
                                                        pass
                                                        # 23: a*v**m /; (cons_f3) and (cons_f4) and (cons_f48) and (cons_f11) and (With36)
                                                        yield 23, subst3
                                if len(subjects6) >= 1:
                                    tmp70 = subjects6.popleft()
                                    subst3 = Substitution(subst2)
                                    try:
                                        subst3.try_add_variable('i2.2.1.2', tmp70)
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
                                                    # State 2360
                                                    if len(subjects6) == 0:
                                                        pass
                                                        # State 2361
                                                        if len(subjects) == 0:
                                                            pass
                                                            # 23: a*v**m /; (cons_f3) and (cons_f4) and (cons_f48) and (cons_f11) and (With36)
                                                            yield 23, subst3
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
                                    # State 2864
                                    if len(subjects6) == 0:
                                        pass
                                        # State 2865
                                        if len(subjects) == 0:
                                            pass
                                    subjects6.appendleft(tmp74)
                    subjects6.appendleft(tmp7)
                subjects.appendleft(tmp5)
        subst1 = Substitution(subst0)
        try:
            subst1.try_add_variable('i2.2.1.0_1', S(1))
        except ValueError:
            pass
        else:
            pass
            # State 2539
            subst2 = Substitution(subst1)
            try:
                subst2.try_add_variable('i2.2.1.2_1', S(1))
            except ValueError:
                pass
            else:
                pass
                # State 2540
                if len(subjects) >= 1:
                    tmp77 = subjects.popleft()
                    subst3 = Substitution(subst2)
                    try:
                        subst3.try_add_variable('i2.2.1.1', tmp77)
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
                                    if 'i2.2.1.0_1' not in subst3 or 'i2.2.1.1' not in subst3 or cons_f8(c=subst3["i2.2.1.0_1"], x=subst3["i2.2.1.1"]):
                                        pass
                                        # State 2541
                                        if len(subjects) == 0:
                                            pass
                                            # 13: b*v**n /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f4) and (cons_f48) and (cons_f47)
                                            yield 13, subst3
                            if 'i2.2' not in subst3 or 'i2.2.1.1' not in subst3 or cons_f5(p=subst3["i2.2"], x=subst3["i2.2.1.1"]):
                                pass
                                if 'i2.2.1.0_1' not in subst3 or 'i2.2.1.1' not in subst3 or cons_f3(b=subst3["i2.2.1.0_1"], x=subst3["i2.2.1.1"]):
                                    pass
                                    if 'i2.2.1.0' not in subst3 or 'i2.2.1.1' not in subst3 or cons_f8(c=subst3["i2.2.1.0"], x=subst3["i2.2.1.1"]):
                                        pass
                                        if 'i2.2.1.2_1' not in subst3 or 'i2.2.1.1' not in subst3 or cons_f4(n=subst3["i2.2.1.2_1"], x=subst3["i2.2.1.1"]):
                                            pass
                                            # State 2541
                                            if len(subjects) == 0:
                                                pass
                                                # 3: b*v**n /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f4) and (cons_f5) and (cons_f7)
                                                yield 3, subst3
                                                # 4: b*v**n /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f4) and (cons_f5) and (cons_f7) and (cons_f6)
                                                yield 4, subst3
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
                                                # State 2541
                                                if len(subjects) == 0:
                                                    pass
                                                    # 20: b*v**n /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f5) and (cons_f52) and (cons_f54) and (cons_f51)
                                                    yield 20, subst3
                                        # State 2541
                                        if len(subjects) == 0:
                                            pass
                                            # 18: b*v**n /; (cons_f2) and (cons_f3) and (cons_f5) and (cons_f52) and (cons_f51)
                                            yield 18, subst3
                        if 'i2' not in subst3 or 'i2.2.1.1' not in subst3 or cons_f11(Pm=subst3["i2.2.1.1"], x=subst3["i2"]):
                            pass
                            if 'i2' not in subst3 or 'i2.2.1.1' not in subst3 or 'i2.2.1.0' not in subst3 or 'i2.2.0' not in subst3 or 'i2.0' not in subst3 or 'i2.2.1.2_1' not in subst3 or 'i2.2.1.2' not in subst3 or 'i2.2' not in subst3 or 'i2.2.1.0_1' not in subst3 or With36(Pm=subst3["i2.2.1.1"], Qm=subst3["i2.0"], a=subst3["i2.2.0"], b=subst3["i2.2.1.0"], c=subst3["i2.2.1.0_1"], n=subst3["i2.2.1.2"], n2=subst3["i2.2.1.2_1"], p=subst3["i2.2"], x=subst3["i2"]):
                                pass
                                # State 2541
                                if len(subjects) == 0:
                                    pass
                                    # 24: b*v**n /; (cons_f8) and (cons_f48) and (cons_f11) and (With36)
                                    yield 24, subst3
                    subjects.appendleft(tmp77)
            if len(subjects) >= 1:
                tmp79 = subjects.popleft()
                subst2 = Substitution(subst1)
                try:
                    subst2.try_add_variable('i2.2.1.0', tmp79)
                except ValueError:
                    pass
                else:
                    pass
                    if 'i2' not in subst2 or 'i2.2.1.0' not in subst2 or cons_f10(v=subst2["i2.2.1.0"], x=subst2["i2"]):
                        pass
                        # State 2619
                        if len(subjects) == 0:
                            pass
                            # 6: v*a /; (cons_f2) and (cons_f10)
                            yield 6, subst2
                    # State 2619
                    if len(subjects) == 0:
                        pass
                        # 8: v*a /; (cons_f3) and (cons_f27) and (cons_f28)
                        yield 8, subst2
                subjects.appendleft(tmp79)
            if len(subjects) >= 1:
                tmp81 = subjects.popleft()
                subst2 = Substitution(subst1)
                try:
                    subst2.try_add_variable('i2.2.1.1', tmp81)
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
                                            # State 2869
                                            if len(subjects) == 0:
                                                pass
                                                # 16: b*x /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f50) and (cons_f5) and (cons_f49)
                                                yield 16, subst2
                        if 'i2.2.1.0_1' not in subst2 or 'i2.2.1.1' not in subst2 or cons_f3(b=subst2["i2.2.1.0_1"], x=subst2["i2.2.1.1"]):
                            pass
                            if 'i2.2.1.0' not in subst2 or 'i2.2.1.1' not in subst2 or cons_f8(c=subst2["i2.2.1.0"], x=subst2["i2.2.1.1"]):
                                pass
                                # State 2869
                                if len(subjects) == 0:
                                    pass
                                    # 12: b*x /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f47)
                                    yield 12, subst2
                subjects.appendleft(tmp81)
            if len(subjects) >= 1 and isinstance(subjects[0], Pow):
                tmp83 = subjects.popleft()
                subjects84 = deque(tmp83._args)
                # State 2542
                if len(subjects84) >= 1:
                    tmp85 = subjects84.popleft()
                    subst2 = Substitution(subst1)
                    try:
                        subst2.try_add_variable('i2.2.1.1', tmp85)
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
                                    if 'i2.2.1.0_1' not in subst2 or 'i2.2.1.1' not in subst2 or cons_f8(c=subst2["i2.2.1.0_1"], x=subst2["i2.2.1.1"]):
                                        pass
                                        # State 2543
                                        subst3 = Substitution(subst2)
                                        try:
                                            subst3.try_add_variable('i2.2.1.2_1', 1)
                                        except ValueError:
                                            pass
                                        else:
                                            pass
                                            if 'i2.2.1.2' not in subst3 or 'i2.2.1.2_1' not in subst3 or cons_f48(n=subst3["i2.2.1.2"], n2=subst3["i2.2.1.2_1"]):
                                                pass
                                                # State 2544
                                                if len(subjects84) == 0:
                                                    pass
                                                    # State 2545
                                                    if len(subjects) == 0:
                                                        pass
                                                        # 13: b*v**n /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f4) and (cons_f48) and (cons_f47)
                                                        yield 13, subst3
                                        if len(subjects84) >= 1:
                                            tmp88 = subjects84.popleft()
                                            subst3 = Substitution(subst2)
                                            try:
                                                subst3.try_add_variable('i2.2.1.2_1', tmp88)
                                            except ValueError:
                                                pass
                                            else:
                                                pass
                                                if 'i2.2.1.2' not in subst3 or 'i2.2.1.2_1' not in subst3 or cons_f48(n=subst3["i2.2.1.2"], n2=subst3["i2.2.1.2_1"]):
                                                    pass
                                                    # State 2544
                                                    if len(subjects84) == 0:
                                                        pass
                                                        # State 2545
                                                        if len(subjects) == 0:
                                                            pass
                                                            # 13: b*v**n /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f4) and (cons_f48) and (cons_f47)
                                                            yield 13, subst3
                                            subjects84.appendleft(tmp88)
                            if 'i2.2' not in subst2 or 'i2.2.1.1' not in subst2 or cons_f5(p=subst2["i2.2"], x=subst2["i2.2.1.1"]):
                                pass
                                if 'i2.2.1.0_1' not in subst2 or 'i2.2.1.1' not in subst2 or cons_f3(b=subst2["i2.2.1.0_1"], x=subst2["i2.2.1.1"]):
                                    pass
                                    if 'i2.2.1.0' not in subst2 or 'i2.2.1.1' not in subst2 or cons_f8(c=subst2["i2.2.1.0"], x=subst2["i2.2.1.1"]):
                                        pass
                                        if 'i2.2.1.2_1' not in subst2 or 'i2.2.1.1' not in subst2 or cons_f4(n=subst2["i2.2.1.2_1"], x=subst2["i2.2.1.1"]):
                                            pass
                                            # State 2543
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
                                                        # State 2544
                                                        if len(subjects84) == 0:
                                                            pass
                                                            # State 2545
                                                            if len(subjects) == 0:
                                                                pass
                                                                # 3: b*v**n /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f4) and (cons_f5) and (cons_f7)
                                                                yield 3, subst3
                                                                # 4: b*v**n /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f4) and (cons_f5) and (cons_f7) and (cons_f6)
                                                                yield 4, subst3
                                            if len(subjects84) >= 1:
                                                tmp91 = subjects84.popleft()
                                                subst3 = Substitution(subst2)
                                                try:
                                                    subst3.try_add_variable('i2.2.1.2_1', tmp91)
                                                except ValueError:
                                                    pass
                                                else:
                                                    pass
                                                    if 'i2.2.1.2_1' not in subst3 or 'i2.2.1.1' not in subst3 or cons_f4(n=subst3["i2.2.1.2_1"], x=subst3["i2.2.1.1"]):
                                                        pass
                                                        if 'i2.2.1.2' not in subst3 or 'i2.2.1.2_1' not in subst3 or cons_f7(j=subst3["i2.2.1.2"], n=subst3["i2.2.1.2_1"]):
                                                            pass
                                                            # State 2544
                                                            if len(subjects84) == 0:
                                                                pass
                                                                # State 2545
                                                                if len(subjects) == 0:
                                                                    pass
                                                                    # 3: b*v**n /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f4) and (cons_f5) and (cons_f7)
                                                                    yield 3, subst3
                                                                    # 4: b*v**n /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f4) and (cons_f5) and (cons_f7) and (cons_f6)
                                                                    yield 4, subst3
                                                subjects84.appendleft(tmp91)
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
                                                # State 2543
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
                                                            # State 2544
                                                            if len(subjects84) == 0:
                                                                pass
                                                                # State 2545
                                                                if len(subjects) == 0:
                                                                    pass
                                                                    # 20: b*v**n /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f5) and (cons_f52) and (cons_f54) and (cons_f51)
                                                                    yield 20, subst3
                                                if len(subjects84) >= 1:
                                                    tmp94 = subjects84.popleft()
                                                    subst3 = Substitution(subst2)
                                                    try:
                                                        subst3.try_add_variable('i2.2.1.2_1', tmp94)
                                                    except ValueError:
                                                        pass
                                                    else:
                                                        pass
                                                        if 'i2.2.1.2_1' not in subst3 or 'i2.2.1.1' not in subst3 or cons_f52(q=subst3["i2.2.1.2_1"], x=subst3["i2.2.1.1"]):
                                                            pass
                                                            if 'i2.2.1.2' not in subst3 or 'i2.2.1.2_1' not in subst3 or cons_f51(p=subst3["i2.2.1.2"], q=subst3["i2.2.1.2_1"]):
                                                                pass
                                                                # State 2544
                                                                if len(subjects84) == 0:
                                                                    pass
                                                                    # State 2545
                                                                    if len(subjects) == 0:
                                                                        pass
                                                                        # 20: b*v**n /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f5) and (cons_f52) and (cons_f54) and (cons_f51)
                                                                        yield 20, subst3
                                                    subjects84.appendleft(tmp94)
                                        # State 2543
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
                                                    # State 2544
                                                    if len(subjects84) == 0:
                                                        pass
                                                        # State 2545
                                                        if len(subjects) == 0:
                                                            pass
                                                            # 18: b*v**n /; (cons_f2) and (cons_f3) and (cons_f5) and (cons_f52) and (cons_f51)
                                                            yield 18, subst3
                                        if len(subjects84) >= 1:
                                            tmp97 = subjects84.popleft()
                                            subst3 = Substitution(subst2)
                                            try:
                                                subst3.try_add_variable('i2.2.1.2_1', tmp97)
                                            except ValueError:
                                                pass
                                            else:
                                                pass
                                                if 'i2.2.1.2_1' not in subst3 or 'i2.2.1.1' not in subst3 or cons_f52(q=subst3["i2.2.1.2_1"], x=subst3["i2.2.1.1"]):
                                                    pass
                                                    if 'i2.2.1.2' not in subst3 or 'i2.2.1.2_1' not in subst3 or cons_f51(p=subst3["i2.2.1.2"], q=subst3["i2.2.1.2_1"]):
                                                        pass
                                                        # State 2544
                                                        if len(subjects84) == 0:
                                                            pass
                                                            # State 2545
                                                            if len(subjects) == 0:
                                                                pass
                                                                # 18: b*v**n /; (cons_f2) and (cons_f3) and (cons_f5) and (cons_f52) and (cons_f51)
                                                                yield 18, subst3
                                            subjects84.appendleft(tmp97)
                        if 'i2' not in subst2 or 'i2.2.1.1' not in subst2 or cons_f11(Pm=subst2["i2.2.1.1"], x=subst2["i2"]):
                            pass
                            if 'i2' not in subst2 or 'i2.2.1.1' not in subst2 or 'i2.2.1.0' not in subst2 or 'i2.2.0' not in subst2 or 'i2.0' not in subst2 or 'i2.2.1.2_1' not in subst2 or 'i2.2.1.2' not in subst2 or 'i2.2' not in subst2 or 'i2.2.1.0_1' not in subst2 or With36(Pm=subst2["i2.2.1.1"], Qm=subst2["i2.0"], a=subst2["i2.2.0"], b=subst2["i2.2.1.0"], c=subst2["i2.2.1.0_1"], n=subst2["i2.2.1.2"], n2=subst2["i2.2.1.2_1"], p=subst2["i2.2"], x=subst2["i2"]):
                                pass
                                # State 2543
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
                                            # State 2544
                                            if len(subjects84) == 0:
                                                pass
                                                # State 2545
                                                if len(subjects) == 0:
                                                    pass
                                                    # 24: b*v**n /; (cons_f8) and (cons_f48) and (cons_f11) and (With36)
                                                    yield 24, subst3
                                if len(subjects84) >= 1:
                                    tmp100 = subjects84.popleft()
                                    subst3 = Substitution(subst2)
                                    try:
                                        subst3.try_add_variable('i2.2.1.2_1', tmp100)
                                    except ValueError:
                                        pass
                                    else:
                                        pass
                                        if 'i2.2.1.2' not in subst3 or 'i2.2.1.2_1' not in subst3 or cons_f48(n=subst3["i2.2.1.2"], n2=subst3["i2.2.1.2_1"]):
                                            pass
                                            if 'i2' not in subst3 or 'i2.2.1.1' not in subst3 or 'i2.2.1.0' not in subst3 or 'i2.2.0' not in subst3 or 'i2.0' not in subst3 or 'i2.2.1.2_1' not in subst3 or 'i2.2.1.2' not in subst3 or 'i2.2' not in subst3 or 'i2.2.1.0_1' not in subst3 or With36(Pm=subst3["i2.2.1.1"], Qm=subst3["i2.0"], a=subst3["i2.2.0"], b=subst3["i2.2.1.0"], c=subst3["i2.2.1.0_1"], n=subst3["i2.2.1.2"], n2=subst3["i2.2.1.2_1"], p=subst3["i2.2"], x=subst3["i2"]):
                                                pass
                                                # State 2544
                                                if len(subjects84) == 0:
                                                    pass
                                                    # State 2545
                                                    if len(subjects) == 0:
                                                        pass
                                                        # 24: b*v**n /; (cons_f8) and (cons_f48) and (cons_f11) and (With36)
                                                        yield 24, subst3
                                    subjects84.appendleft(tmp100)
                    subjects84.appendleft(tmp85)
                subjects.appendleft(tmp83)
        subst1 = Substitution(subst0)
        try:
            subst1.try_add_variable('i2.2.1.0_2', S(1))
        except ValueError:
            pass
        else:
            pass
            # State 2621
            if len(subjects) >= 1:
                tmp103 = subjects.popleft()
                subst2 = Substitution(subst1)
                try:
                    subst2.try_add_variable('i2.2.1.0', tmp103)
                except ValueError:
                    pass
                else:
                    pass
                    if 'i2' not in subst2 or 'i2.2.1.0' not in subst2 or cons_f10(v=subst2["i2.2.1.0"], x=subst2["i2"]):
                        pass
                        # State 2622
                        if len(subjects) == 0:
                            pass
                            # 7: v*b /; (cons_f3) and (cons_f10)
                            yield 7, subst2
                subjects.appendleft(tmp103)
            subst2 = Substitution(subst1)
            try:
                subst2.try_add_variable('i2.2.1.2_2', S(1))
            except ValueError:
                pass
            else:
                pass
                # State 2987
                if len(subjects) >= 1:
                    tmp106 = subjects.popleft()
                    subst3 = Substitution(subst2)
                    try:
                        subst3.try_add_variable('i2.2.1.1', tmp106)
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
                                                # State 2988
                                                if len(subjects) == 0:
                                                    pass
                                                    # 21: c*x**r /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f5) and (cons_f52) and (cons_f54) and (cons_f53)
                                                    yield 21, subst3
                    subjects.appendleft(tmp106)
            if len(subjects) >= 1 and isinstance(subjects[0], Pow):
                tmp108 = subjects.popleft()
                subjects109 = deque(tmp108._args)
                # State 2989
                if len(subjects109) >= 1:
                    tmp110 = subjects109.popleft()
                    subst2 = Substitution(subst1)
                    try:
                        subst2.try_add_variable('i2.2.1.1', tmp110)
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
                                                # State 2990
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
                                                            # State 2991
                                                            if len(subjects109) == 0:
                                                                pass
                                                                # State 2992
                                                                if len(subjects) == 0:
                                                                    pass
                                                                    # 21: c*x**r /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f5) and (cons_f52) and (cons_f54) and (cons_f53)
                                                                    yield 21, subst3
                                                if len(subjects109) >= 1:
                                                    tmp113 = subjects109.popleft()
                                                    subst3 = Substitution(subst2)
                                                    try:
                                                        subst3.try_add_variable('i2.2.1.2_2', tmp113)
                                                    except ValueError:
                                                        pass
                                                    else:
                                                        pass
                                                        if 'i2.2.1.2_2' not in subst3 or 'i2.2.1.1' not in subst3 or cons_f54(r=subst3["i2.2.1.2_2"], x=subst3["i2.2.1.1"]):
                                                            pass
                                                            if 'i2.2.1.2' not in subst3 or 'i2.2.1.2_2' not in subst3 or cons_f53(p=subst3["i2.2.1.2"], r=subst3["i2.2.1.2_2"]):
                                                                pass
                                                                # State 2991
                                                                if len(subjects109) == 0:
                                                                    pass
                                                                    # State 2992
                                                                    if len(subjects) == 0:
                                                                        pass
                                                                        # 21: c*x**r /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f5) and (cons_f52) and (cons_f54) and (cons_f53)
                                                                        yield 21, subst3
                                                    subjects109.appendleft(tmp113)
                    subjects109.appendleft(tmp110)
                subjects.appendleft(tmp108)
        if len(subjects) >= 1 and isinstance(subjects[0], Mul):
            tmp115 = subjects.popleft()
            associative1 = tmp115
            associative_type1 = type(tmp115)
            subjects116 = deque(tmp115._args)
            matcher = CommutativeMatcher2363.get()
            tmp117 = subjects116
            subjects116 = []
            for s in tmp117:
                matcher.add_subject(s)
            for pattern_index, subst1 in matcher.match(tmp117, subst0):
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
                                        # State 2370
                                        if len(subjects) == 0:
                                            pass
                                            # 1: a*v**m /; (cons_f2) and (cons_f3) and (cons_f4) and (cons_f5) and (cons_f6)
                                            yield 1, subst1
                                    # State 2370
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
                                                # State 2538
                                                if len(subjects) == 0:
                                                    pass
                                                    # 5: a*v**m /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f4) and (cons_f5) and (cons_f7) and (cons_f9)
                                                    yield 5, subst1
                                            # State 2538
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
                                                # State 2550
                                                if len(subjects) == 0:
                                                    pass
                                                    # 4: b*v**n /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f4) and (cons_f5) and (cons_f7) and (cons_f6)
                                                    yield 4, subst1
                                            # State 2550
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
                            # State 2620
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
                                # State 2620
                                if len(subjects) == 0:
                                    pass
                                    # 8: v*a /; (cons_f3) and (cons_f27) and (cons_f28)
                                    yield 8, subst1
                if pattern_index == 4:
                    pass
                    if 'i2' not in subst1 or 'i2.2.1.0' not in subst1 or cons_f10(v=subst1["i2.2.1.0"], x=subst1["i2"]):
                        pass
                        if 'i2.2.1.0_2' not in subst1 or 'i2' not in subst1 or cons_f3(b=subst1["i2.2.1.0_2"], x=subst1["i2"]):
                            pass
                            # State 2623
                            if len(subjects) == 0:
                                pass
                                # 7: v*b /; (cons_f3) and (cons_f10)
                                yield 7, subst1
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
                                                        # State 2791
                                                        if len(subjects) == 0:
                                                            pass
                                                            # 9: a*v**m /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f19) and (cons_f4) and (cons_f39) and (cons_f41) and (cons_f42)
                                                            yield 9, subst1
                if pattern_index == 6:
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
                                                            # State 2829
                                                            if len(subjects) == 0:
                                                                pass
                                                                # 10: d*x**j /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f19) and (cons_f4) and (cons_f5) and (cons_f7) and (cons_f44) and (cons_f46)
                                                                yield 10, subst1
                if pattern_index == 7:
                    pass
                    if 'i2.2.0' not in subst1 or 'i2.2.1.1' not in subst1 or cons_f2(a=subst1["i2.2.0"], x=subst1["i2.2.1.1"]):
                        pass
                        if 'i2.2.1.0_1' not in subst1 or 'i2.2.1.1' not in subst1 or cons_f3(b=subst1["i2.2.1.0_1"], x=subst1["i2.2.1.1"]):
                            pass
                            if 'i2.2.1.0' not in subst1 or 'i2.2.1.1' not in subst1 or cons_f8(c=subst1["i2.2.1.0"], x=subst1["i2.2.1.1"]):
                                pass
                                if 'i2.2.1.0' not in subst1 or 'i2.2.1.0_1' not in subst1 or 'i2.2.0' not in subst1 or cons_f47(a=subst1["i2.2.0"], b=subst1["i2.2.1.0_1"], c=subst1["i2.2.1.0"]):
                                    pass
                                    # State 2868
                                    if len(subjects) == 0:
                                        pass
                                        # 11: c*x**2 /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f47)
                                        yield 11, subst1
                if pattern_index == 8:
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
                                                # State 2870
                                                if len(subjects) == 0:
                                                    pass
                                                    # 16: b*x /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f50) and (cons_f5) and (cons_f49)
                                                    yield 16, subst1
                        if 'i2.2.1.0_1' not in subst1 or 'i2.2.1.1' not in subst1 or cons_f3(b=subst1["i2.2.1.0_1"], x=subst1["i2.2.1.1"]):
                            pass
                            if 'i2.2.1.0' not in subst1 or 'i2.2.1.1' not in subst1 or cons_f8(c=subst1["i2.2.1.0"], x=subst1["i2.2.1.1"]):
                                pass
                                if 'i2.2.1.0' not in subst1 or 'i2.2.1.0_1' not in subst1 or 'i2.2.0' not in subst1 or cons_f47(a=subst1["i2.2.0"], b=subst1["i2.2.1.0_1"], c=subst1["i2.2.1.0"]):
                                    pass
                                    # State 2870
                                    if len(subjects) == 0:
                                        pass
                                        # 12: b*x /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f47)
                                        yield 12, subst1
                if pattern_index == 9:
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
                                            # State 2905
                                            if len(subjects) == 0:
                                                pass
                                                # 13: b*v**n /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f4) and (cons_f48) and (cons_f47)
                                                yield 13, subst1
                if pattern_index == 10:
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
                                            # State 2906
                                            if len(subjects) == 0:
                                                pass
                                                # 14: d*x**j /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f4) and (cons_f48) and (cons_f47)
                                                yield 14, subst1
                if pattern_index == 11:
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
                                                # State 2916
                                                if len(subjects) == 0:
                                                    pass
                                                    # 15: c*x**2 /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f50) and (cons_f5) and (cons_f49)
                                                    yield 15, subst1
                if pattern_index == 12:
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
                                        # State 2940
                                        if len(subjects) == 0:
                                            pass
                                            # 17: a*v**m /; (cons_f2) and (cons_f3) and (cons_f5) and (cons_f52) and (cons_f51)
                                            yield 17, subst1
                if pattern_index == 13:
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
                                        # State 2941
                                        if len(subjects) == 0:
                                            pass
                                            # 18: b*v**n /; (cons_f2) and (cons_f3) and (cons_f5) and (cons_f52) and (cons_f51)
                                            yield 18, subst1
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
                                        if 'i2.2.1.0_2' not in subst1 or 'i2.2.1.1' not in subst1 or cons_f8(c=subst1["i2.2.1.0_2"], x=subst1["i2.2.1.1"]):
                                            pass
                                            if 'i2.2.1.2_2' not in subst1 or 'i2.2.1.1' not in subst1 or cons_f54(r=subst1["i2.2.1.2_2"], x=subst1["i2.2.1.1"]):
                                                pass
                                                if 'i2.2.1.2' not in subst1 or 'i2.2.1.2_2' not in subst1 or cons_f53(p=subst1["i2.2.1.2"], r=subst1["i2.2.1.2_2"]):
                                                    pass
                                                    # State 2985
                                                    if len(subjects) == 0:
                                                        pass
                                                        # 19: a*v**m /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f5) and (cons_f52) and (cons_f54) and (cons_f51) and (cons_f53)
                                                        yield 19, subst1
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
                                        if 'i2.2.1.0_2' not in subst1 or 'i2.2.1.1' not in subst1 or cons_f8(c=subst1["i2.2.1.0_2"], x=subst1["i2.2.1.1"]):
                                            pass
                                            if 'i2.2.1.2_2' not in subst1 or 'i2.2.1.1' not in subst1 or cons_f54(r=subst1["i2.2.1.2_2"], x=subst1["i2.2.1.1"]):
                                                pass
                                                # State 2986
                                                if len(subjects) == 0:
                                                    pass
                                                    # 20: b*v**n /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f5) and (cons_f52) and (cons_f54) and (cons_f51)
                                                    yield 20, subst1
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
                                    if 'i2.2.1.0_2' not in subst1 or 'i2.2.1.1' not in subst1 or cons_f8(c=subst1["i2.2.1.0_2"], x=subst1["i2.2.1.1"]):
                                        pass
                                        if 'i2.2.1.2_2' not in subst1 or 'i2.2.1.1' not in subst1 or cons_f54(r=subst1["i2.2.1.2_2"], x=subst1["i2.2.1.1"]):
                                            pass
                                            if 'i2.2.1.2' not in subst1 or 'i2.2.1.2_2' not in subst1 or cons_f53(p=subst1["i2.2.1.2"], r=subst1["i2.2.1.2_2"]):
                                                pass
                                                # State 2997
                                                if len(subjects) == 0:
                                                    pass
                                                    # 21: c*x**r /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f5) and (cons_f52) and (cons_f54) and (cons_f53)
                                                    yield 21, subst1
                if pattern_index == 17:
                    pass
                    if 'i2' not in subst1 or 'i2.2.1.0' not in subst1 or cons_f3(b=subst1["i2.2.1.0"], x=subst1["i2"]):
                        pass
                        if 'i2.2.1.2' not in subst1 or 'i2' not in subst1 or cons_f4(n=subst1["i2.2.1.2"], x=subst1["i2"]):
                            pass
                            if 'i2' not in subst1 or 'i2.2.1.1' not in subst1 or cons_f11(Pm=subst1["i2.2.1.1"], x=subst1["i2"]):
                                pass
                                if 'i2' not in subst1 or 'i2.2.1.1' not in subst1 or 'i2.2.1.0' not in subst1 or 'i2.2.0' not in subst1 or 'i2.0' not in subst1 or 'i2.2' not in subst1 or 'i2.2.1.2' not in subst1 or With35(Pm=subst1["i2.2.1.1"], Qm=subst1["i2.0"], a=subst1["i2.2.0"], b=subst1["i2.2.1.0"], n=subst1["i2.2.1.2"], p=subst1["i2.2"], x=subst1["i2"]):
                                    pass
                                    # State 3055
                                    if len(subjects) == 0:
                                        pass
                                        # 22: a*v**m /; (cons_f3) and (cons_f4) and (cons_f11) and (With35)
                                        yield 22, subst1
                if pattern_index == 18:
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
                                        # State 3067
                                        if len(subjects) == 0:
                                            pass
                                            # 23: a*v**m /; (cons_f3) and (cons_f4) and (cons_f48) and (cons_f11) and (With36)
                                            yield 23, subst1
                if pattern_index == 19:
                    pass
                    if 'i2.2.1.2' not in subst1 or 'i2.2.1.2_1' not in subst1 or cons_f48(n=subst1["i2.2.1.2"], n2=subst1["i2.2.1.2_1"]):
                        pass
                        if 'i2' not in subst1 or 'i2.2.1.1' not in subst1 or cons_f11(Pm=subst1["i2.2.1.1"], x=subst1["i2"]):
                            pass
                            if 'i2' not in subst1 or 'i2.2.1.1' not in subst1 or 'i2.2.1.0' not in subst1 or 'i2.2.0' not in subst1 or 'i2.0' not in subst1 or 'i2.2.1.2_1' not in subst1 or 'i2.2.1.2' not in subst1 or 'i2.2' not in subst1 or 'i2.2.1.0_1' not in subst1 or With36(Pm=subst1["i2.2.1.1"], Qm=subst1["i2.0"], a=subst1["i2.2.0"], b=subst1["i2.2.1.0"], c=subst1["i2.2.1.0_1"], n=subst1["i2.2.1.2"], n2=subst1["i2.2.1.2_1"], p=subst1["i2.2"], x=subst1["i2"]):
                                pass
                                if 'i2' not in subst1 or 'i2.2.1.0_1' not in subst1 or cons_f8(c=subst1["i2.2.1.0_1"], x=subst1["i2"]):
                                    pass
                                    # State 3068
                                    if len(subjects) == 0:
                                        pass
                                        # 24: b*v**n /; (cons_f8) and (cons_f48) and (cons_f11) and (With36)
                                        yield 24, subst1
            subjects.appendleft(tmp115)
        return
        yield


from matchpy.matching.many_to_one import CommutativeMatcher
from .generated_part000009 import *
from matchpy.utils import VariableWithCount
from multiset import Multiset
from collections import deque