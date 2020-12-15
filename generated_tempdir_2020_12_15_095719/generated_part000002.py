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
    6: (6, Multiset({}), [
      (VariableWithCount('i2.2.1.0_1', 1, 1, S(1)), Mul),
      (VariableWithCount('i2.2.1.1', 1, 1, None), Mul)
]),
    7: (7, Multiset({4: 1}), [
      (VariableWithCount('i2.2.1.0_1', 1, 1, S(1)), Mul)
]),
    8: (8, Multiset({5: 1}), [
      (VariableWithCount('i2.2.1.0', 1, 1, S(1)), Mul)
]),
    9: (9, Multiset({6: 1}), [
      (VariableWithCount('i2.2.1.0', 1, 1, S(1)), Mul)
]),
    10: (10, Multiset({7: 1}), [
      (VariableWithCount('i2.2.1.0_1', 1, 1, S(1)), Mul)
]),
    11: (11, Multiset({8: 1}), [
      (VariableWithCount('i2.2.1.0', 1, 1, S(1)), Mul)
]),
    12: (12, Multiset({9: 1}), [
      (VariableWithCount('i2.2.1.0_1', 1, 1, S(1)), Mul)
]),
    13: (13, Multiset({10: 1}), [
      (VariableWithCount('i2.2.1.0_2', 1, 1, S(1)), Mul)
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
            subst1.try_add_variable('i2.2.1.2', S(1))
        except ValueError:
            pass
        else:
            pass
            # State 2316
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
                                    # State 2317
                                    if len(subjects) == 0:
                                        pass
                                        # 0: v**m /; (cons_f2) and (cons_f3) and (cons_f4) and (cons_f5)
                                        yield 0, subst2
                        if 'i2.2' not in subst2 or 'i2.2.1.1' not in subst2 or cons_f5(p=subst2["i2.2"], x=subst2["i2.2.1.1"]):
                            pass
                            if 'i2.2.1.0_1' not in subst2 or 'i2.2.1.1' not in subst2 or cons_f3(b=subst2["i2.2.1.0_1"], x=subst2["i2.2.1.1"]):
                                pass
                                if 'i2.2.1.0' not in subst2 or 'i2.2.1.1' not in subst2 or cons_f8(c=subst2["i2.2.1.0"], x=subst2["i2.2.1.1"]):
                                    pass
                                    if 'i2.2.1.2_1' not in subst2 or 'i2.2.1.1' not in subst2 or cons_f4(n=subst2["i2.2.1.2_1"], x=subst2["i2.2.1.1"]):
                                        pass
                                        # State 2317
                                        if len(subjects) == 0:
                                            pass
                                            # 1: v**m /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f4) and (cons_f5) and (cons_f7)
                                            yield 1, subst2
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
                                            # State 2317
                                            if len(subjects) == 0:
                                                pass
                                                # 8: v**m /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f5) and (cons_f52) and (cons_f54) and (cons_f51) and (cons_f53)
                                                yield 8, subst2
                                    # State 2317
                                    if len(subjects) == 0:
                                        pass
                                        # 6: v**m /; (cons_f2) and (cons_f3) and (cons_f5) and (cons_f52) and (cons_f51)
                                        yield 6, subst2
                subjects.appendleft(tmp2)
        subst1 = Substitution(subst0)
        try:
            subst1.try_add_variable('i2.2.1.2_1', S(1))
        except ValueError:
            pass
        else:
            pass
            # State 2512
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
                                if 'i2.2.1.0_1' not in subst2 or 'i2.2.1.1' not in subst2 or cons_f8(c=subst2["i2.2.1.0_1"], x=subst2["i2.2.1.1"]):
                                    pass
                                    # State 2513
                                    if len(subjects) == 0:
                                        pass
                                        # 4: v**n /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f4) and (cons_f48)
                                        yield 4, subst2
                        if 'i2.2' not in subst2 or 'i2.2.1.1' not in subst2 or cons_f5(p=subst2["i2.2"], x=subst2["i2.2.1.1"]):
                            pass
                            if 'i2.2.1.0_1' not in subst2 or 'i2.2.1.1' not in subst2 or cons_f3(b=subst2["i2.2.1.0_1"], x=subst2["i2.2.1.1"]):
                                pass
                                if 'i2.2.1.0' not in subst2 or 'i2.2.1.1' not in subst2 or cons_f8(c=subst2["i2.2.1.0"], x=subst2["i2.2.1.1"]):
                                    pass
                                    if 'i2.2.1.2_1' not in subst2 or 'i2.2.1.1' not in subst2 or cons_f4(n=subst2["i2.2.1.2_1"], x=subst2["i2.2.1.1"]):
                                        pass
                                        # State 2513
                                        if len(subjects) == 0:
                                            pass
                                            # 2: v**n /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f4) and (cons_f5) and (cons_f7)
                                            yield 2, subst2
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
                                            # State 2513
                                            if len(subjects) == 0:
                                                pass
                                                # 9: v**n /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f5) and (cons_f52) and (cons_f54) and (cons_f51)
                                                yield 9, subst2
                                    # State 2513
                                    if len(subjects) == 0:
                                        pass
                                        # 7: v**n /; (cons_f2) and (cons_f3) and (cons_f5) and (cons_f52) and (cons_f51)
                                        yield 7, subst2
                subjects.appendleft(tmp5)
        subst1 = Substitution(subst0)
        try:
            subst1.try_add_variable('i2.2.1.2_2', S(1))
        except ValueError:
            pass
        else:
            pass
            # State 2959
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
                                            # State 2960
                                            if len(subjects) == 0:
                                                pass
                                                # 10: x**r /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f5) and (cons_f52) and (cons_f54) and (cons_f53)
                                                yield 10, subst2
                subjects.appendleft(tmp8)
        if len(subjects) >= 1 and isinstance(subjects[0], Pow):
            tmp10 = subjects.popleft()
            subjects11 = deque(tmp10._args)
            # State 2318
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
                                    # State 2319
                                    subst2 = Substitution(subst1)
                                    try:
                                        subst2.try_add_variable('i2.2.1.2', 1)
                                    except ValueError:
                                        pass
                                    else:
                                        pass
                                        if 'i2.2.1.2' not in subst2 or 'i2.2.1.1' not in subst2 or cons_f4(n=subst2["i2.2.1.2"], x=subst2["i2.2.1.1"]):
                                            pass
                                            # State 2320
                                            if len(subjects11) == 0:
                                                pass
                                                # State 2321
                                                if len(subjects) == 0:
                                                    pass
                                                    # 0: v**m /; (cons_f2) and (cons_f3) and (cons_f4) and (cons_f5)
                                                    yield 0, subst2
                                    if len(subjects11) >= 1:
                                        tmp15 = subjects11.popleft()
                                        subst2 = Substitution(subst1)
                                        try:
                                            subst2.try_add_variable('i2.2.1.2', tmp15)
                                        except ValueError:
                                            pass
                                        else:
                                            pass
                                            if 'i2.2.1.2' not in subst2 or 'i2.2.1.1' not in subst2 or cons_f4(n=subst2["i2.2.1.2"], x=subst2["i2.2.1.1"]):
                                                pass
                                                # State 2320
                                                if len(subjects11) == 0:
                                                    pass
                                                    # State 2321
                                                    if len(subjects) == 0:
                                                        pass
                                                        # 0: v**m /; (cons_f2) and (cons_f3) and (cons_f4) and (cons_f5)
                                                        yield 0, subst2
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
                                        # State 2844
                                        if len(subjects11) == 0:
                                            pass
                                            # State 2845
                                            if len(subjects) == 0:
                                                pass
                                        subjects11.appendleft(tmp25)
                                if 'i2.2.1.0_1' not in subst1 or 'i2.2.1.1' not in subst1 or cons_f8(c=subst1["i2.2.1.0_1"], x=subst1["i2.2.1.1"]):
                                    pass
                                    # State 2319
                                    subst2 = Substitution(subst1)
                                    try:
                                        subst2.try_add_variable('i2.2.1.2', 1)
                                    except ValueError:
                                        pass
                                    else:
                                        pass
                                    if len(subjects11) >= 1:
                                        tmp27 = subjects11.popleft()
                                        subst2 = Substitution(subst1)
                                        try:
                                            subst2.try_add_variable('i2.2.1.2', tmp27)
                                        except ValueError:
                                            pass
                                        else:
                                            pass
                                        subjects11.appendleft(tmp27)
                                    subst2 = Substitution(subst1)
                                    try:
                                        subst2.try_add_variable('i2.2.1.2_1', 1)
                                    except ValueError:
                                        pass
                                    else:
                                        pass
                                        if 'i2.2.1.2' not in subst2 or 'i2.2.1.2_1' not in subst2 or cons_f48(n=subst2["i2.2.1.2"], n2=subst2["i2.2.1.2_1"]):
                                            pass
                                            # State 2514
                                            if len(subjects11) == 0:
                                                pass
                                                # State 2515
                                                if len(subjects) == 0:
                                                    pass
                                                    # 4: v**n /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f4) and (cons_f48)
                                                    yield 4, subst2
                                    if len(subjects11) >= 1:
                                        tmp30 = subjects11.popleft()
                                        subst2 = Substitution(subst1)
                                        try:
                                            subst2.try_add_variable('i2.2.1.2_1', tmp30)
                                        except ValueError:
                                            pass
                                        else:
                                            pass
                                            if 'i2.2.1.2' not in subst2 or 'i2.2.1.2_1' not in subst2 or cons_f48(n=subst2["i2.2.1.2"], n2=subst2["i2.2.1.2_1"]):
                                                pass
                                                # State 2514
                                                if len(subjects11) == 0:
                                                    pass
                                                    # State 2515
                                                    if len(subjects) == 0:
                                                        pass
                                                        # 4: v**n /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f4) and (cons_f48)
                                                        yield 4, subst2
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
                                            if 'i2.2.1.2' not in subst2 or 'i2.2.1.1' not in subst2 or cons_f4(n=subst2["i2.2.1.2"], x=subst2["i2.2.1.1"]):
                                                pass
                                                if 'i2.2.1.2' not in subst2 or 'i2.2.1.2_1' not in subst2 or cons_f48(n=subst2["i2.2.1.2"], n2=subst2["i2.2.1.2_1"]):
                                                    pass
                                                    # State 2888
                                                    if len(subjects11) == 0:
                                                        pass
                                                        # State 2889
                                                        if len(subjects) == 0:
                                                            pass
                                                            # 5: x**j /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f4) and (cons_f48)
                                                            yield 5, subst2
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
                                        # State 2844
                                        if len(subjects11) == 0:
                                            pass
                                            # State 2845
                                            if len(subjects) == 0:
                                                pass
                                        subjects11.appendleft(tmp37)
                        if 'i2.2' not in subst1 or 'i2.2.1.1' not in subst1 or cons_f5(p=subst1["i2.2"], x=subst1["i2.2.1.1"]):
                            pass
                            if 'i2.2.1.0_1' not in subst1 or 'i2.2.1.1' not in subst1 or cons_f3(b=subst1["i2.2.1.0_1"], x=subst1["i2.2.1.1"]):
                                pass
                                if 'i2.2.1.0' not in subst1 or 'i2.2.1.1' not in subst1 or cons_f8(c=subst1["i2.2.1.0"], x=subst1["i2.2.1.1"]):
                                    pass
                                    if 'i2.2.1.2_1' not in subst1 or 'i2.2.1.1' not in subst1 or cons_f4(n=subst1["i2.2.1.2_1"], x=subst1["i2.2.1.1"]):
                                        pass
                                        # State 2319
                                        subst2 = Substitution(subst1)
                                        try:
                                            subst2.try_add_variable('i2.2.1.2', 1)
                                        except ValueError:
                                            pass
                                        else:
                                            pass
                                            if 'i2.2.1.2' not in subst2 or 'i2.2.1.2_1' not in subst2 or cons_f7(j=subst2["i2.2.1.2"], n=subst2["i2.2.1.2_1"]):
                                                pass
                                                # State 2320
                                                if len(subjects11) == 0:
                                                    pass
                                                    # State 2321
                                                    if len(subjects) == 0:
                                                        pass
                                                        # 1: v**m /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f4) and (cons_f5) and (cons_f7)
                                                        yield 1, subst2
                                        if len(subjects11) >= 1:
                                            tmp39 = subjects11.popleft()
                                            subst2 = Substitution(subst1)
                                            try:
                                                subst2.try_add_variable('i2.2.1.2', tmp39)
                                            except ValueError:
                                                pass
                                            else:
                                                pass
                                                if 'i2.2.1.2' not in subst2 or 'i2.2.1.2_1' not in subst2 or cons_f7(j=subst2["i2.2.1.2"], n=subst2["i2.2.1.2_1"]):
                                                    pass
                                                    # State 2320
                                                    if len(subjects11) == 0:
                                                        pass
                                                        # State 2321
                                                        if len(subjects) == 0:
                                                            pass
                                                            # 1: v**m /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f4) and (cons_f5) and (cons_f7)
                                                            yield 1, subst2
                                            subjects11.appendleft(tmp39)
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
                                                    # State 2514
                                                    if len(subjects11) == 0:
                                                        pass
                                                        # State 2515
                                                        if len(subjects) == 0:
                                                            pass
                                                            # 2: v**n /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f4) and (cons_f5) and (cons_f7)
                                                            yield 2, subst2
                                        if len(subjects11) >= 1:
                                            tmp42 = subjects11.popleft()
                                            subst2 = Substitution(subst1)
                                            try:
                                                subst2.try_add_variable('i2.2.1.2_1', tmp42)
                                            except ValueError:
                                                pass
                                            else:
                                                pass
                                                if 'i2.2.1.2_1' not in subst2 or 'i2.2.1.1' not in subst2 or cons_f4(n=subst2["i2.2.1.2_1"], x=subst2["i2.2.1.1"]):
                                                    pass
                                                    if 'i2.2.1.2' not in subst2 or 'i2.2.1.2_1' not in subst2 or cons_f7(j=subst2["i2.2.1.2"], n=subst2["i2.2.1.2_1"]):
                                                        pass
                                                        # State 2514
                                                        if len(subjects11) == 0:
                                                            pass
                                                            # State 2515
                                                            if len(subjects) == 0:
                                                                pass
                                                                # 2: v**n /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f4) and (cons_f5) and (cons_f7)
                                                                yield 2, subst2
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
                                            # State 2844
                                            if len(subjects11) == 0:
                                                pass
                                                # State 2845
                                                if len(subjects) == 0:
                                                    pass
                                            subjects11.appendleft(tmp49)
                        if 'i2.2.1.0_1' not in subst1 or 'i2.2.1.1' not in subst1 or cons_f3(b=subst1["i2.2.1.0_1"], x=subst1["i2.2.1.1"]):
                            pass
                            if 'i2.2.1.0' not in subst1 or 'i2.2.1.1' not in subst1 or cons_f8(c=subst1["i2.2.1.0"], x=subst1["i2.2.1.1"]):
                                pass
                                # State 2319
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
                                    # State 2844
                                    if len(subjects11) == 0:
                                        pass
                                        # State 2845
                                        if len(subjects) == 0:
                                            pass
                                            # 3: x**2 /; (cons_f2) and (cons_f3) and (cons_f8)
                                            yield 3, subst1
                                    subjects11.appendleft(tmp61)
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
                                            # State 2319
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
                                                            # State 2320
                                                            if len(subjects11) == 0:
                                                                pass
                                                                # State 2321
                                                                if len(subjects) == 0:
                                                                    pass
                                                                    # 8: v**m /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f5) and (cons_f52) and (cons_f54) and (cons_f51) and (cons_f53)
                                                                    yield 8, subst2
                                            if len(subjects11) >= 1:
                                                tmp63 = subjects11.popleft()
                                                subst2 = Substitution(subst1)
                                                try:
                                                    subst2.try_add_variable('i2.2.1.2', tmp63)
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
                                                                # State 2320
                                                                if len(subjects11) == 0:
                                                                    pass
                                                                    # State 2321
                                                                    if len(subjects) == 0:
                                                                        pass
                                                                        # 8: v**m /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f5) and (cons_f52) and (cons_f54) and (cons_f51) and (cons_f53)
                                                                        yield 8, subst2
                                                subjects11.appendleft(tmp63)
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
                                                        # State 2514
                                                        if len(subjects11) == 0:
                                                            pass
                                                            # State 2515
                                                            if len(subjects) == 0:
                                                                pass
                                                                # 9: v**n /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f5) and (cons_f52) and (cons_f54) and (cons_f51)
                                                                yield 9, subst2
                                            if len(subjects11) >= 1:
                                                tmp66 = subjects11.popleft()
                                                subst2 = Substitution(subst1)
                                                try:
                                                    subst2.try_add_variable('i2.2.1.2_1', tmp66)
                                                except ValueError:
                                                    pass
                                                else:
                                                    pass
                                                    if 'i2.2.1.2_1' not in subst2 or 'i2.2.1.1' not in subst2 or cons_f52(q=subst2["i2.2.1.2_1"], x=subst2["i2.2.1.1"]):
                                                        pass
                                                        if 'i2.2.1.2' not in subst2 or 'i2.2.1.2_1' not in subst2 or cons_f51(p=subst2["i2.2.1.2"], q=subst2["i2.2.1.2_1"]):
                                                            pass
                                                            # State 2514
                                                            if len(subjects11) == 0:
                                                                pass
                                                                # State 2515
                                                                if len(subjects) == 0:
                                                                    pass
                                                                    # 9: v**n /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f5) and (cons_f52) and (cons_f54) and (cons_f51)
                                                                    yield 9, subst2
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
                                                subjects11.appendleft(tmp68)
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
                                                        # State 2961
                                                        if len(subjects11) == 0:
                                                            pass
                                                            # State 2962
                                                            if len(subjects) == 0:
                                                                pass
                                                                # 10: x**r /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f5) and (cons_f52) and (cons_f54) and (cons_f53)
                                                                yield 10, subst2
                                            if len(subjects11) >= 1:
                                                tmp71 = subjects11.popleft()
                                                subst2 = Substitution(subst1)
                                                try:
                                                    subst2.try_add_variable('i2.2.1.2_2', tmp71)
                                                except ValueError:
                                                    pass
                                                else:
                                                    pass
                                                    if 'i2.2.1.2_2' not in subst2 or 'i2.2.1.1' not in subst2 or cons_f54(r=subst2["i2.2.1.2_2"], x=subst2["i2.2.1.1"]):
                                                        pass
                                                        if 'i2.2.1.2' not in subst2 or 'i2.2.1.2_2' not in subst2 or cons_f53(p=subst2["i2.2.1.2"], r=subst2["i2.2.1.2_2"]):
                                                            pass
                                                            # State 2961
                                                            if len(subjects11) == 0:
                                                                pass
                                                                # State 2962
                                                                if len(subjects) == 0:
                                                                    pass
                                                                    # 10: x**r /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f5) and (cons_f52) and (cons_f54) and (cons_f53)
                                                                    yield 10, subst2
                                                subjects11.appendleft(tmp71)
                                            if len(subjects11) >= 1 and subjects11[0] == Integer(2):
                                                tmp73 = subjects11.popleft()
                                                # State 2844
                                                if len(subjects11) == 0:
                                                    pass
                                                    # State 2845
                                                    if len(subjects) == 0:
                                                        pass
                                                subjects11.appendleft(tmp73)
                                    # State 2319
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
                                                # State 2320
                                                if len(subjects11) == 0:
                                                    pass
                                                    # State 2321
                                                    if len(subjects) == 0:
                                                        pass
                                                        # 6: v**m /; (cons_f2) and (cons_f3) and (cons_f5) and (cons_f52) and (cons_f51)
                                                        yield 6, subst2
                                    if len(subjects11) >= 1:
                                        tmp75 = subjects11.popleft()
                                        subst2 = Substitution(subst1)
                                        try:
                                            subst2.try_add_variable('i2.2.1.2', tmp75)
                                        except ValueError:
                                            pass
                                        else:
                                            pass
                                            if 'i2.2.1.2' not in subst2 or 'i2.2.1.1' not in subst2 or cons_f5(p=subst2["i2.2.1.2"], x=subst2["i2.2.1.1"]):
                                                pass
                                                if 'i2.2.1.2' not in subst2 or 'i2.2.1.2_1' not in subst2 or cons_f51(p=subst2["i2.2.1.2"], q=subst2["i2.2.1.2_1"]):
                                                    pass
                                                    # State 2320
                                                    if len(subjects11) == 0:
                                                        pass
                                                        # State 2321
                                                        if len(subjects) == 0:
                                                            pass
                                                            # 6: v**m /; (cons_f2) and (cons_f3) and (cons_f5) and (cons_f52) and (cons_f51)
                                                            yield 6, subst2
                                        subjects11.appendleft(tmp75)
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
                                                # State 2514
                                                if len(subjects11) == 0:
                                                    pass
                                                    # State 2515
                                                    if len(subjects) == 0:
                                                        pass
                                                        # 7: v**n /; (cons_f2) and (cons_f3) and (cons_f5) and (cons_f52) and (cons_f51)
                                                        yield 7, subst2
                                    if len(subjects11) >= 1:
                                        tmp78 = subjects11.popleft()
                                        subst2 = Substitution(subst1)
                                        try:
                                            subst2.try_add_variable('i2.2.1.2_1', tmp78)
                                        except ValueError:
                                            pass
                                        else:
                                            pass
                                            if 'i2.2.1.2_1' not in subst2 or 'i2.2.1.1' not in subst2 or cons_f52(q=subst2["i2.2.1.2_1"], x=subst2["i2.2.1.1"]):
                                                pass
                                                if 'i2.2.1.2' not in subst2 or 'i2.2.1.2_1' not in subst2 or cons_f51(p=subst2["i2.2.1.2"], q=subst2["i2.2.1.2_1"]):
                                                    pass
                                                    # State 2514
                                                    if len(subjects11) == 0:
                                                        pass
                                                        # State 2515
                                                        if len(subjects) == 0:
                                                            pass
                                                            # 7: v**n /; (cons_f2) and (cons_f3) and (cons_f5) and (cons_f52) and (cons_f51)
                                                            yield 7, subst2
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
                                        # State 2844
                                        if len(subjects11) == 0:
                                            pass
                                            # State 2845
                                            if len(subjects) == 0:
                                                pass
                                        subjects11.appendleft(tmp85)
                subjects11.appendleft(tmp12)
            subjects.appendleft(tmp10)
        return
        yield


from collections import deque