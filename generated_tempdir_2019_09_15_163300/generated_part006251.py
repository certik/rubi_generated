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


class CommutativeMatcher39256(CommutativeMatcher):
    _instance = None
    patterns = {
    0: (0, Multiset({0: 1}), [
      (VariableWithCount('i2.2.1.2.2.0', 1, 1, S(1)), Mul)
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
        if CommutativeMatcher39256._instance is None:
            CommutativeMatcher39256._instance = CommutativeMatcher39256()
        return CommutativeMatcher39256._instance

    @staticmethod
    def get_match_iter(subject):
        subjects = deque([subject]) if subject is not None else deque()
        subst0 = Substitution()
        # State 39255
        subst1 = Substitution(subst0)
        try:
            subst1.try_add_variable('i2.2.1.2.2.2', S(1))
        except ValueError:
            pass
        else:
            pass
            # State 39257
            subst2 = Substitution(subst1)
            try:
                subst2.try_add_variable('i2.2.1.2.2.2.0', S(0))
            except ValueError:
                pass
            else:
                pass
                # State 39258
                subst3 = Substitution(subst2)
                try:
                    subst3.try_add_variable('i2.2.1.2.2.2.1.0', S(1))
                except ValueError:
                    pass
                else:
                    pass
                    # State 39259
                    if len(subjects) >= 1 and isinstance(subjects[0], Pow):
                        tmp4 = subjects.popleft()
                        subjects5 = deque(tmp4._args)
                        # State 39260
                        if len(subjects5) >= 1:
                            tmp6 = subjects5.popleft()
                            subst4 = Substitution(subst3)
                            try:
                                subst4.try_add_variable('i2.2.1.1', tmp6)
                            except ValueError:
                                pass
                            else:
                                pass
                                # State 39261
                                if len(subjects5) >= 1:
                                    tmp8 = subjects5.popleft()
                                    subst5 = Substitution(subst4)
                                    try:
                                        subst5.try_add_variable('i2.2.1.2', tmp8)
                                    except ValueError:
                                        pass
                                    else:
                                        pass
                                        # State 39262
                                        if len(subjects5) == 0:
                                            pass
                                            # State 39263
                                            if len(subjects) == 0:
                                                pass
                                                # 0: (x**j*f + e)**p
                                                yield 0, subst5
                                    subjects5.appendleft(tmp8)
                            subjects5.appendleft(tmp6)
                        subjects.appendleft(tmp4)
                if len(subjects) >= 1 and isinstance(subjects[0], Mul):
                    tmp10 = subjects.popleft()
                    associative1 = tmp10
                    associative_type1 = type(tmp10)
                    subjects11 = deque(tmp10._args)
                    matcher = CommutativeMatcher39265.get()
                    tmp12 = subjects11
                    subjects11 = []
                    for s in tmp12:
                        matcher.add_subject(s)
                    for pattern_index, subst3 in matcher.match(tmp12, subst2):
                        pass
                        if pattern_index == 0:
                            pass
                            # State 39270
                            if len(subjects) == 0:
                                pass
                                # 0: (x**j*f + e)**p
                                yield 0, subst3
                    subjects.appendleft(tmp10)
            if len(subjects) >= 1 and isinstance(subjects[0], Add):
                tmp13 = subjects.popleft()
                associative1 = tmp13
                associative_type1 = type(tmp13)
                subjects14 = deque(tmp13._args)
                matcher = CommutativeMatcher39272.get()
                tmp15 = subjects14
                subjects14 = []
                for s in tmp15:
                    matcher.add_subject(s)
                for pattern_index, subst2 in matcher.match(tmp15, subst1):
                    pass
                    if pattern_index == 0:
                        pass
                        # State 39285
                        if len(subjects) == 0:
                            pass
                            # 0: (x**j*f + e)**p
                            yield 0, subst2
                subjects.appendleft(tmp13)
        if len(subjects) >= 1 and isinstance(subjects[0], Pow):
            tmp16 = subjects.popleft()
            subjects17 = deque(tmp16._args)
            # State 39286
            subst1 = Substitution(subst0)
            try:
                subst1.try_add_variable('i2.2.1.2.2.2.0', S(0))
            except ValueError:
                pass
            else:
                pass
                # State 39287
                subst2 = Substitution(subst1)
                try:
                    subst2.try_add_variable('i2.2.1.2.2.2.1.0', S(1))
                except ValueError:
                    pass
                else:
                    pass
                    # State 39288
                    if len(subjects17) >= 1 and isinstance(subjects17[0], Pow):
                        tmp20 = subjects17.popleft()
                        subjects21 = deque(tmp20._args)
                        # State 39289
                        if len(subjects21) >= 1:
                            tmp22 = subjects21.popleft()
                            subst3 = Substitution(subst2)
                            try:
                                subst3.try_add_variable('i2.2.1.1', tmp22)
                            except ValueError:
                                pass
                            else:
                                pass
                                # State 39290
                                if len(subjects21) >= 1:
                                    tmp24 = subjects21.popleft()
                                    subst4 = Substitution(subst3)
                                    try:
                                        subst4.try_add_variable('i2.2.1.2', tmp24)
                                    except ValueError:
                                        pass
                                    else:
                                        pass
                                        # State 39291
                                        if len(subjects21) == 0:
                                            pass
                                            # State 39292
                                            subst5 = Substitution(subst4)
                                            try:
                                                subst5.try_add_variable('i2.2.1.2.2.2', 1)
                                            except ValueError:
                                                pass
                                            else:
                                                pass
                                                # State 39293
                                                if len(subjects17) == 0:
                                                    pass
                                                    # State 39294
                                                    if len(subjects) == 0:
                                                        pass
                                                        # 0: (x**j*f + e)**p
                                                        yield 0, subst5
                                            if len(subjects17) >= 1:
                                                tmp27 = subjects17.popleft()
                                                subst5 = Substitution(subst4)
                                                try:
                                                    subst5.try_add_variable('i2.2.1.2.2.2', tmp27)
                                                except ValueError:
                                                    pass
                                                else:
                                                    pass
                                                    # State 39293
                                                    if len(subjects17) == 0:
                                                        pass
                                                        # State 39294
                                                        if len(subjects) == 0:
                                                            pass
                                                            # 0: (x**j*f + e)**p
                                                            yield 0, subst5
                                                subjects17.appendleft(tmp27)
                                    subjects21.appendleft(tmp24)
                            subjects21.appendleft(tmp22)
                        subjects17.appendleft(tmp20)
                if len(subjects17) >= 1 and isinstance(subjects17[0], Mul):
                    tmp29 = subjects17.popleft()
                    associative1 = tmp29
                    associative_type1 = type(tmp29)
                    subjects30 = deque(tmp29._args)
                    matcher = CommutativeMatcher39296.get()
                    tmp31 = subjects30
                    subjects30 = []
                    for s in tmp31:
                        matcher.add_subject(s)
                    for pattern_index, subst2 in matcher.match(tmp31, subst1):
                        pass
                        if pattern_index == 0:
                            pass
                            # State 39301
                            subst3 = Substitution(subst2)
                            try:
                                subst3.try_add_variable('i2.2.1.2.2.2', 1)
                            except ValueError:
                                pass
                            else:
                                pass
                                # State 39302
                                if len(subjects17) == 0:
                                    pass
                                    # State 39303
                                    if len(subjects) == 0:
                                        pass
                                        # 0: (x**j*f + e)**p
                                        yield 0, subst3
                            if len(subjects17) >= 1:
                                tmp33 = []
                                tmp33.append(subjects17.popleft())
                                while True:
                                    if len(tmp33) > 1:
                                        tmp34 = create_operation_expression(associative1, tmp33)
                                    elif len(tmp33) == 1:
                                        tmp34 = tmp33[0]
                                    else:
                                        assert False, "Unreachable"
                                    subst3 = Substitution(subst2)
                                    try:
                                        subst3.try_add_variable('i2.2.1.2.2.2', tmp34)
                                    except ValueError:
                                        pass
                                    else:
                                        pass
                                        # State 39302
                                        if len(subjects17) == 0:
                                            pass
                                            # State 39303
                                            if len(subjects) == 0:
                                                pass
                                                # 0: (x**j*f + e)**p
                                                yield 0, subst3
                                    if len(subjects17) == 0:
                                        break
                                    tmp33.append(subjects17.popleft())
                                subjects17.extendleft(reversed(tmp33))
                    subjects17.appendleft(tmp29)
            if len(subjects17) >= 1 and isinstance(subjects17[0], Add):
                tmp36 = subjects17.popleft()
                associative1 = tmp36
                associative_type1 = type(tmp36)
                subjects37 = deque(tmp36._args)
                matcher = CommutativeMatcher39305.get()
                tmp38 = subjects37
                subjects37 = []
                for s in tmp38:
                    matcher.add_subject(s)
                for pattern_index, subst1 in matcher.match(tmp38, subst0):
                    pass
                    if pattern_index == 0:
                        pass
                        # State 39318
                        subst2 = Substitution(subst1)
                        try:
                            subst2.try_add_variable('i2.2.1.2.2.2', 1)
                        except ValueError:
                            pass
                        else:
                            pass
                            # State 39319
                            if len(subjects17) == 0:
                                pass
                                # State 39320
                                if len(subjects) == 0:
                                    pass
                                    # 0: (x**j*f + e)**p
                                    yield 0, subst2
                        if len(subjects17) >= 1:
                            tmp40 = []
                            tmp40.append(subjects17.popleft())
                            while True:
                                if len(tmp40) > 1:
                                    tmp41 = create_operation_expression(associative1, tmp40)
                                elif len(tmp40) == 1:
                                    tmp41 = tmp40[0]
                                else:
                                    assert False, "Unreachable"
                                subst2 = Substitution(subst1)
                                try:
                                    subst2.try_add_variable('i2.2.1.2.2.2', tmp41)
                                except ValueError:
                                    pass
                                else:
                                    pass
                                    # State 39319
                                    if len(subjects17) == 0:
                                        pass
                                        # State 39320
                                        if len(subjects) == 0:
                                            pass
                                            # 0: (x**j*f + e)**p
                                            yield 0, subst2
                                if len(subjects17) == 0:
                                    break
                                tmp40.append(subjects17.popleft())
                            subjects17.extendleft(reversed(tmp40))
                subjects17.appendleft(tmp36)
            subjects.appendleft(tmp16)
        return
        yield


from .generated_part006253 import *
from matchpy.matching.many_to_one import CommutativeMatcher
from collections import deque
from .generated_part006256 import *
from .generated_part006255 import *
from matchpy.utils import VariableWithCount
from multiset import Multiset
from .generated_part006252 import *