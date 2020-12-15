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


class CommutativeMatcher2328(CommutativeMatcher):
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
    6: (6, Multiset({8: 1, 9: 1}), [
      (VariableWithCount('i2.2.0', 1, 1, None), Add)
]),
    7: (7, Multiset({10: 1, 11: 1}), [
      (VariableWithCount('i2.2.0', 1, 1, None), Add)
]),
    8: (8, Multiset({12: 1, 13: 1}), [
      
]),
    9: (9, Multiset({14: 1, 15: 1, 16: 1}), [
      
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
        if CommutativeMatcher2328._instance is None:
            CommutativeMatcher2328._instance = CommutativeMatcher2328()
        return CommutativeMatcher2328._instance

    @staticmethod
    def get_match_iter(subject):
        subjects = deque([subject]) if subject is not None else deque()
        subst0 = Substitution()
        # State 2327
        subst1 = Substitution(subst0)
        try:
            subst1.try_add_variable('i2.2.1.0', S(1))
        except ValueError:
            pass
        else:
            pass
            # State 2329
            subst2 = Substitution(subst1)
            try:
                subst2.try_add_variable('i2.2.1.2', S(1))
            except ValueError:
                pass
            else:
                pass
                # State 2330
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
                                        # State 2331
                                        if len(subjects) == 0:
                                            pass
                                            # 0: a*v**m /; (cons_f2) and (cons_f3) and (cons_f4) and (cons_f5)
                                            yield 0, subst3
                                            # 1: a*v**m /; (cons_f2) and (cons_f3) and (cons_f4) and (cons_f5) and (cons_f6)
                                            yield 1, subst3
                            if 'i2.2' not in subst3 or 'i2.2.1.1' not in subst3 or cons_f5(p=subst3["i2.2"], x=subst3["i2.2.1.1"]):
                                pass
                                if 'i2.2.1.0_1' not in subst3 or 'i2.2.1.1' not in subst3 or cons_f3(b=subst3["i2.2.1.0_1"], x=subst3["i2.2.1.1"]):
                                    pass
                                    if 'i2.2.1.0' not in subst3 or 'i2.2.1.1' not in subst3 or cons_f8(c=subst3["i2.2.1.0"], x=subst3["i2.2.1.1"]):
                                        pass
                                        if 'i2.2.1.2_1' not in subst3 or 'i2.2.1.1' not in subst3 or cons_f4(n=subst3["i2.2.1.2_1"], x=subst3["i2.2.1.1"]):
                                            pass
                                            # State 2331
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
                                                # State 2331
                                                if len(subjects) == 0:
                                                    pass
                                                    # 14: a*v**m /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f5) and (cons_f52) and (cons_f54) and (cons_f51) and (cons_f53)
                                                    yield 14, subst3
                                        # State 2331
                                        if len(subjects) == 0:
                                            pass
                                            # 12: a*v**m /; (cons_f2) and (cons_f3) and (cons_f5) and (cons_f52) and (cons_f51)
                                            yield 12, subst3
                    subjects.appendleft(tmp3)
            if len(subjects) >= 1 and isinstance(subjects[0], Pow):
                tmp5 = subjects.popleft()
                subjects6 = deque(tmp5._args)
                # State 2332
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
                                        # State 2333
                                        subst3 = Substitution(subst2)
                                        try:
                                            subst3.try_add_variable('i2.2.1.2', 1)
                                        except ValueError:
                                            pass
                                        else:
                                            pass
                                            if 'i2.2.1.2' not in subst3 or 'i2.2.1.1' not in subst3 or cons_f4(n=subst3["i2.2.1.2"], x=subst3["i2.2.1.1"]):
                                                pass
                                                # State 2334
                                                if len(subjects6) == 0:
                                                    pass
                                                    # State 2335
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
                                                    # State 2334
                                                    if len(subjects6) == 0:
                                                        pass
                                                        # State 2335
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
                                            # State 2852
                                            if len(subjects6) == 0:
                                                pass
                                                # State 2853
                                                if len(subjects) == 0:
                                                    pass
                                            subjects6.appendleft(tmp14)
                                    if 'i2.2.1.0_1' not in subst2 or 'i2.2.1.1' not in subst2 or cons_f8(c=subst2["i2.2.1.0_1"], x=subst2["i2.2.1.1"]):
                                        pass
                                        # State 2333
                                        subst3 = Substitution(subst2)
                                        try:
                                            subst3.try_add_variable('i2.2.1.2', 1)
                                        except ValueError:
                                            pass
                                        else:
                                            pass
                                        if len(subjects6) >= 1:
                                            tmp16 = subjects6.popleft()
                                            subst3 = Substitution(subst2)
                                            try:
                                                subst3.try_add_variable('i2.2.1.2', tmp16)
                                            except ValueError:
                                                pass
                                            else:
                                                pass
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
                                                if 'i2.2.1.2' not in subst3 or 'i2.2.1.1' not in subst3 or cons_f4(n=subst3["i2.2.1.2"], x=subst3["i2.2.1.1"]):
                                                    pass
                                                    if 'i2.2.1.2' not in subst3 or 'i2.2.1.2_1' not in subst3 or cons_f48(n=subst3["i2.2.1.2"], n2=subst3["i2.2.1.2_1"]):
                                                        pass
                                                        # State 2895
                                                        if len(subjects6) == 0:
                                                            pass
                                                            # State 2896
                                                            if len(subjects) == 0:
                                                                pass
                                                                # 11: d*x**j /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f4) and (cons_f48) and (cons_f47)
                                                                yield 11, subst3
                                            subjects6.appendleft(tmp18)
                                        if len(subjects6) >= 1 and subjects6[0] == Integer(2):
                                            tmp20 = subjects6.popleft()
                                            # State 2852
                                            if len(subjects6) == 0:
                                                pass
                                                # State 2853
                                                if len(subjects) == 0:
                                                    pass
                                            subjects6.appendleft(tmp20)
                            if 'i2.2' not in subst2 or 'i2.2.1.1' not in subst2 or cons_f5(p=subst2["i2.2"], x=subst2["i2.2.1.1"]):
                                pass
                                if 'i2.2.1.0_1' not in subst2 or 'i2.2.1.1' not in subst2 or cons_f3(b=subst2["i2.2.1.0_1"], x=subst2["i2.2.1.1"]):
                                    pass
                                    if 'i2.2.1.0' not in subst2 or 'i2.2.1.1' not in subst2 or cons_f8(c=subst2["i2.2.1.0"], x=subst2["i2.2.1.1"]):
                                        pass
                                        if 'i2.2.1.2_1' not in subst2 or 'i2.2.1.1' not in subst2 or cons_f4(n=subst2["i2.2.1.2_1"], x=subst2["i2.2.1.1"]):
                                            pass
                                            # State 2333
                                            subst3 = Substitution(subst2)
                                            try:
                                                subst3.try_add_variable('i2.2.1.2', 1)
                                            except ValueError:
                                                pass
                                            else:
                                                pass
                                                if 'i2.2.1.2' not in subst3 or 'i2.2.1.2_1' not in subst3 or cons_f7(j=subst3["i2.2.1.2"], n=subst3["i2.2.1.2_1"]):
                                                    pass
                                                    # State 2334
                                                    if len(subjects6) == 0:
                                                        pass
                                                        # State 2335
                                                        if len(subjects) == 0:
                                                            pass
                                                            # 2: a*v**m /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f4) and (cons_f5) and (cons_f7)
                                                            yield 2, subst3
                                                            # 5: a*v**m /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f4) and (cons_f5) and (cons_f7) and (cons_f9)
                                                            yield 5, subst3
                                            if len(subjects6) >= 1:
                                                tmp22 = subjects6.popleft()
                                                subst3 = Substitution(subst2)
                                                try:
                                                    subst3.try_add_variable('i2.2.1.2', tmp22)
                                                except ValueError:
                                                    pass
                                                else:
                                                    pass
                                                    if 'i2.2.1.2' not in subst3 or 'i2.2.1.2_1' not in subst3 or cons_f7(j=subst3["i2.2.1.2"], n=subst3["i2.2.1.2_1"]):
                                                        pass
                                                        # State 2334
                                                        if len(subjects6) == 0:
                                                            pass
                                                            # State 2335
                                                            if len(subjects) == 0:
                                                                pass
                                                                # 2: a*v**m /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f4) and (cons_f5) and (cons_f7)
                                                                yield 2, subst3
                                                                # 5: a*v**m /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f4) and (cons_f5) and (cons_f7) and (cons_f9)
                                                                yield 5, subst3
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
                                                # State 2852
                                                if len(subjects6) == 0:
                                                    pass
                                                    # State 2853
                                                    if len(subjects) == 0:
                                                        pass
                                                subjects6.appendleft(tmp26)
                            if 'i2.2.1.0_1' not in subst2 or 'i2.2.1.1' not in subst2 or cons_f3(b=subst2["i2.2.1.0_1"], x=subst2["i2.2.1.1"]):
                                pass
                                if 'i2.2.1.0' not in subst2 or 'i2.2.1.1' not in subst2 or cons_f8(c=subst2["i2.2.1.0"], x=subst2["i2.2.1.1"]):
                                    pass
                                    # State 2333
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
                                        subjects6.appendleft(tmp30)
                                    if len(subjects6) >= 1 and subjects6[0] == Integer(2):
                                        tmp32 = subjects6.popleft()
                                        # State 2852
                                        if len(subjects6) == 0:
                                            pass
                                            # State 2853
                                            if len(subjects) == 0:
                                                pass
                                                # 8: c*x**2 /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f47)
                                                yield 8, subst2
                                        subjects6.appendleft(tmp32)
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
                                                # State 2333
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
                                                                # State 2334
                                                                if len(subjects6) == 0:
                                                                    pass
                                                                    # State 2335
                                                                    if len(subjects) == 0:
                                                                        pass
                                                                        # 14: a*v**m /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f5) and (cons_f52) and (cons_f54) and (cons_f51) and (cons_f53)
                                                                        yield 14, subst3
                                                if len(subjects6) >= 1:
                                                    tmp34 = subjects6.popleft()
                                                    subst3 = Substitution(subst2)
                                                    try:
                                                        subst3.try_add_variable('i2.2.1.2', tmp34)
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
                                                                    # State 2334
                                                                    if len(subjects6) == 0:
                                                                        pass
                                                                        # State 2335
                                                                        if len(subjects) == 0:
                                                                            pass
                                                                            # 14: a*v**m /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f5) and (cons_f52) and (cons_f54) and (cons_f51) and (cons_f53)
                                                                            yield 14, subst3
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
                                                    # State 2852
                                                    if len(subjects6) == 0:
                                                        pass
                                                        # State 2853
                                                        if len(subjects) == 0:
                                                            pass
                                                    subjects6.appendleft(tmp38)
                                        # State 2333
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
                                                    # State 2334
                                                    if len(subjects6) == 0:
                                                        pass
                                                        # State 2335
                                                        if len(subjects) == 0:
                                                            pass
                                                            # 12: a*v**m /; (cons_f2) and (cons_f3) and (cons_f5) and (cons_f52) and (cons_f51)
                                                            yield 12, subst3
                                        if len(subjects6) >= 1:
                                            tmp40 = subjects6.popleft()
                                            subst3 = Substitution(subst2)
                                            try:
                                                subst3.try_add_variable('i2.2.1.2', tmp40)
                                            except ValueError:
                                                pass
                                            else:
                                                pass
                                                if 'i2.2.1.2' not in subst3 or 'i2.2.1.1' not in subst3 or cons_f5(p=subst3["i2.2.1.2"], x=subst3["i2.2.1.1"]):
                                                    pass
                                                    if 'i2.2.1.2' not in subst3 or 'i2.2.1.2_1' not in subst3 or cons_f51(p=subst3["i2.2.1.2"], q=subst3["i2.2.1.2_1"]):
                                                        pass
                                                        # State 2334
                                                        if len(subjects6) == 0:
                                                            pass
                                                            # State 2335
                                                            if len(subjects) == 0:
                                                                pass
                                                                # 12: a*v**m /; (cons_f2) and (cons_f3) and (cons_f5) and (cons_f52) and (cons_f51)
                                                                yield 12, subst3
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
                                            # State 2852
                                            if len(subjects6) == 0:
                                                pass
                                                # State 2853
                                                if len(subjects) == 0:
                                                    pass
                                            subjects6.appendleft(tmp44)
                    subjects6.appendleft(tmp7)
                subjects.appendleft(tmp5)
        subst1 = Substitution(subst0)
        try:
            subst1.try_add_variable('i2.2.1.0_1', S(1))
        except ValueError:
            pass
        else:
            pass
            # State 2521
            subst2 = Substitution(subst1)
            try:
                subst2.try_add_variable('i2.2.1.2_1', S(1))
            except ValueError:
                pass
            else:
                pass
                # State 2522
                if len(subjects) >= 1:
                    tmp47 = subjects.popleft()
                    subst3 = Substitution(subst2)
                    try:
                        subst3.try_add_variable('i2.2.1.1', tmp47)
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
                                        # State 2523
                                        if len(subjects) == 0:
                                            pass
                                            # 10: b*v**n /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f4) and (cons_f48) and (cons_f47)
                                            yield 10, subst3
                            if 'i2.2' not in subst3 or 'i2.2.1.1' not in subst3 or cons_f5(p=subst3["i2.2"], x=subst3["i2.2.1.1"]):
                                pass
                                if 'i2.2.1.0_1' not in subst3 or 'i2.2.1.1' not in subst3 or cons_f3(b=subst3["i2.2.1.0_1"], x=subst3["i2.2.1.1"]):
                                    pass
                                    if 'i2.2.1.0' not in subst3 or 'i2.2.1.1' not in subst3 or cons_f8(c=subst3["i2.2.1.0"], x=subst3["i2.2.1.1"]):
                                        pass
                                        if 'i2.2.1.2_1' not in subst3 or 'i2.2.1.1' not in subst3 or cons_f4(n=subst3["i2.2.1.2_1"], x=subst3["i2.2.1.1"]):
                                            pass
                                            # State 2523
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
                                                # State 2523
                                                if len(subjects) == 0:
                                                    pass
                                                    # 15: b*v**n /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f5) and (cons_f52) and (cons_f54) and (cons_f51)
                                                    yield 15, subst3
                                        # State 2523
                                        if len(subjects) == 0:
                                            pass
                                            # 13: b*v**n /; (cons_f2) and (cons_f3) and (cons_f5) and (cons_f52) and (cons_f51)
                                            yield 13, subst3
                    subjects.appendleft(tmp47)
            if len(subjects) >= 1:
                tmp49 = subjects.popleft()
                subst2 = Substitution(subst1)
                try:
                    subst2.try_add_variable('i2.2.1.0', tmp49)
                except ValueError:
                    pass
                else:
                    pass
                    if 'i2' not in subst2 or 'i2.2.1.0' not in subst2 or cons_f10(v=subst2["i2.2.1.0"], x=subst2["i2"]):
                        pass
                        # State 2609
                        if len(subjects) == 0:
                            pass
                            # 6: v*a /; (cons_f2) and (cons_f10)
                            yield 6, subst2
                subjects.appendleft(tmp49)
            if len(subjects) >= 1:
                tmp51 = subjects.popleft()
                subst2 = Substitution(subst1)
                try:
                    subst2.try_add_variable('i2.2.1.1', tmp51)
                except ValueError:
                    pass
                else:
                    pass
                    if 'i2.2.0' not in subst2 or 'i2.2.1.1' not in subst2 or cons_f2(a=subst2["i2.2.0"], x=subst2["i2.2.1.1"]):
                        pass
                        if 'i2.2.1.0_1' not in subst2 or 'i2.2.1.1' not in subst2 or cons_f3(b=subst2["i2.2.1.0_1"], x=subst2["i2.2.1.1"]):
                            pass
                            if 'i2.2.1.0' not in subst2 or 'i2.2.1.1' not in subst2 or cons_f8(c=subst2["i2.2.1.0"], x=subst2["i2.2.1.1"]):
                                pass
                                # State 2857
                                if len(subjects) == 0:
                                    pass
                                    # 9: b*x /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f47)
                                    yield 9, subst2
                subjects.appendleft(tmp51)
            if len(subjects) >= 1 and isinstance(subjects[0], Pow):
                tmp53 = subjects.popleft()
                subjects54 = deque(tmp53._args)
                # State 2524
                if len(subjects54) >= 1:
                    tmp55 = subjects54.popleft()
                    subst2 = Substitution(subst1)
                    try:
                        subst2.try_add_variable('i2.2.1.1', tmp55)
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
                                        # State 2525
                                        subst3 = Substitution(subst2)
                                        try:
                                            subst3.try_add_variable('i2.2.1.2_1', 1)
                                        except ValueError:
                                            pass
                                        else:
                                            pass
                                            if 'i2.2.1.2' not in subst3 or 'i2.2.1.2_1' not in subst3 or cons_f48(n=subst3["i2.2.1.2"], n2=subst3["i2.2.1.2_1"]):
                                                pass
                                                # State 2526
                                                if len(subjects54) == 0:
                                                    pass
                                                    # State 2527
                                                    if len(subjects) == 0:
                                                        pass
                                                        # 10: b*v**n /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f4) and (cons_f48) and (cons_f47)
                                                        yield 10, subst3
                                        if len(subjects54) >= 1:
                                            tmp58 = subjects54.popleft()
                                            subst3 = Substitution(subst2)
                                            try:
                                                subst3.try_add_variable('i2.2.1.2_1', tmp58)
                                            except ValueError:
                                                pass
                                            else:
                                                pass
                                                if 'i2.2.1.2' not in subst3 or 'i2.2.1.2_1' not in subst3 or cons_f48(n=subst3["i2.2.1.2"], n2=subst3["i2.2.1.2_1"]):
                                                    pass
                                                    # State 2526
                                                    if len(subjects54) == 0:
                                                        pass
                                                        # State 2527
                                                        if len(subjects) == 0:
                                                            pass
                                                            # 10: b*v**n /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f4) and (cons_f48) and (cons_f47)
                                                            yield 10, subst3
                                            subjects54.appendleft(tmp58)
                            if 'i2.2' not in subst2 or 'i2.2.1.1' not in subst2 or cons_f5(p=subst2["i2.2"], x=subst2["i2.2.1.1"]):
                                pass
                                if 'i2.2.1.0_1' not in subst2 or 'i2.2.1.1' not in subst2 or cons_f3(b=subst2["i2.2.1.0_1"], x=subst2["i2.2.1.1"]):
                                    pass
                                    if 'i2.2.1.0' not in subst2 or 'i2.2.1.1' not in subst2 or cons_f8(c=subst2["i2.2.1.0"], x=subst2["i2.2.1.1"]):
                                        pass
                                        if 'i2.2.1.2_1' not in subst2 or 'i2.2.1.1' not in subst2 or cons_f4(n=subst2["i2.2.1.2_1"], x=subst2["i2.2.1.1"]):
                                            pass
                                            # State 2525
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
                                                        # State 2526
                                                        if len(subjects54) == 0:
                                                            pass
                                                            # State 2527
                                                            if len(subjects) == 0:
                                                                pass
                                                                # 3: b*v**n /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f4) and (cons_f5) and (cons_f7)
                                                                yield 3, subst3
                                                                # 4: b*v**n /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f4) and (cons_f5) and (cons_f7) and (cons_f6)
                                                                yield 4, subst3
                                            if len(subjects54) >= 1:
                                                tmp61 = subjects54.popleft()
                                                subst3 = Substitution(subst2)
                                                try:
                                                    subst3.try_add_variable('i2.2.1.2_1', tmp61)
                                                except ValueError:
                                                    pass
                                                else:
                                                    pass
                                                    if 'i2.2.1.2_1' not in subst3 or 'i2.2.1.1' not in subst3 or cons_f4(n=subst3["i2.2.1.2_1"], x=subst3["i2.2.1.1"]):
                                                        pass
                                                        if 'i2.2.1.2' not in subst3 or 'i2.2.1.2_1' not in subst3 or cons_f7(j=subst3["i2.2.1.2"], n=subst3["i2.2.1.2_1"]):
                                                            pass
                                                            # State 2526
                                                            if len(subjects54) == 0:
                                                                pass
                                                                # State 2527
                                                                if len(subjects) == 0:
                                                                    pass
                                                                    # 3: b*v**n /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f4) and (cons_f5) and (cons_f7)
                                                                    yield 3, subst3
                                                                    # 4: b*v**n /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f4) and (cons_f5) and (cons_f7) and (cons_f6)
                                                                    yield 4, subst3
                                                subjects54.appendleft(tmp61)
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
                                                # State 2525
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
                                                            # State 2526
                                                            if len(subjects54) == 0:
                                                                pass
                                                                # State 2527
                                                                if len(subjects) == 0:
                                                                    pass
                                                                    # 15: b*v**n /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f5) and (cons_f52) and (cons_f54) and (cons_f51)
                                                                    yield 15, subst3
                                                if len(subjects54) >= 1:
                                                    tmp64 = subjects54.popleft()
                                                    subst3 = Substitution(subst2)
                                                    try:
                                                        subst3.try_add_variable('i2.2.1.2_1', tmp64)
                                                    except ValueError:
                                                        pass
                                                    else:
                                                        pass
                                                        if 'i2.2.1.2_1' not in subst3 or 'i2.2.1.1' not in subst3 or cons_f52(q=subst3["i2.2.1.2_1"], x=subst3["i2.2.1.1"]):
                                                            pass
                                                            if 'i2.2.1.2' not in subst3 or 'i2.2.1.2_1' not in subst3 or cons_f51(p=subst3["i2.2.1.2"], q=subst3["i2.2.1.2_1"]):
                                                                pass
                                                                # State 2526
                                                                if len(subjects54) == 0:
                                                                    pass
                                                                    # State 2527
                                                                    if len(subjects) == 0:
                                                                        pass
                                                                        # 15: b*v**n /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f5) and (cons_f52) and (cons_f54) and (cons_f51)
                                                                        yield 15, subst3
                                                    subjects54.appendleft(tmp64)
                                        # State 2525
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
                                                    # State 2526
                                                    if len(subjects54) == 0:
                                                        pass
                                                        # State 2527
                                                        if len(subjects) == 0:
                                                            pass
                                                            # 13: b*v**n /; (cons_f2) and (cons_f3) and (cons_f5) and (cons_f52) and (cons_f51)
                                                            yield 13, subst3
                                        if len(subjects54) >= 1:
                                            tmp67 = subjects54.popleft()
                                            subst3 = Substitution(subst2)
                                            try:
                                                subst3.try_add_variable('i2.2.1.2_1', tmp67)
                                            except ValueError:
                                                pass
                                            else:
                                                pass
                                                if 'i2.2.1.2_1' not in subst3 or 'i2.2.1.1' not in subst3 or cons_f52(q=subst3["i2.2.1.2_1"], x=subst3["i2.2.1.1"]):
                                                    pass
                                                    if 'i2.2.1.2' not in subst3 or 'i2.2.1.2_1' not in subst3 or cons_f51(p=subst3["i2.2.1.2"], q=subst3["i2.2.1.2_1"]):
                                                        pass
                                                        # State 2526
                                                        if len(subjects54) == 0:
                                                            pass
                                                            # State 2527
                                                            if len(subjects) == 0:
                                                                pass
                                                                # 13: b*v**n /; (cons_f2) and (cons_f3) and (cons_f5) and (cons_f52) and (cons_f51)
                                                                yield 13, subst3
                                            subjects54.appendleft(tmp67)
                    subjects54.appendleft(tmp55)
                subjects.appendleft(tmp53)
        subst1 = Substitution(subst0)
        try:
            subst1.try_add_variable('i2.2.1.0_2', S(1))
        except ValueError:
            pass
        else:
            pass
            # State 2611
            if len(subjects) >= 1:
                tmp70 = subjects.popleft()
                subst2 = Substitution(subst1)
                try:
                    subst2.try_add_variable('i2.2.1.0', tmp70)
                except ValueError:
                    pass
                else:
                    pass
                    if 'i2' not in subst2 or 'i2.2.1.0' not in subst2 or cons_f10(v=subst2["i2.2.1.0"], x=subst2["i2"]):
                        pass
                        # State 2612
                        if len(subjects) == 0:
                            pass
                            # 7: v*b /; (cons_f3) and (cons_f10)
                            yield 7, subst2
                subjects.appendleft(tmp70)
            subst2 = Substitution(subst1)
            try:
                subst2.try_add_variable('i2.2.1.2_2', S(1))
            except ValueError:
                pass
            else:
                pass
                # State 2969
                if len(subjects) >= 1:
                    tmp73 = subjects.popleft()
                    subst3 = Substitution(subst2)
                    try:
                        subst3.try_add_variable('i2.2.1.1', tmp73)
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
                                                # State 2970
                                                if len(subjects) == 0:
                                                    pass
                                                    # 16: c*x**r /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f5) and (cons_f52) and (cons_f54) and (cons_f53)
                                                    yield 16, subst3
                    subjects.appendleft(tmp73)
            if len(subjects) >= 1 and isinstance(subjects[0], Pow):
                tmp75 = subjects.popleft()
                subjects76 = deque(tmp75._args)
                # State 2971
                if len(subjects76) >= 1:
                    tmp77 = subjects76.popleft()
                    subst2 = Substitution(subst1)
                    try:
                        subst2.try_add_variable('i2.2.1.1', tmp77)
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
                                                # State 2972
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
                                                            # State 2973
                                                            if len(subjects76) == 0:
                                                                pass
                                                                # State 2974
                                                                if len(subjects) == 0:
                                                                    pass
                                                                    # 16: c*x**r /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f5) and (cons_f52) and (cons_f54) and (cons_f53)
                                                                    yield 16, subst3
                                                if len(subjects76) >= 1:
                                                    tmp80 = subjects76.popleft()
                                                    subst3 = Substitution(subst2)
                                                    try:
                                                        subst3.try_add_variable('i2.2.1.2_2', tmp80)
                                                    except ValueError:
                                                        pass
                                                    else:
                                                        pass
                                                        if 'i2.2.1.2_2' not in subst3 or 'i2.2.1.1' not in subst3 or cons_f54(r=subst3["i2.2.1.2_2"], x=subst3["i2.2.1.1"]):
                                                            pass
                                                            if 'i2.2.1.2' not in subst3 or 'i2.2.1.2_2' not in subst3 or cons_f53(p=subst3["i2.2.1.2"], r=subst3["i2.2.1.2_2"]):
                                                                pass
                                                                # State 2973
                                                                if len(subjects76) == 0:
                                                                    pass
                                                                    # State 2974
                                                                    if len(subjects) == 0:
                                                                        pass
                                                                        # 16: c*x**r /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f5) and (cons_f52) and (cons_f54) and (cons_f53)
                                                                        yield 16, subst3
                                                    subjects76.appendleft(tmp80)
                    subjects76.appendleft(tmp77)
                subjects.appendleft(tmp75)
        if len(subjects) >= 1 and isinstance(subjects[0], Mul):
            tmp82 = subjects.popleft()
            associative1 = tmp82
            associative_type1 = type(tmp82)
            subjects83 = deque(tmp82._args)
            matcher = CommutativeMatcher2337.get()
            tmp84 = subjects83
            subjects83 = []
            for s in tmp84:
                matcher.add_subject(s)
            for pattern_index, subst1 in matcher.match(tmp84, subst0):
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
                                        # State 2344
                                        if len(subjects) == 0:
                                            pass
                                            # 1: a*v**m /; (cons_f2) and (cons_f3) and (cons_f4) and (cons_f5) and (cons_f6)
                                            yield 1, subst1
                                    # State 2344
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
                                                # State 2520
                                                if len(subjects) == 0:
                                                    pass
                                                    # 5: a*v**m /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f4) and (cons_f5) and (cons_f7) and (cons_f9)
                                                    yield 5, subst1
                                            # State 2520
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
                                                # State 2532
                                                if len(subjects) == 0:
                                                    pass
                                                    # 4: b*v**n /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f4) and (cons_f5) and (cons_f7) and (cons_f6)
                                                    yield 4, subst1
                                            # State 2532
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
                            # State 2610
                            if len(subjects) == 0:
                                pass
                                # 6: v*a /; (cons_f2) and (cons_f10)
                                yield 6, subst1
                if pattern_index == 4:
                    pass
                    if 'i2' not in subst1 or 'i2.2.1.0' not in subst1 or cons_f10(v=subst1["i2.2.1.0"], x=subst1["i2"]):
                        pass
                        if 'i2.2.1.0_2' not in subst1 or 'i2' not in subst1 or cons_f3(b=subst1["i2.2.1.0_2"], x=subst1["i2"]):
                            pass
                            # State 2613
                            if len(subjects) == 0:
                                pass
                                # 7: v*b /; (cons_f3) and (cons_f10)
                                yield 7, subst1
                if pattern_index == 5:
                    pass
                    if 'i2.2.0' not in subst1 or 'i2.2.1.1' not in subst1 or cons_f2(a=subst1["i2.2.0"], x=subst1["i2.2.1.1"]):
                        pass
                        if 'i2.2.1.0_1' not in subst1 or 'i2.2.1.1' not in subst1 or cons_f3(b=subst1["i2.2.1.0_1"], x=subst1["i2.2.1.1"]):
                            pass
                            if 'i2.2.1.0' not in subst1 or 'i2.2.1.1' not in subst1 or cons_f8(c=subst1["i2.2.1.0"], x=subst1["i2.2.1.1"]):
                                pass
                                if 'i2.2.1.0' not in subst1 or 'i2.2.1.0_1' not in subst1 or 'i2.2.0' not in subst1 or cons_f47(a=subst1["i2.2.0"], b=subst1["i2.2.1.0_1"], c=subst1["i2.2.1.0"]):
                                    pass
                                    # State 2856
                                    if len(subjects) == 0:
                                        pass
                                        # 8: c*x**2 /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f47)
                                        yield 8, subst1
                if pattern_index == 6:
                    pass
                    if 'i2.2.0' not in subst1 or 'i2.2.1.1' not in subst1 or cons_f2(a=subst1["i2.2.0"], x=subst1["i2.2.1.1"]):
                        pass
                        if 'i2.2.1.0_1' not in subst1 or 'i2.2.1.1' not in subst1 or cons_f3(b=subst1["i2.2.1.0_1"], x=subst1["i2.2.1.1"]):
                            pass
                            if 'i2.2.1.0' not in subst1 or 'i2.2.1.1' not in subst1 or cons_f8(c=subst1["i2.2.1.0"], x=subst1["i2.2.1.1"]):
                                pass
                                if 'i2.2.1.0' not in subst1 or 'i2.2.1.0_1' not in subst1 or 'i2.2.0' not in subst1 or cons_f47(a=subst1["i2.2.0"], b=subst1["i2.2.1.0_1"], c=subst1["i2.2.1.0"]):
                                    pass
                                    # State 2858
                                    if len(subjects) == 0:
                                        pass
                                        # 9: b*x /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f47)
                                        yield 9, subst1
                if pattern_index == 7:
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
                                            # State 2894
                                            if len(subjects) == 0:
                                                pass
                                                # 10: b*v**n /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f4) and (cons_f48) and (cons_f47)
                                                yield 10, subst1
                if pattern_index == 8:
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
                                            # State 2899
                                            if len(subjects) == 0:
                                                pass
                                                # 11: d*x**j /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f4) and (cons_f48) and (cons_f47)
                                                yield 11, subst1
                if pattern_index == 9:
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
                                        # State 2933
                                        if len(subjects) == 0:
                                            pass
                                            # 12: a*v**m /; (cons_f2) and (cons_f3) and (cons_f5) and (cons_f52) and (cons_f51)
                                            yield 12, subst1
                if pattern_index == 10:
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
                                        # State 2934
                                        if len(subjects) == 0:
                                            pass
                                            # 13: b*v**n /; (cons_f2) and (cons_f3) and (cons_f5) and (cons_f52) and (cons_f51)
                                            yield 13, subst1
                if pattern_index == 11:
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
                                                    # State 2967
                                                    if len(subjects) == 0:
                                                        pass
                                                        # 14: a*v**m /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f5) and (cons_f52) and (cons_f54) and (cons_f51) and (cons_f53)
                                                        yield 14, subst1
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
                                        if 'i2.2.1.0_2' not in subst1 or 'i2.2.1.1' not in subst1 or cons_f8(c=subst1["i2.2.1.0_2"], x=subst1["i2.2.1.1"]):
                                            pass
                                            if 'i2.2.1.2_2' not in subst1 or 'i2.2.1.1' not in subst1 or cons_f54(r=subst1["i2.2.1.2_2"], x=subst1["i2.2.1.1"]):
                                                pass
                                                # State 2968
                                                if len(subjects) == 0:
                                                    pass
                                                    # 15: b*v**n /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f5) and (cons_f52) and (cons_f54) and (cons_f51)
                                                    yield 15, subst1
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
                                    if 'i2.2.1.0_2' not in subst1 or 'i2.2.1.1' not in subst1 or cons_f8(c=subst1["i2.2.1.0_2"], x=subst1["i2.2.1.1"]):
                                        pass
                                        if 'i2.2.1.2_2' not in subst1 or 'i2.2.1.1' not in subst1 or cons_f54(r=subst1["i2.2.1.2_2"], x=subst1["i2.2.1.1"]):
                                            pass
                                            if 'i2.2.1.2' not in subst1 or 'i2.2.1.2_2' not in subst1 or cons_f53(p=subst1["i2.2.1.2"], r=subst1["i2.2.1.2_2"]):
                                                pass
                                                # State 2979
                                                if len(subjects) == 0:
                                                    pass
                                                    # 16: c*x**r /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f5) and (cons_f52) and (cons_f54) and (cons_f53)
                                                    yield 16, subst1
            subjects.appendleft(tmp82)
        return
        yield


from matchpy.matching.many_to_one import CommutativeMatcher
from .generated_part000005 import *
from matchpy.utils import VariableWithCount
from multiset import Multiset
from collections import deque