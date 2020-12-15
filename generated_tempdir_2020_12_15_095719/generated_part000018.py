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


class CommutativeMatcher2651(CommutativeMatcher):
    _instance = None
    patterns = {
    0: (0, Multiset({0: 1}), [
      (VariableWithCount('i2.1.0', 1, 1, None), Add)
]),
    1: (1, Multiset({1: 1, 2: 1}), [
      
]),
    2: (2, Multiset({3: 1, 4: 1}), [
      (VariableWithCount('i2.1.0', 1, 1, S(0)), Add)
]),
    3: (3, Multiset({5: 1}), [
      (VariableWithCount('i2.1.0', 1, 1, None), Add)
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
        if CommutativeMatcher2651._instance is None:
            CommutativeMatcher2651._instance = CommutativeMatcher2651()
        return CommutativeMatcher2651._instance

    @staticmethod
    def get_match_iter(subject):
        subjects = deque([subject]) if subject is not None else deque()
        subst0 = Substitution()
        # State 2650
        subst1 = Substitution(subst0)
        try:
            subst1.try_add_variable('i2.1.1.0_1', S(1))
        except ValueError:
            pass
        else:
            pass
            # State 2652
            if len(subjects) >= 1:
                tmp2 = subjects.popleft()
                subst2 = Substitution(subst1)
                try:
                    subst2.try_add_variable('i2.1.1.0', tmp2)
                except ValueError:
                    pass
                else:
                    pass
                    if 'i2.1.1.0' not in subst2 or 'i2.0' not in subst2 or cons_f2(a=subst2["i2.0"], x=subst2["i2.1.1.0"]):
                        pass
                        if 'i2.1.1.0' not in subst2 or 'i2.1.0' not in subst2 or cons_f3(b=subst2["i2.1.0"], x=subst2["i2.1.1.0"]):
                            pass
                            if 'i2.1.1.0_1' not in subst2 or 'i2.1.1.0' not in subst2 or cons_f8(c=subst2["i2.1.1.0_1"], x=subst2["i2.1.1.0"]):
                                pass
                                if 'i2.1.0' not in subst2 or 'i2.1.1.0_1' not in subst2 or 'i2.1.1.0' not in subst2 or 'i2.0' not in subst2 or cons_f14(a=subst2["i2.0"], b=subst2["i2.1.0"], c=subst2["i2.1.1.0_1"], x=subst2["i2.1.1.0"]):
                                    pass
                                    # State 2653
                                    if len(subjects) == 0:
                                        pass
                                        # 0: x*c /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f14)
                                        yield 0, subst2
                subjects.appendleft(tmp2)
            if len(subjects) >= 1:
                tmp4 = subjects.popleft()
                subst2 = Substitution(subst1)
                try:
                    subst2.try_add_variable('i2.2.0', tmp4)
                except ValueError:
                    pass
                else:
                    pass
                    # State 2769
                    if len(subjects) == 0:
                        pass
                        # 2: b*v /; (cons_f3)
                        yield 2, subst2
                subjects.appendleft(tmp4)
            if len(subjects) >= 1:
                tmp6 = subjects.popleft()
                subst2 = Substitution(subst1)
                try:
                    subst2.try_add_variable('i2.2.1.0', tmp6)
                except ValueError:
                    pass
                else:
                    pass
                    # State 2785
                    if len(subjects) == 0:
                        pass
                        # 4: B*v /; (cons_f37) and (cons_f35)
                        yield 4, subst2
                subjects.appendleft(tmp6)
        subst1 = Substitution(subst0)
        try:
            subst1.try_add_variable('i2.1.1.0', S(1))
        except ValueError:
            pass
        else:
            pass
            # State 2759
            if len(subjects) >= 1 and isinstance(subjects[0], Pow):
                tmp9 = subjects.popleft()
                subjects10 = deque(tmp9._args)
                # State 2760
                if len(subjects10) >= 1:
                    tmp11 = subjects10.popleft()
                    subst2 = Substitution(subst1)
                    try:
                        subst2.try_add_variable('i2.2.0', tmp11)
                    except ValueError:
                        pass
                    else:
                        pass
                        # State 2761
                        if len(subjects10) >= 1 and subjects10[0] == Integer(2):
                            tmp13 = subjects10.popleft()
                            # State 2762
                            if len(subjects10) == 0:
                                pass
                                # State 2763
                                if len(subjects) == 0:
                                    pass
                                    # 1: c*v**2 /; (cons_f8)
                                    yield 1, subst2
                            subjects10.appendleft(tmp13)
                    subjects10.appendleft(tmp11)
                if len(subjects10) >= 1:
                    tmp14 = subjects10.popleft()
                    subst2 = Substitution(subst1)
                    try:
                        subst2.try_add_variable('i2.2.1.0', tmp14)
                    except ValueError:
                        pass
                    else:
                        pass
                        # State 2778
                        if len(subjects10) >= 1 and subjects10[0] == Integer(2):
                            tmp16 = subjects10.popleft()
                            # State 2779
                            if len(subjects10) == 0:
                                pass
                                # State 2780
                                if len(subjects) == 0:
                                    pass
                                    # 3: C*v**2 /; (cons_f38) and (cons_f35)
                                    yield 3, subst2
                            subjects10.appendleft(tmp16)
                    subjects10.appendleft(tmp14)
                subjects.appendleft(tmp9)
            if len(subjects) >= 1:
                tmp17 = subjects.popleft()
                subst2 = Substitution(subst1)
                try:
                    subst2.try_add_variable('i2.2.1.1', tmp17)
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
                                if 'i2.1.0' not in subst2 or 'i2.2.1.1' not in subst2 or cons_f29(d=subst2["i2.1.0"], x=subst2["i2.2.1.1"]):
                                    pass
                                    if 'i2.1.1.0' not in subst2 or 'i2.2.1.1' not in subst2 or cons_f50(e=subst2["i2.1.1.0"], x=subst2["i2.2.1.1"]):
                                        pass
                                        if 'i2.2' not in subst2 or 'i2.2.1.1' not in subst2 or cons_f5(p=subst2["i2.2"], x=subst2["i2.2.1.1"]):
                                            pass
                                            # State 2922
                                            if len(subjects) == 0:
                                                pass
                                                # 5: e*x /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f50) and (cons_f5) and (cons_f49)
                                                yield 5, subst2
                subjects.appendleft(tmp17)
        if len(subjects) >= 1 and isinstance(subjects[0], Mul):
            tmp19 = subjects.popleft()
            associative1 = tmp19
            associative_type1 = type(tmp19)
            subjects20 = deque(tmp19._args)
            matcher = CommutativeMatcher2655.get()
            tmp21 = subjects20
            subjects20 = []
            for s in tmp21:
                matcher.add_subject(s)
            for pattern_index, subst1 in matcher.match(tmp21, subst0):
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
                                    # State 2656
                                    if len(subjects) == 0:
                                        pass
                                        # 0: x*c /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f14)
                                        yield 0, subst1
                if pattern_index == 1:
                    pass
                    if 'i2' not in subst1 or 'i2.1.1.0' not in subst1 or cons_f8(c=subst1["i2.1.1.0"], x=subst1["i2"]):
                        pass
                        # State 2768
                        if len(subjects) == 0:
                            pass
                            # 1: c*v**2 /; (cons_f8)
                            yield 1, subst1
                if pattern_index == 2:
                    pass
                    if 'i2.1.1.0_1' not in subst1 or 'i2' not in subst1 or cons_f3(b=subst1["i2.1.1.0_1"], x=subst1["i2"]):
                        pass
                        # State 2770
                        if len(subjects) == 0:
                            pass
                            # 2: b*v /; (cons_f3)
                            yield 2, subst1
                if pattern_index == 3:
                    pass
                    if 'i2' not in subst1 or 'i2.1.1.0' not in subst1 or cons_f38(C=subst1["i2.1.1.0"], x=subst1["i2"]):
                        pass
                        if 'i2.1.0' not in subst1 or 'i2.2.0' not in subst1 or 'i2.1.1.0_1' not in subst1 or 'i2.1.1.0' not in subst1 or 'i2.2.1.0_1' not in subst1 or cons_f35(A=subst1["i2.1.0"], B=subst1["i2.1.1.0_1"], C=subst1["i2.1.1.0"], a=subst1["i2.2.0"], b=subst1["i2.2.1.0_1"]):
                            pass
                            # State 2784
                            if len(subjects) == 0:
                                pass
                                # 3: C*v**2 /; (cons_f38) and (cons_f35)
                                yield 3, subst1
                if pattern_index == 4:
                    pass
                    if 'i2.1.0' not in subst1 or 'i2.2.0' not in subst1 or 'i2.1.1.0_1' not in subst1 or 'i2.1.1.0' not in subst1 or 'i2.2.1.0_1' not in subst1 or cons_f35(A=subst1["i2.1.0"], B=subst1["i2.1.1.0_1"], C=subst1["i2.1.1.0"], a=subst1["i2.2.0"], b=subst1["i2.2.1.0_1"]):
                        pass
                        if 'i2.1.1.0_1' not in subst1 or 'i2' not in subst1 or cons_f37(B=subst1["i2.1.1.0_1"], x=subst1["i2"]):
                            pass
                            # State 2786
                            if len(subjects) == 0:
                                pass
                                # 4: B*v /; (cons_f37) and (cons_f35)
                                yield 4, subst1
                if pattern_index == 5:
                    pass
                    if 'i2.2.0' not in subst1 or 'i2.2.1.1' not in subst1 or cons_f2(a=subst1["i2.2.0"], x=subst1["i2.2.1.1"]):
                        pass
                        if 'i2.2.1.0_1' not in subst1 or 'i2.2.1.1' not in subst1 or cons_f3(b=subst1["i2.2.1.0_1"], x=subst1["i2.2.1.1"]):
                            pass
                            if 'i2.2.1.0' not in subst1 or 'i2.2.1.1' not in subst1 or cons_f8(c=subst1["i2.2.1.0"], x=subst1["i2.2.1.1"]):
                                pass
                                if 'i2.1.0' not in subst1 or 'i2.2.1.1' not in subst1 or cons_f29(d=subst1["i2.1.0"], x=subst1["i2.2.1.1"]):
                                    pass
                                    if 'i2.1.1.0' not in subst1 or 'i2.2.1.1' not in subst1 or cons_f50(e=subst1["i2.1.1.0"], x=subst1["i2.2.1.1"]):
                                        pass
                                        if 'i2.2' not in subst1 or 'i2.2.1.1' not in subst1 or cons_f5(p=subst1["i2.2"], x=subst1["i2.2.1.1"]):
                                            pass
                                            if 'i2.2.1.0' not in subst1 or 'i2.2.1.0_1' not in subst1 or 'i2.1.0' not in subst1 or 'i2.1.1.0' not in subst1 or cons_f49(b=subst1["i2.2.1.0_1"], c=subst1["i2.2.1.0"], d=subst1["i2.1.0"], e=subst1["i2.1.1.0"]):
                                                pass
                                                # State 2923
                                                if len(subjects) == 0:
                                                    pass
                                                    # 5: e*x /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f50) and (cons_f5) and (cons_f49)
                                                    yield 5, subst1
            subjects.appendleft(tmp19)
        return
        yield


from matchpy.matching.many_to_one import CommutativeMatcher
from .generated_part000019 import *
from matchpy.utils import VariableWithCount
from multiset import Multiset
from collections import deque