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


class CommutativeMatcher40740(CommutativeMatcher):
    _instance = None
    patterns = {
    0: (0, Multiset({0: 1}), [
      (VariableWithCount('i2.2.1.2.0', 1, 1, S(1)), Mul)
]),
    1: (1, Multiset({1: 1}), [
      (VariableWithCount('i2.2.1.2.0', 1, 1, S(1)), Mul)
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
        if CommutativeMatcher40740._instance is None:
            CommutativeMatcher40740._instance = CommutativeMatcher40740()
        return CommutativeMatcher40740._instance

    @staticmethod
    def get_match_iter(subject):
        subjects = deque([subject]) if subject is not None else deque()
        subst0 = Substitution()
        # State 40739
        subst1 = Substitution(subst0)
        try:
            subst1.try_add_variable('i2.2.1.2.2', S(1))
        except ValueError:
            pass
        else:
            pass
            # State 40741
            subst2 = Substitution(subst1)
            try:
                subst2.try_add_variable('i2.2.1.2.2.0', S(1))
            except ValueError:
                pass
            else:
                pass
                # State 40742
                subst3 = Substitution(subst2)
                try:
                    subst3.try_add_variable('i2.2.1.2.2.2', S(1))
                except ValueError:
                    pass
                else:
                    pass
                    # State 40743
                    if len(subjects) >= 1 and isinstance(subjects[0], Add):
                        tmp4 = subjects.popleft()
                        associative1 = tmp4
                        associative_type1 = type(tmp4)
                        subjects5 = deque(tmp4._args)
                        matcher = CommutativeMatcher40745.get()
                        tmp6 = subjects5
                        subjects5 = []
                        for s in tmp6:
                            matcher.add_subject(s)
                        for pattern_index, subst4 in matcher.match(tmp6, subst3):
                            pass
                            if pattern_index == 0:
                                pass
                                # State 40761
                                if len(subjects) == 0:
                                    pass
                                    # 0: (d*(e + f*x + g*x**2)**p)**q /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f50) and (cons_f127) and (cons_f210) and (cons_f52) and (cons_f4) and (cons_f1201) and (cons_f40)
                                    yield 0, subst4
                        subjects.appendleft(tmp4)
                    if len(subjects) >= 1:
                        tmp7 = subjects.popleft()
                        subst4 = Substitution(subst3)
                        try:
                            subst4.try_add_variable('i2.2.1.2.2.1', tmp7)
                        except ValueError:
                            pass
                        else:
                            pass
                            # State 44928
                            if len(subjects) == 0:
                                pass
                                # 1: (d*v**p)**q /; (cons_f29) and (cons_f5) and (cons_f52) and (cons_f554) and (cons_f1202)
                                yield 1, subst4
                        subjects.appendleft(tmp7)
                if len(subjects) >= 1 and isinstance(subjects[0], Pow):
                    tmp9 = subjects.popleft()
                    subjects10 = deque(tmp9._args)
                    # State 40762
                    if len(subjects10) >= 1 and isinstance(subjects10[0], Add):
                        tmp11 = subjects10.popleft()
                        associative1 = tmp11
                        associative_type1 = type(tmp11)
                        subjects12 = deque(tmp11._args)
                        matcher = CommutativeMatcher40764.get()
                        tmp13 = subjects12
                        subjects12 = []
                        for s in tmp13:
                            matcher.add_subject(s)
                        for pattern_index, subst3 in matcher.match(tmp13, subst2):
                            pass
                            if pattern_index == 0:
                                pass
                                # State 40780
                                subst4 = Substitution(subst3)
                                try:
                                    subst4.try_add_variable('i2.2.1.2.2.2', 1)
                                except ValueError:
                                    pass
                                else:
                                    pass
                                    # State 40781
                                    if len(subjects10) == 0:
                                        pass
                                        # State 40782
                                        if len(subjects) == 0:
                                            pass
                                            # 0: (d*(e + f*x + g*x**2)**p)**q /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f50) and (cons_f127) and (cons_f210) and (cons_f52) and (cons_f4) and (cons_f1201) and (cons_f40)
                                            yield 0, subst4
                                if len(subjects10) >= 1:
                                    tmp15 = []
                                    tmp15.append(subjects10.popleft())
                                    while True:
                                        if len(tmp15) > 1:
                                            tmp16 = create_operation_expression(associative1, tmp15)
                                        elif len(tmp15) == 1:
                                            tmp16 = tmp15[0]
                                        else:
                                            assert False, "Unreachable"
                                        subst4 = Substitution(subst3)
                                        try:
                                            subst4.try_add_variable('i2.2.1.2.2.2', tmp16)
                                        except ValueError:
                                            pass
                                        else:
                                            pass
                                            # State 40781
                                            if len(subjects10) == 0:
                                                pass
                                                # State 40782
                                                if len(subjects) == 0:
                                                    pass
                                                    # 0: (d*(e + f*x + g*x**2)**p)**q /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f50) and (cons_f127) and (cons_f210) and (cons_f52) and (cons_f4) and (cons_f1201) and (cons_f40)
                                                    yield 0, subst4
                                        if len(subjects10) == 0:
                                            break
                                        tmp15.append(subjects10.popleft())
                                    subjects10.extendleft(reversed(tmp15))
                        subjects10.appendleft(tmp11)
                    if len(subjects10) >= 1:
                        tmp18 = subjects10.popleft()
                        subst3 = Substitution(subst2)
                        try:
                            subst3.try_add_variable('i2.2.1.2.2.1', tmp18)
                        except ValueError:
                            pass
                        else:
                            pass
                            # State 44929
                            subst4 = Substitution(subst3)
                            try:
                                subst4.try_add_variable('i2.2.1.2.2.2', 1)
                            except ValueError:
                                pass
                            else:
                                pass
                                # State 44930
                                if len(subjects10) == 0:
                                    pass
                                    # State 44931
                                    if len(subjects) == 0:
                                        pass
                                        # 1: (d*v**p)**q /; (cons_f29) and (cons_f5) and (cons_f52) and (cons_f554) and (cons_f1202)
                                        yield 1, subst4
                            if len(subjects10) >= 1:
                                tmp21 = subjects10.popleft()
                                subst4 = Substitution(subst3)
                                try:
                                    subst4.try_add_variable('i2.2.1.2.2.2', tmp21)
                                except ValueError:
                                    pass
                                else:
                                    pass
                                    # State 44930
                                    if len(subjects10) == 0:
                                        pass
                                        # State 44931
                                        if len(subjects) == 0:
                                            pass
                                            # 1: (d*v**p)**q /; (cons_f29) and (cons_f5) and (cons_f52) and (cons_f554) and (cons_f1202)
                                            yield 1, subst4
                                subjects10.appendleft(tmp21)
                        subjects10.appendleft(tmp18)
                    subjects.appendleft(tmp9)
            if len(subjects) >= 1 and isinstance(subjects[0], Mul):
                tmp23 = subjects.popleft()
                associative1 = tmp23
                associative_type1 = type(tmp23)
                subjects24 = deque(tmp23._args)
                matcher = CommutativeMatcher40784.get()
                tmp25 = subjects24
                subjects24 = []
                for s in tmp25:
                    matcher.add_subject(s)
                for pattern_index, subst2 in matcher.match(tmp25, subst1):
                    pass
                    if pattern_index == 0:
                        pass
                        # State 40825
                        if len(subjects) == 0:
                            pass
                            # 0: (d*(e + f*x + g*x**2)**p)**q /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f50) and (cons_f127) and (cons_f210) and (cons_f52) and (cons_f4) and (cons_f1201) and (cons_f40)
                            yield 0, subst2
                    if pattern_index == 1:
                        pass
                        # State 44936
                        if len(subjects) == 0:
                            pass
                            # 1: (d*v**p)**q /; (cons_f29) and (cons_f5) and (cons_f52) and (cons_f554) and (cons_f1202)
                            yield 1, subst2
                subjects.appendleft(tmp23)
        if len(subjects) >= 1 and isinstance(subjects[0], Pow):
            tmp26 = subjects.popleft()
            subjects27 = deque(tmp26._args)
            # State 40826
            subst1 = Substitution(subst0)
            try:
                subst1.try_add_variable('i2.2.1.2.2.0', S(1))
            except ValueError:
                pass
            else:
                pass
                # State 40827
                subst2 = Substitution(subst1)
                try:
                    subst2.try_add_variable('i2.2.1.2.2.2', S(1))
                except ValueError:
                    pass
                else:
                    pass
                    # State 40828
                    if len(subjects27) >= 1 and isinstance(subjects27[0], Add):
                        tmp30 = subjects27.popleft()
                        associative1 = tmp30
                        associative_type1 = type(tmp30)
                        subjects31 = deque(tmp30._args)
                        matcher = CommutativeMatcher40830.get()
                        tmp32 = subjects31
                        subjects31 = []
                        for s in tmp32:
                            matcher.add_subject(s)
                        for pattern_index, subst3 in matcher.match(tmp32, subst2):
                            pass
                            if pattern_index == 0:
                                pass
                                # State 40846
                                subst4 = Substitution(subst3)
                                try:
                                    subst4.try_add_variable('i2.2.1.2.2', 1)
                                except ValueError:
                                    pass
                                else:
                                    pass
                                    # State 40847
                                    if len(subjects27) == 0:
                                        pass
                                        # State 40848
                                        if len(subjects) == 0:
                                            pass
                                            # 0: (d*(e + f*x + g*x**2)**p)**q /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f50) and (cons_f127) and (cons_f210) and (cons_f52) and (cons_f4) and (cons_f1201) and (cons_f40)
                                            yield 0, subst4
                                if len(subjects27) >= 1:
                                    tmp34 = []
                                    tmp34.append(subjects27.popleft())
                                    while True:
                                        if len(tmp34) > 1:
                                            tmp35 = create_operation_expression(associative1, tmp34)
                                        elif len(tmp34) == 1:
                                            tmp35 = tmp34[0]
                                        else:
                                            assert False, "Unreachable"
                                        subst4 = Substitution(subst3)
                                        try:
                                            subst4.try_add_variable('i2.2.1.2.2', tmp35)
                                        except ValueError:
                                            pass
                                        else:
                                            pass
                                            # State 40847
                                            if len(subjects27) == 0:
                                                pass
                                                # State 40848
                                                if len(subjects) == 0:
                                                    pass
                                                    # 0: (d*(e + f*x + g*x**2)**p)**q /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f50) and (cons_f127) and (cons_f210) and (cons_f52) and (cons_f4) and (cons_f1201) and (cons_f40)
                                                    yield 0, subst4
                                        if len(subjects27) == 0:
                                            break
                                        tmp34.append(subjects27.popleft())
                                    subjects27.extendleft(reversed(tmp34))
                        subjects27.appendleft(tmp30)
                    if len(subjects27) >= 1:
                        tmp37 = subjects27.popleft()
                        subst3 = Substitution(subst2)
                        try:
                            subst3.try_add_variable('i2.2.1.2.2.1', tmp37)
                        except ValueError:
                            pass
                        else:
                            pass
                            # State 44937
                            subst4 = Substitution(subst3)
                            try:
                                subst4.try_add_variable('i2.2.1.2.2', 1)
                            except ValueError:
                                pass
                            else:
                                pass
                                # State 44938
                                if len(subjects27) == 0:
                                    pass
                                    # State 44939
                                    if len(subjects) == 0:
                                        pass
                                        # 1: (d*v**p)**q /; (cons_f29) and (cons_f5) and (cons_f52) and (cons_f554) and (cons_f1202)
                                        yield 1, subst4
                            if len(subjects27) >= 1:
                                tmp40 = subjects27.popleft()
                                subst4 = Substitution(subst3)
                                try:
                                    subst4.try_add_variable('i2.2.1.2.2', tmp40)
                                except ValueError:
                                    pass
                                else:
                                    pass
                                    # State 44938
                                    if len(subjects27) == 0:
                                        pass
                                        # State 44939
                                        if len(subjects) == 0:
                                            pass
                                            # 1: (d*v**p)**q /; (cons_f29) and (cons_f5) and (cons_f52) and (cons_f554) and (cons_f1202)
                                            yield 1, subst4
                                subjects27.appendleft(tmp40)
                        subjects27.appendleft(tmp37)
                if len(subjects27) >= 1 and isinstance(subjects27[0], Pow):
                    tmp42 = subjects27.popleft()
                    subjects43 = deque(tmp42._args)
                    # State 40849
                    if len(subjects43) >= 1 and isinstance(subjects43[0], Add):
                        tmp44 = subjects43.popleft()
                        associative1 = tmp44
                        associative_type1 = type(tmp44)
                        subjects45 = deque(tmp44._args)
                        matcher = CommutativeMatcher40851.get()
                        tmp46 = subjects45
                        subjects45 = []
                        for s in tmp46:
                            matcher.add_subject(s)
                        for pattern_index, subst2 in matcher.match(tmp46, subst1):
                            pass
                            if pattern_index == 0:
                                pass
                                # State 40867
                                subst3 = Substitution(subst2)
                                try:
                                    subst3.try_add_variable('i2.2.1.2.2.2', 1)
                                except ValueError:
                                    pass
                                else:
                                    pass
                                    # State 40868
                                    if len(subjects43) == 0:
                                        pass
                                        # State 40869
                                        subst4 = Substitution(subst3)
                                        try:
                                            subst4.try_add_variable('i2.2.1.2.2', 1)
                                        except ValueError:
                                            pass
                                        else:
                                            pass
                                            # State 40870
                                            if len(subjects27) == 0:
                                                pass
                                                # State 40871
                                                if len(subjects) == 0:
                                                    pass
                                                    # 0: (d*(e + f*x + g*x**2)**p)**q /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f50) and (cons_f127) and (cons_f210) and (cons_f52) and (cons_f4) and (cons_f1201) and (cons_f40)
                                                    yield 0, subst4
                                        if len(subjects27) >= 1:
                                            tmp49 = subjects27.popleft()
                                            subst4 = Substitution(subst3)
                                            try:
                                                subst4.try_add_variable('i2.2.1.2.2', tmp49)
                                            except ValueError:
                                                pass
                                            else:
                                                pass
                                                # State 40870
                                                if len(subjects27) == 0:
                                                    pass
                                                    # State 40871
                                                    if len(subjects) == 0:
                                                        pass
                                                        # 0: (d*(e + f*x + g*x**2)**p)**q /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f50) and (cons_f127) and (cons_f210) and (cons_f52) and (cons_f4) and (cons_f1201) and (cons_f40)
                                                        yield 0, subst4
                                            subjects27.appendleft(tmp49)
                                if len(subjects43) >= 1:
                                    tmp51 = []
                                    tmp51.append(subjects43.popleft())
                                    while True:
                                        if len(tmp51) > 1:
                                            tmp52 = create_operation_expression(associative1, tmp51)
                                        elif len(tmp51) == 1:
                                            tmp52 = tmp51[0]
                                        else:
                                            assert False, "Unreachable"
                                        subst3 = Substitution(subst2)
                                        try:
                                            subst3.try_add_variable('i2.2.1.2.2.2', tmp52)
                                        except ValueError:
                                            pass
                                        else:
                                            pass
                                            # State 40868
                                            if len(subjects43) == 0:
                                                pass
                                                # State 40869
                                                subst4 = Substitution(subst3)
                                                try:
                                                    subst4.try_add_variable('i2.2.1.2.2', 1)
                                                except ValueError:
                                                    pass
                                                else:
                                                    pass
                                                    # State 40870
                                                    if len(subjects27) == 0:
                                                        pass
                                                        # State 40871
                                                        if len(subjects) == 0:
                                                            pass
                                                            # 0: (d*(e + f*x + g*x**2)**p)**q /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f50) and (cons_f127) and (cons_f210) and (cons_f52) and (cons_f4) and (cons_f1201) and (cons_f40)
                                                            yield 0, subst4
                                                if len(subjects27) >= 1:
                                                    tmp55 = subjects27.popleft()
                                                    subst4 = Substitution(subst3)
                                                    try:
                                                        subst4.try_add_variable('i2.2.1.2.2', tmp55)
                                                    except ValueError:
                                                        pass
                                                    else:
                                                        pass
                                                        # State 40870
                                                        if len(subjects27) == 0:
                                                            pass
                                                            # State 40871
                                                            if len(subjects) == 0:
                                                                pass
                                                                # 0: (d*(e + f*x + g*x**2)**p)**q /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f50) and (cons_f127) and (cons_f210) and (cons_f52) and (cons_f4) and (cons_f1201) and (cons_f40)
                                                                yield 0, subst4
                                                    subjects27.appendleft(tmp55)
                                        if len(subjects43) == 0:
                                            break
                                        tmp51.append(subjects43.popleft())
                                    subjects43.extendleft(reversed(tmp51))
                        subjects43.appendleft(tmp44)
                    if len(subjects43) >= 1:
                        tmp57 = subjects43.popleft()
                        subst2 = Substitution(subst1)
                        try:
                            subst2.try_add_variable('i2.2.1.2.2.1', tmp57)
                        except ValueError:
                            pass
                        else:
                            pass
                            # State 44940
                            subst3 = Substitution(subst2)
                            try:
                                subst3.try_add_variable('i2.2.1.2.2.2', 1)
                            except ValueError:
                                pass
                            else:
                                pass
                                # State 44941
                                if len(subjects43) == 0:
                                    pass
                                    # State 44942
                                    subst4 = Substitution(subst3)
                                    try:
                                        subst4.try_add_variable('i2.2.1.2.2', 1)
                                    except ValueError:
                                        pass
                                    else:
                                        pass
                                        # State 44943
                                        if len(subjects27) == 0:
                                            pass
                                            # State 44944
                                            if len(subjects) == 0:
                                                pass
                                                # 1: (d*v**p)**q /; (cons_f29) and (cons_f5) and (cons_f52) and (cons_f554) and (cons_f1202)
                                                yield 1, subst4
                                    if len(subjects27) >= 1:
                                        tmp61 = subjects27.popleft()
                                        subst4 = Substitution(subst3)
                                        try:
                                            subst4.try_add_variable('i2.2.1.2.2', tmp61)
                                        except ValueError:
                                            pass
                                        else:
                                            pass
                                            # State 44943
                                            if len(subjects27) == 0:
                                                pass
                                                # State 44944
                                                if len(subjects) == 0:
                                                    pass
                                                    # 1: (d*v**p)**q /; (cons_f29) and (cons_f5) and (cons_f52) and (cons_f554) and (cons_f1202)
                                                    yield 1, subst4
                                        subjects27.appendleft(tmp61)
                            if len(subjects43) >= 1:
                                tmp63 = subjects43.popleft()
                                subst3 = Substitution(subst2)
                                try:
                                    subst3.try_add_variable('i2.2.1.2.2.2', tmp63)
                                except ValueError:
                                    pass
                                else:
                                    pass
                                    # State 44941
                                    if len(subjects43) == 0:
                                        pass
                                        # State 44942
                                        subst4 = Substitution(subst3)
                                        try:
                                            subst4.try_add_variable('i2.2.1.2.2', 1)
                                        except ValueError:
                                            pass
                                        else:
                                            pass
                                            # State 44943
                                            if len(subjects27) == 0:
                                                pass
                                                # State 44944
                                                if len(subjects) == 0:
                                                    pass
                                                    # 1: (d*v**p)**q /; (cons_f29) and (cons_f5) and (cons_f52) and (cons_f554) and (cons_f1202)
                                                    yield 1, subst4
                                        if len(subjects27) >= 1:
                                            tmp66 = subjects27.popleft()
                                            subst4 = Substitution(subst3)
                                            try:
                                                subst4.try_add_variable('i2.2.1.2.2', tmp66)
                                            except ValueError:
                                                pass
                                            else:
                                                pass
                                                # State 44943
                                                if len(subjects27) == 0:
                                                    pass
                                                    # State 44944
                                                    if len(subjects) == 0:
                                                        pass
                                                        # 1: (d*v**p)**q /; (cons_f29) and (cons_f5) and (cons_f52) and (cons_f554) and (cons_f1202)
                                                        yield 1, subst4
                                            subjects27.appendleft(tmp66)
                                subjects43.appendleft(tmp63)
                        subjects43.appendleft(tmp57)
                    subjects27.appendleft(tmp42)
            if len(subjects27) >= 1 and isinstance(subjects27[0], Mul):
                tmp68 = subjects27.popleft()
                associative1 = tmp68
                associative_type1 = type(tmp68)
                subjects69 = deque(tmp68._args)
                matcher = CommutativeMatcher40873.get()
                tmp70 = subjects69
                subjects69 = []
                for s in tmp70:
                    matcher.add_subject(s)
                for pattern_index, subst1 in matcher.match(tmp70, subst0):
                    pass
                    if pattern_index == 0:
                        pass
                        # State 40914
                        subst2 = Substitution(subst1)
                        try:
                            subst2.try_add_variable('i2.2.1.2.2', 1)
                        except ValueError:
                            pass
                        else:
                            pass
                            # State 40915
                            if len(subjects27) == 0:
                                pass
                                # State 40916
                                if len(subjects) == 0:
                                    pass
                                    # 0: (d*(e + f*x + g*x**2)**p)**q /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f50) and (cons_f127) and (cons_f210) and (cons_f52) and (cons_f4) and (cons_f1201) and (cons_f40)
                                    yield 0, subst2
                        if len(subjects27) >= 1:
                            tmp72 = []
                            tmp72.append(subjects27.popleft())
                            while True:
                                if len(tmp72) > 1:
                                    tmp73 = create_operation_expression(associative1, tmp72)
                                elif len(tmp72) == 1:
                                    tmp73 = tmp72[0]
                                else:
                                    assert False, "Unreachable"
                                subst2 = Substitution(subst1)
                                try:
                                    subst2.try_add_variable('i2.2.1.2.2', tmp73)
                                except ValueError:
                                    pass
                                else:
                                    pass
                                    # State 40915
                                    if len(subjects27) == 0:
                                        pass
                                        # State 40916
                                        if len(subjects) == 0:
                                            pass
                                            # 0: (d*(e + f*x + g*x**2)**p)**q /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f50) and (cons_f127) and (cons_f210) and (cons_f52) and (cons_f4) and (cons_f1201) and (cons_f40)
                                            yield 0, subst2
                                if len(subjects27) == 0:
                                    break
                                tmp72.append(subjects27.popleft())
                            subjects27.extendleft(reversed(tmp72))
                    if pattern_index == 1:
                        pass
                        # State 44949
                        subst2 = Substitution(subst1)
                        try:
                            subst2.try_add_variable('i2.2.1.2.2', 1)
                        except ValueError:
                            pass
                        else:
                            pass
                            # State 44950
                            if len(subjects27) == 0:
                                pass
                                # State 44951
                                if len(subjects) == 0:
                                    pass
                                    # 1: (d*v**p)**q /; (cons_f29) and (cons_f5) and (cons_f52) and (cons_f554) and (cons_f1202)
                                    yield 1, subst2
                        if len(subjects27) >= 1:
                            tmp76 = []
                            tmp76.append(subjects27.popleft())
                            while True:
                                if len(tmp76) > 1:
                                    tmp77 = create_operation_expression(associative1, tmp76)
                                elif len(tmp76) == 1:
                                    tmp77 = tmp76[0]
                                else:
                                    assert False, "Unreachable"
                                subst2 = Substitution(subst1)
                                try:
                                    subst2.try_add_variable('i2.2.1.2.2', tmp77)
                                except ValueError:
                                    pass
                                else:
                                    pass
                                    # State 44950
                                    if len(subjects27) == 0:
                                        pass
                                        # State 44951
                                        if len(subjects) == 0:
                                            pass
                                            # 1: (d*v**p)**q /; (cons_f29) and (cons_f5) and (cons_f52) and (cons_f554) and (cons_f1202)
                                            yield 1, subst2
                                if len(subjects27) == 0:
                                    break
                                tmp76.append(subjects27.popleft())
                            subjects27.extendleft(reversed(tmp76))
                subjects27.appendleft(tmp68)
            subjects.appendleft(tmp26)
        return
        yield


from .generated_part000150 import *
from matchpy.matching.many_to_one import CommutativeMatcher
from .generated_part000137 import *
from .generated_part000139 import *
from .generated_part000148 import *
from collections import deque
from .generated_part000141 import *
from .generated_part000146 import *
from matchpy.utils import VariableWithCount
from multiset import Multiset