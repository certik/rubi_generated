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


class CommutativeMatcher111956(CommutativeMatcher):
    _instance = None
    patterns = {
    0: (0, Multiset({0: 1, 1: 1}), [
      
])
}
    subjects = {}
    subjects_by_id = {}
    bipartite = BipartiteGraph()
    associative = Add
    max_optional_count = 0
    anonymous_patterns = {0}

    def __init__(self):
        self.add_subject(None)

    @staticmethod
    def get():
        if CommutativeMatcher111956._instance is None:
            CommutativeMatcher111956._instance = CommutativeMatcher111956()
        return CommutativeMatcher111956._instance

    @staticmethod
    def get_match_iter(subject):
        subjects = deque([subject]) if subject is not None else deque()
        subst0 = Substitution()
        # State 111955
        if len(subjects) >= 1 and subjects[0] == Integer(1):
            tmp1 = subjects.popleft()
            # State 111957
            if len(subjects) == 0:
                pass
                # 0: 1
                yield 0, subst0
            subjects.appendleft(tmp1)
        subst1 = Substitution(subst0)
        try:
            subst1.try_add_variable('i2.2.1.0', S(1))
        except ValueError:
            pass
        else:
            pass
            # State 111958
            if len(subjects) >= 1 and isinstance(subjects[0], Pow):
                tmp3 = subjects.popleft()
                subjects4 = deque(tmp3._args)
                # State 111959
                if len(subjects4) >= 1:
                    tmp5 = subjects4.popleft()
                    subst2 = Substitution(subst1)
                    try:
                        subst2.try_add_variable('i2.2.1.1', tmp5)
                    except ValueError:
                        pass
                    else:
                        pass
                        # State 111960
                        if len(subjects4) >= 1 and subjects4[0] == Integer(2):
                            tmp7 = subjects4.popleft()
                            # State 111961
                            if len(subjects4) == 0:
                                pass
                                # State 111962
                                if len(subjects) == 0:
                                    pass
                                    # 1: e*x**2
                                    yield 1, subst2
                            subjects4.appendleft(tmp7)
                    subjects4.appendleft(tmp5)
                subjects.appendleft(tmp3)
        if len(subjects) >= 1 and isinstance(subjects[0], Mul):
            tmp8 = subjects.popleft()
            associative1 = tmp8
            associative_type1 = type(tmp8)
            subjects9 = deque(tmp8._args)
            matcher = CommutativeMatcher111964.get()
            tmp10 = subjects9
            subjects9 = []
            for s in tmp10:
                matcher.add_subject(s)
            for pattern_index, subst1 in matcher.match(tmp10, subst0):
                pass
                if pattern_index == 0:
                    pass
                    # State 111969
                    if len(subjects) == 0:
                        pass
                        # 1: e*x**2
                        yield 1, subst1
            subjects.appendleft(tmp8)
        return
        yield


from matchpy.matching.many_to_one import CommutativeMatcher
from .generated_part006760 import *
from collections import deque
from matchpy.utils import VariableWithCount
from multiset import Multiset