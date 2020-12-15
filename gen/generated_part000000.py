def match_root(subject):
    subjects = deque([subject]) if subject is not None else deque()
    subst0 = Substitution()
    # State 2301
    if len(subjects) >= 1 and isinstance(subjects[0], Integral):
        tmp1 = subjects.popleft()
        subjects2 = deque((tmp1._args[0],) + tmp1._args[1])
        # State 2302
        subst1 = Substitution(subst0)
        try:
            subst1.try_add_variable('i2.0', S(1))
        except ValueError:
            pass
        else:
            pass
            # State 2303
            subst2 = Substitution(subst1)
            try:
                subst2.try_add_variable('i2.2', S(0))
            except ValueError:
                pass
            else:
                pass
                # State 2304
                if len(subjects2) >= 1:
                    tmp5 = subjects2.popleft()
                    subst3 = Substitution(subst2)
                    try:
                        subst3.try_add_variable('i2.1', tmp5)
                    except ValueError:
                        pass
                    else:
                        pass
                        if 'i2.1' not in subst3 or 'i2.2' not in subst3 or cons_f4(n=subst3["i2.2"], x=subst3["i2.1"]):
                            pass
                            if 'i2.1' not in subst3 or 'i2.0' not in subst3 or cons_f3(b=subst3["i2.0"], x=subst3["i2.1"]):
                                pass
                                # State 2305
                                if len(subjects2) >= 1:
                                    tmp7 = subjects2.popleft()
                                    subst4 = Substitution(subst3)
                                    try:
                                        subst4.try_add_variable('i2.1', tmp7)
                                    except ValueError:
                                        pass
                                    else:
                                        pass
                                        if 'i2.1' not in subst4 or 'i2.2' not in subst4 or cons_f4(n=subst4["i2.2"], x=subst4["i2.1"]):
                                            pass
                                            if 'i2.1' not in subst4 or 'i2.0' not in subst4 or cons_f3(b=subst4["i2.0"], x=subst4["i2.1"]):
                                                pass
                                                # State 2306
                                                if len(subjects2) == 0:
                                                    pass
                                                    # State 2307
                                                    if len(subjects) == 0:
                                                        pass
                                                        tmp_subst = Substitution()
                                                        tmp_subst['x'] = subst4['i2.1']
                                                        tmp_subst['n'] = subst4['i2.2']
                                                        tmp_subst['b'] = subst4['i2.0']
                                                        # 0: Integral(b*x**n, x) /; (cons_f4) and (cons_f3) and (cons_a1)
                                                        yield replacement1, tmp_subst, [(cons_f4), (cons_f3), (cons_a1)]
                                    subjects2.appendleft(tmp7)
                    subjects2.appendleft(tmp5)
            if len(subjects2) >= 1 and isinstance(subjects2[0], Pow):
                tmp9 = subjects2.popleft()
                subjects10 = deque(tmp9._args)
                # State 2308
                if len(subjects10) >= 1:
                    tmp11 = subjects10.popleft()
                    subst2 = Substitution(subst1)
                    try:
                        subst2.try_add_variable('i2.1', tmp11)
                    except ValueError:
                        pass
                    else:
                        pass
                        if 'i2.1' not in subst2 or 'i2.2' not in subst2 or cons_f4(n=subst2["i2.2"], x=subst2["i2.1"]):
                            pass
                            if 'i2.1' not in subst2 or 'i2.0' not in subst2 or cons_f3(b=subst2["i2.0"], x=subst2["i2.1"]):
                                pass
                                # State 2309
                                subst3 = Substitution(subst2)
                                try:
                                    subst3.try_add_variable('i2.2', 0)
                                except ValueError:
                                    pass
                                else:
                                    pass
                                    if 'i2.1' not in subst3 or 'i2.2' not in subst3 or cons_f4(n=subst3["i2.2"], x=subst3["i2.1"]):
                                        pass
                                        if 'i2.2' not in subst3 or cons_a1(n=subst3["i2.2"]):
                                            pass
                                            # State 2310
                                            if len(subjects10) == 0:
                                                pass
                                                # State 2311
                                                if len(subjects2) >= 1:
                                                    tmp14 = subjects2.popleft()
                                                    subst4 = Substitution(subst3)
                                                    try:
                                                        subst4.try_add_variable('i2.1', tmp14)
                                                    except ValueError:
                                                        pass
                                                    else:
                                                        pass
                                                        if 'i2.1' not in subst4 or 'i2.2' not in subst4 or cons_f4(n=subst4["i2.2"], x=subst4["i2.1"]):
                                                            pass
                                                            if 'i2.1' not in subst4 or 'i2.0' not in subst4 or cons_f3(b=subst4["i2.0"], x=subst4["i2.1"]):
                                                                pass
                                                                # State 2312
                                                                if len(subjects2) == 0:
                                                                    pass
                                                                    # State 2313
                                                                    if len(subjects) == 0:
                                                                        pass
                                                                        tmp_subst = Substitution()
                                                                        tmp_subst['x'] = subst4['i2.1']
                                                                        tmp_subst['n'] = subst4['i2.2']
                                                                        tmp_subst['b'] = subst4['i2.0']
                                                                        # 0: Integral(b*x**n, x) /; (cons_f4) and (cons_f3) and (cons_a1)
                                                                        yield replacement1, tmp_subst, [(cons_f4), (cons_f3), (cons_a1)]
                                                    subjects2.appendleft(tmp14)
                                if len(subjects10) >= 1:
                                    tmp16 = subjects10.popleft()
                                    subst3 = Substitution(subst2)
                                    try:
                                        subst3.try_add_variable('i2.2', tmp16)
                                    except ValueError:
                                        pass
                                    else:
                                        pass
                                        if 'i2.1' not in subst3 or 'i2.2' not in subst3 or cons_f4(n=subst3["i2.2"], x=subst3["i2.1"]):
                                            pass
                                            if 'i2.2' not in subst3 or cons_a1(n=subst3["i2.2"]):
                                                pass
                                                # State 2310
                                                if len(subjects10) == 0:
                                                    pass
                                                    # State 2311
                                                    if len(subjects2) >= 1:
                                                        tmp18 = subjects2.popleft()
                                                        subst4 = Substitution(subst3)
                                                        try:
                                                            subst4.try_add_variable('i2.1', tmp18)
                                                        except ValueError:
                                                            pass
                                                        else:
                                                            pass
                                                            if 'i2.1' not in subst4 or 'i2.2' not in subst4 or cons_f4(n=subst4["i2.2"], x=subst4["i2.1"]):
                                                                pass
                                                                if 'i2.1' not in subst4 or 'i2.0' not in subst4 or cons_f3(b=subst4["i2.0"], x=subst4["i2.1"]):
                                                                    pass
                                                                    # State 2312
                                                                    if len(subjects2) == 0:
                                                                        pass
                                                                        # State 2313
                                                                        if len(subjects) == 0:
                                                                            pass
                                                                            tmp_subst = Substitution()
                                                                            tmp_subst['x'] = subst4['i2.1']
                                                                            tmp_subst['n'] = subst4['i2.2']
                                                                            tmp_subst['b'] = subst4['i2.0']
                                                                            # 0: Integral(b*x**n, x) /; (cons_f4) and (cons_f3) and (cons_a1)
                                                                            yield replacement1, tmp_subst, [(cons_f4), (cons_f3), (cons_a1)]
                                                        subjects2.appendleft(tmp18)
                                    subjects10.appendleft(tmp16)
                    subjects10.appendleft(tmp11)
                subjects2.appendleft(tmp9)
        subst1 = Substitution(subst0)
        try:
            subst1.try_add_variable('i2.0_1', S(1))
        except ValueError:
            pass
        else:
            pass
            # State 2325
            if len(subjects2) >= 1:
                tmp21 = subjects2.popleft()
                subst2 = Substitution(subst1)
                try:
                    subst2.try_add_variable('i2.0', tmp21)
                except ValueError:
                    pass
                else:
                    pass
                    if 'i2.0_1' not in subst2 or 'i2.0' not in subst2 or cons_f3(b=subst2["i2.0_1"], x=subst2["i2.0"]):
                        pass
                        # State 2326
                        if len(subjects2) >= 1:
                            tmp23 = subjects2.popleft()
                            subst3 = Substitution(subst2)
                            try:
                                subst3.try_add_variable('i2.0', tmp23)
                            except ValueError:
                                pass
                            else:
                                pass
                                if 'i2.0_1' not in subst3 or 'i2.0' not in subst3 or cons_f3(b=subst3["i2.0_1"], x=subst3["i2.0"]):
                                    pass
                                    # State 2327
                                    if len(subjects2) == 0:
                                        pass
                                        # State 2328
                                        if len(subjects) == 0:
                                            pass
                                            tmp_subst = Substitution()
                                            tmp_subst['x'] = subst3['i2.0']
                                            tmp_subst['b'] = subst3['i2.0_1']
                                            # 1: Integral(b*x, x) /; (cons_f3)
                                            yield replacement2, tmp_subst, [(cons_f3)]
                            subjects2.appendleft(tmp23)
                subjects2.appendleft(tmp21)
        if len(subjects2) >= 1 and isinstance(subjects2[0], Mul):
            tmp25 = subjects2.popleft()
            associative1 = tmp25
            associative_type1 = type(tmp25)
            subjects26 = deque(tmp25._args)
            matcher = CommutativeMatcher2315.get()
            tmp27 = subjects26
            subjects26 = []
            for s in tmp27:
                matcher.add_subject(s)
            for pattern_index, subst1 in matcher.match(tmp27, subst0):
                pass
                if pattern_index == 0:
                    pass
                    if 'i2.1' not in subst1 or 'i2.2' not in subst1 or cons_f4(n=subst1["i2.2"], x=subst1["i2.1"]):
                        pass
                        if 'i2.1' not in subst1 or 'i2.0' not in subst1 or cons_f3(b=subst1["i2.0"], x=subst1["i2.1"]):
                            pass
                            if 'i2.2' not in subst1 or cons_a1(n=subst1["i2.2"]):
                                pass
                                # State 2322
                                if len(subjects2) >= 1:
                                    tmp28 = []
                                    tmp28.append(subjects2.popleft())
                                    while True:
                                        if len(tmp28) > 1:
                                            tmp29 = create_operation_expression(associative1, tmp28)
                                        elif len(tmp28) == 1:
                                            tmp29 = tmp28[0]
                                        else:
                                            assert False, "Unreachable"
                                        subst2 = Substitution(subst1)
                                        try:
                                            subst2.try_add_variable('i2.1', tmp29)
                                        except ValueError:
                                            pass
                                        else:
                                            pass
                                            if 'i2.1' not in subst2 or 'i2.2' not in subst2 or cons_f4(n=subst2["i2.2"], x=subst2["i2.1"]):
                                                pass
                                                if 'i2.1' not in subst2 or 'i2.0' not in subst2 or cons_f3(b=subst2["i2.0"], x=subst2["i2.1"]):
                                                    pass
                                                    # State 2323
                                                    if len(subjects2) == 0:
                                                        pass
                                                        # State 2324
                                                        if len(subjects) == 0:
                                                            pass
                                                            tmp_subst = Substitution()
                                                            tmp_subst['x'] = subst2['i2.1']
                                                            tmp_subst['n'] = subst2['i2.2']
                                                            tmp_subst['b'] = subst2['i2.0']
                                                            # 0: Integral(b*x**n, x) /; (cons_f4) and (cons_f3) and (cons_a1)
                                                            yield replacement1, tmp_subst, [(cons_f4), (cons_f3), (cons_a1)]
                                        if len(subjects2) == 0:
                                            break
                                        tmp28.append(subjects2.popleft())
                                    subjects2.extendleft(reversed(tmp28))
                if pattern_index == 1:
                    pass
                    if 'i2.0_1' not in subst1 or 'i2.0' not in subst1 or cons_f3(b=subst1["i2.0_1"], x=subst1["i2.0"]):
                        pass
                        # State 2329
                        if len(subjects2) >= 1:
                            tmp31 = []
                            tmp31.append(subjects2.popleft())
                            while True:
                                if len(tmp31) > 1:
                                    tmp32 = create_operation_expression(associative1, tmp31)
                                elif len(tmp31) == 1:
                                    tmp32 = tmp31[0]
                                else:
                                    assert False, "Unreachable"
                                subst2 = Substitution(subst1)
                                try:
                                    subst2.try_add_variable('i2.0', tmp32)
                                except ValueError:
                                    pass
                                else:
                                    pass
                                    if 'i2.0_1' not in subst2 or 'i2.0' not in subst2 or cons_f3(b=subst2["i2.0_1"], x=subst2["i2.0"]):
                                        pass
                                        # State 2330
                                        if len(subjects2) == 0:
                                            pass
                                            # State 2331
                                            if len(subjects) == 0:
                                                pass
                                                tmp_subst = Substitution()
                                                tmp_subst['x'] = subst2['i2.0']
                                                tmp_subst['b'] = subst2['i2.0_1']
                                                # 1: Integral(b*x, x) /; (cons_f3)
                                                yield replacement2, tmp_subst, [(cons_f3)]
                                if len(subjects2) == 0:
                                    break
                                tmp31.append(subjects2.popleft())
                            subjects2.extendleft(reversed(tmp31))
            subjects2.appendleft(tmp25)
        subjects.appendleft(tmp1)
    return
    yield


from sympy.integrals.rubi.constraints import *
from sympy.integrals.rubi.rules.binomial_products import *
from sympy.integrals.rubi.rules.exponential import *
from sympy.integrals.rubi.rules.hyperbolic import *
from sympy.integrals.rubi.rules.integrand_simplification import *
from sympy.integrals.rubi.rules.inverse_hyperbolic import *
from sympy.integrals.rubi.rules.inverse_trig import *
from sympy.integrals.rubi.rules.linear_products import *
from sympy.integrals.rubi.rules.logarithms import *
from sympy.integrals.rubi.rules.miscellaneous_algebraic import *
from sympy.integrals.rubi.rules.miscellaneous_integration import *
from sympy.integrals.rubi.rules.miscellaneous_trig import *
from sympy.integrals.rubi.rules.piecewise_linear import *
from sympy.integrals.rubi.rules.quadratic_products import *
from sympy.integrals.rubi.rules.secant import *
from sympy.integrals.rubi.rules.sine import *
from sympy.integrals.rubi.rules.special_functions import *
from sympy.integrals.rubi.rules.tangent import *
from sympy.integrals.rubi.rules.trinomial_products import *
from .generated_part000001 import *
