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


class CommutativeMatcher2728(CommutativeMatcher):
    _instance = None
    patterns = {
    0: (0, Multiset({0: 1}), [
      (VariableWithCount('i2.2.0_1', 1, 1, None), Add)
]),
    1: (1, Multiset({1: 1}), [
      (VariableWithCount('i2.2.0_1', 1, 1, None), Add)
]),
    2: (2, Multiset({2: 1}), [
      (VariableWithCount('i2.2.0_1', 1, 1, None), Add)
])
}
    subjects = {}
    subjects_by_id = {}
    bipartite = BipartiteGraph()
    associative = Add
    max_optional_count = 0
    anonymous_patterns = set()

    def __init__(self):
        self.add_subject(None)

    @staticmethod
    def get():
        if CommutativeMatcher2728._instance is None:
            CommutativeMatcher2728._instance = CommutativeMatcher2728()
        return CommutativeMatcher2728._instance

    @staticmethod
    def get_match_iter(subject):
        subjects = deque([subject]) if subject is not None else deque()
        subst0 = Substitution()
        # State 2727
        subst1 = Substitution(subst0)
        try:
            subst1.try_add_variable('i2.2.1.0_2', S(1))
        except ValueError:
            pass
        else:
            pass
            # State 2729
            if len(subjects) >= 1:
                tmp2 = subjects.popleft()
                subst2 = Substitution(subst1)
                try:
                    subst2.try_add_variable('i2.2.1.0', tmp2)
                except ValueError:
                    pass
                else:
                    pass
                    # State 2730
                    if len(subjects) == 0:
                        pass
                        # 0: v*b /; (cons_f29) and (cons_f27) and (cons_f28)
                        yield 0, subst2
                subjects.appendleft(tmp2)
        subst1 = Substitution(subst0)
        try:
            subst1.try_add_variable('i2.2.1.0_1', S(1))
        except ValueError:
            pass
        else:
            pass
            # State 2797
            subst2 = Substitution(subst1)
            try:
                subst2.try_add_variable('i2.2.1.2_1', S(1))
            except ValueError:
                pass
            else:
                pass
                # State 2798
                if len(subjects) >= 1:
                    tmp6 = subjects.popleft()
                    subst3 = Substitution(subst2)
                    try:
                        subst3.try_add_variable('i2.2.1.1', tmp6)
                    except ValueError:
                        pass
                    else:
                        pass
                        if 'i2.2.0' not in subst3 or 'i2.2.1.1' not in subst3 or cons_f2(a=subst3["i2.2.0"], x=subst3["i2.2.1.1"]):
                            pass
                            if 'i2.2.1.0' not in subst3 or 'i2.2.1.1' not in subst3 or cons_f3(b=subst3["i2.2.1.0"], x=subst3["i2.2.1.1"]):
                                pass
                                if 'i2.2.0_1' not in subst3 or 'i2.2.1.1' not in subst3 or cons_f8(c=subst3["i2.2.0_1"], x=subst3["i2.2.1.1"]):
                                    pass
                                    if 'i2.2.1.0_1' not in subst3 or 'i2.2.1.1' not in subst3 or cons_f29(d=subst3["i2.2.1.0_1"], x=subst3["i2.2.1.1"]):
                                        pass
                                        if 'i2.2' not in subst3 or 'i2.2.1.1' not in subst3 or cons_f19(m=subst3["i2.2"], x=subst3["i2.2.1.1"]):
                                            pass
                                            if 'i2.2.1.2' not in subst3 or 'i2.2.1.1' not in subst3 or cons_f4(n=subst3["i2.2.1.2"], x=subst3["i2.2.1.1"]):
                                                pass
                                                # State 2799
                                                if len(subjects) == 0:
                                                    pass
                                                    # 1: b*v**n /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f19) and (cons_f4) and (cons_f39) and (cons_f41)
                                                    yield 1, subst3
                        if 'i2.2.0_1' not in subst3 or 'i2.2.1.1' not in subst3 or cons_f2(a=subst3["i2.2.0_1"], x=subst3["i2.2.1.1"]):
                            pass
                            if 'i2.2.1.0_1' not in subst3 or 'i2.2.1.1' not in subst3 or cons_f3(b=subst3["i2.2.1.0_1"], x=subst3["i2.2.1.1"]):
                                pass
                                if 'i2.2.0' not in subst3 or 'i2.2.1.1' not in subst3 or cons_f8(c=subst3["i2.2.0"], x=subst3["i2.2.1.1"]):
                                    pass
                                    if 'i2.2.1.0' not in subst3 or 'i2.2.1.1' not in subst3 or cons_f29(d=subst3["i2.2.1.0"], x=subst3["i2.2.1.1"]):
                                        pass
                                        if 'i2.2_1' not in subst3 or 'i2.2.1.1' not in subst3 or cons_f19(m=subst3["i2.2_1"], x=subst3["i2.2.1.1"]):
                                            pass
                                            if 'i2.2.1.2_1' not in subst3 or 'i2.2.1.1' not in subst3 or cons_f4(n=subst3["i2.2.1.2_1"], x=subst3["i2.2.1.1"]):
                                                pass
                                                if 'i2.2' not in subst3 or 'i2.2.1.1' not in subst3 or cons_f5(p=subst3["i2.2"], x=subst3["i2.2.1.1"]):
                                                    pass
                                                    # State 2799
                                                    if len(subjects) == 0:
                                                        pass
                                                        # 2: b*v**n /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f19) and (cons_f4) and (cons_f5) and (cons_f7) and (cons_f44)
                                                        yield 2, subst3
                    subjects.appendleft(tmp6)
            if len(subjects) >= 1 and isinstance(subjects[0], Pow):
                tmp8 = subjects.popleft()
                subjects9 = deque(tmp8._args)
                # State 2800
                if len(subjects9) >= 1:
                    tmp10 = subjects9.popleft()
                    subst2 = Substitution(subst1)
                    try:
                        subst2.try_add_variable('i2.2.1.1', tmp10)
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
                                                # State 2801
                                                subst3 = Substitution(subst2)
                                                try:
                                                    subst3.try_add_variable('i2.2.1.2_1', 1)
                                                except ValueError:
                                                    pass
                                                else:
                                                    pass
                                                    if 'i2.2.1.2' not in subst3 or 'i2.2.1.2_1' not in subst3 or cons_f39(n=subst3["i2.2.1.2"], q=subst3["i2.2.1.2_1"]):
                                                        pass
                                                        # State 2802
                                                        if len(subjects9) == 0:
                                                            pass
                                                            # State 2803
                                                            if len(subjects) == 0:
                                                                pass
                                                                # 1: b*v**n /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f19) and (cons_f4) and (cons_f39) and (cons_f41)
                                                                yield 1, subst3
                                                if len(subjects9) >= 1:
                                                    tmp13 = subjects9.popleft()
                                                    subst3 = Substitution(subst2)
                                                    try:
                                                        subst3.try_add_variable('i2.2.1.2_1', tmp13)
                                                    except ValueError:
                                                        pass
                                                    else:
                                                        pass
                                                        if 'i2.2.1.2' not in subst3 or 'i2.2.1.2_1' not in subst3 or cons_f39(n=subst3["i2.2.1.2"], q=subst3["i2.2.1.2_1"]):
                                                            pass
                                                            # State 2802
                                                            if len(subjects9) == 0:
                                                                pass
                                                                # State 2803
                                                                if len(subjects) == 0:
                                                                    pass
                                                                    # 1: b*v**n /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f19) and (cons_f4) and (cons_f39) and (cons_f41)
                                                                    yield 1, subst3
                                                    subjects9.appendleft(tmp13)
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
                                                    # State 2801
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
                                                                # State 2802
                                                                if len(subjects9) == 0:
                                                                    pass
                                                                    # State 2803
                                                                    if len(subjects) == 0:
                                                                        pass
                                                                        # 2: b*v**n /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f19) and (cons_f4) and (cons_f5) and (cons_f7) and (cons_f44)
                                                                        yield 2, subst3
                                                    if len(subjects9) >= 1:
                                                        tmp16 = subjects9.popleft()
                                                        subst3 = Substitution(subst2)
                                                        try:
                                                            subst3.try_add_variable('i2.2.1.2_1', tmp16)
                                                        except ValueError:
                                                            pass
                                                        else:
                                                            pass
                                                            if 'i2.2.1.2_1' not in subst3 or 'i2.2.1.1' not in subst3 or cons_f4(n=subst3["i2.2.1.2_1"], x=subst3["i2.2.1.1"]):
                                                                pass
                                                                if 'i2.2.1.2' not in subst3 or 'i2.2.1.2_1' not in subst3 or cons_f7(j=subst3["i2.2.1.2"], n=subst3["i2.2.1.2_1"]):
                                                                    pass
                                                                    # State 2802
                                                                    if len(subjects9) == 0:
                                                                        pass
                                                                        # State 2803
                                                                        if len(subjects) == 0:
                                                                            pass
                                                                            # 2: b*v**n /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f19) and (cons_f4) and (cons_f5) and (cons_f7) and (cons_f44)
                                                                            yield 2, subst3
                                                        subjects9.appendleft(tmp16)
                    subjects9.appendleft(tmp10)
                subjects.appendleft(tmp8)
        if len(subjects) >= 1 and isinstance(subjects[0], Mul):
            tmp18 = subjects.popleft()
            associative1 = tmp18
            associative_type1 = type(tmp18)
            subjects19 = deque(tmp18._args)
            matcher = CommutativeMatcher2732.get()
            tmp20 = subjects19
            subjects19 = []
            for s in tmp20:
                matcher.add_subject(s)
            for pattern_index, subst1 in matcher.match(tmp20, subst0):
                pass
                if pattern_index == 0:
                    pass
                    if 'i2.2.1.0_2' not in subst1 or 'i2' not in subst1 or cons_f29(d=subst1["i2.2.1.0_2"], x=subst1["i2"]):
                        pass
                        if 'i2.2.1.0_2' not in subst1 or 'i2.2.1.0_1' not in subst1 or 'i2.2.0' not in subst1 or 'i2.2.0_1' not in subst1 or cons_f27(a=subst1["i2.2.0"], b=subst1["i2.2.1.0_1"], c=subst1["i2.2.0_1"], d=subst1["i2.2.1.0_2"]):
                            pass
                            if 'i2' not in subst1 or 'i2.2.1.0_2' not in subst1 or 'i2.2.0_1' not in subst1 or 'i2.2.0' not in subst1 or 'i2.2_1' not in subst1 or 'i2.2.1.0_1' not in subst1 or cons_f28(a=subst1["i2.2.0"], b=subst1["i2.2.1.0_1"], c=subst1["i2.2.0_1"], d=subst1["i2.2.1.0_2"], n=subst1["i2.2_1"], x=subst1["i2"]):
                                pass
                                # State 2733
                                if len(subjects) == 0:
                                    pass
                                    # 0: v*b /; (cons_f29) and (cons_f27) and (cons_f28)
                                    yield 0, subst1
                if pattern_index == 1:
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
                                            if 'i2.2.1.2' not in subst1 or 'i2.2.1.2_1' not in subst1 or cons_f39(n=subst1["i2.2.1.2"], q=subst1["i2.2.1.2_1"]):
                                                pass
                                                if 'i2.2.1.0_1' not in subst1 or 'i2.2.1.0' not in subst1 or 'i2.2.0' not in subst1 or 'i2.2.0_1' not in subst1 or cons_f41(a=subst1["i2.2.0"], b=subst1["i2.2.1.0"], c=subst1["i2.2.0_1"], d=subst1["i2.2.1.0_1"]):
                                                    pass
                                                    # State 2810
                                                    if len(subjects) == 0:
                                                        pass
                                                        # 1: b*v**n /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f19) and (cons_f4) and (cons_f39) and (cons_f41)
                                                        yield 1, subst1
                if pattern_index == 2:
                    pass
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
                                                if 'i2.2.1.2' not in subst1 or 'i2.2.1.2_1' not in subst1 or cons_f7(j=subst1["i2.2.1.2"], n=subst1["i2.2.1.2_1"]):
                                                    pass
                                                    if 'i2.2.0' not in subst1 or 'i2.2.0_1' not in subst1 or 'i2.2.1.0_1' not in subst1 or 'i2.2.1.0' not in subst1 or cons_f44(a=subst1["i2.2.0_1"], b=subst1["i2.2.1.0_1"], c=subst1["i2.2.0"], d=subst1["i2.2.1.0"]):
                                                        pass
                                                        # State 2819
                                                        if len(subjects) == 0:
                                                            pass
                                                            # 2: b*v**n /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f19) and (cons_f4) and (cons_f5) and (cons_f7) and (cons_f44)
                                                            yield 2, subst1
            subjects.appendleft(tmp18)
        return
        yield


from matchpy.matching.many_to_one import CommutativeMatcher
from .generated_part000013 import *
from matchpy.utils import VariableWithCount
from multiset import Multiset
from collections import deque