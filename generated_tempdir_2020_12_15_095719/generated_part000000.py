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
                subst2.try_add_variable('i2.2', S(1))
            except ValueError:
                pass
            else:
                pass
                # State 2304
                if len(subjects2) >= 1 and isinstance(subjects2[0], Add):
                    tmp5 = subjects2.popleft()
                    associative1 = tmp5
                    associative_type1 = type(tmp5)
                    subjects6 = deque(tmp5._args)
                    matcher = CommutativeMatcher2306.get()
                    tmp7 = subjects6
                    subjects6 = []
                    for s in tmp7:
                        matcher.add_subject(s)
                    for pattern_index, subst3 in matcher.match(tmp7, subst2):
                        pass
                        if pattern_index == 0:
                            pass
                            if 'i2.2.0' not in subst3 or 'i2.2.1.1' not in subst3 or cons_f2(a=subst3["i2.2.0"], x=subst3["i2.2.1.1"]):
                                pass
                                if 'i2.2.1.0' not in subst3 or 'i2.2.1.1' not in subst3 or cons_f3(b=subst3["i2.2.1.0"], x=subst3["i2.2.1.1"]):
                                    pass
                                    if 'i2.2.1.2' not in subst3 or 'i2.2.1.1' not in subst3 or cons_f4(n=subst3["i2.2.1.2"], x=subst3["i2.2.1.1"]):
                                        pass
                                        if 'i2.2' not in subst3 or 'i2.2.1.1' not in subst3 or cons_f5(p=subst3["i2.2"], x=subst3["i2.2.1.1"]):
                                            pass
                                            if 'i2.2.0' not in subst3 or cons_f1(a=subst3["i2.2.0"]):
                                                pass
                                                # State 2323
                                                if len(subjects2) >= 1:
                                                    tmp8 = []
                                                    tmp8.append(subjects2.popleft())
                                                    while True:
                                                        if len(tmp8) > 1:
                                                            tmp9 = create_operation_expression(associative1, tmp8)
                                                        elif len(tmp8) == 1:
                                                            tmp9 = tmp8[0]
                                                        else:
                                                            assert False, "Unreachable"
                                                        subst4 = Substitution(subst3)
                                                        try:
                                                            subst4.try_add_variable('i2.2.1.1', tmp9)
                                                        except ValueError:
                                                            pass
                                                        else:
                                                            pass
                                                            if 'i2.2.0' not in subst4 or 'i2.2.1.1' not in subst4 or cons_f2(a=subst4["i2.2.0"], x=subst4["i2.2.1.1"]):
                                                                pass
                                                                if 'i2.2.1.0' not in subst4 or 'i2.2.1.1' not in subst4 or cons_f3(b=subst4["i2.2.1.0"], x=subst4["i2.2.1.1"]):
                                                                    pass
                                                                    if 'i2.2.1.2' not in subst4 or 'i2.2.1.1' not in subst4 or cons_f4(n=subst4["i2.2.1.2"], x=subst4["i2.2.1.1"]):
                                                                        pass
                                                                        if 'i2.2' not in subst4 or 'i2.2.1.1' not in subst4 or cons_f5(p=subst4["i2.2"], x=subst4["i2.2.1.1"]):
                                                                            pass
                                                                            # State 2324
                                                                            if len(subjects2) == 0:
                                                                                pass
                                                                                # State 2325
                                                                                if len(subjects) == 0:
                                                                                    pass
                                                                                    tmp_subst = Substitution()
                                                                                    tmp_subst['x'] = subst4['i2.2.1.1']
                                                                                    tmp_subst['n'] = subst4['i2.2.1.2']
                                                                                    tmp_subst['b'] = subst4['i2.2.1.0']
                                                                                    tmp_subst['a'] = subst4['i2.2.0']
                                                                                    tmp_subst['p'] = subst4['i2.2']
                                                                                    tmp_subst['u'] = subst4['i2.0']
                                                                                    # 0: Integral(u*(a + b*x**n)**p, x) /; (cons_f2) and (cons_f3) and (cons_f4) and (cons_f5) and (cons_f1)
                                                                                    yield replacement1, tmp_subst, [(cons_f2), (cons_f3), (cons_f4), (cons_f5), (cons_f1)]
                                                        if len(subjects2) == 0:
                                                            break
                                                        tmp8.append(subjects2.popleft())
                                                    subjects2.extendleft(reversed(tmp8))
                        if pattern_index == 1:
                            pass
                            if 'i2.2.0' not in subst3 or 'i2.2.1.1' not in subst3 or cons_f2(a=subst3["i2.2.0"], x=subst3["i2.2.1.1"]):
                                pass
                                if 'i2.2.1.0' not in subst3 or 'i2.2.1.1' not in subst3 or cons_f3(b=subst3["i2.2.1.0"], x=subst3["i2.2.1.1"]):
                                    pass
                                    if 'i2.2.1.2' not in subst3 or 'i2.2.1.1' not in subst3 or cons_f4(n=subst3["i2.2.1.2"], x=subst3["i2.2.1.1"]):
                                        pass
                                        if 'i2.2' not in subst3 or 'i2.2.1.1' not in subst3 or cons_f5(p=subst3["i2.2"], x=subst3["i2.2.1.1"]):
                                            pass
                                            if 'i2.2.1.0' not in subst3 or cons_f6(b=subst3["i2.2.1.0"]):
                                                pass
                                                # State 2420
                                                if len(subjects2) >= 1:
                                                    tmp11 = []
                                                    tmp11.append(subjects2.popleft())
                                                    while True:
                                                        if len(tmp11) > 1:
                                                            tmp12 = create_operation_expression(associative1, tmp11)
                                                        elif len(tmp11) == 1:
                                                            tmp12 = tmp11[0]
                                                        else:
                                                            assert False, "Unreachable"
                                                        subst4 = Substitution(subst3)
                                                        try:
                                                            subst4.try_add_variable('i2.2.1.1', tmp12)
                                                        except ValueError:
                                                            pass
                                                        else:
                                                            pass
                                                            if 'i2.2.0' not in subst4 or 'i2.2.1.1' not in subst4 or cons_f2(a=subst4["i2.2.0"], x=subst4["i2.2.1.1"]):
                                                                pass
                                                                if 'i2.2.1.0' not in subst4 or 'i2.2.1.1' not in subst4 or cons_f3(b=subst4["i2.2.1.0"], x=subst4["i2.2.1.1"]):
                                                                    pass
                                                                    if 'i2.2.1.2' not in subst4 or 'i2.2.1.1' not in subst4 or cons_f4(n=subst4["i2.2.1.2"], x=subst4["i2.2.1.1"]):
                                                                        pass
                                                                        if 'i2.2' not in subst4 or 'i2.2.1.1' not in subst4 or cons_f5(p=subst4["i2.2"], x=subst4["i2.2.1.1"]):
                                                                            pass
                                                                            # State 2421
                                                                            if len(subjects2) == 0:
                                                                                pass
                                                                                # State 2422
                                                                                if len(subjects) == 0:
                                                                                    pass
                                                                                    tmp_subst = Substitution()
                                                                                    tmp_subst['x'] = subst4['i2.2.1.1']
                                                                                    tmp_subst['n'] = subst4['i2.2.1.2']
                                                                                    tmp_subst['b'] = subst4['i2.2.1.0']
                                                                                    tmp_subst['a'] = subst4['i2.2.0']
                                                                                    tmp_subst['p'] = subst4['i2.2']
                                                                                    tmp_subst['u'] = subst4['i2.0']
                                                                                    # 1: Integral(u*(a + b*x**n)**p, x) /; (cons_f2) and (cons_f3) and (cons_f4) and (cons_f5) and (cons_f6)
                                                                                    yield replacement2, tmp_subst, [(cons_f2), (cons_f3), (cons_f4), (cons_f5), (cons_f6)]
                                                        if len(subjects2) == 0:
                                                            break
                                                        tmp11.append(subjects2.popleft())
                                                    subjects2.extendleft(reversed(tmp11))
                        if pattern_index == 2:
                            pass
                            if 'i2.2.0' not in subst3 or 'i2.2.1.1' not in subst3 or cons_f2(a=subst3["i2.2.0"], x=subst3["i2.2.1.1"]):
                                pass
                                if 'i2.2' not in subst3 or 'i2.2.1.1' not in subst3 or cons_f5(p=subst3["i2.2"], x=subst3["i2.2.1.1"]):
                                    pass
                                    if 'i2.2.0' not in subst3 or cons_f1(a=subst3["i2.2.0"]):
                                        pass
                                        if 'i2.2.1.0_1' not in subst3 or 'i2.2.1.1' not in subst3 or cons_f3(b=subst3["i2.2.1.0_1"], x=subst3["i2.2.1.1"]):
                                            pass
                                            if 'i2.2.1.0' not in subst3 or 'i2.2.1.1' not in subst3 or cons_f8(c=subst3["i2.2.1.0"], x=subst3["i2.2.1.1"]):
                                                pass
                                                if 'i2.2.1.2_1' not in subst3 or 'i2.2.1.1' not in subst3 or cons_f4(n=subst3["i2.2.1.2_1"], x=subst3["i2.2.1.1"]):
                                                    pass
                                                    if 'i2.2.1.2' not in subst3 or 'i2.2.1.2_1' not in subst3 or cons_f7(j=subst3["i2.2.1.2"], n=subst3["i2.2.1.2_1"]):
                                                        pass
                                                        # State 2517
                                                        if len(subjects2) >= 1:
                                                            tmp14 = []
                                                            tmp14.append(subjects2.popleft())
                                                            while True:
                                                                if len(tmp14) > 1:
                                                                    tmp15 = create_operation_expression(associative1, tmp14)
                                                                elif len(tmp14) == 1:
                                                                    tmp15 = tmp14[0]
                                                                else:
                                                                    assert False, "Unreachable"
                                                                subst4 = Substitution(subst3)
                                                                try:
                                                                    subst4.try_add_variable('i2.2.1.1', tmp15)
                                                                except ValueError:
                                                                    pass
                                                                else:
                                                                    pass
                                                                    if 'i2.2.0' not in subst4 or 'i2.2.1.1' not in subst4 or cons_f2(a=subst4["i2.2.0"], x=subst4["i2.2.1.1"]):
                                                                        pass
                                                                        if 'i2.2' not in subst4 or 'i2.2.1.1' not in subst4 or cons_f5(p=subst4["i2.2"], x=subst4["i2.2.1.1"]):
                                                                            pass
                                                                            if 'i2.2.1.0_1' not in subst4 or 'i2.2.1.1' not in subst4 or cons_f3(b=subst4["i2.2.1.0_1"], x=subst4["i2.2.1.1"]):
                                                                                pass
                                                                                if 'i2.2.1.0' not in subst4 or 'i2.2.1.1' not in subst4 or cons_f8(c=subst4["i2.2.1.0"], x=subst4["i2.2.1.1"]):
                                                                                    pass
                                                                                    if 'i2.2.1.2_1' not in subst4 or 'i2.2.1.1' not in subst4 or cons_f4(n=subst4["i2.2.1.2_1"], x=subst4["i2.2.1.1"]):
                                                                                        pass
                                                                                        # State 2518
                                                                                        if len(subjects2) == 0:
                                                                                            pass
                                                                                            # State 2519
                                                                                            if len(subjects) == 0:
                                                                                                pass
                                                                                                tmp_subst = Substitution()
                                                                                                tmp_subst['x'] = subst4['i2.2.1.1']
                                                                                                tmp_subst['j'] = subst4['i2.2.1.2']
                                                                                                tmp_subst['c'] = subst4['i2.2.1.0']
                                                                                                tmp_subst['n'] = subst4['i2.2.1.2_1']
                                                                                                tmp_subst['b'] = subst4['i2.2.1.0_1']
                                                                                                tmp_subst['a'] = subst4['i2.2.0']
                                                                                                tmp_subst['p'] = subst4['i2.2']
                                                                                                tmp_subst['u'] = subst4['i2.0']
                                                                                                # 2: Integral(u*(a + b*x**n + c*x**j)**p, x) /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f4) and (cons_f5) and (cons_f7) and (cons_f1)
                                                                                                yield replacement3, tmp_subst, [(cons_f2), (cons_f3), (cons_f8), (cons_f4), (cons_f5), (cons_f7), (cons_f1)]
                                                                if len(subjects2) == 0:
                                                                    break
                                                                tmp14.append(subjects2.popleft())
                                                            subjects2.extendleft(reversed(tmp14))
                        if pattern_index == 3:
                            pass
                            if 'i2.2.0' not in subst3 or 'i2.2.1.1' not in subst3 or cons_f2(a=subst3["i2.2.0"], x=subst3["i2.2.1.1"]):
                                pass
                                if 'i2.2' not in subst3 or 'i2.2.1.1' not in subst3 or cons_f5(p=subst3["i2.2"], x=subst3["i2.2.1.1"]):
                                    pass
                                    if 'i2.2.1.0_1' not in subst3 or 'i2.2.1.1' not in subst3 or cons_f3(b=subst3["i2.2.1.0_1"], x=subst3["i2.2.1.1"]):
                                        pass
                                        if 'i2.2.1.0' not in subst3 or 'i2.2.1.1' not in subst3 or cons_f8(c=subst3["i2.2.1.0"], x=subst3["i2.2.1.1"]):
                                            pass
                                            if 'i2.2.1.2_1' not in subst3 or 'i2.2.1.1' not in subst3 or cons_f4(n=subst3["i2.2.1.2_1"], x=subst3["i2.2.1.1"]):
                                                pass
                                                if 'i2.2.1.2' not in subst3 or 'i2.2.1.2_1' not in subst3 or cons_f7(j=subst3["i2.2.1.2"], n=subst3["i2.2.1.2_1"]):
                                                    pass
                                                    if 'i2.2.1.0_1' not in subst3 or cons_f6(b=subst3["i2.2.1.0_1"]):
                                                        pass
                                                        # State 2571
                                                        if len(subjects2) >= 1:
                                                            tmp17 = []
                                                            tmp17.append(subjects2.popleft())
                                                            while True:
                                                                if len(tmp17) > 1:
                                                                    tmp18 = create_operation_expression(associative1, tmp17)
                                                                elif len(tmp17) == 1:
                                                                    tmp18 = tmp17[0]
                                                                else:
                                                                    assert False, "Unreachable"
                                                                subst4 = Substitution(subst3)
                                                                try:
                                                                    subst4.try_add_variable('i2.2.1.1', tmp18)
                                                                except ValueError:
                                                                    pass
                                                                else:
                                                                    pass
                                                                    if 'i2.2.0' not in subst4 or 'i2.2.1.1' not in subst4 or cons_f2(a=subst4["i2.2.0"], x=subst4["i2.2.1.1"]):
                                                                        pass
                                                                        if 'i2.2' not in subst4 or 'i2.2.1.1' not in subst4 or cons_f5(p=subst4["i2.2"], x=subst4["i2.2.1.1"]):
                                                                            pass
                                                                            if 'i2.2.1.0_1' not in subst4 or 'i2.2.1.1' not in subst4 or cons_f3(b=subst4["i2.2.1.0_1"], x=subst4["i2.2.1.1"]):
                                                                                pass
                                                                                if 'i2.2.1.0' not in subst4 or 'i2.2.1.1' not in subst4 or cons_f8(c=subst4["i2.2.1.0"], x=subst4["i2.2.1.1"]):
                                                                                    pass
                                                                                    if 'i2.2.1.2_1' not in subst4 or 'i2.2.1.1' not in subst4 or cons_f4(n=subst4["i2.2.1.2_1"], x=subst4["i2.2.1.1"]):
                                                                                        pass
                                                                                        # State 2572
                                                                                        if len(subjects2) == 0:
                                                                                            pass
                                                                                            # State 2573
                                                                                            if len(subjects) == 0:
                                                                                                pass
                                                                                                tmp_subst = Substitution()
                                                                                                tmp_subst['x'] = subst4['i2.2.1.1']
                                                                                                tmp_subst['j'] = subst4['i2.2.1.2']
                                                                                                tmp_subst['c'] = subst4['i2.2.1.0']
                                                                                                tmp_subst['n'] = subst4['i2.2.1.2_1']
                                                                                                tmp_subst['b'] = subst4['i2.2.1.0_1']
                                                                                                tmp_subst['a'] = subst4['i2.2.0']
                                                                                                tmp_subst['p'] = subst4['i2.2']
                                                                                                tmp_subst['u'] = subst4['i2.0']
                                                                                                # 3: Integral(u*(a + b*x**n + c*x**j)**p, x) /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f4) and (cons_f5) and (cons_f7) and (cons_f6)
                                                                                                yield replacement4, tmp_subst, [(cons_f2), (cons_f3), (cons_f8), (cons_f4), (cons_f5), (cons_f7), (cons_f6)]
                                                                if len(subjects2) == 0:
                                                                    break
                                                                tmp17.append(subjects2.popleft())
                                                            subjects2.extendleft(reversed(tmp17))
                        if pattern_index == 4:
                            pass
                            if 'i2.2.0' not in subst3 or 'i2.2.1.1' not in subst3 or cons_f2(a=subst3["i2.2.0"], x=subst3["i2.2.1.1"]):
                                pass
                                if 'i2.2' not in subst3 or 'i2.2.1.1' not in subst3 or cons_f5(p=subst3["i2.2"], x=subst3["i2.2.1.1"]):
                                    pass
                                    if 'i2.2.1.0_1' not in subst3 or 'i2.2.1.1' not in subst3 or cons_f3(b=subst3["i2.2.1.0_1"], x=subst3["i2.2.1.1"]):
                                        pass
                                        if 'i2.2.1.0' not in subst3 or 'i2.2.1.1' not in subst3 or cons_f8(c=subst3["i2.2.1.0"], x=subst3["i2.2.1.1"]):
                                            pass
                                            if 'i2.2.1.2_1' not in subst3 or 'i2.2.1.1' not in subst3 or cons_f4(n=subst3["i2.2.1.2_1"], x=subst3["i2.2.1.1"]):
                                                pass
                                                if 'i2.2.1.2' not in subst3 or 'i2.2.1.2_1' not in subst3 or cons_f7(j=subst3["i2.2.1.2"], n=subst3["i2.2.1.2_1"]):
                                                    pass
                                                    if 'i2.2.1.0' not in subst3 or cons_f9(c=subst3["i2.2.1.0"]):
                                                        pass
                                                        # State 2586
                                                        if len(subjects2) >= 1:
                                                            tmp20 = []
                                                            tmp20.append(subjects2.popleft())
                                                            while True:
                                                                if len(tmp20) > 1:
                                                                    tmp21 = create_operation_expression(associative1, tmp20)
                                                                elif len(tmp20) == 1:
                                                                    tmp21 = tmp20[0]
                                                                else:
                                                                    assert False, "Unreachable"
                                                                subst4 = Substitution(subst3)
                                                                try:
                                                                    subst4.try_add_variable('i2.2.1.1', tmp21)
                                                                except ValueError:
                                                                    pass
                                                                else:
                                                                    pass
                                                                    if 'i2.2.0' not in subst4 or 'i2.2.1.1' not in subst4 or cons_f2(a=subst4["i2.2.0"], x=subst4["i2.2.1.1"]):
                                                                        pass
                                                                        if 'i2.2' not in subst4 or 'i2.2.1.1' not in subst4 or cons_f5(p=subst4["i2.2"], x=subst4["i2.2.1.1"]):
                                                                            pass
                                                                            if 'i2.2.1.0_1' not in subst4 or 'i2.2.1.1' not in subst4 or cons_f3(b=subst4["i2.2.1.0_1"], x=subst4["i2.2.1.1"]):
                                                                                pass
                                                                                if 'i2.2.1.0' not in subst4 or 'i2.2.1.1' not in subst4 or cons_f8(c=subst4["i2.2.1.0"], x=subst4["i2.2.1.1"]):
                                                                                    pass
                                                                                    if 'i2.2.1.2_1' not in subst4 or 'i2.2.1.1' not in subst4 or cons_f4(n=subst4["i2.2.1.2_1"], x=subst4["i2.2.1.1"]):
                                                                                        pass
                                                                                        # State 2587
                                                                                        if len(subjects2) == 0:
                                                                                            pass
                                                                                            # State 2588
                                                                                            if len(subjects) == 0:
                                                                                                pass
                                                                                                tmp_subst = Substitution()
                                                                                                tmp_subst['x'] = subst4['i2.2.1.1']
                                                                                                tmp_subst['j'] = subst4['i2.2.1.2']
                                                                                                tmp_subst['c'] = subst4['i2.2.1.0']
                                                                                                tmp_subst['n'] = subst4['i2.2.1.2_1']
                                                                                                tmp_subst['b'] = subst4['i2.2.1.0_1']
                                                                                                tmp_subst['a'] = subst4['i2.2.0']
                                                                                                tmp_subst['p'] = subst4['i2.2']
                                                                                                tmp_subst['u'] = subst4['i2.0']
                                                                                                # 4: Integral(u*(a + b*x**n + c*x**j)**p, x) /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f4) and (cons_f5) and (cons_f7) and (cons_f9)
                                                                                                yield replacement5, tmp_subst, [(cons_f2), (cons_f3), (cons_f8), (cons_f4), (cons_f5), (cons_f7), (cons_f9)]
                                                                if len(subjects2) == 0:
                                                                    break
                                                                tmp20.append(subjects2.popleft())
                                                            subjects2.extendleft(reversed(tmp20))
                        if pattern_index == 5:
                            pass
                            if 'i2' not in subst3 or 'i2.2.1.0_1' not in subst3 or cons_f2(a=subst3["i2.2.1.0_1"], x=subst3["i2"]):
                                pass
                                if 'i2.2.1.0_2' not in subst3 or 'i2' not in subst3 or cons_f3(b=subst3["i2.2.1.0_2"], x=subst3["i2"]):
                                    pass
                                    if 'i2' not in subst3 or 'i2.2.1.0' not in subst3 or cons_f10(v=subst3["i2.2.1.0"], x=subst3["i2"]):
                                        pass
                                        # State 2606
                                        if len(subjects2) >= 1:
                                            tmp23 = []
                                            tmp23.append(subjects2.popleft())
                                            while True:
                                                if len(tmp23) > 1:
                                                    tmp24 = create_operation_expression(associative1, tmp23)
                                                elif len(tmp23) == 1:
                                                    tmp24 = tmp23[0]
                                                else:
                                                    assert False, "Unreachable"
                                                subst4 = Substitution(subst3)
                                                try:
                                                    subst4.try_add_variable('i2', tmp24)
                                                except ValueError:
                                                    pass
                                                else:
                                                    pass
                                                    if 'i2' not in subst4 or 'i2.2.1.0_1' not in subst4 or cons_f2(a=subst4["i2.2.1.0_1"], x=subst4["i2"]):
                                                        pass
                                                        if 'i2.2.1.0_2' not in subst4 or 'i2' not in subst4 or cons_f3(b=subst4["i2.2.1.0_2"], x=subst4["i2"]):
                                                            pass
                                                            if 'i2' not in subst4 or 'i2.2.1.0' not in subst4 or cons_f10(v=subst4["i2.2.1.0"], x=subst4["i2"]):
                                                                pass
                                                                # State 2607
                                                                if len(subjects2) == 0:
                                                                    pass
                                                                    # State 2608
                                                                    if len(subjects) == 0:
                                                                        pass
                                                                        tmp_subst = Substitution()
                                                                        tmp_subst['v'] = subst4['i2.2.1.0']
                                                                        tmp_subst['a'] = subst4['i2.2.1.0_1']
                                                                        tmp_subst['b'] = subst4['i2.2.1.0_2']
                                                                        tmp_subst['w'] = subst4['i2.2.0']
                                                                        tmp_subst['p'] = subst4['i2.2']
                                                                        tmp_subst['u'] = subst4['i2.0']
                                                                        tmp_subst['x'] = subst4['i2']
                                                                        # 5: Integral(u*(a*v + b*v + w)**p, x) /; (cons_f2) and (cons_f3) and (cons_f10)
                                                                        yield replacement6, tmp_subst, [(cons_f2), (cons_f3), (cons_f10)]
                                                if len(subjects2) == 0:
                                                    break
                                                tmp23.append(subjects2.popleft())
                                            subjects2.extendleft(reversed(tmp23))
                        if pattern_index == 6:
                            pass
                            if 'i2.2.0' not in subst3 or 'i2.2.1.1' not in subst3 or cons_f2(a=subst3["i2.2.0"], x=subst3["i2.2.1.1"]):
                                pass
                                if 'i2.2.1.0_1' not in subst3 or 'i2.2.1.1' not in subst3 or cons_f3(b=subst3["i2.2.1.0_1"], x=subst3["i2.2.1.1"]):
                                    pass
                                    if 'i2.2.1.0' not in subst3 or 'i2.2.1.1' not in subst3 or cons_f8(c=subst3["i2.2.1.0"], x=subst3["i2.2.1.1"]):
                                        pass
                                        if 'i2.2.1.0' not in subst3 or 'i2.2.1.0_1' not in subst3 or 'i2.2.0' not in subst3 or cons_f47(a=subst3["i2.2.0"], b=subst3["i2.2.1.0_1"], c=subst3["i2.2.1.0"]):
                                            pass
                                            # State 2849
                                            if len(subjects2) >= 1:
                                                tmp26 = []
                                                tmp26.append(subjects2.popleft())
                                                while True:
                                                    if len(tmp26) > 1:
                                                        tmp27 = create_operation_expression(associative1, tmp26)
                                                    elif len(tmp26) == 1:
                                                        tmp27 = tmp26[0]
                                                    else:
                                                        assert False, "Unreachable"
                                                    subst4 = Substitution(subst3)
                                                    try:
                                                        subst4.try_add_variable('i2.2.1.1', tmp27)
                                                    except ValueError:
                                                        pass
                                                    else:
                                                        pass
                                                        if 'i2.2.0' not in subst4 or 'i2.2.1.1' not in subst4 or cons_f2(a=subst4["i2.2.0"], x=subst4["i2.2.1.1"]):
                                                            pass
                                                            if 'i2.2.1.0_1' not in subst4 or 'i2.2.1.1' not in subst4 or cons_f3(b=subst4["i2.2.1.0_1"], x=subst4["i2.2.1.1"]):
                                                                pass
                                                                if 'i2.2.1.0' not in subst4 or 'i2.2.1.1' not in subst4 or cons_f8(c=subst4["i2.2.1.0"], x=subst4["i2.2.1.1"]):
                                                                    pass
                                                                    # State 2850
                                                                    if len(subjects2) == 0:
                                                                        pass
                                                                        # State 2851
                                                                        if len(subjects) == 0:
                                                                            pass
                                                                            tmp_subst = Substitution()
                                                                            tmp_subst['x'] = subst4['i2.2.1.1']
                                                                            tmp_subst['c'] = subst4['i2.2.1.0']
                                                                            tmp_subst['b'] = subst4['i2.2.1.0_1']
                                                                            tmp_subst['a'] = subst4['i2.2.0']
                                                                            tmp_subst['p'] = subst4['i2.2']
                                                                            tmp_subst['u'] = subst4['i2.0']
                                                                            # 26: Integral(u*(a + b*x + c*x**2)**p, x) /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f47) and (cons_f40)
                                                                            yield replacement27, tmp_subst, [(cons_f2), (cons_f3), (cons_f8), (cons_f47), (cons_f40)]
                                                    if len(subjects2) == 0:
                                                        break
                                                    tmp26.append(subjects2.popleft())
                                                subjects2.extendleft(reversed(tmp26))
                        if pattern_index == 7:
                            pass
                            if 'i2.2.0' not in subst3 or 'i2.2.1.1' not in subst3 or cons_f2(a=subst3["i2.2.0"], x=subst3["i2.2.1.1"]):
                                pass
                                if 'i2.2.1.0' not in subst3 or 'i2.2.1.1' not in subst3 or cons_f3(b=subst3["i2.2.1.0"], x=subst3["i2.2.1.1"]):
                                    pass
                                    if 'i2.2.1.2' not in subst3 or 'i2.2.1.1' not in subst3 or cons_f4(n=subst3["i2.2.1.2"], x=subst3["i2.2.1.1"]):
                                        pass
                                        if 'i2.2.1.0_1' not in subst3 or 'i2.2.1.1' not in subst3 or cons_f8(c=subst3["i2.2.1.0_1"], x=subst3["i2.2.1.1"]):
                                            pass
                                            if 'i2.2.1.2' not in subst3 or 'i2.2.1.2_1' not in subst3 or cons_f48(n=subst3["i2.2.1.2"], n2=subst3["i2.2.1.2_1"]):
                                                pass
                                                if 'i2.2.1.0_1' not in subst3 or 'i2.2.1.0' not in subst3 or 'i2.2.0' not in subst3 or cons_f47(a=subst3["i2.2.0"], b=subst3["i2.2.1.0"], c=subst3["i2.2.1.0_1"]):
                                                    pass
                                                    # State 2891
                                                    if len(subjects2) >= 1:
                                                        tmp29 = []
                                                        tmp29.append(subjects2.popleft())
                                                        while True:
                                                            if len(tmp29) > 1:
                                                                tmp30 = create_operation_expression(associative1, tmp29)
                                                            elif len(tmp29) == 1:
                                                                tmp30 = tmp29[0]
                                                            else:
                                                                assert False, "Unreachable"
                                                            subst4 = Substitution(subst3)
                                                            try:
                                                                subst4.try_add_variable('i2.2.1.1', tmp30)
                                                            except ValueError:
                                                                pass
                                                            else:
                                                                pass
                                                                if 'i2.2.0' not in subst4 or 'i2.2.1.1' not in subst4 or cons_f2(a=subst4["i2.2.0"], x=subst4["i2.2.1.1"]):
                                                                    pass
                                                                    if 'i2.2.1.0' not in subst4 or 'i2.2.1.1' not in subst4 or cons_f3(b=subst4["i2.2.1.0"], x=subst4["i2.2.1.1"]):
                                                                        pass
                                                                        if 'i2.2.1.2' not in subst4 or 'i2.2.1.1' not in subst4 or cons_f4(n=subst4["i2.2.1.2"], x=subst4["i2.2.1.1"]):
                                                                            pass
                                                                            if 'i2.2.1.0_1' not in subst4 or 'i2.2.1.1' not in subst4 or cons_f8(c=subst4["i2.2.1.0_1"], x=subst4["i2.2.1.1"]):
                                                                                pass
                                                                                # State 2892
                                                                                if len(subjects2) == 0:
                                                                                    pass
                                                                                    # State 2893
                                                                                    if len(subjects) == 0:
                                                                                        pass
                                                                                        tmp_subst = Substitution()
                                                                                        tmp_subst['x'] = subst4['i2.2.1.1']
                                                                                        tmp_subst['n'] = subst4['i2.2.1.2']
                                                                                        tmp_subst['b'] = subst4['i2.2.1.0']
                                                                                        tmp_subst['n2'] = subst4['i2.2.1.2_1']
                                                                                        tmp_subst['c'] = subst4['i2.2.1.0_1']
                                                                                        tmp_subst['a'] = subst4['i2.2.0']
                                                                                        tmp_subst['p'] = subst4['i2.2']
                                                                                        tmp_subst['u'] = subst4['i2.0']
                                                                                        # 27: Integral(u*(a + b*x**n + c*x**n2)**p, x) /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f4) and (cons_f48) and (cons_f47) and (cons_f40)
                                                                                        yield replacement28, tmp_subst, [(cons_f2), (cons_f3), (cons_f8), (cons_f4), (cons_f48), (cons_f47), (cons_f40)]
                                                            if len(subjects2) == 0:
                                                                break
                                                            tmp29.append(subjects2.popleft())
                                                        subjects2.extendleft(reversed(tmp29))
                        if pattern_index == 8:
                            pass
                            if 'i2.2.1.0_1' not in subst3 or 'i2.2.1.1' not in subst3 or cons_f3(b=subst3["i2.2.1.0_1"], x=subst3["i2.2.1.1"]):
                                pass
                                if 'i2.2.1.0' not in subst3 or 'i2.2.1.1' not in subst3 or cons_f2(a=subst3["i2.2.1.0"], x=subst3["i2.2.1.1"]):
                                    pass
                                    if 'i2.2.1.2' not in subst3 or 'i2.2.1.1' not in subst3 or cons_f5(p=subst3["i2.2.1.2"], x=subst3["i2.2.1.1"]):
                                        pass
                                        if 'i2.2.1.2_1' not in subst3 or 'i2.2.1.1' not in subst3 or cons_f52(q=subst3["i2.2.1.2_1"], x=subst3["i2.2.1.1"]):
                                            pass
                                            if 'i2.2.1.2' not in subst3 or 'i2.2.1.2_1' not in subst3 or cons_f51(p=subst3["i2.2.1.2"], q=subst3["i2.2.1.2_1"]):
                                                pass
                                                # State 2930
                                                if len(subjects2) >= 1:
                                                    tmp32 = []
                                                    tmp32.append(subjects2.popleft())
                                                    while True:
                                                        if len(tmp32) > 1:
                                                            tmp33 = create_operation_expression(associative1, tmp32)
                                                        elif len(tmp32) == 1:
                                                            tmp33 = tmp32[0]
                                                        else:
                                                            assert False, "Unreachable"
                                                        subst4 = Substitution(subst3)
                                                        try:
                                                            subst4.try_add_variable('i2.2.1.1', tmp33)
                                                        except ValueError:
                                                            pass
                                                        else:
                                                            pass
                                                            if 'i2.2.1.0_1' not in subst4 or 'i2.2.1.1' not in subst4 or cons_f3(b=subst4["i2.2.1.0_1"], x=subst4["i2.2.1.1"]):
                                                                pass
                                                                if 'i2.2.1.0' not in subst4 or 'i2.2.1.1' not in subst4 or cons_f2(a=subst4["i2.2.1.0"], x=subst4["i2.2.1.1"]):
                                                                    pass
                                                                    if 'i2.2.1.2' not in subst4 or 'i2.2.1.1' not in subst4 or cons_f5(p=subst4["i2.2.1.2"], x=subst4["i2.2.1.1"]):
                                                                        pass
                                                                        if 'i2.2.1.2_1' not in subst4 or 'i2.2.1.1' not in subst4 or cons_f52(q=subst4["i2.2.1.2_1"], x=subst4["i2.2.1.1"]):
                                                                            pass
                                                                            # State 2931
                                                                            if len(subjects2) == 0:
                                                                                pass
                                                                                # State 2932
                                                                                if len(subjects) == 0:
                                                                                    pass
                                                                                    tmp_subst = Substitution()
                                                                                    tmp_subst['x'] = subst4['i2.2.1.1']
                                                                                    tmp_subst['p'] = subst4['i2.2.1.2']
                                                                                    tmp_subst['a'] = subst4['i2.2.1.0']
                                                                                    tmp_subst['q'] = subst4['i2.2.1.2_1']
                                                                                    tmp_subst['b'] = subst4['i2.2.1.0_1']
                                                                                    tmp_subst['m'] = subst4['i2.2']
                                                                                    tmp_subst['u'] = subst4['i2.0']
                                                                                    # 29: Integral(u*(a*x**p + b*x**q)**m, x) /; (cons_f2) and (cons_f3) and (cons_f5) and (cons_f52) and (cons_f20) and (cons_f51)
                                                                                    yield replacement30, tmp_subst, [(cons_f2), (cons_f3), (cons_f5), (cons_f52), (cons_f20), (cons_f51)]
                                                        if len(subjects2) == 0:
                                                            break
                                                        tmp32.append(subjects2.popleft())
                                                    subjects2.extendleft(reversed(tmp32))
                        if pattern_index == 9:
                            pass
                            if 'i2.2.1.0_1' not in subst3 or 'i2.2.1.1' not in subst3 or cons_f3(b=subst3["i2.2.1.0_1"], x=subst3["i2.2.1.1"]):
                                pass
                                if 'i2.2.1.0' not in subst3 or 'i2.2.1.1' not in subst3 or cons_f2(a=subst3["i2.2.1.0"], x=subst3["i2.2.1.1"]):
                                    pass
                                    if 'i2.2.1.2' not in subst3 or 'i2.2.1.1' not in subst3 or cons_f5(p=subst3["i2.2.1.2"], x=subst3["i2.2.1.1"]):
                                        pass
                                        if 'i2.2.1.2_1' not in subst3 or 'i2.2.1.1' not in subst3 or cons_f52(q=subst3["i2.2.1.2_1"], x=subst3["i2.2.1.1"]):
                                            pass
                                            if 'i2.2.1.2' not in subst3 or 'i2.2.1.2_1' not in subst3 or cons_f51(p=subst3["i2.2.1.2"], q=subst3["i2.2.1.2_1"]):
                                                pass
                                                if 'i2.2.1.0_2' not in subst3 or 'i2.2.1.1' not in subst3 or cons_f8(c=subst3["i2.2.1.0_2"], x=subst3["i2.2.1.1"]):
                                                    pass
                                                    if 'i2.2.1.2_2' not in subst3 or 'i2.2.1.1' not in subst3 or cons_f54(r=subst3["i2.2.1.2_2"], x=subst3["i2.2.1.1"]):
                                                        pass
                                                        if 'i2.2.1.2' not in subst3 or 'i2.2.1.2_2' not in subst3 or cons_f53(p=subst3["i2.2.1.2"], r=subst3["i2.2.1.2_2"]):
                                                            pass
                                                            # State 2964
                                                            if len(subjects2) >= 1:
                                                                tmp35 = []
                                                                tmp35.append(subjects2.popleft())
                                                                while True:
                                                                    if len(tmp35) > 1:
                                                                        tmp36 = create_operation_expression(associative1, tmp35)
                                                                    elif len(tmp35) == 1:
                                                                        tmp36 = tmp35[0]
                                                                    else:
                                                                        assert False, "Unreachable"
                                                                    subst4 = Substitution(subst3)
                                                                    try:
                                                                        subst4.try_add_variable('i2.2.1.1', tmp36)
                                                                    except ValueError:
                                                                        pass
                                                                    else:
                                                                        pass
                                                                        if 'i2.2.1.0_1' not in subst4 or 'i2.2.1.1' not in subst4 or cons_f3(b=subst4["i2.2.1.0_1"], x=subst4["i2.2.1.1"]):
                                                                            pass
                                                                            if 'i2.2.1.0' not in subst4 or 'i2.2.1.1' not in subst4 or cons_f2(a=subst4["i2.2.1.0"], x=subst4["i2.2.1.1"]):
                                                                                pass
                                                                                if 'i2.2.1.2' not in subst4 or 'i2.2.1.1' not in subst4 or cons_f5(p=subst4["i2.2.1.2"], x=subst4["i2.2.1.1"]):
                                                                                    pass
                                                                                    if 'i2.2.1.2_1' not in subst4 or 'i2.2.1.1' not in subst4 or cons_f52(q=subst4["i2.2.1.2_1"], x=subst4["i2.2.1.1"]):
                                                                                        pass
                                                                                        if 'i2.2.1.0_2' not in subst4 or 'i2.2.1.1' not in subst4 or cons_f8(c=subst4["i2.2.1.0_2"], x=subst4["i2.2.1.1"]):
                                                                                            pass
                                                                                            if 'i2.2.1.2_2' not in subst4 or 'i2.2.1.1' not in subst4 or cons_f54(r=subst4["i2.2.1.2_2"], x=subst4["i2.2.1.1"]):
                                                                                                pass
                                                                                                # State 2965
                                                                                                if len(subjects2) == 0:
                                                                                                    pass
                                                                                                    # State 2966
                                                                                                    if len(subjects) == 0:
                                                                                                        pass
                                                                                                        tmp_subst = Substitution()
                                                                                                        tmp_subst['x'] = subst4['i2.2.1.1']
                                                                                                        tmp_subst['p'] = subst4['i2.2.1.2']
                                                                                                        tmp_subst['a'] = subst4['i2.2.1.0']
                                                                                                        tmp_subst['q'] = subst4['i2.2.1.2_1']
                                                                                                        tmp_subst['b'] = subst4['i2.2.1.0_1']
                                                                                                        tmp_subst['r'] = subst4['i2.2.1.2_2']
                                                                                                        tmp_subst['c'] = subst4['i2.2.1.0_2']
                                                                                                        tmp_subst['m'] = subst4['i2.2']
                                                                                                        tmp_subst['u'] = subst4['i2.0']
                                                                                                        # 30: Integral(u*(a*x**p + b*x**q + c*x**r)**m, x) /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f5) and (cons_f52) and (cons_f54) and (cons_f20) and (cons_f51) and (cons_f53)
                                                                                                        yield replacement31, tmp_subst, [(cons_f2), (cons_f3), (cons_f8), (cons_f5), (cons_f52), (cons_f54), (cons_f20), (cons_f51), (cons_f53)]
                                                                    if len(subjects2) == 0:
                                                                        break
                                                                    tmp35.append(subjects2.popleft())
                                                                subjects2.extendleft(reversed(tmp35))
                    subjects2.appendleft(tmp5)
                subst3 = Substitution(subst2)
                try:
                    subst3.try_add_variable('i2.2.0', S(0))
                except ValueError:
                    pass
                else:
                    pass
                    # State 2397
                    subst4 = Substitution(subst3)
                    try:
                        subst4.try_add_variable('i2.2.1.0', S(1))
                    except ValueError:
                        pass
                    else:
                        pass
                        # State 2398
                        subst5 = Substitution(subst4)
                        try:
                            subst5.try_add_variable('i2.2.1.2', S(1))
                        except ValueError:
                            pass
                        else:
                            pass
                            # State 2399
                            if len(subjects2) >= 1:
                                tmp41 = subjects2.popleft()
                                subst6 = Substitution(subst5)
                                try:
                                    subst6.try_add_variable('i2.2.1.1', tmp41)
                                except ValueError:
                                    pass
                                else:
                                    pass
                                    if 'i2.2.0' not in subst6 or 'i2.2.1.1' not in subst6 or cons_f2(a=subst6["i2.2.0"], x=subst6["i2.2.1.1"]):
                                        pass
                                        if 'i2.2.1.0' not in subst6 or 'i2.2.1.1' not in subst6 or cons_f3(b=subst6["i2.2.1.0"], x=subst6["i2.2.1.1"]):
                                            pass
                                            if 'i2.2.1.2' not in subst6 or 'i2.2.1.1' not in subst6 or cons_f4(n=subst6["i2.2.1.2"], x=subst6["i2.2.1.1"]):
                                                pass
                                                if 'i2.2' not in subst6 or 'i2.2.1.1' not in subst6 or cons_f5(p=subst6["i2.2"], x=subst6["i2.2.1.1"]):
                                                    pass
                                                    # State 2400
                                                    if len(subjects2) >= 1:
                                                        tmp43 = subjects2.popleft()
                                                        subst7 = Substitution(subst6)
                                                        try:
                                                            subst7.try_add_variable('i2.2.1.1', tmp43)
                                                        except ValueError:
                                                            pass
                                                        else:
                                                            pass
                                                            if 'i2.2.0' not in subst7 or 'i2.2.1.1' not in subst7 or cons_f2(a=subst7["i2.2.0"], x=subst7["i2.2.1.1"]):
                                                                pass
                                                                if 'i2.2.1.0' not in subst7 or 'i2.2.1.1' not in subst7 or cons_f3(b=subst7["i2.2.1.0"], x=subst7["i2.2.1.1"]):
                                                                    pass
                                                                    if 'i2.2.1.2' not in subst7 or 'i2.2.1.1' not in subst7 or cons_f4(n=subst7["i2.2.1.2"], x=subst7["i2.2.1.1"]):
                                                                        pass
                                                                        if 'i2.2' not in subst7 or 'i2.2.1.1' not in subst7 or cons_f5(p=subst7["i2.2"], x=subst7["i2.2.1.1"]):
                                                                            pass
                                                                            # State 2401
                                                                            if len(subjects2) == 0:
                                                                                pass
                                                                                # State 2402
                                                                                if len(subjects) == 0:
                                                                                    pass
                                                                                    tmp_subst = Substitution()
                                                                                    tmp_subst['x'] = subst7['i2.2.1.1']
                                                                                    tmp_subst['n'] = subst7['i2.2.1.2']
                                                                                    tmp_subst['b'] = subst7['i2.2.1.0']
                                                                                    tmp_subst['a'] = subst7['i2.2.0']
                                                                                    tmp_subst['p'] = subst7['i2.2']
                                                                                    tmp_subst['u'] = subst7['i2.0']
                                                                                    # 1: Integral(u*(a + b*x**n)**p, x) /; (cons_f2) and (cons_f3) and (cons_f4) and (cons_f5) and (cons_f6)
                                                                                    yield replacement2, tmp_subst, [(cons_f2), (cons_f3), (cons_f4), (cons_f5), (cons_f6)]
                                                        subjects2.appendleft(tmp43)
                                subjects2.appendleft(tmp41)
                        if len(subjects2) >= 1 and isinstance(subjects2[0], Pow):
                            tmp45 = subjects2.popleft()
                            subjects46 = deque(tmp45._args)
                            # State 2403
                            if len(subjects46) >= 1:
                                tmp47 = subjects46.popleft()
                                subst5 = Substitution(subst4)
                                try:
                                    subst5.try_add_variable('i2.2.1.1', tmp47)
                                except ValueError:
                                    pass
                                else:
                                    pass
                                    if 'i2.2.0' not in subst5 or 'i2.2.1.1' not in subst5 or cons_f2(a=subst5["i2.2.0"], x=subst5["i2.2.1.1"]):
                                        pass
                                        if 'i2.2.1.0' not in subst5 or 'i2.2.1.1' not in subst5 or cons_f3(b=subst5["i2.2.1.0"], x=subst5["i2.2.1.1"]):
                                            pass
                                            if 'i2.2.1.2' not in subst5 or 'i2.2.1.1' not in subst5 or cons_f4(n=subst5["i2.2.1.2"], x=subst5["i2.2.1.1"]):
                                                pass
                                                if 'i2.2' not in subst5 or 'i2.2.1.1' not in subst5 or cons_f5(p=subst5["i2.2"], x=subst5["i2.2.1.1"]):
                                                    pass
                                                    # State 2404
                                                    subst6 = Substitution(subst5)
                                                    try:
                                                        subst6.try_add_variable('i2.2.1.2', 1)
                                                    except ValueError:
                                                        pass
                                                    else:
                                                        pass
                                                        if 'i2.2.1.2' not in subst6 or 'i2.2.1.1' not in subst6 or cons_f4(n=subst6["i2.2.1.2"], x=subst6["i2.2.1.1"]):
                                                            pass
                                                            # State 2405
                                                            if len(subjects46) == 0:
                                                                pass
                                                                # State 2406
                                                                if len(subjects2) >= 1:
                                                                    tmp50 = subjects2.popleft()
                                                                    subst7 = Substitution(subst6)
                                                                    try:
                                                                        subst7.try_add_variable('i2.2.1.1', tmp50)
                                                                    except ValueError:
                                                                        pass
                                                                    else:
                                                                        pass
                                                                        if 'i2.2.0' not in subst7 or 'i2.2.1.1' not in subst7 or cons_f2(a=subst7["i2.2.0"], x=subst7["i2.2.1.1"]):
                                                                            pass
                                                                            if 'i2.2.1.0' not in subst7 or 'i2.2.1.1' not in subst7 or cons_f3(b=subst7["i2.2.1.0"], x=subst7["i2.2.1.1"]):
                                                                                pass
                                                                                if 'i2.2.1.2' not in subst7 or 'i2.2.1.1' not in subst7 or cons_f4(n=subst7["i2.2.1.2"], x=subst7["i2.2.1.1"]):
                                                                                    pass
                                                                                    if 'i2.2' not in subst7 or 'i2.2.1.1' not in subst7 or cons_f5(p=subst7["i2.2"], x=subst7["i2.2.1.1"]):
                                                                                        pass
                                                                                        # State 2407
                                                                                        if len(subjects2) == 0:
                                                                                            pass
                                                                                            # State 2408
                                                                                            if len(subjects) == 0:
                                                                                                pass
                                                                                                tmp_subst = Substitution()
                                                                                                tmp_subst['x'] = subst7['i2.2.1.1']
                                                                                                tmp_subst['n'] = subst7['i2.2.1.2']
                                                                                                tmp_subst['b'] = subst7['i2.2.1.0']
                                                                                                tmp_subst['a'] = subst7['i2.2.0']
                                                                                                tmp_subst['p'] = subst7['i2.2']
                                                                                                tmp_subst['u'] = subst7['i2.0']
                                                                                                # 1: Integral(u*(a + b*x**n)**p, x) /; (cons_f2) and (cons_f3) and (cons_f4) and (cons_f5) and (cons_f6)
                                                                                                yield replacement2, tmp_subst, [(cons_f2), (cons_f3), (cons_f4), (cons_f5), (cons_f6)]
                                                                    subjects2.appendleft(tmp50)
                                                    if len(subjects46) >= 1:
                                                        tmp52 = subjects46.popleft()
                                                        subst6 = Substitution(subst5)
                                                        try:
                                                            subst6.try_add_variable('i2.2.1.2', tmp52)
                                                        except ValueError:
                                                            pass
                                                        else:
                                                            pass
                                                            if 'i2.2.1.2' not in subst6 or 'i2.2.1.1' not in subst6 or cons_f4(n=subst6["i2.2.1.2"], x=subst6["i2.2.1.1"]):
                                                                pass
                                                                # State 2405
                                                                if len(subjects46) == 0:
                                                                    pass
                                                                    # State 2406
                                                                    if len(subjects2) >= 1:
                                                                        tmp54 = subjects2.popleft()
                                                                        subst7 = Substitution(subst6)
                                                                        try:
                                                                            subst7.try_add_variable('i2.2.1.1', tmp54)
                                                                        except ValueError:
                                                                            pass
                                                                        else:
                                                                            pass
                                                                            if 'i2.2.0' not in subst7 or 'i2.2.1.1' not in subst7 or cons_f2(a=subst7["i2.2.0"], x=subst7["i2.2.1.1"]):
                                                                                pass
                                                                                if 'i2.2.1.0' not in subst7 or 'i2.2.1.1' not in subst7 or cons_f3(b=subst7["i2.2.1.0"], x=subst7["i2.2.1.1"]):
                                                                                    pass
                                                                                    if 'i2.2.1.2' not in subst7 or 'i2.2.1.1' not in subst7 or cons_f4(n=subst7["i2.2.1.2"], x=subst7["i2.2.1.1"]):
                                                                                        pass
                                                                                        if 'i2.2' not in subst7 or 'i2.2.1.1' not in subst7 or cons_f5(p=subst7["i2.2"], x=subst7["i2.2.1.1"]):
                                                                                            pass
                                                                                            # State 2407
                                                                                            if len(subjects2) == 0:
                                                                                                pass
                                                                                                # State 2408
                                                                                                if len(subjects) == 0:
                                                                                                    pass
                                                                                                    tmp_subst = Substitution()
                                                                                                    tmp_subst['x'] = subst7['i2.2.1.1']
                                                                                                    tmp_subst['n'] = subst7['i2.2.1.2']
                                                                                                    tmp_subst['b'] = subst7['i2.2.1.0']
                                                                                                    tmp_subst['a'] = subst7['i2.2.0']
                                                                                                    tmp_subst['p'] = subst7['i2.2']
                                                                                                    tmp_subst['u'] = subst7['i2.0']
                                                                                                    # 1: Integral(u*(a + b*x**n)**p, x) /; (cons_f2) and (cons_f3) and (cons_f4) and (cons_f5) and (cons_f6)
                                                                                                    yield replacement2, tmp_subst, [(cons_f2), (cons_f3), (cons_f4), (cons_f5), (cons_f6)]
                                                                        subjects2.appendleft(tmp54)
                                                        subjects46.appendleft(tmp52)
                                subjects46.appendleft(tmp47)
                            subjects2.appendleft(tmp45)
                    if len(subjects2) >= 1 and isinstance(subjects2[0], Mul):
                        tmp56 = subjects2.popleft()
                        associative1 = tmp56
                        associative_type1 = type(tmp56)
                        subjects57 = deque(tmp56._args)
                        matcher = CommutativeMatcher2410.get()
                        tmp58 = subjects57
                        subjects57 = []
                        for s in tmp58:
                            matcher.add_subject(s)
                        for pattern_index, subst4 in matcher.match(tmp58, subst3):
                            pass
                            if pattern_index == 0:
                                pass
                                if 'i2.2.0' not in subst4 or 'i2.2.1.1' not in subst4 or cons_f2(a=subst4["i2.2.0"], x=subst4["i2.2.1.1"]):
                                    pass
                                    if 'i2.2.1.0' not in subst4 or 'i2.2.1.1' not in subst4 or cons_f3(b=subst4["i2.2.1.0"], x=subst4["i2.2.1.1"]):
                                        pass
                                        if 'i2.2.1.2' not in subst4 or 'i2.2.1.1' not in subst4 or cons_f4(n=subst4["i2.2.1.2"], x=subst4["i2.2.1.1"]):
                                            pass
                                            if 'i2.2' not in subst4 or 'i2.2.1.1' not in subst4 or cons_f5(p=subst4["i2.2"], x=subst4["i2.2.1.1"]):
                                                pass
                                                if 'i2.2.1.0' not in subst4 or cons_f6(b=subst4["i2.2.1.0"]):
                                                    pass
                                                    # State 2417
                                                    if len(subjects2) >= 1:
                                                        tmp59 = []
                                                        tmp59.append(subjects2.popleft())
                                                        while True:
                                                            if len(tmp59) > 1:
                                                                tmp60 = create_operation_expression(associative1, tmp59)
                                                            elif len(tmp59) == 1:
                                                                tmp60 = tmp59[0]
                                                            else:
                                                                assert False, "Unreachable"
                                                            subst5 = Substitution(subst4)
                                                            try:
                                                                subst5.try_add_variable('i2.2.1.1', tmp60)
                                                            except ValueError:
                                                                pass
                                                            else:
                                                                pass
                                                                if 'i2.2.0' not in subst5 or 'i2.2.1.1' not in subst5 or cons_f2(a=subst5["i2.2.0"], x=subst5["i2.2.1.1"]):
                                                                    pass
                                                                    if 'i2.2.1.0' not in subst5 or 'i2.2.1.1' not in subst5 or cons_f3(b=subst5["i2.2.1.0"], x=subst5["i2.2.1.1"]):
                                                                        pass
                                                                        if 'i2.2.1.2' not in subst5 or 'i2.2.1.1' not in subst5 or cons_f4(n=subst5["i2.2.1.2"], x=subst5["i2.2.1.1"]):
                                                                            pass
                                                                            if 'i2.2' not in subst5 or 'i2.2.1.1' not in subst5 or cons_f5(p=subst5["i2.2"], x=subst5["i2.2.1.1"]):
                                                                                pass
                                                                                # State 2418
                                                                                if len(subjects2) == 0:
                                                                                    pass
                                                                                    # State 2419
                                                                                    if len(subjects) == 0:
                                                                                        pass
                                                                                        tmp_subst = Substitution()
                                                                                        tmp_subst['x'] = subst5['i2.2.1.1']
                                                                                        tmp_subst['n'] = subst5['i2.2.1.2']
                                                                                        tmp_subst['b'] = subst5['i2.2.1.0']
                                                                                        tmp_subst['a'] = subst5['i2.2.0']
                                                                                        tmp_subst['p'] = subst5['i2.2']
                                                                                        tmp_subst['u'] = subst5['i2.0']
                                                                                        # 1: Integral(u*(a + b*x**n)**p, x) /; (cons_f2) and (cons_f3) and (cons_f4) and (cons_f5) and (cons_f6)
                                                                                        yield replacement2, tmp_subst, [(cons_f2), (cons_f3), (cons_f4), (cons_f5), (cons_f6)]
                                                            if len(subjects2) == 0:
                                                                break
                                                            tmp59.append(subjects2.popleft())
                                                        subjects2.extendleft(reversed(tmp59))
                        subjects2.appendleft(tmp56)
            if len(subjects2) >= 1 and isinstance(subjects2[0], Pow):
                tmp62 = subjects2.popleft()
                subjects63 = deque(tmp62._args)
                # State 2326
                if len(subjects63) >= 1 and isinstance(subjects63[0], Add):
                    tmp64 = subjects63.popleft()
                    associative1 = tmp64
                    associative_type1 = type(tmp64)
                    subjects65 = deque(tmp64._args)
                    matcher = CommutativeMatcher2328.get()
                    tmp66 = subjects65
                    subjects65 = []
                    for s in tmp66:
                        matcher.add_subject(s)
                    for pattern_index, subst2 in matcher.match(tmp66, subst1):
                        pass
                        if pattern_index == 0:
                            pass
                            if 'i2.2.0' not in subst2 or 'i2.2.1.1' not in subst2 or cons_f2(a=subst2["i2.2.0"], x=subst2["i2.2.1.1"]):
                                pass
                                if 'i2.2.1.0' not in subst2 or 'i2.2.1.1' not in subst2 or cons_f3(b=subst2["i2.2.1.0"], x=subst2["i2.2.1.1"]):
                                    pass
                                    if 'i2.2.1.2' not in subst2 or 'i2.2.1.1' not in subst2 or cons_f4(n=subst2["i2.2.1.2"], x=subst2["i2.2.1.1"]):
                                        pass
                                        if 'i2.2' not in subst2 or 'i2.2.1.1' not in subst2 or cons_f5(p=subst2["i2.2"], x=subst2["i2.2.1.1"]):
                                            pass
                                            if 'i2.2.0' not in subst2 or cons_f1(a=subst2["i2.2.0"]):
                                                pass
                                                # State 2345
                                                subst3 = Substitution(subst2)
                                                try:
                                                    subst3.try_add_variable('i2.2', 1)
                                                except ValueError:
                                                    pass
                                                else:
                                                    pass
                                                    if 'i2.2' not in subst3 or 'i2.2.1.1' not in subst3 or cons_f5(p=subst3["i2.2"], x=subst3["i2.2.1.1"]):
                                                        pass
                                                        # State 2346
                                                        if len(subjects63) == 0:
                                                            pass
                                                            # State 2347
                                                            if len(subjects2) >= 1:
                                                                tmp68 = subjects2.popleft()
                                                                subst4 = Substitution(subst3)
                                                                try:
                                                                    subst4.try_add_variable('i2.2.1.1', tmp68)
                                                                except ValueError:
                                                                    pass
                                                                else:
                                                                    pass
                                                                    if 'i2.2.0' not in subst4 or 'i2.2.1.1' not in subst4 or cons_f2(a=subst4["i2.2.0"], x=subst4["i2.2.1.1"]):
                                                                        pass
                                                                        if 'i2.2.1.0' not in subst4 or 'i2.2.1.1' not in subst4 or cons_f3(b=subst4["i2.2.1.0"], x=subst4["i2.2.1.1"]):
                                                                            pass
                                                                            if 'i2.2.1.2' not in subst4 or 'i2.2.1.1' not in subst4 or cons_f4(n=subst4["i2.2.1.2"], x=subst4["i2.2.1.1"]):
                                                                                pass
                                                                                if 'i2.2' not in subst4 or 'i2.2.1.1' not in subst4 or cons_f5(p=subst4["i2.2"], x=subst4["i2.2.1.1"]):
                                                                                    pass
                                                                                    # State 2348
                                                                                    if len(subjects2) == 0:
                                                                                        pass
                                                                                        # State 2349
                                                                                        if len(subjects) == 0:
                                                                                            pass
                                                                                            tmp_subst = Substitution()
                                                                                            tmp_subst['x'] = subst4['i2.2.1.1']
                                                                                            tmp_subst['n'] = subst4['i2.2.1.2']
                                                                                            tmp_subst['b'] = subst4['i2.2.1.0']
                                                                                            tmp_subst['a'] = subst4['i2.2.0']
                                                                                            tmp_subst['p'] = subst4['i2.2']
                                                                                            tmp_subst['u'] = subst4['i2.0']
                                                                                            # 0: Integral(u*(a + b*x**n)**p, x) /; (cons_f2) and (cons_f3) and (cons_f4) and (cons_f5) and (cons_f1)
                                                                                            yield replacement1, tmp_subst, [(cons_f2), (cons_f3), (cons_f4), (cons_f5), (cons_f1)]
                                                                subjects2.appendleft(tmp68)
                                                if len(subjects63) >= 1:
                                                    tmp70 = []
                                                    tmp70.append(subjects63.popleft())
                                                    while True:
                                                        if len(tmp70) > 1:
                                                            tmp71 = create_operation_expression(associative1, tmp70)
                                                        elif len(tmp70) == 1:
                                                            tmp71 = tmp70[0]
                                                        else:
                                                            assert False, "Unreachable"
                                                        subst3 = Substitution(subst2)
                                                        try:
                                                            subst3.try_add_variable('i2.2', tmp71)
                                                        except ValueError:
                                                            pass
                                                        else:
                                                            pass
                                                            if 'i2.2' not in subst3 or 'i2.2.1.1' not in subst3 or cons_f5(p=subst3["i2.2"], x=subst3["i2.2.1.1"]):
                                                                pass
                                                                # State 2346
                                                                if len(subjects63) == 0:
                                                                    pass
                                                                    # State 2347
                                                                    if len(subjects2) >= 1:
                                                                        tmp73 = subjects2.popleft()
                                                                        subst4 = Substitution(subst3)
                                                                        try:
                                                                            subst4.try_add_variable('i2.2.1.1', tmp73)
                                                                        except ValueError:
                                                                            pass
                                                                        else:
                                                                            pass
                                                                            if 'i2.2.0' not in subst4 or 'i2.2.1.1' not in subst4 or cons_f2(a=subst4["i2.2.0"], x=subst4["i2.2.1.1"]):
                                                                                pass
                                                                                if 'i2.2.1.0' not in subst4 or 'i2.2.1.1' not in subst4 or cons_f3(b=subst4["i2.2.1.0"], x=subst4["i2.2.1.1"]):
                                                                                    pass
                                                                                    if 'i2.2.1.2' not in subst4 or 'i2.2.1.1' not in subst4 or cons_f4(n=subst4["i2.2.1.2"], x=subst4["i2.2.1.1"]):
                                                                                        pass
                                                                                        if 'i2.2' not in subst4 or 'i2.2.1.1' not in subst4 or cons_f5(p=subst4["i2.2"], x=subst4["i2.2.1.1"]):
                                                                                            pass
                                                                                            # State 2348
                                                                                            if len(subjects2) == 0:
                                                                                                pass
                                                                                                # State 2349
                                                                                                if len(subjects) == 0:
                                                                                                    pass
                                                                                                    tmp_subst = Substitution()
                                                                                                    tmp_subst['x'] = subst4['i2.2.1.1']
                                                                                                    tmp_subst['n'] = subst4['i2.2.1.2']
                                                                                                    tmp_subst['b'] = subst4['i2.2.1.0']
                                                                                                    tmp_subst['a'] = subst4['i2.2.0']
                                                                                                    tmp_subst['p'] = subst4['i2.2']
                                                                                                    tmp_subst['u'] = subst4['i2.0']
                                                                                                    # 0: Integral(u*(a + b*x**n)**p, x) /; (cons_f2) and (cons_f3) and (cons_f4) and (cons_f5) and (cons_f1)
                                                                                                    yield replacement1, tmp_subst, [(cons_f2), (cons_f3), (cons_f4), (cons_f5), (cons_f1)]
                                                                        subjects2.appendleft(tmp73)
                                                        if len(subjects63) == 0:
                                                            break
                                                        tmp70.append(subjects63.popleft())
                                                    subjects63.extendleft(reversed(tmp70))
                        if pattern_index == 1:
                            pass
                            if 'i2.2.0' not in subst2 or 'i2.2.1.1' not in subst2 or cons_f2(a=subst2["i2.2.0"], x=subst2["i2.2.1.1"]):
                                pass
                                if 'i2.2.1.0' not in subst2 or 'i2.2.1.1' not in subst2 or cons_f3(b=subst2["i2.2.1.0"], x=subst2["i2.2.1.1"]):
                                    pass
                                    if 'i2.2.1.2' not in subst2 or 'i2.2.1.1' not in subst2 or cons_f4(n=subst2["i2.2.1.2"], x=subst2["i2.2.1.1"]):
                                        pass
                                        if 'i2.2' not in subst2 or 'i2.2.1.1' not in subst2 or cons_f5(p=subst2["i2.2"], x=subst2["i2.2.1.1"]):
                                            pass
                                            if 'i2.2.1.0' not in subst2 or cons_f6(b=subst2["i2.2.1.0"]):
                                                pass
                                                # State 2452
                                                subst3 = Substitution(subst2)
                                                try:
                                                    subst3.try_add_variable('i2.2', 1)
                                                except ValueError:
                                                    pass
                                                else:
                                                    pass
                                                    if 'i2.2' not in subst3 or 'i2.2.1.1' not in subst3 or cons_f5(p=subst3["i2.2"], x=subst3["i2.2.1.1"]):
                                                        pass
                                                        # State 2453
                                                        if len(subjects63) == 0:
                                                            pass
                                                            # State 2454
                                                            if len(subjects2) >= 1:
                                                                tmp76 = subjects2.popleft()
                                                                subst4 = Substitution(subst3)
                                                                try:
                                                                    subst4.try_add_variable('i2.2.1.1', tmp76)
                                                                except ValueError:
                                                                    pass
                                                                else:
                                                                    pass
                                                                    if 'i2.2.0' not in subst4 or 'i2.2.1.1' not in subst4 or cons_f2(a=subst4["i2.2.0"], x=subst4["i2.2.1.1"]):
                                                                        pass
                                                                        if 'i2.2.1.0' not in subst4 or 'i2.2.1.1' not in subst4 or cons_f3(b=subst4["i2.2.1.0"], x=subst4["i2.2.1.1"]):
                                                                            pass
                                                                            if 'i2.2.1.2' not in subst4 or 'i2.2.1.1' not in subst4 or cons_f4(n=subst4["i2.2.1.2"], x=subst4["i2.2.1.1"]):
                                                                                pass
                                                                                if 'i2.2' not in subst4 or 'i2.2.1.1' not in subst4 or cons_f5(p=subst4["i2.2"], x=subst4["i2.2.1.1"]):
                                                                                    pass
                                                                                    # State 2455
                                                                                    if len(subjects2) == 0:
                                                                                        pass
                                                                                        # State 2456
                                                                                        if len(subjects) == 0:
                                                                                            pass
                                                                                            tmp_subst = Substitution()
                                                                                            tmp_subst['x'] = subst4['i2.2.1.1']
                                                                                            tmp_subst['n'] = subst4['i2.2.1.2']
                                                                                            tmp_subst['b'] = subst4['i2.2.1.0']
                                                                                            tmp_subst['a'] = subst4['i2.2.0']
                                                                                            tmp_subst['p'] = subst4['i2.2']
                                                                                            tmp_subst['u'] = subst4['i2.0']
                                                                                            # 1: Integral(u*(a + b*x**n)**p, x) /; (cons_f2) and (cons_f3) and (cons_f4) and (cons_f5) and (cons_f6)
                                                                                            yield replacement2, tmp_subst, [(cons_f2), (cons_f3), (cons_f4), (cons_f5), (cons_f6)]
                                                                subjects2.appendleft(tmp76)
                                                if len(subjects63) >= 1:
                                                    tmp78 = []
                                                    tmp78.append(subjects63.popleft())
                                                    while True:
                                                        if len(tmp78) > 1:
                                                            tmp79 = create_operation_expression(associative1, tmp78)
                                                        elif len(tmp78) == 1:
                                                            tmp79 = tmp78[0]
                                                        else:
                                                            assert False, "Unreachable"
                                                        subst3 = Substitution(subst2)
                                                        try:
                                                            subst3.try_add_variable('i2.2', tmp79)
                                                        except ValueError:
                                                            pass
                                                        else:
                                                            pass
                                                            if 'i2.2' not in subst3 or 'i2.2.1.1' not in subst3 or cons_f5(p=subst3["i2.2"], x=subst3["i2.2.1.1"]):
                                                                pass
                                                                # State 2453
                                                                if len(subjects63) == 0:
                                                                    pass
                                                                    # State 2454
                                                                    if len(subjects2) >= 1:
                                                                        tmp81 = subjects2.popleft()
                                                                        subst4 = Substitution(subst3)
                                                                        try:
                                                                            subst4.try_add_variable('i2.2.1.1', tmp81)
                                                                        except ValueError:
                                                                            pass
                                                                        else:
                                                                            pass
                                                                            if 'i2.2.0' not in subst4 or 'i2.2.1.1' not in subst4 or cons_f2(a=subst4["i2.2.0"], x=subst4["i2.2.1.1"]):
                                                                                pass
                                                                                if 'i2.2.1.0' not in subst4 or 'i2.2.1.1' not in subst4 or cons_f3(b=subst4["i2.2.1.0"], x=subst4["i2.2.1.1"]):
                                                                                    pass
                                                                                    if 'i2.2.1.2' not in subst4 or 'i2.2.1.1' not in subst4 or cons_f4(n=subst4["i2.2.1.2"], x=subst4["i2.2.1.1"]):
                                                                                        pass
                                                                                        if 'i2.2' not in subst4 or 'i2.2.1.1' not in subst4 or cons_f5(p=subst4["i2.2"], x=subst4["i2.2.1.1"]):
                                                                                            pass
                                                                                            # State 2455
                                                                                            if len(subjects2) == 0:
                                                                                                pass
                                                                                                # State 2456
                                                                                                if len(subjects) == 0:
                                                                                                    pass
                                                                                                    tmp_subst = Substitution()
                                                                                                    tmp_subst['x'] = subst4['i2.2.1.1']
                                                                                                    tmp_subst['n'] = subst4['i2.2.1.2']
                                                                                                    tmp_subst['b'] = subst4['i2.2.1.0']
                                                                                                    tmp_subst['a'] = subst4['i2.2.0']
                                                                                                    tmp_subst['p'] = subst4['i2.2']
                                                                                                    tmp_subst['u'] = subst4['i2.0']
                                                                                                    # 1: Integral(u*(a + b*x**n)**p, x) /; (cons_f2) and (cons_f3) and (cons_f4) and (cons_f5) and (cons_f6)
                                                                                                    yield replacement2, tmp_subst, [(cons_f2), (cons_f3), (cons_f4), (cons_f5), (cons_f6)]
                                                                        subjects2.appendleft(tmp81)
                                                        if len(subjects63) == 0:
                                                            break
                                                        tmp78.append(subjects63.popleft())
                                                    subjects63.extendleft(reversed(tmp78))
                        if pattern_index == 2:
                            pass
                            if 'i2.2.0' not in subst2 or 'i2.2.1.1' not in subst2 or cons_f2(a=subst2["i2.2.0"], x=subst2["i2.2.1.1"]):
                                pass
                                if 'i2.2' not in subst2 or 'i2.2.1.1' not in subst2 or cons_f5(p=subst2["i2.2"], x=subst2["i2.2.1.1"]):
                                    pass
                                    if 'i2.2.0' not in subst2 or cons_f1(a=subst2["i2.2.0"]):
                                        pass
                                        if 'i2.2.1.0_1' not in subst2 or 'i2.2.1.1' not in subst2 or cons_f3(b=subst2["i2.2.1.0_1"], x=subst2["i2.2.1.1"]):
                                            pass
                                            if 'i2.2.1.0' not in subst2 or 'i2.2.1.1' not in subst2 or cons_f8(c=subst2["i2.2.1.0"], x=subst2["i2.2.1.1"]):
                                                pass
                                                if 'i2.2.1.2_1' not in subst2 or 'i2.2.1.1' not in subst2 or cons_f4(n=subst2["i2.2.1.2_1"], x=subst2["i2.2.1.1"]):
                                                    pass
                                                    if 'i2.2.1.2' not in subst2 or 'i2.2.1.2_1' not in subst2 or cons_f7(j=subst2["i2.2.1.2"], n=subst2["i2.2.1.2_1"]):
                                                        pass
                                                        # State 2533
                                                        subst3 = Substitution(subst2)
                                                        try:
                                                            subst3.try_add_variable('i2.2', 1)
                                                        except ValueError:
                                                            pass
                                                        else:
                                                            pass
                                                            if 'i2.2' not in subst3 or 'i2.2.1.1' not in subst3 or cons_f5(p=subst3["i2.2"], x=subst3["i2.2.1.1"]):
                                                                pass
                                                                # State 2534
                                                                if len(subjects63) == 0:
                                                                    pass
                                                                    # State 2535
                                                                    if len(subjects2) >= 1:
                                                                        tmp84 = subjects2.popleft()
                                                                        subst4 = Substitution(subst3)
                                                                        try:
                                                                            subst4.try_add_variable('i2.2.1.1', tmp84)
                                                                        except ValueError:
                                                                            pass
                                                                        else:
                                                                            pass
                                                                            if 'i2.2.0' not in subst4 or 'i2.2.1.1' not in subst4 or cons_f2(a=subst4["i2.2.0"], x=subst4["i2.2.1.1"]):
                                                                                pass
                                                                                if 'i2.2' not in subst4 or 'i2.2.1.1' not in subst4 or cons_f5(p=subst4["i2.2"], x=subst4["i2.2.1.1"]):
                                                                                    pass
                                                                                    if 'i2.2.1.0_1' not in subst4 or 'i2.2.1.1' not in subst4 or cons_f3(b=subst4["i2.2.1.0_1"], x=subst4["i2.2.1.1"]):
                                                                                        pass
                                                                                        if 'i2.2.1.0' not in subst4 or 'i2.2.1.1' not in subst4 or cons_f8(c=subst4["i2.2.1.0"], x=subst4["i2.2.1.1"]):
                                                                                            pass
                                                                                            if 'i2.2.1.2_1' not in subst4 or 'i2.2.1.1' not in subst4 or cons_f4(n=subst4["i2.2.1.2_1"], x=subst4["i2.2.1.1"]):
                                                                                                pass
                                                                                                # State 2536
                                                                                                if len(subjects2) == 0:
                                                                                                    pass
                                                                                                    # State 2537
                                                                                                    if len(subjects) == 0:
                                                                                                        pass
                                                                                                        tmp_subst = Substitution()
                                                                                                        tmp_subst['x'] = subst4['i2.2.1.1']
                                                                                                        tmp_subst['j'] = subst4['i2.2.1.2']
                                                                                                        tmp_subst['c'] = subst4['i2.2.1.0']
                                                                                                        tmp_subst['n'] = subst4['i2.2.1.2_1']
                                                                                                        tmp_subst['b'] = subst4['i2.2.1.0_1']
                                                                                                        tmp_subst['a'] = subst4['i2.2.0']
                                                                                                        tmp_subst['p'] = subst4['i2.2']
                                                                                                        tmp_subst['u'] = subst4['i2.0']
                                                                                                        # 2: Integral(u*(a + b*x**n + c*x**j)**p, x) /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f4) and (cons_f5) and (cons_f7) and (cons_f1)
                                                                                                        yield replacement3, tmp_subst, [(cons_f2), (cons_f3), (cons_f8), (cons_f4), (cons_f5), (cons_f7), (cons_f1)]
                                                                        subjects2.appendleft(tmp84)
                                                        if len(subjects63) >= 1:
                                                            tmp86 = []
                                                            tmp86.append(subjects63.popleft())
                                                            while True:
                                                                if len(tmp86) > 1:
                                                                    tmp87 = create_operation_expression(associative1, tmp86)
                                                                elif len(tmp86) == 1:
                                                                    tmp87 = tmp86[0]
                                                                else:
                                                                    assert False, "Unreachable"
                                                                subst3 = Substitution(subst2)
                                                                try:
                                                                    subst3.try_add_variable('i2.2', tmp87)
                                                                except ValueError:
                                                                    pass
                                                                else:
                                                                    pass
                                                                    if 'i2.2' not in subst3 or 'i2.2.1.1' not in subst3 or cons_f5(p=subst3["i2.2"], x=subst3["i2.2.1.1"]):
                                                                        pass
                                                                        # State 2534
                                                                        if len(subjects63) == 0:
                                                                            pass
                                                                            # State 2535
                                                                            if len(subjects2) >= 1:
                                                                                tmp89 = subjects2.popleft()
                                                                                subst4 = Substitution(subst3)
                                                                                try:
                                                                                    subst4.try_add_variable('i2.2.1.1', tmp89)
                                                                                except ValueError:
                                                                                    pass
                                                                                else:
                                                                                    pass
                                                                                    if 'i2.2.0' not in subst4 or 'i2.2.1.1' not in subst4 or cons_f2(a=subst4["i2.2.0"], x=subst4["i2.2.1.1"]):
                                                                                        pass
                                                                                        if 'i2.2' not in subst4 or 'i2.2.1.1' not in subst4 or cons_f5(p=subst4["i2.2"], x=subst4["i2.2.1.1"]):
                                                                                            pass
                                                                                            if 'i2.2.1.0_1' not in subst4 or 'i2.2.1.1' not in subst4 or cons_f3(b=subst4["i2.2.1.0_1"], x=subst4["i2.2.1.1"]):
                                                                                                pass
                                                                                                if 'i2.2.1.0' not in subst4 or 'i2.2.1.1' not in subst4 or cons_f8(c=subst4["i2.2.1.0"], x=subst4["i2.2.1.1"]):
                                                                                                    pass
                                                                                                    if 'i2.2.1.2_1' not in subst4 or 'i2.2.1.1' not in subst4 or cons_f4(n=subst4["i2.2.1.2_1"], x=subst4["i2.2.1.1"]):
                                                                                                        pass
                                                                                                        # State 2536
                                                                                                        if len(subjects2) == 0:
                                                                                                            pass
                                                                                                            # State 2537
                                                                                                            if len(subjects) == 0:
                                                                                                                pass
                                                                                                                tmp_subst = Substitution()
                                                                                                                tmp_subst['x'] = subst4['i2.2.1.1']
                                                                                                                tmp_subst['j'] = subst4['i2.2.1.2']
                                                                                                                tmp_subst['c'] = subst4['i2.2.1.0']
                                                                                                                tmp_subst['n'] = subst4['i2.2.1.2_1']
                                                                                                                tmp_subst['b'] = subst4['i2.2.1.0_1']
                                                                                                                tmp_subst['a'] = subst4['i2.2.0']
                                                                                                                tmp_subst['p'] = subst4['i2.2']
                                                                                                                tmp_subst['u'] = subst4['i2.0']
                                                                                                                # 2: Integral(u*(a + b*x**n + c*x**j)**p, x) /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f4) and (cons_f5) and (cons_f7) and (cons_f1)
                                                                                                                yield replacement3, tmp_subst, [(cons_f2), (cons_f3), (cons_f8), (cons_f4), (cons_f5), (cons_f7), (cons_f1)]
                                                                                subjects2.appendleft(tmp89)
                                                                if len(subjects63) == 0:
                                                                    break
                                                                tmp86.append(subjects63.popleft())
                                                            subjects63.extendleft(reversed(tmp86))
                        if pattern_index == 3:
                            pass
                            if 'i2.2.0' not in subst2 or 'i2.2.1.1' not in subst2 or cons_f2(a=subst2["i2.2.0"], x=subst2["i2.2.1.1"]):
                                pass
                                if 'i2.2' not in subst2 or 'i2.2.1.1' not in subst2 or cons_f5(p=subst2["i2.2"], x=subst2["i2.2.1.1"]):
                                    pass
                                    if 'i2.2.1.0_1' not in subst2 or 'i2.2.1.1' not in subst2 or cons_f3(b=subst2["i2.2.1.0_1"], x=subst2["i2.2.1.1"]):
                                        pass
                                        if 'i2.2.1.0' not in subst2 or 'i2.2.1.1' not in subst2 or cons_f8(c=subst2["i2.2.1.0"], x=subst2["i2.2.1.1"]):
                                            pass
                                            if 'i2.2.1.2_1' not in subst2 or 'i2.2.1.1' not in subst2 or cons_f4(n=subst2["i2.2.1.2_1"], x=subst2["i2.2.1.1"]):
                                                pass
                                                if 'i2.2.1.2' not in subst2 or 'i2.2.1.2_1' not in subst2 or cons_f7(j=subst2["i2.2.1.2"], n=subst2["i2.2.1.2_1"]):
                                                    pass
                                                    if 'i2.2.1.0_1' not in subst2 or cons_f6(b=subst2["i2.2.1.0_1"]):
                                                        pass
                                                        # State 2574
                                                        subst3 = Substitution(subst2)
                                                        try:
                                                            subst3.try_add_variable('i2.2', 1)
                                                        except ValueError:
                                                            pass
                                                        else:
                                                            pass
                                                            if 'i2.2' not in subst3 or 'i2.2.1.1' not in subst3 or cons_f5(p=subst3["i2.2"], x=subst3["i2.2.1.1"]):
                                                                pass
                                                                # State 2575
                                                                if len(subjects63) == 0:
                                                                    pass
                                                                    # State 2576
                                                                    if len(subjects2) >= 1:
                                                                        tmp92 = subjects2.popleft()
                                                                        subst4 = Substitution(subst3)
                                                                        try:
                                                                            subst4.try_add_variable('i2.2.1.1', tmp92)
                                                                        except ValueError:
                                                                            pass
                                                                        else:
                                                                            pass
                                                                            if 'i2.2.0' not in subst4 or 'i2.2.1.1' not in subst4 or cons_f2(a=subst4["i2.2.0"], x=subst4["i2.2.1.1"]):
                                                                                pass
                                                                                if 'i2.2' not in subst4 or 'i2.2.1.1' not in subst4 or cons_f5(p=subst4["i2.2"], x=subst4["i2.2.1.1"]):
                                                                                    pass
                                                                                    if 'i2.2.1.0_1' not in subst4 or 'i2.2.1.1' not in subst4 or cons_f3(b=subst4["i2.2.1.0_1"], x=subst4["i2.2.1.1"]):
                                                                                        pass
                                                                                        if 'i2.2.1.0' not in subst4 or 'i2.2.1.1' not in subst4 or cons_f8(c=subst4["i2.2.1.0"], x=subst4["i2.2.1.1"]):
                                                                                            pass
                                                                                            if 'i2.2.1.2_1' not in subst4 or 'i2.2.1.1' not in subst4 or cons_f4(n=subst4["i2.2.1.2_1"], x=subst4["i2.2.1.1"]):
                                                                                                pass
                                                                                                # State 2577
                                                                                                if len(subjects2) == 0:
                                                                                                    pass
                                                                                                    # State 2578
                                                                                                    if len(subjects) == 0:
                                                                                                        pass
                                                                                                        tmp_subst = Substitution()
                                                                                                        tmp_subst['x'] = subst4['i2.2.1.1']
                                                                                                        tmp_subst['j'] = subst4['i2.2.1.2']
                                                                                                        tmp_subst['c'] = subst4['i2.2.1.0']
                                                                                                        tmp_subst['n'] = subst4['i2.2.1.2_1']
                                                                                                        tmp_subst['b'] = subst4['i2.2.1.0_1']
                                                                                                        tmp_subst['a'] = subst4['i2.2.0']
                                                                                                        tmp_subst['p'] = subst4['i2.2']
                                                                                                        tmp_subst['u'] = subst4['i2.0']
                                                                                                        # 3: Integral(u*(a + b*x**n + c*x**j)**p, x) /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f4) and (cons_f5) and (cons_f7) and (cons_f6)
                                                                                                        yield replacement4, tmp_subst, [(cons_f2), (cons_f3), (cons_f8), (cons_f4), (cons_f5), (cons_f7), (cons_f6)]
                                                                        subjects2.appendleft(tmp92)
                                                        if len(subjects63) >= 1:
                                                            tmp94 = []
                                                            tmp94.append(subjects63.popleft())
                                                            while True:
                                                                if len(tmp94) > 1:
                                                                    tmp95 = create_operation_expression(associative1, tmp94)
                                                                elif len(tmp94) == 1:
                                                                    tmp95 = tmp94[0]
                                                                else:
                                                                    assert False, "Unreachable"
                                                                subst3 = Substitution(subst2)
                                                                try:
                                                                    subst3.try_add_variable('i2.2', tmp95)
                                                                except ValueError:
                                                                    pass
                                                                else:
                                                                    pass
                                                                    if 'i2.2' not in subst3 or 'i2.2.1.1' not in subst3 or cons_f5(p=subst3["i2.2"], x=subst3["i2.2.1.1"]):
                                                                        pass
                                                                        # State 2575
                                                                        if len(subjects63) == 0:
                                                                            pass
                                                                            # State 2576
                                                                            if len(subjects2) >= 1:
                                                                                tmp97 = subjects2.popleft()
                                                                                subst4 = Substitution(subst3)
                                                                                try:
                                                                                    subst4.try_add_variable('i2.2.1.1', tmp97)
                                                                                except ValueError:
                                                                                    pass
                                                                                else:
                                                                                    pass
                                                                                    if 'i2.2.0' not in subst4 or 'i2.2.1.1' not in subst4 or cons_f2(a=subst4["i2.2.0"], x=subst4["i2.2.1.1"]):
                                                                                        pass
                                                                                        if 'i2.2' not in subst4 or 'i2.2.1.1' not in subst4 or cons_f5(p=subst4["i2.2"], x=subst4["i2.2.1.1"]):
                                                                                            pass
                                                                                            if 'i2.2.1.0_1' not in subst4 or 'i2.2.1.1' not in subst4 or cons_f3(b=subst4["i2.2.1.0_1"], x=subst4["i2.2.1.1"]):
                                                                                                pass
                                                                                                if 'i2.2.1.0' not in subst4 or 'i2.2.1.1' not in subst4 or cons_f8(c=subst4["i2.2.1.0"], x=subst4["i2.2.1.1"]):
                                                                                                    pass
                                                                                                    if 'i2.2.1.2_1' not in subst4 or 'i2.2.1.1' not in subst4 or cons_f4(n=subst4["i2.2.1.2_1"], x=subst4["i2.2.1.1"]):
                                                                                                        pass
                                                                                                        # State 2577
                                                                                                        if len(subjects2) == 0:
                                                                                                            pass
                                                                                                            # State 2578
                                                                                                            if len(subjects) == 0:
                                                                                                                pass
                                                                                                                tmp_subst = Substitution()
                                                                                                                tmp_subst['x'] = subst4['i2.2.1.1']
                                                                                                                tmp_subst['j'] = subst4['i2.2.1.2']
                                                                                                                tmp_subst['c'] = subst4['i2.2.1.0']
                                                                                                                tmp_subst['n'] = subst4['i2.2.1.2_1']
                                                                                                                tmp_subst['b'] = subst4['i2.2.1.0_1']
                                                                                                                tmp_subst['a'] = subst4['i2.2.0']
                                                                                                                tmp_subst['p'] = subst4['i2.2']
                                                                                                                tmp_subst['u'] = subst4['i2.0']
                                                                                                                # 3: Integral(u*(a + b*x**n + c*x**j)**p, x) /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f4) and (cons_f5) and (cons_f7) and (cons_f6)
                                                                                                                yield replacement4, tmp_subst, [(cons_f2), (cons_f3), (cons_f8), (cons_f4), (cons_f5), (cons_f7), (cons_f6)]
                                                                                subjects2.appendleft(tmp97)
                                                                if len(subjects63) == 0:
                                                                    break
                                                                tmp94.append(subjects63.popleft())
                                                            subjects63.extendleft(reversed(tmp94))
                        if pattern_index == 4:
                            pass
                            if 'i2.2.0' not in subst2 or 'i2.2.1.1' not in subst2 or cons_f2(a=subst2["i2.2.0"], x=subst2["i2.2.1.1"]):
                                pass
                                if 'i2.2' not in subst2 or 'i2.2.1.1' not in subst2 or cons_f5(p=subst2["i2.2"], x=subst2["i2.2.1.1"]):
                                    pass
                                    if 'i2.2.1.0_1' not in subst2 or 'i2.2.1.1' not in subst2 or cons_f3(b=subst2["i2.2.1.0_1"], x=subst2["i2.2.1.1"]):
                                        pass
                                        if 'i2.2.1.0' not in subst2 or 'i2.2.1.1' not in subst2 or cons_f8(c=subst2["i2.2.1.0"], x=subst2["i2.2.1.1"]):
                                            pass
                                            if 'i2.2.1.2_1' not in subst2 or 'i2.2.1.1' not in subst2 or cons_f4(n=subst2["i2.2.1.2_1"], x=subst2["i2.2.1.1"]):
                                                pass
                                                if 'i2.2.1.2' not in subst2 or 'i2.2.1.2_1' not in subst2 or cons_f7(j=subst2["i2.2.1.2"], n=subst2["i2.2.1.2_1"]):
                                                    pass
                                                    if 'i2.2.1.0' not in subst2 or cons_f9(c=subst2["i2.2.1.0"]):
                                                        pass
                                                        # State 2589
                                                        subst3 = Substitution(subst2)
                                                        try:
                                                            subst3.try_add_variable('i2.2', 1)
                                                        except ValueError:
                                                            pass
                                                        else:
                                                            pass
                                                            if 'i2.2' not in subst3 or 'i2.2.1.1' not in subst3 or cons_f5(p=subst3["i2.2"], x=subst3["i2.2.1.1"]):
                                                                pass
                                                                # State 2590
                                                                if len(subjects63) == 0:
                                                                    pass
                                                                    # State 2591
                                                                    if len(subjects2) >= 1:
                                                                        tmp100 = subjects2.popleft()
                                                                        subst4 = Substitution(subst3)
                                                                        try:
                                                                            subst4.try_add_variable('i2.2.1.1', tmp100)
                                                                        except ValueError:
                                                                            pass
                                                                        else:
                                                                            pass
                                                                            if 'i2.2.0' not in subst4 or 'i2.2.1.1' not in subst4 or cons_f2(a=subst4["i2.2.0"], x=subst4["i2.2.1.1"]):
                                                                                pass
                                                                                if 'i2.2' not in subst4 or 'i2.2.1.1' not in subst4 or cons_f5(p=subst4["i2.2"], x=subst4["i2.2.1.1"]):
                                                                                    pass
                                                                                    if 'i2.2.1.0_1' not in subst4 or 'i2.2.1.1' not in subst4 or cons_f3(b=subst4["i2.2.1.0_1"], x=subst4["i2.2.1.1"]):
                                                                                        pass
                                                                                        if 'i2.2.1.0' not in subst4 or 'i2.2.1.1' not in subst4 or cons_f8(c=subst4["i2.2.1.0"], x=subst4["i2.2.1.1"]):
                                                                                            pass
                                                                                            if 'i2.2.1.2_1' not in subst4 or 'i2.2.1.1' not in subst4 or cons_f4(n=subst4["i2.2.1.2_1"], x=subst4["i2.2.1.1"]):
                                                                                                pass
                                                                                                # State 2592
                                                                                                if len(subjects2) == 0:
                                                                                                    pass
                                                                                                    # State 2593
                                                                                                    if len(subjects) == 0:
                                                                                                        pass
                                                                                                        tmp_subst = Substitution()
                                                                                                        tmp_subst['x'] = subst4['i2.2.1.1']
                                                                                                        tmp_subst['j'] = subst4['i2.2.1.2']
                                                                                                        tmp_subst['c'] = subst4['i2.2.1.0']
                                                                                                        tmp_subst['n'] = subst4['i2.2.1.2_1']
                                                                                                        tmp_subst['b'] = subst4['i2.2.1.0_1']
                                                                                                        tmp_subst['a'] = subst4['i2.2.0']
                                                                                                        tmp_subst['p'] = subst4['i2.2']
                                                                                                        tmp_subst['u'] = subst4['i2.0']
                                                                                                        # 4: Integral(u*(a + b*x**n + c*x**j)**p, x) /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f4) and (cons_f5) and (cons_f7) and (cons_f9)
                                                                                                        yield replacement5, tmp_subst, [(cons_f2), (cons_f3), (cons_f8), (cons_f4), (cons_f5), (cons_f7), (cons_f9)]
                                                                        subjects2.appendleft(tmp100)
                                                        if len(subjects63) >= 1:
                                                            tmp102 = []
                                                            tmp102.append(subjects63.popleft())
                                                            while True:
                                                                if len(tmp102) > 1:
                                                                    tmp103 = create_operation_expression(associative1, tmp102)
                                                                elif len(tmp102) == 1:
                                                                    tmp103 = tmp102[0]
                                                                else:
                                                                    assert False, "Unreachable"
                                                                subst3 = Substitution(subst2)
                                                                try:
                                                                    subst3.try_add_variable('i2.2', tmp103)
                                                                except ValueError:
                                                                    pass
                                                                else:
                                                                    pass
                                                                    if 'i2.2' not in subst3 or 'i2.2.1.1' not in subst3 or cons_f5(p=subst3["i2.2"], x=subst3["i2.2.1.1"]):
                                                                        pass
                                                                        # State 2590
                                                                        if len(subjects63) == 0:
                                                                            pass
                                                                            # State 2591
                                                                            if len(subjects2) >= 1:
                                                                                tmp105 = subjects2.popleft()
                                                                                subst4 = Substitution(subst3)
                                                                                try:
                                                                                    subst4.try_add_variable('i2.2.1.1', tmp105)
                                                                                except ValueError:
                                                                                    pass
                                                                                else:
                                                                                    pass
                                                                                    if 'i2.2.0' not in subst4 or 'i2.2.1.1' not in subst4 or cons_f2(a=subst4["i2.2.0"], x=subst4["i2.2.1.1"]):
                                                                                        pass
                                                                                        if 'i2.2' not in subst4 or 'i2.2.1.1' not in subst4 or cons_f5(p=subst4["i2.2"], x=subst4["i2.2.1.1"]):
                                                                                            pass
                                                                                            if 'i2.2.1.0_1' not in subst4 or 'i2.2.1.1' not in subst4 or cons_f3(b=subst4["i2.2.1.0_1"], x=subst4["i2.2.1.1"]):
                                                                                                pass
                                                                                                if 'i2.2.1.0' not in subst4 or 'i2.2.1.1' not in subst4 or cons_f8(c=subst4["i2.2.1.0"], x=subst4["i2.2.1.1"]):
                                                                                                    pass
                                                                                                    if 'i2.2.1.2_1' not in subst4 or 'i2.2.1.1' not in subst4 or cons_f4(n=subst4["i2.2.1.2_1"], x=subst4["i2.2.1.1"]):
                                                                                                        pass
                                                                                                        # State 2592
                                                                                                        if len(subjects2) == 0:
                                                                                                            pass
                                                                                                            # State 2593
                                                                                                            if len(subjects) == 0:
                                                                                                                pass
                                                                                                                tmp_subst = Substitution()
                                                                                                                tmp_subst['x'] = subst4['i2.2.1.1']
                                                                                                                tmp_subst['j'] = subst4['i2.2.1.2']
                                                                                                                tmp_subst['c'] = subst4['i2.2.1.0']
                                                                                                                tmp_subst['n'] = subst4['i2.2.1.2_1']
                                                                                                                tmp_subst['b'] = subst4['i2.2.1.0_1']
                                                                                                                tmp_subst['a'] = subst4['i2.2.0']
                                                                                                                tmp_subst['p'] = subst4['i2.2']
                                                                                                                tmp_subst['u'] = subst4['i2.0']
                                                                                                                # 4: Integral(u*(a + b*x**n + c*x**j)**p, x) /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f4) and (cons_f5) and (cons_f7) and (cons_f9)
                                                                                                                yield replacement5, tmp_subst, [(cons_f2), (cons_f3), (cons_f8), (cons_f4), (cons_f5), (cons_f7), (cons_f9)]
                                                                                subjects2.appendleft(tmp105)
                                                                if len(subjects63) == 0:
                                                                    break
                                                                tmp102.append(subjects63.popleft())
                                                            subjects63.extendleft(reversed(tmp102))
                        if pattern_index == 5:
                            pass
                            if 'i2' not in subst2 or 'i2.2.1.0_1' not in subst2 or cons_f2(a=subst2["i2.2.1.0_1"], x=subst2["i2"]):
                                pass
                                if 'i2.2.1.0_2' not in subst2 or 'i2' not in subst2 or cons_f3(b=subst2["i2.2.1.0_2"], x=subst2["i2"]):
                                    pass
                                    if 'i2' not in subst2 or 'i2.2.1.0' not in subst2 or cons_f10(v=subst2["i2.2.1.0"], x=subst2["i2"]):
                                        pass
                                        # State 2614
                                        subst3 = Substitution(subst2)
                                        try:
                                            subst3.try_add_variable('i2.2', 1)
                                        except ValueError:
                                            pass
                                        else:
                                            pass
                                            # State 2615
                                            if len(subjects63) == 0:
                                                pass
                                                # State 2616
                                                if len(subjects2) >= 1:
                                                    tmp108 = subjects2.popleft()
                                                    subst4 = Substitution(subst3)
                                                    try:
                                                        subst4.try_add_variable('i2', tmp108)
                                                    except ValueError:
                                                        pass
                                                    else:
                                                        pass
                                                        if 'i2' not in subst4 or 'i2.2.1.0_1' not in subst4 or cons_f2(a=subst4["i2.2.1.0_1"], x=subst4["i2"]):
                                                            pass
                                                            if 'i2.2.1.0_2' not in subst4 or 'i2' not in subst4 or cons_f3(b=subst4["i2.2.1.0_2"], x=subst4["i2"]):
                                                                pass
                                                                if 'i2' not in subst4 or 'i2.2.1.0' not in subst4 or cons_f10(v=subst4["i2.2.1.0"], x=subst4["i2"]):
                                                                    pass
                                                                    # State 2617
                                                                    if len(subjects2) == 0:
                                                                        pass
                                                                        # State 2618
                                                                        if len(subjects) == 0:
                                                                            pass
                                                                            tmp_subst = Substitution()
                                                                            tmp_subst['v'] = subst4['i2.2.1.0']
                                                                            tmp_subst['a'] = subst4['i2.2.1.0_1']
                                                                            tmp_subst['b'] = subst4['i2.2.1.0_2']
                                                                            tmp_subst['w'] = subst4['i2.2.0']
                                                                            tmp_subst['p'] = subst4['i2.2']
                                                                            tmp_subst['u'] = subst4['i2.0']
                                                                            tmp_subst['x'] = subst4['i2']
                                                                            # 5: Integral(u*(a*v + b*v + w)**p, x) /; (cons_f2) and (cons_f3) and (cons_f10)
                                                                            yield replacement6, tmp_subst, [(cons_f2), (cons_f3), (cons_f10)]
                                                    subjects2.appendleft(tmp108)
                                        if len(subjects63) >= 1:
                                            tmp110 = []
                                            tmp110.append(subjects63.popleft())
                                            while True:
                                                if len(tmp110) > 1:
                                                    tmp111 = create_operation_expression(associative1, tmp110)
                                                elif len(tmp110) == 1:
                                                    tmp111 = tmp110[0]
                                                else:
                                                    assert False, "Unreachable"
                                                subst3 = Substitution(subst2)
                                                try:
                                                    subst3.try_add_variable('i2.2', tmp111)
                                                except ValueError:
                                                    pass
                                                else:
                                                    pass
                                                    # State 2615
                                                    if len(subjects63) == 0:
                                                        pass
                                                        # State 2616
                                                        if len(subjects2) >= 1:
                                                            tmp113 = subjects2.popleft()
                                                            subst4 = Substitution(subst3)
                                                            try:
                                                                subst4.try_add_variable('i2', tmp113)
                                                            except ValueError:
                                                                pass
                                                            else:
                                                                pass
                                                                if 'i2' not in subst4 or 'i2.2.1.0_1' not in subst4 or cons_f2(a=subst4["i2.2.1.0_1"], x=subst4["i2"]):
                                                                    pass
                                                                    if 'i2.2.1.0_2' not in subst4 or 'i2' not in subst4 or cons_f3(b=subst4["i2.2.1.0_2"], x=subst4["i2"]):
                                                                        pass
                                                                        if 'i2' not in subst4 or 'i2.2.1.0' not in subst4 or cons_f10(v=subst4["i2.2.1.0"], x=subst4["i2"]):
                                                                            pass
                                                                            # State 2617
                                                                            if len(subjects2) == 0:
                                                                                pass
                                                                                # State 2618
                                                                                if len(subjects) == 0:
                                                                                    pass
                                                                                    tmp_subst = Substitution()
                                                                                    tmp_subst['v'] = subst4['i2.2.1.0']
                                                                                    tmp_subst['a'] = subst4['i2.2.1.0_1']
                                                                                    tmp_subst['b'] = subst4['i2.2.1.0_2']
                                                                                    tmp_subst['w'] = subst4['i2.2.0']
                                                                                    tmp_subst['p'] = subst4['i2.2']
                                                                                    tmp_subst['u'] = subst4['i2.0']
                                                                                    tmp_subst['x'] = subst4['i2']
                                                                                    # 5: Integral(u*(a*v + b*v + w)**p, x) /; (cons_f2) and (cons_f3) and (cons_f10)
                                                                                    yield replacement6, tmp_subst, [(cons_f2), (cons_f3), (cons_f10)]
                                                            subjects2.appendleft(tmp113)
                                                if len(subjects63) == 0:
                                                    break
                                                tmp110.append(subjects63.popleft())
                                            subjects63.extendleft(reversed(tmp110))
                        if pattern_index == 6:
                            pass
                            if 'i2.2.0' not in subst2 or 'i2.2.1.1' not in subst2 or cons_f2(a=subst2["i2.2.0"], x=subst2["i2.2.1.1"]):
                                pass
                                if 'i2.2.1.0_1' not in subst2 or 'i2.2.1.1' not in subst2 or cons_f3(b=subst2["i2.2.1.0_1"], x=subst2["i2.2.1.1"]):
                                    pass
                                    if 'i2.2.1.0' not in subst2 or 'i2.2.1.1' not in subst2 or cons_f8(c=subst2["i2.2.1.0"], x=subst2["i2.2.1.1"]):
                                        pass
                                        if 'i2.2.1.0' not in subst2 or 'i2.2.1.0_1' not in subst2 or 'i2.2.0' not in subst2 or cons_f47(a=subst2["i2.2.0"], b=subst2["i2.2.1.0_1"], c=subst2["i2.2.1.0"]):
                                            pass
                                            # State 2859
                                            subst3 = Substitution(subst2)
                                            try:
                                                subst3.try_add_variable('i2.2', 1)
                                            except ValueError:
                                                pass
                                            else:
                                                pass
                                                if 'i2.2' not in subst3 or cons_f40(p=subst3["i2.2"]):
                                                    pass
                                                    # State 2860
                                                    if len(subjects63) == 0:
                                                        pass
                                                        # State 2861
                                                        if len(subjects2) >= 1:
                                                            tmp116 = subjects2.popleft()
                                                            subst4 = Substitution(subst3)
                                                            try:
                                                                subst4.try_add_variable('i2.2.1.1', tmp116)
                                                            except ValueError:
                                                                pass
                                                            else:
                                                                pass
                                                                if 'i2.2.0' not in subst4 or 'i2.2.1.1' not in subst4 or cons_f2(a=subst4["i2.2.0"], x=subst4["i2.2.1.1"]):
                                                                    pass
                                                                    if 'i2.2.1.0_1' not in subst4 or 'i2.2.1.1' not in subst4 or cons_f3(b=subst4["i2.2.1.0_1"], x=subst4["i2.2.1.1"]):
                                                                        pass
                                                                        if 'i2.2.1.0' not in subst4 or 'i2.2.1.1' not in subst4 or cons_f8(c=subst4["i2.2.1.0"], x=subst4["i2.2.1.1"]):
                                                                            pass
                                                                            # State 2862
                                                                            if len(subjects2) == 0:
                                                                                pass
                                                                                # State 2863
                                                                                if len(subjects) == 0:
                                                                                    pass
                                                                                    tmp_subst = Substitution()
                                                                                    tmp_subst['x'] = subst4['i2.2.1.1']
                                                                                    tmp_subst['c'] = subst4['i2.2.1.0']
                                                                                    tmp_subst['b'] = subst4['i2.2.1.0_1']
                                                                                    tmp_subst['a'] = subst4['i2.2.0']
                                                                                    tmp_subst['p'] = subst4['i2.2']
                                                                                    tmp_subst['u'] = subst4['i2.0']
                                                                                    # 26: Integral(u*(a + b*x + c*x**2)**p, x) /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f47) and (cons_f40)
                                                                                    yield replacement27, tmp_subst, [(cons_f2), (cons_f3), (cons_f8), (cons_f47), (cons_f40)]
                                                            subjects2.appendleft(tmp116)
                                            if len(subjects63) >= 1:
                                                tmp118 = []
                                                tmp118.append(subjects63.popleft())
                                                while True:
                                                    if len(tmp118) > 1:
                                                        tmp119 = create_operation_expression(associative1, tmp118)
                                                    elif len(tmp118) == 1:
                                                        tmp119 = tmp118[0]
                                                    else:
                                                        assert False, "Unreachable"
                                                    subst3 = Substitution(subst2)
                                                    try:
                                                        subst3.try_add_variable('i2.2', tmp119)
                                                    except ValueError:
                                                        pass
                                                    else:
                                                        pass
                                                        if 'i2.2' not in subst3 or cons_f40(p=subst3["i2.2"]):
                                                            pass
                                                            # State 2860
                                                            if len(subjects63) == 0:
                                                                pass
                                                                # State 2861
                                                                if len(subjects2) >= 1:
                                                                    tmp121 = subjects2.popleft()
                                                                    subst4 = Substitution(subst3)
                                                                    try:
                                                                        subst4.try_add_variable('i2.2.1.1', tmp121)
                                                                    except ValueError:
                                                                        pass
                                                                    else:
                                                                        pass
                                                                        if 'i2.2.0' not in subst4 or 'i2.2.1.1' not in subst4 or cons_f2(a=subst4["i2.2.0"], x=subst4["i2.2.1.1"]):
                                                                            pass
                                                                            if 'i2.2.1.0_1' not in subst4 or 'i2.2.1.1' not in subst4 or cons_f3(b=subst4["i2.2.1.0_1"], x=subst4["i2.2.1.1"]):
                                                                                pass
                                                                                if 'i2.2.1.0' not in subst4 or 'i2.2.1.1' not in subst4 or cons_f8(c=subst4["i2.2.1.0"], x=subst4["i2.2.1.1"]):
                                                                                    pass
                                                                                    # State 2862
                                                                                    if len(subjects2) == 0:
                                                                                        pass
                                                                                        # State 2863
                                                                                        if len(subjects) == 0:
                                                                                            pass
                                                                                            tmp_subst = Substitution()
                                                                                            tmp_subst['x'] = subst4['i2.2.1.1']
                                                                                            tmp_subst['c'] = subst4['i2.2.1.0']
                                                                                            tmp_subst['b'] = subst4['i2.2.1.0_1']
                                                                                            tmp_subst['a'] = subst4['i2.2.0']
                                                                                            tmp_subst['p'] = subst4['i2.2']
                                                                                            tmp_subst['u'] = subst4['i2.0']
                                                                                            # 26: Integral(u*(a + b*x + c*x**2)**p, x) /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f47) and (cons_f40)
                                                                                            yield replacement27, tmp_subst, [(cons_f2), (cons_f3), (cons_f8), (cons_f47), (cons_f40)]
                                                                    subjects2.appendleft(tmp121)
                                                    if len(subjects63) == 0:
                                                        break
                                                    tmp118.append(subjects63.popleft())
                                                subjects63.extendleft(reversed(tmp118))
                        if pattern_index == 7:
                            pass
                            if 'i2.2.0' not in subst2 or 'i2.2.1.1' not in subst2 or cons_f2(a=subst2["i2.2.0"], x=subst2["i2.2.1.1"]):
                                pass
                                if 'i2.2.1.0' not in subst2 or 'i2.2.1.1' not in subst2 or cons_f3(b=subst2["i2.2.1.0"], x=subst2["i2.2.1.1"]):
                                    pass
                                    if 'i2.2.1.2' not in subst2 or 'i2.2.1.1' not in subst2 or cons_f4(n=subst2["i2.2.1.2"], x=subst2["i2.2.1.1"]):
                                        pass
                                        if 'i2.2.1.0_1' not in subst2 or 'i2.2.1.1' not in subst2 or cons_f8(c=subst2["i2.2.1.0_1"], x=subst2["i2.2.1.1"]):
                                            pass
                                            if 'i2.2.1.2' not in subst2 or 'i2.2.1.2_1' not in subst2 or cons_f48(n=subst2["i2.2.1.2"], n2=subst2["i2.2.1.2_1"]):
                                                pass
                                                if 'i2.2.1.0_1' not in subst2 or 'i2.2.1.0' not in subst2 or 'i2.2.0' not in subst2 or cons_f47(a=subst2["i2.2.0"], b=subst2["i2.2.1.0"], c=subst2["i2.2.1.0_1"]):
                                                    pass
                                                    # State 2900
                                                    subst3 = Substitution(subst2)
                                                    try:
                                                        subst3.try_add_variable('i2.2', 1)
                                                    except ValueError:
                                                        pass
                                                    else:
                                                        pass
                                                        if 'i2.2' not in subst3 or cons_f40(p=subst3["i2.2"]):
                                                            pass
                                                            # State 2901
                                                            if len(subjects63) == 0:
                                                                pass
                                                                # State 2902
                                                                if len(subjects2) >= 1:
                                                                    tmp124 = subjects2.popleft()
                                                                    subst4 = Substitution(subst3)
                                                                    try:
                                                                        subst4.try_add_variable('i2.2.1.1', tmp124)
                                                                    except ValueError:
                                                                        pass
                                                                    else:
                                                                        pass
                                                                        if 'i2.2.0' not in subst4 or 'i2.2.1.1' not in subst4 or cons_f2(a=subst4["i2.2.0"], x=subst4["i2.2.1.1"]):
                                                                            pass
                                                                            if 'i2.2.1.0' not in subst4 or 'i2.2.1.1' not in subst4 or cons_f3(b=subst4["i2.2.1.0"], x=subst4["i2.2.1.1"]):
                                                                                pass
                                                                                if 'i2.2.1.2' not in subst4 or 'i2.2.1.1' not in subst4 or cons_f4(n=subst4["i2.2.1.2"], x=subst4["i2.2.1.1"]):
                                                                                    pass
                                                                                    if 'i2.2.1.0_1' not in subst4 or 'i2.2.1.1' not in subst4 or cons_f8(c=subst4["i2.2.1.0_1"], x=subst4["i2.2.1.1"]):
                                                                                        pass
                                                                                        # State 2903
                                                                                        if len(subjects2) == 0:
                                                                                            pass
                                                                                            # State 2904
                                                                                            if len(subjects) == 0:
                                                                                                pass
                                                                                                tmp_subst = Substitution()
                                                                                                tmp_subst['x'] = subst4['i2.2.1.1']
                                                                                                tmp_subst['n'] = subst4['i2.2.1.2']
                                                                                                tmp_subst['b'] = subst4['i2.2.1.0']
                                                                                                tmp_subst['n2'] = subst4['i2.2.1.2_1']
                                                                                                tmp_subst['c'] = subst4['i2.2.1.0_1']
                                                                                                tmp_subst['a'] = subst4['i2.2.0']
                                                                                                tmp_subst['p'] = subst4['i2.2']
                                                                                                tmp_subst['u'] = subst4['i2.0']
                                                                                                # 27: Integral(u*(a + b*x**n + c*x**n2)**p, x) /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f4) and (cons_f48) and (cons_f47) and (cons_f40)
                                                                                                yield replacement28, tmp_subst, [(cons_f2), (cons_f3), (cons_f8), (cons_f4), (cons_f48), (cons_f47), (cons_f40)]
                                                                    subjects2.appendleft(tmp124)
                                                    if len(subjects63) >= 1:
                                                        tmp126 = []
                                                        tmp126.append(subjects63.popleft())
                                                        while True:
                                                            if len(tmp126) > 1:
                                                                tmp127 = create_operation_expression(associative1, tmp126)
                                                            elif len(tmp126) == 1:
                                                                tmp127 = tmp126[0]
                                                            else:
                                                                assert False, "Unreachable"
                                                            subst3 = Substitution(subst2)
                                                            try:
                                                                subst3.try_add_variable('i2.2', tmp127)
                                                            except ValueError:
                                                                pass
                                                            else:
                                                                pass
                                                                if 'i2.2' not in subst3 or cons_f40(p=subst3["i2.2"]):
                                                                    pass
                                                                    # State 2901
                                                                    if len(subjects63) == 0:
                                                                        pass
                                                                        # State 2902
                                                                        if len(subjects2) >= 1:
                                                                            tmp129 = subjects2.popleft()
                                                                            subst4 = Substitution(subst3)
                                                                            try:
                                                                                subst4.try_add_variable('i2.2.1.1', tmp129)
                                                                            except ValueError:
                                                                                pass
                                                                            else:
                                                                                pass
                                                                                if 'i2.2.0' not in subst4 or 'i2.2.1.1' not in subst4 or cons_f2(a=subst4["i2.2.0"], x=subst4["i2.2.1.1"]):
                                                                                    pass
                                                                                    if 'i2.2.1.0' not in subst4 or 'i2.2.1.1' not in subst4 or cons_f3(b=subst4["i2.2.1.0"], x=subst4["i2.2.1.1"]):
                                                                                        pass
                                                                                        if 'i2.2.1.2' not in subst4 or 'i2.2.1.1' not in subst4 or cons_f4(n=subst4["i2.2.1.2"], x=subst4["i2.2.1.1"]):
                                                                                            pass
                                                                                            if 'i2.2.1.0_1' not in subst4 or 'i2.2.1.1' not in subst4 or cons_f8(c=subst4["i2.2.1.0_1"], x=subst4["i2.2.1.1"]):
                                                                                                pass
                                                                                                # State 2903
                                                                                                if len(subjects2) == 0:
                                                                                                    pass
                                                                                                    # State 2904
                                                                                                    if len(subjects) == 0:
                                                                                                        pass
                                                                                                        tmp_subst = Substitution()
                                                                                                        tmp_subst['x'] = subst4['i2.2.1.1']
                                                                                                        tmp_subst['n'] = subst4['i2.2.1.2']
                                                                                                        tmp_subst['b'] = subst4['i2.2.1.0']
                                                                                                        tmp_subst['n2'] = subst4['i2.2.1.2_1']
                                                                                                        tmp_subst['c'] = subst4['i2.2.1.0_1']
                                                                                                        tmp_subst['a'] = subst4['i2.2.0']
                                                                                                        tmp_subst['p'] = subst4['i2.2']
                                                                                                        tmp_subst['u'] = subst4['i2.0']
                                                                                                        # 27: Integral(u*(a + b*x**n + c*x**n2)**p, x) /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f4) and (cons_f48) and (cons_f47) and (cons_f40)
                                                                                                        yield replacement28, tmp_subst, [(cons_f2), (cons_f3), (cons_f8), (cons_f4), (cons_f48), (cons_f47), (cons_f40)]
                                                                            subjects2.appendleft(tmp129)
                                                            if len(subjects63) == 0:
                                                                break
                                                            tmp126.append(subjects63.popleft())
                                                        subjects63.extendleft(reversed(tmp126))
                        if pattern_index == 8:
                            pass
                            if 'i2.2.1.0_1' not in subst2 or 'i2.2.1.1' not in subst2 or cons_f3(b=subst2["i2.2.1.0_1"], x=subst2["i2.2.1.1"]):
                                pass
                                if 'i2.2.1.0' not in subst2 or 'i2.2.1.1' not in subst2 or cons_f2(a=subst2["i2.2.1.0"], x=subst2["i2.2.1.1"]):
                                    pass
                                    if 'i2.2.1.2' not in subst2 or 'i2.2.1.1' not in subst2 or cons_f5(p=subst2["i2.2.1.2"], x=subst2["i2.2.1.1"]):
                                        pass
                                        if 'i2.2.1.2_1' not in subst2 or 'i2.2.1.1' not in subst2 or cons_f52(q=subst2["i2.2.1.2_1"], x=subst2["i2.2.1.1"]):
                                            pass
                                            if 'i2.2.1.2' not in subst2 or 'i2.2.1.2_1' not in subst2 or cons_f51(p=subst2["i2.2.1.2"], q=subst2["i2.2.1.2_1"]):
                                                pass
                                                # State 2935
                                                subst3 = Substitution(subst2)
                                                try:
                                                    subst3.try_add_variable('i2.2', 1)
                                                except ValueError:
                                                    pass
                                                else:
                                                    pass
                                                    if 'i2.2' not in subst3 or cons_f20(m=subst3["i2.2"]):
                                                        pass
                                                        # State 2936
                                                        if len(subjects63) == 0:
                                                            pass
                                                            # State 2937
                                                            if len(subjects2) >= 1:
                                                                tmp132 = subjects2.popleft()
                                                                subst4 = Substitution(subst3)
                                                                try:
                                                                    subst4.try_add_variable('i2.2.1.1', tmp132)
                                                                except ValueError:
                                                                    pass
                                                                else:
                                                                    pass
                                                                    if 'i2.2.1.0_1' not in subst4 or 'i2.2.1.1' not in subst4 or cons_f3(b=subst4["i2.2.1.0_1"], x=subst4["i2.2.1.1"]):
                                                                        pass
                                                                        if 'i2.2.1.0' not in subst4 or 'i2.2.1.1' not in subst4 or cons_f2(a=subst4["i2.2.1.0"], x=subst4["i2.2.1.1"]):
                                                                            pass
                                                                            if 'i2.2.1.2' not in subst4 or 'i2.2.1.1' not in subst4 or cons_f5(p=subst4["i2.2.1.2"], x=subst4["i2.2.1.1"]):
                                                                                pass
                                                                                if 'i2.2.1.2_1' not in subst4 or 'i2.2.1.1' not in subst4 or cons_f52(q=subst4["i2.2.1.2_1"], x=subst4["i2.2.1.1"]):
                                                                                    pass
                                                                                    # State 2938
                                                                                    if len(subjects2) == 0:
                                                                                        pass
                                                                                        # State 2939
                                                                                        if len(subjects) == 0:
                                                                                            pass
                                                                                            tmp_subst = Substitution()
                                                                                            tmp_subst['x'] = subst4['i2.2.1.1']
                                                                                            tmp_subst['p'] = subst4['i2.2.1.2']
                                                                                            tmp_subst['a'] = subst4['i2.2.1.0']
                                                                                            tmp_subst['q'] = subst4['i2.2.1.2_1']
                                                                                            tmp_subst['b'] = subst4['i2.2.1.0_1']
                                                                                            tmp_subst['m'] = subst4['i2.2']
                                                                                            tmp_subst['u'] = subst4['i2.0']
                                                                                            # 29: Integral(u*(a*x**p + b*x**q)**m, x) /; (cons_f2) and (cons_f3) and (cons_f5) and (cons_f52) and (cons_f20) and (cons_f51)
                                                                                            yield replacement30, tmp_subst, [(cons_f2), (cons_f3), (cons_f5), (cons_f52), (cons_f20), (cons_f51)]
                                                                subjects2.appendleft(tmp132)
                                                if len(subjects63) >= 1:
                                                    tmp134 = []
                                                    tmp134.append(subjects63.popleft())
                                                    while True:
                                                        if len(tmp134) > 1:
                                                            tmp135 = create_operation_expression(associative1, tmp134)
                                                        elif len(tmp134) == 1:
                                                            tmp135 = tmp134[0]
                                                        else:
                                                            assert False, "Unreachable"
                                                        subst3 = Substitution(subst2)
                                                        try:
                                                            subst3.try_add_variable('i2.2', tmp135)
                                                        except ValueError:
                                                            pass
                                                        else:
                                                            pass
                                                            if 'i2.2' not in subst3 or cons_f20(m=subst3["i2.2"]):
                                                                pass
                                                                # State 2936
                                                                if len(subjects63) == 0:
                                                                    pass
                                                                    # State 2937
                                                                    if len(subjects2) >= 1:
                                                                        tmp137 = subjects2.popleft()
                                                                        subst4 = Substitution(subst3)
                                                                        try:
                                                                            subst4.try_add_variable('i2.2.1.1', tmp137)
                                                                        except ValueError:
                                                                            pass
                                                                        else:
                                                                            pass
                                                                            if 'i2.2.1.0_1' not in subst4 or 'i2.2.1.1' not in subst4 or cons_f3(b=subst4["i2.2.1.0_1"], x=subst4["i2.2.1.1"]):
                                                                                pass
                                                                                if 'i2.2.1.0' not in subst4 or 'i2.2.1.1' not in subst4 or cons_f2(a=subst4["i2.2.1.0"], x=subst4["i2.2.1.1"]):
                                                                                    pass
                                                                                    if 'i2.2.1.2' not in subst4 or 'i2.2.1.1' not in subst4 or cons_f5(p=subst4["i2.2.1.2"], x=subst4["i2.2.1.1"]):
                                                                                        pass
                                                                                        if 'i2.2.1.2_1' not in subst4 or 'i2.2.1.1' not in subst4 or cons_f52(q=subst4["i2.2.1.2_1"], x=subst4["i2.2.1.1"]):
                                                                                            pass
                                                                                            # State 2938
                                                                                            if len(subjects2) == 0:
                                                                                                pass
                                                                                                # State 2939
                                                                                                if len(subjects) == 0:
                                                                                                    pass
                                                                                                    tmp_subst = Substitution()
                                                                                                    tmp_subst['x'] = subst4['i2.2.1.1']
                                                                                                    tmp_subst['p'] = subst4['i2.2.1.2']
                                                                                                    tmp_subst['a'] = subst4['i2.2.1.0']
                                                                                                    tmp_subst['q'] = subst4['i2.2.1.2_1']
                                                                                                    tmp_subst['b'] = subst4['i2.2.1.0_1']
                                                                                                    tmp_subst['m'] = subst4['i2.2']
                                                                                                    tmp_subst['u'] = subst4['i2.0']
                                                                                                    # 29: Integral(u*(a*x**p + b*x**q)**m, x) /; (cons_f2) and (cons_f3) and (cons_f5) and (cons_f52) and (cons_f20) and (cons_f51)
                                                                                                    yield replacement30, tmp_subst, [(cons_f2), (cons_f3), (cons_f5), (cons_f52), (cons_f20), (cons_f51)]
                                                                        subjects2.appendleft(tmp137)
                                                        if len(subjects63) == 0:
                                                            break
                                                        tmp134.append(subjects63.popleft())
                                                    subjects63.extendleft(reversed(tmp134))
                        if pattern_index == 9:
                            pass
                            if 'i2.2.1.0_1' not in subst2 or 'i2.2.1.1' not in subst2 or cons_f3(b=subst2["i2.2.1.0_1"], x=subst2["i2.2.1.1"]):
                                pass
                                if 'i2.2.1.0' not in subst2 or 'i2.2.1.1' not in subst2 or cons_f2(a=subst2["i2.2.1.0"], x=subst2["i2.2.1.1"]):
                                    pass
                                    if 'i2.2.1.2' not in subst2 or 'i2.2.1.1' not in subst2 or cons_f5(p=subst2["i2.2.1.2"], x=subst2["i2.2.1.1"]):
                                        pass
                                        if 'i2.2.1.2_1' not in subst2 or 'i2.2.1.1' not in subst2 or cons_f52(q=subst2["i2.2.1.2_1"], x=subst2["i2.2.1.1"]):
                                            pass
                                            if 'i2.2.1.2' not in subst2 or 'i2.2.1.2_1' not in subst2 or cons_f51(p=subst2["i2.2.1.2"], q=subst2["i2.2.1.2_1"]):
                                                pass
                                                if 'i2.2.1.0_2' not in subst2 or 'i2.2.1.1' not in subst2 or cons_f8(c=subst2["i2.2.1.0_2"], x=subst2["i2.2.1.1"]):
                                                    pass
                                                    if 'i2.2.1.2_2' not in subst2 or 'i2.2.1.1' not in subst2 or cons_f54(r=subst2["i2.2.1.2_2"], x=subst2["i2.2.1.1"]):
                                                        pass
                                                        if 'i2.2.1.2' not in subst2 or 'i2.2.1.2_2' not in subst2 or cons_f53(p=subst2["i2.2.1.2"], r=subst2["i2.2.1.2_2"]):
                                                            pass
                                                            # State 2980
                                                            subst3 = Substitution(subst2)
                                                            try:
                                                                subst3.try_add_variable('i2.2', 1)
                                                            except ValueError:
                                                                pass
                                                            else:
                                                                pass
                                                                if 'i2.2' not in subst3 or cons_f20(m=subst3["i2.2"]):
                                                                    pass
                                                                    # State 2981
                                                                    if len(subjects63) == 0:
                                                                        pass
                                                                        # State 2982
                                                                        if len(subjects2) >= 1:
                                                                            tmp140 = subjects2.popleft()
                                                                            subst4 = Substitution(subst3)
                                                                            try:
                                                                                subst4.try_add_variable('i2.2.1.1', tmp140)
                                                                            except ValueError:
                                                                                pass
                                                                            else:
                                                                                pass
                                                                                if 'i2.2.1.0_1' not in subst4 or 'i2.2.1.1' not in subst4 or cons_f3(b=subst4["i2.2.1.0_1"], x=subst4["i2.2.1.1"]):
                                                                                    pass
                                                                                    if 'i2.2.1.0' not in subst4 or 'i2.2.1.1' not in subst4 or cons_f2(a=subst4["i2.2.1.0"], x=subst4["i2.2.1.1"]):
                                                                                        pass
                                                                                        if 'i2.2.1.2' not in subst4 or 'i2.2.1.1' not in subst4 or cons_f5(p=subst4["i2.2.1.2"], x=subst4["i2.2.1.1"]):
                                                                                            pass
                                                                                            if 'i2.2.1.2_1' not in subst4 or 'i2.2.1.1' not in subst4 or cons_f52(q=subst4["i2.2.1.2_1"], x=subst4["i2.2.1.1"]):
                                                                                                pass
                                                                                                if 'i2.2.1.0_2' not in subst4 or 'i2.2.1.1' not in subst4 or cons_f8(c=subst4["i2.2.1.0_2"], x=subst4["i2.2.1.1"]):
                                                                                                    pass
                                                                                                    if 'i2.2.1.2_2' not in subst4 or 'i2.2.1.1' not in subst4 or cons_f54(r=subst4["i2.2.1.2_2"], x=subst4["i2.2.1.1"]):
                                                                                                        pass
                                                                                                        # State 2983
                                                                                                        if len(subjects2) == 0:
                                                                                                            pass
                                                                                                            # State 2984
                                                                                                            if len(subjects) == 0:
                                                                                                                pass
                                                                                                                tmp_subst = Substitution()
                                                                                                                tmp_subst['x'] = subst4['i2.2.1.1']
                                                                                                                tmp_subst['p'] = subst4['i2.2.1.2']
                                                                                                                tmp_subst['a'] = subst4['i2.2.1.0']
                                                                                                                tmp_subst['q'] = subst4['i2.2.1.2_1']
                                                                                                                tmp_subst['b'] = subst4['i2.2.1.0_1']
                                                                                                                tmp_subst['r'] = subst4['i2.2.1.2_2']
                                                                                                                tmp_subst['c'] = subst4['i2.2.1.0_2']
                                                                                                                tmp_subst['m'] = subst4['i2.2']
                                                                                                                tmp_subst['u'] = subst4['i2.0']
                                                                                                                # 30: Integral(u*(a*x**p + b*x**q + c*x**r)**m, x) /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f5) and (cons_f52) and (cons_f54) and (cons_f20) and (cons_f51) and (cons_f53)
                                                                                                                yield replacement31, tmp_subst, [(cons_f2), (cons_f3), (cons_f8), (cons_f5), (cons_f52), (cons_f54), (cons_f20), (cons_f51), (cons_f53)]
                                                                            subjects2.appendleft(tmp140)
                                                            if len(subjects63) >= 1:
                                                                tmp142 = []
                                                                tmp142.append(subjects63.popleft())
                                                                while True:
                                                                    if len(tmp142) > 1:
                                                                        tmp143 = create_operation_expression(associative1, tmp142)
                                                                    elif len(tmp142) == 1:
                                                                        tmp143 = tmp142[0]
                                                                    else:
                                                                        assert False, "Unreachable"
                                                                    subst3 = Substitution(subst2)
                                                                    try:
                                                                        subst3.try_add_variable('i2.2', tmp143)
                                                                    except ValueError:
                                                                        pass
                                                                    else:
                                                                        pass
                                                                        if 'i2.2' not in subst3 or cons_f20(m=subst3["i2.2"]):
                                                                            pass
                                                                            # State 2981
                                                                            if len(subjects63) == 0:
                                                                                pass
                                                                                # State 2982
                                                                                if len(subjects2) >= 1:
                                                                                    tmp145 = subjects2.popleft()
                                                                                    subst4 = Substitution(subst3)
                                                                                    try:
                                                                                        subst4.try_add_variable('i2.2.1.1', tmp145)
                                                                                    except ValueError:
                                                                                        pass
                                                                                    else:
                                                                                        pass
                                                                                        if 'i2.2.1.0_1' not in subst4 or 'i2.2.1.1' not in subst4 or cons_f3(b=subst4["i2.2.1.0_1"], x=subst4["i2.2.1.1"]):
                                                                                            pass
                                                                                            if 'i2.2.1.0' not in subst4 or 'i2.2.1.1' not in subst4 or cons_f2(a=subst4["i2.2.1.0"], x=subst4["i2.2.1.1"]):
                                                                                                pass
                                                                                                if 'i2.2.1.2' not in subst4 or 'i2.2.1.1' not in subst4 or cons_f5(p=subst4["i2.2.1.2"], x=subst4["i2.2.1.1"]):
                                                                                                    pass
                                                                                                    if 'i2.2.1.2_1' not in subst4 or 'i2.2.1.1' not in subst4 or cons_f52(q=subst4["i2.2.1.2_1"], x=subst4["i2.2.1.1"]):
                                                                                                        pass
                                                                                                        if 'i2.2.1.0_2' not in subst4 or 'i2.2.1.1' not in subst4 or cons_f8(c=subst4["i2.2.1.0_2"], x=subst4["i2.2.1.1"]):
                                                                                                            pass
                                                                                                            if 'i2.2.1.2_2' not in subst4 or 'i2.2.1.1' not in subst4 or cons_f54(r=subst4["i2.2.1.2_2"], x=subst4["i2.2.1.1"]):
                                                                                                                pass
                                                                                                                # State 2983
                                                                                                                if len(subjects2) == 0:
                                                                                                                    pass
                                                                                                                    # State 2984
                                                                                                                    if len(subjects) == 0:
                                                                                                                        pass
                                                                                                                        tmp_subst = Substitution()
                                                                                                                        tmp_subst['x'] = subst4['i2.2.1.1']
                                                                                                                        tmp_subst['p'] = subst4['i2.2.1.2']
                                                                                                                        tmp_subst['a'] = subst4['i2.2.1.0']
                                                                                                                        tmp_subst['q'] = subst4['i2.2.1.2_1']
                                                                                                                        tmp_subst['b'] = subst4['i2.2.1.0_1']
                                                                                                                        tmp_subst['r'] = subst4['i2.2.1.2_2']
                                                                                                                        tmp_subst['c'] = subst4['i2.2.1.0_2']
                                                                                                                        tmp_subst['m'] = subst4['i2.2']
                                                                                                                        tmp_subst['u'] = subst4['i2.0']
                                                                                                                        # 30: Integral(u*(a*x**p + b*x**q + c*x**r)**m, x) /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f5) and (cons_f52) and (cons_f54) and (cons_f20) and (cons_f51) and (cons_f53)
                                                                                                                        yield replacement31, tmp_subst, [(cons_f2), (cons_f3), (cons_f8), (cons_f5), (cons_f52), (cons_f54), (cons_f20), (cons_f51), (cons_f53)]
                                                                                    subjects2.appendleft(tmp145)
                                                                    if len(subjects63) == 0:
                                                                        break
                                                                    tmp142.append(subjects63.popleft())
                                                                subjects63.extendleft(reversed(tmp142))
                    subjects63.appendleft(tmp64)
                subst2 = Substitution(subst1)
                try:
                    subst2.try_add_variable('i2.2.0', S(0))
                except ValueError:
                    pass
                else:
                    pass
                    # State 2423
                    subst3 = Substitution(subst2)
                    try:
                        subst3.try_add_variable('i2.2.1.0', S(1))
                    except ValueError:
                        pass
                    else:
                        pass
                        # State 2424
                        subst4 = Substitution(subst3)
                        try:
                            subst4.try_add_variable('i2.2.1.2', S(1))
                        except ValueError:
                            pass
                        else:
                            pass
                            # State 2425
                            if len(subjects63) >= 1:
                                tmp150 = subjects63.popleft()
                                subst5 = Substitution(subst4)
                                try:
                                    subst5.try_add_variable('i2.2.1.1', tmp150)
                                except ValueError:
                                    pass
                                else:
                                    pass
                                    if 'i2.2.0' not in subst5 or 'i2.2.1.1' not in subst5 or cons_f2(a=subst5["i2.2.0"], x=subst5["i2.2.1.1"]):
                                        pass
                                        if 'i2.2.1.0' not in subst5 or 'i2.2.1.1' not in subst5 or cons_f3(b=subst5["i2.2.1.0"], x=subst5["i2.2.1.1"]):
                                            pass
                                            if 'i2.2.1.2' not in subst5 or 'i2.2.1.1' not in subst5 or cons_f4(n=subst5["i2.2.1.2"], x=subst5["i2.2.1.1"]):
                                                pass
                                                if 'i2.2' not in subst5 or 'i2.2.1.1' not in subst5 or cons_f5(p=subst5["i2.2"], x=subst5["i2.2.1.1"]):
                                                    pass
                                                    # State 2426
                                                    subst6 = Substitution(subst5)
                                                    try:
                                                        subst6.try_add_variable('i2.2', 1)
                                                    except ValueError:
                                                        pass
                                                    else:
                                                        pass
                                                        if 'i2.2' not in subst6 or 'i2.2.1.1' not in subst6 or cons_f5(p=subst6["i2.2"], x=subst6["i2.2.1.1"]):
                                                            pass
                                                            # State 2427
                                                            if len(subjects63) == 0:
                                                                pass
                                                                # State 2428
                                                                if len(subjects2) >= 1:
                                                                    tmp153 = subjects2.popleft()
                                                                    subst7 = Substitution(subst6)
                                                                    try:
                                                                        subst7.try_add_variable('i2.2.1.1', tmp153)
                                                                    except ValueError:
                                                                        pass
                                                                    else:
                                                                        pass
                                                                        if 'i2.2.0' not in subst7 or 'i2.2.1.1' not in subst7 or cons_f2(a=subst7["i2.2.0"], x=subst7["i2.2.1.1"]):
                                                                            pass
                                                                            if 'i2.2.1.0' not in subst7 or 'i2.2.1.1' not in subst7 or cons_f3(b=subst7["i2.2.1.0"], x=subst7["i2.2.1.1"]):
                                                                                pass
                                                                                if 'i2.2.1.2' not in subst7 or 'i2.2.1.1' not in subst7 or cons_f4(n=subst7["i2.2.1.2"], x=subst7["i2.2.1.1"]):
                                                                                    pass
                                                                                    if 'i2.2' not in subst7 or 'i2.2.1.1' not in subst7 or cons_f5(p=subst7["i2.2"], x=subst7["i2.2.1.1"]):
                                                                                        pass
                                                                                        # State 2429
                                                                                        if len(subjects2) == 0:
                                                                                            pass
                                                                                            # State 2430
                                                                                            if len(subjects) == 0:
                                                                                                pass
                                                                                                tmp_subst = Substitution()
                                                                                                tmp_subst['x'] = subst7['i2.2.1.1']
                                                                                                tmp_subst['n'] = subst7['i2.2.1.2']
                                                                                                tmp_subst['b'] = subst7['i2.2.1.0']
                                                                                                tmp_subst['a'] = subst7['i2.2.0']
                                                                                                tmp_subst['p'] = subst7['i2.2']
                                                                                                tmp_subst['u'] = subst7['i2.0']
                                                                                                # 1: Integral(u*(a + b*x**n)**p, x) /; (cons_f2) and (cons_f3) and (cons_f4) and (cons_f5) and (cons_f6)
                                                                                                yield replacement2, tmp_subst, [(cons_f2), (cons_f3), (cons_f4), (cons_f5), (cons_f6)]
                                                                    subjects2.appendleft(tmp153)
                                                    if len(subjects63) >= 1:
                                                        tmp155 = subjects63.popleft()
                                                        subst6 = Substitution(subst5)
                                                        try:
                                                            subst6.try_add_variable('i2.2', tmp155)
                                                        except ValueError:
                                                            pass
                                                        else:
                                                            pass
                                                            if 'i2.2' not in subst6 or 'i2.2.1.1' not in subst6 or cons_f5(p=subst6["i2.2"], x=subst6["i2.2.1.1"]):
                                                                pass
                                                                # State 2427
                                                                if len(subjects63) == 0:
                                                                    pass
                                                                    # State 2428
                                                                    if len(subjects2) >= 1:
                                                                        tmp157 = subjects2.popleft()
                                                                        subst7 = Substitution(subst6)
                                                                        try:
                                                                            subst7.try_add_variable('i2.2.1.1', tmp157)
                                                                        except ValueError:
                                                                            pass
                                                                        else:
                                                                            pass
                                                                            if 'i2.2.0' not in subst7 or 'i2.2.1.1' not in subst7 or cons_f2(a=subst7["i2.2.0"], x=subst7["i2.2.1.1"]):
                                                                                pass
                                                                                if 'i2.2.1.0' not in subst7 or 'i2.2.1.1' not in subst7 or cons_f3(b=subst7["i2.2.1.0"], x=subst7["i2.2.1.1"]):
                                                                                    pass
                                                                                    if 'i2.2.1.2' not in subst7 or 'i2.2.1.1' not in subst7 or cons_f4(n=subst7["i2.2.1.2"], x=subst7["i2.2.1.1"]):
                                                                                        pass
                                                                                        if 'i2.2' not in subst7 or 'i2.2.1.1' not in subst7 or cons_f5(p=subst7["i2.2"], x=subst7["i2.2.1.1"]):
                                                                                            pass
                                                                                            # State 2429
                                                                                            if len(subjects2) == 0:
                                                                                                pass
                                                                                                # State 2430
                                                                                                if len(subjects) == 0:
                                                                                                    pass
                                                                                                    tmp_subst = Substitution()
                                                                                                    tmp_subst['x'] = subst7['i2.2.1.1']
                                                                                                    tmp_subst['n'] = subst7['i2.2.1.2']
                                                                                                    tmp_subst['b'] = subst7['i2.2.1.0']
                                                                                                    tmp_subst['a'] = subst7['i2.2.0']
                                                                                                    tmp_subst['p'] = subst7['i2.2']
                                                                                                    tmp_subst['u'] = subst7['i2.0']
                                                                                                    # 1: Integral(u*(a + b*x**n)**p, x) /; (cons_f2) and (cons_f3) and (cons_f4) and (cons_f5) and (cons_f6)
                                                                                                    yield replacement2, tmp_subst, [(cons_f2), (cons_f3), (cons_f4), (cons_f5), (cons_f6)]
                                                                        subjects2.appendleft(tmp157)
                                                        subjects63.appendleft(tmp155)
                                subjects63.appendleft(tmp150)
                        if len(subjects63) >= 1 and isinstance(subjects63[0], Pow):
                            tmp159 = subjects63.popleft()
                            subjects160 = deque(tmp159._args)
                            # State 2431
                            if len(subjects160) >= 1:
                                tmp161 = subjects160.popleft()
                                subst4 = Substitution(subst3)
                                try:
                                    subst4.try_add_variable('i2.2.1.1', tmp161)
                                except ValueError:
                                    pass
                                else:
                                    pass
                                    if 'i2.2.0' not in subst4 or 'i2.2.1.1' not in subst4 or cons_f2(a=subst4["i2.2.0"], x=subst4["i2.2.1.1"]):
                                        pass
                                        if 'i2.2.1.0' not in subst4 or 'i2.2.1.1' not in subst4 or cons_f3(b=subst4["i2.2.1.0"], x=subst4["i2.2.1.1"]):
                                            pass
                                            if 'i2.2.1.2' not in subst4 or 'i2.2.1.1' not in subst4 or cons_f4(n=subst4["i2.2.1.2"], x=subst4["i2.2.1.1"]):
                                                pass
                                                if 'i2.2' not in subst4 or 'i2.2.1.1' not in subst4 or cons_f5(p=subst4["i2.2"], x=subst4["i2.2.1.1"]):
                                                    pass
                                                    # State 2432
                                                    subst5 = Substitution(subst4)
                                                    try:
                                                        subst5.try_add_variable('i2.2.1.2', 1)
                                                    except ValueError:
                                                        pass
                                                    else:
                                                        pass
                                                        if 'i2.2.1.2' not in subst5 or 'i2.2.1.1' not in subst5 or cons_f4(n=subst5["i2.2.1.2"], x=subst5["i2.2.1.1"]):
                                                            pass
                                                            # State 2433
                                                            if len(subjects160) == 0:
                                                                pass
                                                                # State 2434
                                                                subst6 = Substitution(subst5)
                                                                try:
                                                                    subst6.try_add_variable('i2.2', 1)
                                                                except ValueError:
                                                                    pass
                                                                else:
                                                                    pass
                                                                    if 'i2.2' not in subst6 or 'i2.2.1.1' not in subst6 or cons_f5(p=subst6["i2.2"], x=subst6["i2.2.1.1"]):
                                                                        pass
                                                                        # State 2435
                                                                        if len(subjects63) == 0:
                                                                            pass
                                                                            # State 2436
                                                                            if len(subjects2) >= 1:
                                                                                tmp165 = subjects2.popleft()
                                                                                subst7 = Substitution(subst6)
                                                                                try:
                                                                                    subst7.try_add_variable('i2.2.1.1', tmp165)
                                                                                except ValueError:
                                                                                    pass
                                                                                else:
                                                                                    pass
                                                                                    if 'i2.2.0' not in subst7 or 'i2.2.1.1' not in subst7 or cons_f2(a=subst7["i2.2.0"], x=subst7["i2.2.1.1"]):
                                                                                        pass
                                                                                        if 'i2.2.1.0' not in subst7 or 'i2.2.1.1' not in subst7 or cons_f3(b=subst7["i2.2.1.0"], x=subst7["i2.2.1.1"]):
                                                                                            pass
                                                                                            if 'i2.2.1.2' not in subst7 or 'i2.2.1.1' not in subst7 or cons_f4(n=subst7["i2.2.1.2"], x=subst7["i2.2.1.1"]):
                                                                                                pass
                                                                                                if 'i2.2' not in subst7 or 'i2.2.1.1' not in subst7 or cons_f5(p=subst7["i2.2"], x=subst7["i2.2.1.1"]):
                                                                                                    pass
                                                                                                    # State 2437
                                                                                                    if len(subjects2) == 0:
                                                                                                        pass
                                                                                                        # State 2438
                                                                                                        if len(subjects) == 0:
                                                                                                            pass
                                                                                                            tmp_subst = Substitution()
                                                                                                            tmp_subst['x'] = subst7['i2.2.1.1']
                                                                                                            tmp_subst['n'] = subst7['i2.2.1.2']
                                                                                                            tmp_subst['b'] = subst7['i2.2.1.0']
                                                                                                            tmp_subst['a'] = subst7['i2.2.0']
                                                                                                            tmp_subst['p'] = subst7['i2.2']
                                                                                                            tmp_subst['u'] = subst7['i2.0']
                                                                                                            # 1: Integral(u*(a + b*x**n)**p, x) /; (cons_f2) and (cons_f3) and (cons_f4) and (cons_f5) and (cons_f6)
                                                                                                            yield replacement2, tmp_subst, [(cons_f2), (cons_f3), (cons_f4), (cons_f5), (cons_f6)]
                                                                                subjects2.appendleft(tmp165)
                                                                if len(subjects63) >= 1:
                                                                    tmp167 = subjects63.popleft()
                                                                    subst6 = Substitution(subst5)
                                                                    try:
                                                                        subst6.try_add_variable('i2.2', tmp167)
                                                                    except ValueError:
                                                                        pass
                                                                    else:
                                                                        pass
                                                                        if 'i2.2' not in subst6 or 'i2.2.1.1' not in subst6 or cons_f5(p=subst6["i2.2"], x=subst6["i2.2.1.1"]):
                                                                            pass
                                                                            # State 2435
                                                                            if len(subjects63) == 0:
                                                                                pass
                                                                                # State 2436
                                                                                if len(subjects2) >= 1:
                                                                                    tmp169 = subjects2.popleft()
                                                                                    subst7 = Substitution(subst6)
                                                                                    try:
                                                                                        subst7.try_add_variable('i2.2.1.1', tmp169)
                                                                                    except ValueError:
                                                                                        pass
                                                                                    else:
                                                                                        pass
                                                                                        if 'i2.2.0' not in subst7 or 'i2.2.1.1' not in subst7 or cons_f2(a=subst7["i2.2.0"], x=subst7["i2.2.1.1"]):
                                                                                            pass
                                                                                            if 'i2.2.1.0' not in subst7 or 'i2.2.1.1' not in subst7 or cons_f3(b=subst7["i2.2.1.0"], x=subst7["i2.2.1.1"]):
                                                                                                pass
                                                                                                if 'i2.2.1.2' not in subst7 or 'i2.2.1.1' not in subst7 or cons_f4(n=subst7["i2.2.1.2"], x=subst7["i2.2.1.1"]):
                                                                                                    pass
                                                                                                    if 'i2.2' not in subst7 or 'i2.2.1.1' not in subst7 or cons_f5(p=subst7["i2.2"], x=subst7["i2.2.1.1"]):
                                                                                                        pass
                                                                                                        # State 2437
                                                                                                        if len(subjects2) == 0:
                                                                                                            pass
                                                                                                            # State 2438
                                                                                                            if len(subjects) == 0:
                                                                                                                pass
                                                                                                                tmp_subst = Substitution()
                                                                                                                tmp_subst['x'] = subst7['i2.2.1.1']
                                                                                                                tmp_subst['n'] = subst7['i2.2.1.2']
                                                                                                                tmp_subst['b'] = subst7['i2.2.1.0']
                                                                                                                tmp_subst['a'] = subst7['i2.2.0']
                                                                                                                tmp_subst['p'] = subst7['i2.2']
                                                                                                                tmp_subst['u'] = subst7['i2.0']
                                                                                                                # 1: Integral(u*(a + b*x**n)**p, x) /; (cons_f2) and (cons_f3) and (cons_f4) and (cons_f5) and (cons_f6)
                                                                                                                yield replacement2, tmp_subst, [(cons_f2), (cons_f3), (cons_f4), (cons_f5), (cons_f6)]
                                                                                    subjects2.appendleft(tmp169)
                                                                    subjects63.appendleft(tmp167)
                                                    if len(subjects160) >= 1:
                                                        tmp171 = subjects160.popleft()
                                                        subst5 = Substitution(subst4)
                                                        try:
                                                            subst5.try_add_variable('i2.2.1.2', tmp171)
                                                        except ValueError:
                                                            pass
                                                        else:
                                                            pass
                                                            if 'i2.2.1.2' not in subst5 or 'i2.2.1.1' not in subst5 or cons_f4(n=subst5["i2.2.1.2"], x=subst5["i2.2.1.1"]):
                                                                pass
                                                                # State 2433
                                                                if len(subjects160) == 0:
                                                                    pass
                                                                    # State 2434
                                                                    subst6 = Substitution(subst5)
                                                                    try:
                                                                        subst6.try_add_variable('i2.2', 1)
                                                                    except ValueError:
                                                                        pass
                                                                    else:
                                                                        pass
                                                                        if 'i2.2' not in subst6 or 'i2.2.1.1' not in subst6 or cons_f5(p=subst6["i2.2"], x=subst6["i2.2.1.1"]):
                                                                            pass
                                                                            # State 2435
                                                                            if len(subjects63) == 0:
                                                                                pass
                                                                                # State 2436
                                                                                if len(subjects2) >= 1:
                                                                                    tmp174 = subjects2.popleft()
                                                                                    subst7 = Substitution(subst6)
                                                                                    try:
                                                                                        subst7.try_add_variable('i2.2.1.1', tmp174)
                                                                                    except ValueError:
                                                                                        pass
                                                                                    else:
                                                                                        pass
                                                                                        if 'i2.2.0' not in subst7 or 'i2.2.1.1' not in subst7 or cons_f2(a=subst7["i2.2.0"], x=subst7["i2.2.1.1"]):
                                                                                            pass
                                                                                            if 'i2.2.1.0' not in subst7 or 'i2.2.1.1' not in subst7 or cons_f3(b=subst7["i2.2.1.0"], x=subst7["i2.2.1.1"]):
                                                                                                pass
                                                                                                if 'i2.2.1.2' not in subst7 or 'i2.2.1.1' not in subst7 or cons_f4(n=subst7["i2.2.1.2"], x=subst7["i2.2.1.1"]):
                                                                                                    pass
                                                                                                    if 'i2.2' not in subst7 or 'i2.2.1.1' not in subst7 or cons_f5(p=subst7["i2.2"], x=subst7["i2.2.1.1"]):
                                                                                                        pass
                                                                                                        # State 2437
                                                                                                        if len(subjects2) == 0:
                                                                                                            pass
                                                                                                            # State 2438
                                                                                                            if len(subjects) == 0:
                                                                                                                pass
                                                                                                                tmp_subst = Substitution()
                                                                                                                tmp_subst['x'] = subst7['i2.2.1.1']
                                                                                                                tmp_subst['n'] = subst7['i2.2.1.2']
                                                                                                                tmp_subst['b'] = subst7['i2.2.1.0']
                                                                                                                tmp_subst['a'] = subst7['i2.2.0']
                                                                                                                tmp_subst['p'] = subst7['i2.2']
                                                                                                                tmp_subst['u'] = subst7['i2.0']
                                                                                                                # 1: Integral(u*(a + b*x**n)**p, x) /; (cons_f2) and (cons_f3) and (cons_f4) and (cons_f5) and (cons_f6)
                                                                                                                yield replacement2, tmp_subst, [(cons_f2), (cons_f3), (cons_f4), (cons_f5), (cons_f6)]
                                                                                    subjects2.appendleft(tmp174)
                                                                    if len(subjects63) >= 1:
                                                                        tmp176 = subjects63.popleft()
                                                                        subst6 = Substitution(subst5)
                                                                        try:
                                                                            subst6.try_add_variable('i2.2', tmp176)
                                                                        except ValueError:
                                                                            pass
                                                                        else:
                                                                            pass
                                                                            if 'i2.2' not in subst6 or 'i2.2.1.1' not in subst6 or cons_f5(p=subst6["i2.2"], x=subst6["i2.2.1.1"]):
                                                                                pass
                                                                                # State 2435
                                                                                if len(subjects63) == 0:
                                                                                    pass
                                                                                    # State 2436
                                                                                    if len(subjects2) >= 1:
                                                                                        tmp178 = subjects2.popleft()
                                                                                        subst7 = Substitution(subst6)
                                                                                        try:
                                                                                            subst7.try_add_variable('i2.2.1.1', tmp178)
                                                                                        except ValueError:
                                                                                            pass
                                                                                        else:
                                                                                            pass
                                                                                            if 'i2.2.0' not in subst7 or 'i2.2.1.1' not in subst7 or cons_f2(a=subst7["i2.2.0"], x=subst7["i2.2.1.1"]):
                                                                                                pass
                                                                                                if 'i2.2.1.0' not in subst7 or 'i2.2.1.1' not in subst7 or cons_f3(b=subst7["i2.2.1.0"], x=subst7["i2.2.1.1"]):
                                                                                                    pass
                                                                                                    if 'i2.2.1.2' not in subst7 or 'i2.2.1.1' not in subst7 or cons_f4(n=subst7["i2.2.1.2"], x=subst7["i2.2.1.1"]):
                                                                                                        pass
                                                                                                        if 'i2.2' not in subst7 or 'i2.2.1.1' not in subst7 or cons_f5(p=subst7["i2.2"], x=subst7["i2.2.1.1"]):
                                                                                                            pass
                                                                                                            # State 2437
                                                                                                            if len(subjects2) == 0:
                                                                                                                pass
                                                                                                                # State 2438
                                                                                                                if len(subjects) == 0:
                                                                                                                    pass
                                                                                                                    tmp_subst = Substitution()
                                                                                                                    tmp_subst['x'] = subst7['i2.2.1.1']
                                                                                                                    tmp_subst['n'] = subst7['i2.2.1.2']
                                                                                                                    tmp_subst['b'] = subst7['i2.2.1.0']
                                                                                                                    tmp_subst['a'] = subst7['i2.2.0']
                                                                                                                    tmp_subst['p'] = subst7['i2.2']
                                                                                                                    tmp_subst['u'] = subst7['i2.0']
                                                                                                                    # 1: Integral(u*(a + b*x**n)**p, x) /; (cons_f2) and (cons_f3) and (cons_f4) and (cons_f5) and (cons_f6)
                                                                                                                    yield replacement2, tmp_subst, [(cons_f2), (cons_f3), (cons_f4), (cons_f5), (cons_f6)]
                                                                                        subjects2.appendleft(tmp178)
                                                                        subjects63.appendleft(tmp176)
                                                        subjects160.appendleft(tmp171)
                                subjects160.appendleft(tmp161)
                            subjects63.appendleft(tmp159)
                    if len(subjects63) >= 1 and isinstance(subjects63[0], Mul):
                        tmp180 = subjects63.popleft()
                        associative1 = tmp180
                        associative_type1 = type(tmp180)
                        subjects181 = deque(tmp180._args)
                        matcher = CommutativeMatcher2440.get()
                        tmp182 = subjects181
                        subjects181 = []
                        for s in tmp182:
                            matcher.add_subject(s)
                        for pattern_index, subst3 in matcher.match(tmp182, subst2):
                            pass
                            if pattern_index == 0:
                                pass
                                if 'i2.2.0' not in subst3 or 'i2.2.1.1' not in subst3 or cons_f2(a=subst3["i2.2.0"], x=subst3["i2.2.1.1"]):
                                    pass
                                    if 'i2.2.1.0' not in subst3 or 'i2.2.1.1' not in subst3 or cons_f3(b=subst3["i2.2.1.0"], x=subst3["i2.2.1.1"]):
                                        pass
                                        if 'i2.2.1.2' not in subst3 or 'i2.2.1.1' not in subst3 or cons_f4(n=subst3["i2.2.1.2"], x=subst3["i2.2.1.1"]):
                                            pass
                                            if 'i2.2' not in subst3 or 'i2.2.1.1' not in subst3 or cons_f5(p=subst3["i2.2"], x=subst3["i2.2.1.1"]):
                                                pass
                                                if 'i2.2.1.0' not in subst3 or cons_f6(b=subst3["i2.2.1.0"]):
                                                    pass
                                                    # State 2447
                                                    subst4 = Substitution(subst3)
                                                    try:
                                                        subst4.try_add_variable('i2.2', 1)
                                                    except ValueError:
                                                        pass
                                                    else:
                                                        pass
                                                        if 'i2.2' not in subst4 or 'i2.2.1.1' not in subst4 or cons_f5(p=subst4["i2.2"], x=subst4["i2.2.1.1"]):
                                                            pass
                                                            # State 2448
                                                            if len(subjects63) == 0:
                                                                pass
                                                                # State 2449
                                                                if len(subjects2) >= 1:
                                                                    tmp184 = subjects2.popleft()
                                                                    subst5 = Substitution(subst4)
                                                                    try:
                                                                        subst5.try_add_variable('i2.2.1.1', tmp184)
                                                                    except ValueError:
                                                                        pass
                                                                    else:
                                                                        pass
                                                                        if 'i2.2.0' not in subst5 or 'i2.2.1.1' not in subst5 or cons_f2(a=subst5["i2.2.0"], x=subst5["i2.2.1.1"]):
                                                                            pass
                                                                            if 'i2.2.1.0' not in subst5 or 'i2.2.1.1' not in subst5 or cons_f3(b=subst5["i2.2.1.0"], x=subst5["i2.2.1.1"]):
                                                                                pass
                                                                                if 'i2.2.1.2' not in subst5 or 'i2.2.1.1' not in subst5 or cons_f4(n=subst5["i2.2.1.2"], x=subst5["i2.2.1.1"]):
                                                                                    pass
                                                                                    if 'i2.2' not in subst5 or 'i2.2.1.1' not in subst5 or cons_f5(p=subst5["i2.2"], x=subst5["i2.2.1.1"]):
                                                                                        pass
                                                                                        # State 2450
                                                                                        if len(subjects2) == 0:
                                                                                            pass
                                                                                            # State 2451
                                                                                            if len(subjects) == 0:
                                                                                                pass
                                                                                                tmp_subst = Substitution()
                                                                                                tmp_subst['x'] = subst5['i2.2.1.1']
                                                                                                tmp_subst['n'] = subst5['i2.2.1.2']
                                                                                                tmp_subst['b'] = subst5['i2.2.1.0']
                                                                                                tmp_subst['a'] = subst5['i2.2.0']
                                                                                                tmp_subst['p'] = subst5['i2.2']
                                                                                                tmp_subst['u'] = subst5['i2.0']
                                                                                                # 1: Integral(u*(a + b*x**n)**p, x) /; (cons_f2) and (cons_f3) and (cons_f4) and (cons_f5) and (cons_f6)
                                                                                                yield replacement2, tmp_subst, [(cons_f2), (cons_f3), (cons_f4), (cons_f5), (cons_f6)]
                                                                    subjects2.appendleft(tmp184)
                                                    if len(subjects63) >= 1:
                                                        tmp186 = []
                                                        tmp186.append(subjects63.popleft())
                                                        while True:
                                                            if len(tmp186) > 1:
                                                                tmp187 = create_operation_expression(associative1, tmp186)
                                                            elif len(tmp186) == 1:
                                                                tmp187 = tmp186[0]
                                                            else:
                                                                assert False, "Unreachable"
                                                            subst4 = Substitution(subst3)
                                                            try:
                                                                subst4.try_add_variable('i2.2', tmp187)
                                                            except ValueError:
                                                                pass
                                                            else:
                                                                pass
                                                                if 'i2.2' not in subst4 or 'i2.2.1.1' not in subst4 or cons_f5(p=subst4["i2.2"], x=subst4["i2.2.1.1"]):
                                                                    pass
                                                                    # State 2448
                                                                    if len(subjects63) == 0:
                                                                        pass
                                                                        # State 2449
                                                                        if len(subjects2) >= 1:
                                                                            tmp189 = subjects2.popleft()
                                                                            subst5 = Substitution(subst4)
                                                                            try:
                                                                                subst5.try_add_variable('i2.2.1.1', tmp189)
                                                                            except ValueError:
                                                                                pass
                                                                            else:
                                                                                pass
                                                                                if 'i2.2.0' not in subst5 or 'i2.2.1.1' not in subst5 or cons_f2(a=subst5["i2.2.0"], x=subst5["i2.2.1.1"]):
                                                                                    pass
                                                                                    if 'i2.2.1.0' not in subst5 or 'i2.2.1.1' not in subst5 or cons_f3(b=subst5["i2.2.1.0"], x=subst5["i2.2.1.1"]):
                                                                                        pass
                                                                                        if 'i2.2.1.2' not in subst5 or 'i2.2.1.1' not in subst5 or cons_f4(n=subst5["i2.2.1.2"], x=subst5["i2.2.1.1"]):
                                                                                            pass
                                                                                            if 'i2.2' not in subst5 or 'i2.2.1.1' not in subst5 or cons_f5(p=subst5["i2.2"], x=subst5["i2.2.1.1"]):
                                                                                                pass
                                                                                                # State 2450
                                                                                                if len(subjects2) == 0:
                                                                                                    pass
                                                                                                    # State 2451
                                                                                                    if len(subjects) == 0:
                                                                                                        pass
                                                                                                        tmp_subst = Substitution()
                                                                                                        tmp_subst['x'] = subst5['i2.2.1.1']
                                                                                                        tmp_subst['n'] = subst5['i2.2.1.2']
                                                                                                        tmp_subst['b'] = subst5['i2.2.1.0']
                                                                                                        tmp_subst['a'] = subst5['i2.2.0']
                                                                                                        tmp_subst['p'] = subst5['i2.2']
                                                                                                        tmp_subst['u'] = subst5['i2.0']
                                                                                                        # 1: Integral(u*(a + b*x**n)**p, x) /; (cons_f2) and (cons_f3) and (cons_f4) and (cons_f5) and (cons_f6)
                                                                                                        yield replacement2, tmp_subst, [(cons_f2), (cons_f3), (cons_f4), (cons_f5), (cons_f6)]
                                                                            subjects2.appendleft(tmp189)
                                                            if len(subjects63) == 0:
                                                                break
                                                            tmp186.append(subjects63.popleft())
                                                        subjects63.extendleft(reversed(tmp186))
                        subjects63.appendleft(tmp180)
                if len(subjects63) >= 1:
                    tmp191 = subjects63.popleft()
                    subst2 = Substitution(subst1)
                    try:
                        subst2.try_add_variable('i2.1', tmp191)
                    except ValueError:
                        pass
                    else:
                        pass
                        if 'i2.1' not in subst2 or 'i2' not in subst2 or cons_f11(Pm=subst2["i2.1"], x=subst2["i2"]):
                            pass
                            # State 2636
                            if len(subjects63) >= 1:
                                tmp193 = subjects63.popleft()
                                subst3 = Substitution(subst2)
                                try:
                                    subst3.try_add_variable('i2.2', tmp193)
                                except ValueError:
                                    pass
                                else:
                                    pass
                                    if 'i2.2' not in subst3 or cons_f12(p=subst3["i2.2"]):
                                        pass
                                        if 'i2.2' not in subst3 or cons_f13(p=subst3["i2.2"]):
                                            pass
                                            # State 2637
                                            if len(subjects63) == 0:
                                                pass
                                                # State 2638
                                                if len(subjects2) >= 1:
                                                    tmp195 = subjects2.popleft()
                                                    subst4 = Substitution(subst3)
                                                    try:
                                                        subst4.try_add_variable('i2', tmp195)
                                                    except ValueError:
                                                        pass
                                                    else:
                                                        pass
                                                        if 'i2.1' not in subst4 or 'i2' not in subst4 or cons_f11(Pm=subst4["i2.1"], x=subst4["i2"]):
                                                            pass
                                                            # State 2639
                                                            if len(subjects2) == 0:
                                                                pass
                                                                # State 2640
                                                                if len(subjects) == 0:
                                                                    pass
                                                                    tmp_subst = Substitution()
                                                                    tmp_subst['Pm'] = subst4['i2.1']
                                                                    tmp_subst['p'] = subst4['i2.2']
                                                                    tmp_subst['u'] = subst4['i2.0']
                                                                    tmp_subst['x'] = subst4['i2']
                                                                    # 6: Integral(Pm**p*u, x) /; (cons_f11) and (cons_f12) and (cons_f13)
                                                                    yield replacement7, tmp_subst, [(cons_f11), (cons_f12), (cons_f13)]
                                                    subjects2.appendleft(tmp195)
                                subjects63.appendleft(tmp193)
                    subjects63.appendleft(tmp191)
                subjects2.appendleft(tmp62)
        if len(subjects2) >= 1:
            tmp197 = subjects2.popleft()
            subst1 = Substitution(subst0)
            try:
                subst1.try_add_variable('i1', tmp197)
            except ValueError:
                pass
            else:
                pass
                if 'i1' not in subst1 or 'i2' not in subst1 or cons_f2(a=subst1["i1"], x=subst1["i2"]):
                    pass
                    # State 2647
                    if len(subjects2) >= 1:
                        tmp199 = subjects2.popleft()
                        subst2 = Substitution(subst1)
                        try:
                            subst2.try_add_variable('i2', tmp199)
                        except ValueError:
                            pass
                        else:
                            pass
                            if 'i1' not in subst2 or 'i2' not in subst2 or cons_f2(a=subst2["i1"], x=subst2["i2"]):
                                pass
                                # State 2648
                                if len(subjects2) == 0:
                                    pass
                                    # State 2649
                                    if len(subjects) == 0:
                                        pass
                                        tmp_subst = Substitution()
                                        tmp_subst['a'] = subst2['i1']
                                        tmp_subst['x'] = subst2['i2']
                                        # 7: Integral(a, x) /; (cons_f2) and (cons_f2)
                                        yield replacement8, tmp_subst, [(cons_f2), (cons_f2)]
                        subjects2.appendleft(tmp199)
                if 'i1' not in subst1 or cons_f17(u=subst1["i1"]):
                    pass
                    # State 2647
                    if len(subjects2) >= 1:
                        tmp201 = subjects2.popleft()
                        subst2 = Substitution(subst1)
                        try:
                            subst2.try_add_variable('i2', tmp201)
                        except ValueError:
                            pass
                        else:
                            pass
                            # State 2648
                            if len(subjects2) == 0:
                                pass
                                # State 2649
                                if len(subjects) == 0:
                                    pass
                                    tmp_subst = Substitution()
                                    tmp_subst['u'] = subst2['i1']
                                    tmp_subst['x'] = subst2['i2']
                                    # 12: Integral(u, x) /; (cons_f17)
                                    yield replacement13, tmp_subst, [(cons_f17)]
                        subjects2.appendleft(tmp201)
            subjects2.appendleft(tmp197)
        if len(subjects2) >= 1 and isinstance(subjects2[0], Mul):
            tmp203 = subjects2.popleft()
            associative1 = tmp203
            associative_type1 = type(tmp203)
            subjects204 = deque(tmp203._args)
            matcher = CommutativeMatcher2351.get()
            tmp205 = subjects204
            subjects204 = []
            for s in tmp205:
                matcher.add_subject(s)
            for pattern_index, subst1 in matcher.match(tmp205, subst0):
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
                                    if 'i2.2.0' not in subst1 or cons_f1(a=subst1["i2.2.0"]):
                                        pass
                                        # State 2394
                                        if len(subjects2) >= 1:
                                            tmp206 = []
                                            tmp206.append(subjects2.popleft())
                                            while True:
                                                if len(tmp206) > 1:
                                                    tmp207 = create_operation_expression(associative1, tmp206)
                                                elif len(tmp206) == 1:
                                                    tmp207 = tmp206[0]
                                                else:
                                                    assert False, "Unreachable"
                                                subst2 = Substitution(subst1)
                                                try:
                                                    subst2.try_add_variable('i2.2.1.1', tmp207)
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
                                                                    # State 2395
                                                                    if len(subjects2) == 0:
                                                                        pass
                                                                        # State 2396
                                                                        if len(subjects) == 0:
                                                                            pass
                                                                            tmp_subst = Substitution()
                                                                            tmp_subst['x'] = subst2['i2.2.1.1']
                                                                            tmp_subst['n'] = subst2['i2.2.1.2']
                                                                            tmp_subst['b'] = subst2['i2.2.1.0']
                                                                            tmp_subst['a'] = subst2['i2.2.0']
                                                                            tmp_subst['p'] = subst2['i2.2']
                                                                            tmp_subst['u'] = subst2['i2.0']
                                                                            # 0: Integral(u*(a + b*x**n)**p, x) /; (cons_f2) and (cons_f3) and (cons_f4) and (cons_f5) and (cons_f1)
                                                                            yield replacement1, tmp_subst, [(cons_f2), (cons_f3), (cons_f4), (cons_f5), (cons_f1)]
                                                if len(subjects2) == 0:
                                                    break
                                                tmp206.append(subjects2.popleft())
                                            subjects2.extendleft(reversed(tmp206))
                if pattern_index == 1:
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
                                        # State 2501
                                        if len(subjects2) >= 1:
                                            tmp209 = []
                                            tmp209.append(subjects2.popleft())
                                            while True:
                                                if len(tmp209) > 1:
                                                    tmp210 = create_operation_expression(associative1, tmp209)
                                                elif len(tmp209) == 1:
                                                    tmp210 = tmp209[0]
                                                else:
                                                    assert False, "Unreachable"
                                                subst2 = Substitution(subst1)
                                                try:
                                                    subst2.try_add_variable('i2.2.1.1', tmp210)
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
                                                                    # State 2502
                                                                    if len(subjects2) == 0:
                                                                        pass
                                                                        # State 2503
                                                                        if len(subjects) == 0:
                                                                            pass
                                                                            tmp_subst = Substitution()
                                                                            tmp_subst['x'] = subst2['i2.2.1.1']
                                                                            tmp_subst['n'] = subst2['i2.2.1.2']
                                                                            tmp_subst['b'] = subst2['i2.2.1.0']
                                                                            tmp_subst['a'] = subst2['i2.2.0']
                                                                            tmp_subst['p'] = subst2['i2.2']
                                                                            tmp_subst['u'] = subst2['i2.0']
                                                                            # 1: Integral(u*(a + b*x**n)**p, x) /; (cons_f2) and (cons_f3) and (cons_f4) and (cons_f5) and (cons_f6)
                                                                            yield replacement2, tmp_subst, [(cons_f2), (cons_f3), (cons_f4), (cons_f5), (cons_f6)]
                                                if len(subjects2) == 0:
                                                    break
                                                tmp209.append(subjects2.popleft())
                                            subjects2.extendleft(reversed(tmp209))
                if pattern_index == 2:
                    pass
                    if 'i2.2.0' not in subst1 or 'i2.2.1.1' not in subst1 or cons_f2(a=subst1["i2.2.0"], x=subst1["i2.2.1.1"]):
                        pass
                        if 'i2.2' not in subst1 or 'i2.2.1.1' not in subst1 or cons_f5(p=subst1["i2.2"], x=subst1["i2.2.1.1"]):
                            pass
                            if 'i2.2.0' not in subst1 or cons_f1(a=subst1["i2.2.0"]):
                                pass
                                if 'i2.2.1.0_1' not in subst1 or 'i2.2.1.1' not in subst1 or cons_f3(b=subst1["i2.2.1.0_1"], x=subst1["i2.2.1.1"]):
                                    pass
                                    if 'i2.2.1.0' not in subst1 or 'i2.2.1.1' not in subst1 or cons_f8(c=subst1["i2.2.1.0"], x=subst1["i2.2.1.1"]):
                                        pass
                                        if 'i2.2.1.2_1' not in subst1 or 'i2.2.1.1' not in subst1 or cons_f4(n=subst1["i2.2.1.2_1"], x=subst1["i2.2.1.1"]):
                                            pass
                                            if 'i2.2.1.2' not in subst1 or 'i2.2.1.2_1' not in subst1 or cons_f7(j=subst1["i2.2.1.2"], n=subst1["i2.2.1.2_1"]):
                                                pass
                                                # State 2568
                                                if len(subjects2) >= 1:
                                                    tmp212 = []
                                                    tmp212.append(subjects2.popleft())
                                                    while True:
                                                        if len(tmp212) > 1:
                                                            tmp213 = create_operation_expression(associative1, tmp212)
                                                        elif len(tmp212) == 1:
                                                            tmp213 = tmp212[0]
                                                        else:
                                                            assert False, "Unreachable"
                                                        subst2 = Substitution(subst1)
                                                        try:
                                                            subst2.try_add_variable('i2.2.1.1', tmp213)
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
                                                                            if 'i2.2.1.2_1' not in subst2 or 'i2.2.1.1' not in subst2 or cons_f4(n=subst2["i2.2.1.2_1"], x=subst2["i2.2.1.1"]):
                                                                                pass
                                                                                # State 2569
                                                                                if len(subjects2) == 0:
                                                                                    pass
                                                                                    # State 2570
                                                                                    if len(subjects) == 0:
                                                                                        pass
                                                                                        tmp_subst = Substitution()
                                                                                        tmp_subst['x'] = subst2['i2.2.1.1']
                                                                                        tmp_subst['j'] = subst2['i2.2.1.2']
                                                                                        tmp_subst['c'] = subst2['i2.2.1.0']
                                                                                        tmp_subst['n'] = subst2['i2.2.1.2_1']
                                                                                        tmp_subst['b'] = subst2['i2.2.1.0_1']
                                                                                        tmp_subst['a'] = subst2['i2.2.0']
                                                                                        tmp_subst['p'] = subst2['i2.2']
                                                                                        tmp_subst['u'] = subst2['i2.0']
                                                                                        # 2: Integral(u*(a + b*x**n + c*x**j)**p, x) /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f4) and (cons_f5) and (cons_f7) and (cons_f1)
                                                                                        yield replacement3, tmp_subst, [(cons_f2), (cons_f3), (cons_f8), (cons_f4), (cons_f5), (cons_f7), (cons_f1)]
                                                        if len(subjects2) == 0:
                                                            break
                                                        tmp212.append(subjects2.popleft())
                                                    subjects2.extendleft(reversed(tmp212))
                if pattern_index == 3:
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
                                                # State 2583
                                                if len(subjects2) >= 1:
                                                    tmp215 = []
                                                    tmp215.append(subjects2.popleft())
                                                    while True:
                                                        if len(tmp215) > 1:
                                                            tmp216 = create_operation_expression(associative1, tmp215)
                                                        elif len(tmp215) == 1:
                                                            tmp216 = tmp215[0]
                                                        else:
                                                            assert False, "Unreachable"
                                                        subst2 = Substitution(subst1)
                                                        try:
                                                            subst2.try_add_variable('i2.2.1.1', tmp216)
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
                                                                            if 'i2.2.1.2_1' not in subst2 or 'i2.2.1.1' not in subst2 or cons_f4(n=subst2["i2.2.1.2_1"], x=subst2["i2.2.1.1"]):
                                                                                pass
                                                                                # State 2584
                                                                                if len(subjects2) == 0:
                                                                                    pass
                                                                                    # State 2585
                                                                                    if len(subjects) == 0:
                                                                                        pass
                                                                                        tmp_subst = Substitution()
                                                                                        tmp_subst['x'] = subst2['i2.2.1.1']
                                                                                        tmp_subst['j'] = subst2['i2.2.1.2']
                                                                                        tmp_subst['c'] = subst2['i2.2.1.0']
                                                                                        tmp_subst['n'] = subst2['i2.2.1.2_1']
                                                                                        tmp_subst['b'] = subst2['i2.2.1.0_1']
                                                                                        tmp_subst['a'] = subst2['i2.2.0']
                                                                                        tmp_subst['p'] = subst2['i2.2']
                                                                                        tmp_subst['u'] = subst2['i2.0']
                                                                                        # 3: Integral(u*(a + b*x**n + c*x**j)**p, x) /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f4) and (cons_f5) and (cons_f7) and (cons_f6)
                                                                                        yield replacement4, tmp_subst, [(cons_f2), (cons_f3), (cons_f8), (cons_f4), (cons_f5), (cons_f7), (cons_f6)]
                                                        if len(subjects2) == 0:
                                                            break
                                                        tmp215.append(subjects2.popleft())
                                                    subjects2.extendleft(reversed(tmp215))
                if pattern_index == 4:
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
                                                # State 2598
                                                if len(subjects2) >= 1:
                                                    tmp218 = []
                                                    tmp218.append(subjects2.popleft())
                                                    while True:
                                                        if len(tmp218) > 1:
                                                            tmp219 = create_operation_expression(associative1, tmp218)
                                                        elif len(tmp218) == 1:
                                                            tmp219 = tmp218[0]
                                                        else:
                                                            assert False, "Unreachable"
                                                        subst2 = Substitution(subst1)
                                                        try:
                                                            subst2.try_add_variable('i2.2.1.1', tmp219)
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
                                                                            if 'i2.2.1.2_1' not in subst2 or 'i2.2.1.1' not in subst2 or cons_f4(n=subst2["i2.2.1.2_1"], x=subst2["i2.2.1.1"]):
                                                                                pass
                                                                                # State 2599
                                                                                if len(subjects2) == 0:
                                                                                    pass
                                                                                    # State 2600
                                                                                    if len(subjects) == 0:
                                                                                        pass
                                                                                        tmp_subst = Substitution()
                                                                                        tmp_subst['x'] = subst2['i2.2.1.1']
                                                                                        tmp_subst['j'] = subst2['i2.2.1.2']
                                                                                        tmp_subst['c'] = subst2['i2.2.1.0']
                                                                                        tmp_subst['n'] = subst2['i2.2.1.2_1']
                                                                                        tmp_subst['b'] = subst2['i2.2.1.0_1']
                                                                                        tmp_subst['a'] = subst2['i2.2.0']
                                                                                        tmp_subst['p'] = subst2['i2.2']
                                                                                        tmp_subst['u'] = subst2['i2.0']
                                                                                        # 4: Integral(u*(a + b*x**n + c*x**j)**p, x) /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f4) and (cons_f5) and (cons_f7) and (cons_f9)
                                                                                        yield replacement5, tmp_subst, [(cons_f2), (cons_f3), (cons_f8), (cons_f4), (cons_f5), (cons_f7), (cons_f9)]
                                                        if len(subjects2) == 0:
                                                            break
                                                        tmp218.append(subjects2.popleft())
                                                    subjects2.extendleft(reversed(tmp218))
                if pattern_index == 5:
                    pass
                    if 'i2' not in subst1 or 'i2.2.1.0_1' not in subst1 or cons_f2(a=subst1["i2.2.1.0_1"], x=subst1["i2"]):
                        pass
                        if 'i2.2.1.0_2' not in subst1 or 'i2' not in subst1 or cons_f3(b=subst1["i2.2.1.0_2"], x=subst1["i2"]):
                            pass
                            if 'i2' not in subst1 or 'i2.2.1.0' not in subst1 or cons_f10(v=subst1["i2.2.1.0"], x=subst1["i2"]):
                                pass
                                # State 2633
                                if len(subjects2) >= 1:
                                    tmp221 = []
                                    tmp221.append(subjects2.popleft())
                                    while True:
                                        if len(tmp221) > 1:
                                            tmp222 = create_operation_expression(associative1, tmp221)
                                        elif len(tmp221) == 1:
                                            tmp222 = tmp221[0]
                                        else:
                                            assert False, "Unreachable"
                                        subst2 = Substitution(subst1)
                                        try:
                                            subst2.try_add_variable('i2', tmp222)
                                        except ValueError:
                                            pass
                                        else:
                                            pass
                                            if 'i2' not in subst2 or 'i2.2.1.0_1' not in subst2 or cons_f2(a=subst2["i2.2.1.0_1"], x=subst2["i2"]):
                                                pass
                                                if 'i2.2.1.0_2' not in subst2 or 'i2' not in subst2 or cons_f3(b=subst2["i2.2.1.0_2"], x=subst2["i2"]):
                                                    pass
                                                    if 'i2' not in subst2 or 'i2.2.1.0' not in subst2 or cons_f10(v=subst2["i2.2.1.0"], x=subst2["i2"]):
                                                        pass
                                                        # State 2634
                                                        if len(subjects2) == 0:
                                                            pass
                                                            # State 2635
                                                            if len(subjects) == 0:
                                                                pass
                                                                tmp_subst = Substitution()
                                                                tmp_subst['v'] = subst2['i2.2.1.0']
                                                                tmp_subst['a'] = subst2['i2.2.1.0_1']
                                                                tmp_subst['b'] = subst2['i2.2.1.0_2']
                                                                tmp_subst['w'] = subst2['i2.2.0']
                                                                tmp_subst['p'] = subst2['i2.2']
                                                                tmp_subst['u'] = subst2['i2.0']
                                                                tmp_subst['x'] = subst2['i2']
                                                                # 5: Integral(u*(a*v + b*v + w)**p, x) /; (cons_f2) and (cons_f3) and (cons_f10)
                                                                yield replacement6, tmp_subst, [(cons_f2), (cons_f3), (cons_f10)]
                                        if len(subjects2) == 0:
                                            break
                                        tmp221.append(subjects2.popleft())
                                    subjects2.extendleft(reversed(tmp221))
                if pattern_index == 6:
                    pass
                    if 'i2.1' not in subst1 or 'i2' not in subst1 or cons_f11(Pm=subst1["i2.1"], x=subst1["i2"]):
                        pass
                        if 'i2.2' not in subst1 or cons_f12(p=subst1["i2.2"]):
                            pass
                            if 'i2.2' not in subst1 or cons_f13(p=subst1["i2.2"]):
                                pass
                                # State 2644
                                if len(subjects2) >= 1:
                                    tmp224 = []
                                    tmp224.append(subjects2.popleft())
                                    while True:
                                        if len(tmp224) > 1:
                                            tmp225 = create_operation_expression(associative1, tmp224)
                                        elif len(tmp224) == 1:
                                            tmp225 = tmp224[0]
                                        else:
                                            assert False, "Unreachable"
                                        subst2 = Substitution(subst1)
                                        try:
                                            subst2.try_add_variable('i2', tmp225)
                                        except ValueError:
                                            pass
                                        else:
                                            pass
                                            if 'i2.1' not in subst2 or 'i2' not in subst2 or cons_f11(Pm=subst2["i2.1"], x=subst2["i2"]):
                                                pass
                                                # State 2645
                                                if len(subjects2) == 0:
                                                    pass
                                                    # State 2646
                                                    if len(subjects) == 0:
                                                        pass
                                                        tmp_subst = Substitution()
                                                        tmp_subst['Pm'] = subst2['i2.1']
                                                        tmp_subst['p'] = subst2['i2.2']
                                                        tmp_subst['u'] = subst2['i2.0']
                                                        tmp_subst['x'] = subst2['i2']
                                                        # 6: Integral(Pm**p*u, x) /; (cons_f11) and (cons_f12) and (cons_f13)
                                                        yield replacement7, tmp_subst, [(cons_f11), (cons_f12), (cons_f13)]
                                        if len(subjects2) == 0:
                                            break
                                        tmp224.append(subjects2.popleft())
                                    subjects2.extendleft(reversed(tmp224))
                if pattern_index == 7:
                    pass
                    if 'i2.1.1.0' not in subst1 or 'i2.0' not in subst1 or cons_f2(a=subst1["i2.0"], x=subst1["i2.1.1.0"]):
                        pass
                        if 'i2.1.1.0' not in subst1 or 'i2.1.0' not in subst1 or cons_f3(b=subst1["i2.1.0"], x=subst1["i2.1.1.0"]):
                            pass
                            if 'i2.1.1.0_1' not in subst1 or 'i2.1.1.0' not in subst1 or cons_f8(c=subst1["i2.1.1.0_1"], x=subst1["i2.1.1.0"]):
                                pass
                                if 'i2.1.0' not in subst1 or 'i2.1.1.0_1' not in subst1 or 'i2.1.1.0' not in subst1 or 'i2.0' not in subst1 or cons_f14(a=subst1["i2.0"], b=subst1["i2.1.0"], c=subst1["i2.1.1.0_1"], x=subst1["i2.1.1.0"]):
                                    pass
                                    # State 2658
                                    if len(subjects2) >= 1:
                                        tmp227 = []
                                        tmp227.append(subjects2.popleft())
                                        while True:
                                            if len(tmp227) > 1:
                                                tmp228 = create_operation_expression(associative1, tmp227)
                                            elif len(tmp227) == 1:
                                                tmp228 = tmp227[0]
                                            else:
                                                assert False, "Unreachable"
                                            subst2 = Substitution(subst1)
                                            try:
                                                subst2.try_add_variable('i2.1.1.0', tmp228)
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
                                                                # State 2659
                                                                if len(subjects2) == 0:
                                                                    pass
                                                                    # State 2660
                                                                    if len(subjects) == 0:
                                                                        pass
                                                                        tmp_subst = Substitution()
                                                                        tmp_subst['x'] = subst2['i2.1.1.0']
                                                                        tmp_subst['c'] = subst2['i2.1.1.0_1']
                                                                        tmp_subst['b'] = subst2['i2.1.0']
                                                                        tmp_subst['a'] = subst2['i2.0']
                                                                        # 8: Integral(a*(b + c*x), x) /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f14)
                                                                        yield replacement9, tmp_subst, [(cons_f2), (cons_f3), (cons_f8), (cons_f14)]
                                            if len(subjects2) == 0:
                                                break
                                            tmp227.append(subjects2.popleft())
                                        subjects2.extendleft(reversed(tmp227))
                if pattern_index == 8:
                    pass
                    # State 2662
                    if len(subjects2) >= 1:
                        tmp230 = []
                        tmp230.append(subjects2.popleft())
                        while True:
                            if len(tmp230) > 1:
                                tmp231 = create_operation_expression(associative1, tmp230)
                            elif len(tmp230) == 1:
                                tmp231 = tmp230[0]
                            else:
                                assert False, "Unreachable"
                            subst2 = Substitution(subst1)
                            try:
                                subst2.try_add_variable('i2', tmp231)
                            except ValueError:
                                pass
                            else:
                                pass
                                # State 2663
                                if len(subjects2) == 0:
                                    pass
                                    # State 2664
                                    if len(subjects) == 0:
                                        pass
                                        tmp_subst = Substitution()
                                        tmp_subst['u'] = subst2['i2.0']
                                        tmp_subst['x'] = subst2['i2']
                                        # 9: Integral(-u, x)
                                        yield replacement10, tmp_subst, []
                            if len(subjects2) == 0:
                                break
                            tmp230.append(subjects2.popleft())
                        subjects2.extendleft(reversed(tmp230))
                if pattern_index == 9:
                    pass
                    if 'i2' not in subst1 or 'i2.0' not in subst1 or cons_f2(a=subst1["i2.0"], x=subst1["i2"]):
                        pass
                        if 'i2.0' not in subst1 or cons_f15(a=subst1["i2.0"]):
                            pass
                            # State 2666
                            if len(subjects2) >= 1:
                                tmp233 = []
                                tmp233.append(subjects2.popleft())
                                while True:
                                    if len(tmp233) > 1:
                                        tmp234 = create_operation_expression(associative1, tmp233)
                                    elif len(tmp233) == 1:
                                        tmp234 = tmp233[0]
                                    else:
                                        assert False, "Unreachable"
                                    subst2 = Substitution(subst1)
                                    try:
                                        subst2.try_add_variable('i2', tmp234)
                                    except ValueError:
                                        pass
                                    else:
                                        pass
                                        if 'i2' not in subst2 or 'i2.0' not in subst2 or cons_f2(a=subst2["i2.0"], x=subst2["i2"]):
                                            pass
                                            # State 2667
                                            if len(subjects2) == 0:
                                                pass
                                                # State 2668
                                                if len(subjects) == 0:
                                                    pass
                                                    tmp_subst = Substitution()
                                                    tmp_subst['a'] = subst2['i2.0']
                                                    tmp_subst['u'] = subst2['i2.0_1']
                                                    tmp_subst['x'] = subst2['i2']
                                                    # 10: Integral(I*a*u, x) /; (cons_f2) and (cons_f15)
                                                    yield replacement11, tmp_subst, [(cons_f2), (cons_f15)]
                                    if len(subjects2) == 0:
                                        break
                                    tmp233.append(subjects2.popleft())
                                subjects2.extendleft(reversed(tmp233))
                if pattern_index == 10:
                    pass
                    if 'i2' not in subst1 or 'i2.0' not in subst1 or cons_f2(a=subst1["i2.0"], x=subst1["i2"]):
                        pass
                        if 'i2' not in subst1 or 'i2.0_1' not in subst1 or cons_f16(u=subst1["i2.0_1"], x=subst1["i2"]):
                            pass
                            # State 2669
                            if len(subjects2) >= 1:
                                tmp236 = []
                                tmp236.append(subjects2.popleft())
                                while True:
                                    if len(tmp236) > 1:
                                        tmp237 = create_operation_expression(associative1, tmp236)
                                    elif len(tmp236) == 1:
                                        tmp237 = tmp236[0]
                                    else:
                                        assert False, "Unreachable"
                                    subst2 = Substitution(subst1)
                                    try:
                                        subst2.try_add_variable('i2', tmp237)
                                    except ValueError:
                                        pass
                                    else:
                                        pass
                                        if 'i2' not in subst2 or 'i2.0' not in subst2 or cons_f2(a=subst2["i2.0"], x=subst2["i2"]):
                                            pass
                                            if 'i2' not in subst2 or 'i2.0_1' not in subst2 or cons_f16(u=subst2["i2.0_1"], x=subst2["i2"]):
                                                pass
                                                # State 2670
                                                if len(subjects2) == 0:
                                                    pass
                                                    # State 2671
                                                    if len(subjects) == 0:
                                                        pass
                                                        tmp_subst = Substitution()
                                                        tmp_subst['a'] = subst2['i2.0']
                                                        tmp_subst['u'] = subst2['i2.0_1']
                                                        tmp_subst['x'] = subst2['i2']
                                                        # 11: Integral(a*u, x) /; (cons_f2) and (cons_f16)
                                                        yield replacement12, tmp_subst, [(cons_f2), (cons_f16)]
                                    if len(subjects2) == 0:
                                        break
                                    tmp236.append(subjects2.popleft())
                                subjects2.extendleft(reversed(tmp236))
                if pattern_index == 11:
                    pass
                    if 'i2.2.0_1' not in subst1 or 'i2.2.0' not in subst1 or cons_f8(c=subst1["i2.2.0_1"], x=subst1["i2.2.0"]):
                        pass
                        if 'i2.2.0' not in subst1 or 'i2.2' not in subst1 or cons_f19(m=subst1["i2.2"], x=subst1["i2.2.0"]):
                            pass
                            if 'i2.0' not in subst1 or cons_f17(u=subst1["i2.0"]):
                                pass
                                if 'i2.2.0' not in subst1 or 'i2.0' not in subst1 or cons_f18(u=subst1["i2.0"], x=subst1["i2.2.0"]):
                                    pass
                                    # State 2686
                                    if len(subjects2) >= 1:
                                        tmp239 = []
                                        tmp239.append(subjects2.popleft())
                                        while True:
                                            if len(tmp239) > 1:
                                                tmp240 = create_operation_expression(associative1, tmp239)
                                            elif len(tmp239) == 1:
                                                tmp240 = tmp239[0]
                                            else:
                                                assert False, "Unreachable"
                                            subst2 = Substitution(subst1)
                                            try:
                                                subst2.try_add_variable('i2.2.0', tmp240)
                                            except ValueError:
                                                pass
                                            else:
                                                pass
                                                if 'i2.2.0_1' not in subst2 or 'i2.2.0' not in subst2 or cons_f8(c=subst2["i2.2.0_1"], x=subst2["i2.2.0"]):
                                                    pass
                                                    if 'i2.2.0' not in subst2 or 'i2.2' not in subst2 or cons_f19(m=subst2["i2.2"], x=subst2["i2.2.0"]):
                                                        pass
                                                        if 'i2.2.0' not in subst2 or 'i2.0' not in subst2 or cons_f18(u=subst2["i2.0"], x=subst2["i2.2.0"]):
                                                            pass
                                                            # State 2687
                                                            if len(subjects2) == 0:
                                                                pass
                                                                # State 2688
                                                                if len(subjects) == 0:
                                                                    pass
                                                                    tmp_subst = Substitution()
                                                                    tmp_subst['x'] = subst2['i2.2.0']
                                                                    tmp_subst['c'] = subst2['i2.2.0_1']
                                                                    tmp_subst['m'] = subst2['i2.2']
                                                                    tmp_subst['u'] = subst2['i2.0']
                                                                    # 13: Integral(u*(c*x)**m, x) /; (cons_f8) and (cons_f19) and (cons_f17) and (cons_f18)
                                                                    yield replacement14, tmp_subst, [(cons_f8), (cons_f19), (cons_f17), (cons_f18)]
                                            if len(subjects2) == 0:
                                                break
                                            tmp239.append(subjects2.popleft())
                                        subjects2.extendleft(reversed(tmp239))
                if pattern_index == 12:
                    pass
                    if 'i2' not in subst1 or 'i2.2.0' not in subst1 or cons_f3(b=subst1["i2.2.0"], x=subst1["i2"]):
                        pass
                        if 'i2' not in subst1 or 'i2.2' not in subst1 or cons_f4(n=subst1["i2.2"], x=subst1["i2"]):
                            pass
                            if 'i2.2_1' not in subst1 or cons_f20(m=subst1["i2.2_1"]):
                                pass
                                # State 2697
                                if len(subjects2) >= 1:
                                    tmp242 = []
                                    tmp242.append(subjects2.popleft())
                                    while True:
                                        if len(tmp242) > 1:
                                            tmp243 = create_operation_expression(associative1, tmp242)
                                        elif len(tmp242) == 1:
                                            tmp243 = tmp242[0]
                                        else:
                                            assert False, "Unreachable"
                                        subst2 = Substitution(subst1)
                                        try:
                                            subst2.try_add_variable('i2', tmp243)
                                        except ValueError:
                                            pass
                                        else:
                                            pass
                                            if 'i2' not in subst2 or 'i2.2.0' not in subst2 or cons_f3(b=subst2["i2.2.0"], x=subst2["i2"]):
                                                pass
                                                if 'i2' not in subst2 or 'i2.2' not in subst2 or cons_f4(n=subst2["i2.2"], x=subst2["i2"]):
                                                    pass
                                                    # State 2698
                                                    if len(subjects2) == 0:
                                                        pass
                                                        # State 2699
                                                        if len(subjects) == 0:
                                                            pass
                                                            tmp_subst = Substitution()
                                                            tmp_subst['b'] = subst2['i2.2.0']
                                                            tmp_subst['v'] = subst2['i2.2.0_1']
                                                            tmp_subst['n'] = subst2['i2.2']
                                                            tmp_subst['m'] = subst2['i2.2_1']
                                                            tmp_subst['u'] = subst2['i2.0']
                                                            tmp_subst['x'] = subst2['i2']
                                                            # 14: Integral(u*v**m*(b*v)**n, x) /; (cons_f3) and (cons_f4) and (cons_f20)
                                                            yield replacement15, tmp_subst, [(cons_f3), (cons_f4), (cons_f20)]
                                        if len(subjects2) == 0:
                                            break
                                        tmp242.append(subjects2.popleft())
                                    subjects2.extendleft(reversed(tmp242))
                if pattern_index == 13:
                    pass
                    if 'i2' not in subst1 or 'i2.2.0_1' not in subst1 or cons_f2(a=subst1["i2.2.0_1"], x=subst1["i2"]):
                        pass
                        if 'i2.2.0_2' not in subst1 or 'i2' not in subst1 or cons_f3(b=subst1["i2.2.0_2"], x=subst1["i2"]):
                            pass
                            if 'i2' not in subst1 or 'i2.2' not in subst1 or cons_f19(m=subst1["i2.2"], x=subst1["i2"]):
                                pass
                                if 'i2.2' not in subst1 or cons_f21(m=subst1["i2.2"]):
                                    pass
                                    if 'i2.2_1' not in subst1 or cons_f22(n=subst1["i2.2_1"]):
                                        pass
                                        if 'i2.2_1' not in subst1 or 'i2.2' not in subst1 or cons_f23(m=subst1["i2.2"], n=subst1["i2.2_1"]):
                                            pass
                                            # State 2711
                                            if len(subjects2) >= 1:
                                                tmp245 = []
                                                tmp245.append(subjects2.popleft())
                                                while True:
                                                    if len(tmp245) > 1:
                                                        tmp246 = create_operation_expression(associative1, tmp245)
                                                    elif len(tmp245) == 1:
                                                        tmp246 = tmp245[0]
                                                    else:
                                                        assert False, "Unreachable"
                                                    subst2 = Substitution(subst1)
                                                    try:
                                                        subst2.try_add_variable('i2', tmp246)
                                                    except ValueError:
                                                        pass
                                                    else:
                                                        pass
                                                        if 'i2' not in subst2 or 'i2.2.0_1' not in subst2 or cons_f2(a=subst2["i2.2.0_1"], x=subst2["i2"]):
                                                            pass
                                                            if 'i2.2.0_2' not in subst2 or 'i2' not in subst2 or cons_f3(b=subst2["i2.2.0_2"], x=subst2["i2"]):
                                                                pass
                                                                if 'i2' not in subst2 or 'i2.2' not in subst2 or cons_f19(m=subst2["i2.2"], x=subst2["i2"]):
                                                                    pass
                                                                    # State 2712
                                                                    if len(subjects2) == 0:
                                                                        pass
                                                                        # State 2713
                                                                        if len(subjects) == 0:
                                                                            pass
                                                                            tmp_subst = Substitution()
                                                                            tmp_subst['v'] = subst2['i2.2.0']
                                                                            tmp_subst['a'] = subst2['i2.2.0_1']
                                                                            tmp_subst['m'] = subst2['i2.2']
                                                                            tmp_subst['b'] = subst2['i2.2.0_2']
                                                                            tmp_subst['n'] = subst2['i2.2_1']
                                                                            tmp_subst['u'] = subst2['i2.0']
                                                                            tmp_subst['x'] = subst2['i2']
                                                                            # 15: Integral(u*(a*v)**m*(b*v)**n, x) /; (cons_f2) and (cons_f3) and (cons_f19) and (cons_f21) and (cons_f22) and (cons_f23)
                                                                            yield replacement16, tmp_subst, [(cons_f2), (cons_f3), (cons_f19), (cons_f21), (cons_f22), (cons_f23)]
                                                    if len(subjects2) == 0:
                                                        break
                                                    tmp245.append(subjects2.popleft())
                                                subjects2.extendleft(reversed(tmp245))
                if pattern_index == 14:
                    pass
                    if 'i2' not in subst1 or 'i2.2.0_1' not in subst1 or cons_f2(a=subst1["i2.2.0_1"], x=subst1["i2"]):
                        pass
                        if 'i2.2.0_2' not in subst1 or 'i2' not in subst1 or cons_f3(b=subst1["i2.2.0_2"], x=subst1["i2"]):
                            pass
                            if 'i2' not in subst1 or 'i2.2' not in subst1 or cons_f19(m=subst1["i2.2"], x=subst1["i2"]):
                                pass
                                if 'i2.2' not in subst1 or cons_f21(m=subst1["i2.2"]):
                                    pass
                                    if 'i2.2_1' not in subst1 or 'i2.2' not in subst1 or cons_f23(m=subst1["i2.2"], n=subst1["i2.2_1"]):
                                        pass
                                        if 'i2.2_1' not in subst1 or cons_f24(n=subst1["i2.2_1"]):
                                            pass
                                            # State 2714
                                            if len(subjects2) >= 1:
                                                tmp248 = []
                                                tmp248.append(subjects2.popleft())
                                                while True:
                                                    if len(tmp248) > 1:
                                                        tmp249 = create_operation_expression(associative1, tmp248)
                                                    elif len(tmp248) == 1:
                                                        tmp249 = tmp248[0]
                                                    else:
                                                        assert False, "Unreachable"
                                                    subst2 = Substitution(subst1)
                                                    try:
                                                        subst2.try_add_variable('i2', tmp249)
                                                    except ValueError:
                                                        pass
                                                    else:
                                                        pass
                                                        if 'i2' not in subst2 or 'i2.2.0_1' not in subst2 or cons_f2(a=subst2["i2.2.0_1"], x=subst2["i2"]):
                                                            pass
                                                            if 'i2.2.0_2' not in subst2 or 'i2' not in subst2 or cons_f3(b=subst2["i2.2.0_2"], x=subst2["i2"]):
                                                                pass
                                                                if 'i2' not in subst2 or 'i2.2' not in subst2 or cons_f19(m=subst2["i2.2"], x=subst2["i2"]):
                                                                    pass
                                                                    # State 2715
                                                                    if len(subjects2) == 0:
                                                                        pass
                                                                        # State 2716
                                                                        if len(subjects) == 0:
                                                                            pass
                                                                            tmp_subst = Substitution()
                                                                            tmp_subst['v'] = subst2['i2.2.0']
                                                                            tmp_subst['a'] = subst2['i2.2.0_1']
                                                                            tmp_subst['m'] = subst2['i2.2']
                                                                            tmp_subst['b'] = subst2['i2.2.0_2']
                                                                            tmp_subst['n'] = subst2['i2.2_1']
                                                                            tmp_subst['u'] = subst2['i2.0']
                                                                            tmp_subst['x'] = subst2['i2']
                                                                            # 16: Integral(u*(a*v)**m*(b*v)**n, x) /; (cons_f2) and (cons_f3) and (cons_f19) and (cons_f21) and (cons_f24) and (cons_f23)
                                                                            yield replacement17, tmp_subst, [(cons_f2), (cons_f3), (cons_f19), (cons_f21), (cons_f24), (cons_f23)]
                                                    if len(subjects2) == 0:
                                                        break
                                                    tmp248.append(subjects2.popleft())
                                                subjects2.extendleft(reversed(tmp248))
                if pattern_index == 15:
                    pass
                    if 'i2' not in subst1 or 'i2.2.0_1' not in subst1 or cons_f2(a=subst1["i2.2.0_1"], x=subst1["i2"]):
                        pass
                        if 'i2.2.0_2' not in subst1 or 'i2' not in subst1 or cons_f3(b=subst1["i2.2.0_2"], x=subst1["i2"]):
                            pass
                            if 'i2' not in subst1 or 'i2.2' not in subst1 or cons_f19(m=subst1["i2.2"], x=subst1["i2"]):
                                pass
                                if 'i2.2' not in subst1 or cons_f21(m=subst1["i2.2"]):
                                    pass
                                    if 'i2.2_1' not in subst1 or 'i2.2' not in subst1 or cons_f23(m=subst1["i2.2"], n=subst1["i2.2_1"]):
                                        pass
                                        if 'i2.2_1' not in subst1 or 'i2' not in subst1 or cons_f4(n=subst1["i2.2_1"], x=subst1["i2"]):
                                            pass
                                            if 'i2.2_1' not in subst1 or cons_f25(n=subst1["i2.2_1"]):
                                                pass
                                                # State 2717
                                                if len(subjects2) >= 1:
                                                    tmp251 = []
                                                    tmp251.append(subjects2.popleft())
                                                    while True:
                                                        if len(tmp251) > 1:
                                                            tmp252 = create_operation_expression(associative1, tmp251)
                                                        elif len(tmp251) == 1:
                                                            tmp252 = tmp251[0]
                                                        else:
                                                            assert False, "Unreachable"
                                                        subst2 = Substitution(subst1)
                                                        try:
                                                            subst2.try_add_variable('i2', tmp252)
                                                        except ValueError:
                                                            pass
                                                        else:
                                                            pass
                                                            if 'i2' not in subst2 or 'i2.2.0_1' not in subst2 or cons_f2(a=subst2["i2.2.0_1"], x=subst2["i2"]):
                                                                pass
                                                                if 'i2.2.0_2' not in subst2 or 'i2' not in subst2 or cons_f3(b=subst2["i2.2.0_2"], x=subst2["i2"]):
                                                                    pass
                                                                    if 'i2' not in subst2 or 'i2.2' not in subst2 or cons_f19(m=subst2["i2.2"], x=subst2["i2"]):
                                                                        pass
                                                                        if 'i2.2_1' not in subst2 or 'i2' not in subst2 or cons_f4(n=subst2["i2.2_1"], x=subst2["i2"]):
                                                                            pass
                                                                            # State 2718
                                                                            if len(subjects2) == 0:
                                                                                pass
                                                                                # State 2719
                                                                                if len(subjects) == 0:
                                                                                    pass
                                                                                    tmp_subst = Substitution()
                                                                                    tmp_subst['v'] = subst2['i2.2.0']
                                                                                    tmp_subst['a'] = subst2['i2.2.0_1']
                                                                                    tmp_subst['m'] = subst2['i2.2']
                                                                                    tmp_subst['b'] = subst2['i2.2.0_2']
                                                                                    tmp_subst['n'] = subst2['i2.2_1']
                                                                                    tmp_subst['u'] = subst2['i2.0']
                                                                                    tmp_subst['x'] = subst2['i2']
                                                                                    # 17: Integral(u*(a*v)**m*(b*v)**n, x) /; (cons_f2) and (cons_f3) and (cons_f19) and (cons_f4) and (cons_f21) and (cons_f25) and (cons_f23)
                                                                                    yield replacement18, tmp_subst, [(cons_f2), (cons_f3), (cons_f19), (cons_f4), (cons_f21), (cons_f25), (cons_f23)]
                                                        if len(subjects2) == 0:
                                                            break
                                                        tmp251.append(subjects2.popleft())
                                                    subjects2.extendleft(reversed(tmp251))
                if pattern_index == 16:
                    pass
                    if 'i2' not in subst1 or 'i2.2.0_1' not in subst1 or cons_f2(a=subst1["i2.2.0_1"], x=subst1["i2"]):
                        pass
                        if 'i2.2.0_2' not in subst1 or 'i2' not in subst1 or cons_f3(b=subst1["i2.2.0_2"], x=subst1["i2"]):
                            pass
                            if 'i2' not in subst1 or 'i2.2' not in subst1 or cons_f19(m=subst1["i2.2"], x=subst1["i2"]):
                                pass
                                if 'i2.2' not in subst1 or cons_f21(m=subst1["i2.2"]):
                                    pass
                                    if 'i2.2_1' not in subst1 or 'i2' not in subst1 or cons_f4(n=subst1["i2.2_1"], x=subst1["i2"]):
                                        pass
                                        if 'i2.2_1' not in subst1 or cons_f25(n=subst1["i2.2_1"]):
                                            pass
                                            if 'i2.2_1' not in subst1 or 'i2.2' not in subst1 or cons_f26(m=subst1["i2.2"], n=subst1["i2.2_1"]):
                                                pass
                                                # State 2720
                                                if len(subjects2) >= 1:
                                                    tmp254 = []
                                                    tmp254.append(subjects2.popleft())
                                                    while True:
                                                        if len(tmp254) > 1:
                                                            tmp255 = create_operation_expression(associative1, tmp254)
                                                        elif len(tmp254) == 1:
                                                            tmp255 = tmp254[0]
                                                        else:
                                                            assert False, "Unreachable"
                                                        subst2 = Substitution(subst1)
                                                        try:
                                                            subst2.try_add_variable('i2', tmp255)
                                                        except ValueError:
                                                            pass
                                                        else:
                                                            pass
                                                            if 'i2' not in subst2 or 'i2.2.0_1' not in subst2 or cons_f2(a=subst2["i2.2.0_1"], x=subst2["i2"]):
                                                                pass
                                                                if 'i2.2.0_2' not in subst2 or 'i2' not in subst2 or cons_f3(b=subst2["i2.2.0_2"], x=subst2["i2"]):
                                                                    pass
                                                                    if 'i2' not in subst2 or 'i2.2' not in subst2 or cons_f19(m=subst2["i2.2"], x=subst2["i2"]):
                                                                        pass
                                                                        if 'i2.2_1' not in subst2 or 'i2' not in subst2 or cons_f4(n=subst2["i2.2_1"], x=subst2["i2"]):
                                                                            pass
                                                                            # State 2721
                                                                            if len(subjects2) == 0:
                                                                                pass
                                                                                # State 2722
                                                                                if len(subjects) == 0:
                                                                                    pass
                                                                                    tmp_subst = Substitution()
                                                                                    tmp_subst['v'] = subst2['i2.2.0']
                                                                                    tmp_subst['a'] = subst2['i2.2.0_1']
                                                                                    tmp_subst['m'] = subst2['i2.2']
                                                                                    tmp_subst['b'] = subst2['i2.2.0_2']
                                                                                    tmp_subst['n'] = subst2['i2.2_1']
                                                                                    tmp_subst['u'] = subst2['i2.0']
                                                                                    tmp_subst['x'] = subst2['i2']
                                                                                    # 18: Integral(u*(a*v)**m*(b*v)**n, x) /; (cons_f2) and (cons_f3) and (cons_f19) and (cons_f4) and (cons_f21) and (cons_f25) and (cons_f26)
                                                                                    yield replacement19, tmp_subst, [(cons_f2), (cons_f3), (cons_f19), (cons_f4), (cons_f21), (cons_f25), (cons_f26)]
                                                        if len(subjects2) == 0:
                                                            break
                                                        tmp254.append(subjects2.popleft())
                                                    subjects2.extendleft(reversed(tmp254))
                if pattern_index == 17:
                    pass
                    if 'i2.2_1' not in subst1 or 'i2' not in subst1 or cons_f4(n=subst1["i2.2_1"], x=subst1["i2"]):
                        pass
                        if 'i2' not in subst1 or 'i2.2.0' not in subst1 or cons_f2(a=subst1["i2.2.0"], x=subst1["i2"]):
                            pass
                            if 'i2' not in subst1 or 'i2.2.1.0_1' not in subst1 or cons_f3(b=subst1["i2.2.1.0_1"], x=subst1["i2"]):
                                pass
                                if 'i2' not in subst1 or 'i2.2.0_1' not in subst1 or cons_f8(c=subst1["i2.2.0_1"], x=subst1["i2"]):
                                    pass
                                    if 'i2.2.1.0_2' not in subst1 or 'i2' not in subst1 or cons_f29(d=subst1["i2.2.1.0_2"], x=subst1["i2"]):
                                        pass
                                        if 'i2.2.1.0_2' not in subst1 or 'i2.2.1.0_1' not in subst1 or 'i2.2.0' not in subst1 or 'i2.2.0_1' not in subst1 or cons_f27(a=subst1["i2.2.0"], b=subst1["i2.2.1.0_1"], c=subst1["i2.2.0_1"], d=subst1["i2.2.1.0_2"]):
                                            pass
                                            if 'i2.2' not in subst1 or cons_f20(m=subst1["i2.2"]):
                                                pass
                                                if 'i2' not in subst1 or 'i2.2.1.0_2' not in subst1 or 'i2.2.0_1' not in subst1 or 'i2.2.0' not in subst1 or 'i2.2_1' not in subst1 or 'i2.2.1.0_1' not in subst1 or cons_f28(a=subst1["i2.2.0"], b=subst1["i2.2.1.0_1"], c=subst1["i2.2.0_1"], d=subst1["i2.2.1.0_2"], n=subst1["i2.2_1"], x=subst1["i2"]):
                                                    pass
                                                    # State 2738
                                                    if len(subjects2) >= 1:
                                                        tmp257 = []
                                                        tmp257.append(subjects2.popleft())
                                                        while True:
                                                            if len(tmp257) > 1:
                                                                tmp258 = create_operation_expression(associative1, tmp257)
                                                            elif len(tmp257) == 1:
                                                                tmp258 = tmp257[0]
                                                            else:
                                                                assert False, "Unreachable"
                                                            subst2 = Substitution(subst1)
                                                            try:
                                                                subst2.try_add_variable('i2', tmp258)
                                                            except ValueError:
                                                                pass
                                                            else:
                                                                pass
                                                                if 'i2.2_1' not in subst2 or 'i2' not in subst2 or cons_f4(n=subst2["i2.2_1"], x=subst2["i2"]):
                                                                    pass
                                                                    if 'i2' not in subst2 or 'i2.2.0' not in subst2 or cons_f2(a=subst2["i2.2.0"], x=subst2["i2"]):
                                                                        pass
                                                                        if 'i2' not in subst2 or 'i2.2.1.0_1' not in subst2 or cons_f3(b=subst2["i2.2.1.0_1"], x=subst2["i2"]):
                                                                            pass
                                                                            if 'i2' not in subst2 or 'i2.2.0_1' not in subst2 or cons_f8(c=subst2["i2.2.0_1"], x=subst2["i2"]):
                                                                                pass
                                                                                if 'i2.2.1.0_2' not in subst2 or 'i2' not in subst2 or cons_f29(d=subst2["i2.2.1.0_2"], x=subst2["i2"]):
                                                                                    pass
                                                                                    if 'i2' not in subst2 or 'i2.2.1.0_2' not in subst2 or 'i2.2.0_1' not in subst2 or 'i2.2.0' not in subst2 or 'i2.2_1' not in subst2 or 'i2.2.1.0_1' not in subst2 or cons_f28(a=subst2["i2.2.0"], b=subst2["i2.2.1.0_1"], c=subst2["i2.2.0_1"], d=subst2["i2.2.1.0_2"], n=subst2["i2.2_1"], x=subst2["i2"]):
                                                                                        pass
                                                                                        # State 2739
                                                                                        if len(subjects2) == 0:
                                                                                            pass
                                                                                            # State 2740
                                                                                            if len(subjects) == 0:
                                                                                                pass
                                                                                                tmp_subst = Substitution()
                                                                                                tmp_subst['v'] = subst2['i2.2.1.0']
                                                                                                tmp_subst['b'] = subst2['i2.2.1.0_1']
                                                                                                tmp_subst['a'] = subst2['i2.2.0']
                                                                                                tmp_subst['m'] = subst2['i2.2']
                                                                                                tmp_subst['d'] = subst2['i2.2.1.0_2']
                                                                                                tmp_subst['c'] = subst2['i2.2.0_1']
                                                                                                tmp_subst['n'] = subst2['i2.2_1']
                                                                                                tmp_subst['u'] = subst2['i2.0']
                                                                                                tmp_subst['x'] = subst2['i2']
                                                                                                # 19: Integral(u*(a + b*v)**m*(c + d*v)**n, x) /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f4) and (cons_f27) and (cons_f20) and (cons_f28)
                                                                                                yield replacement20, tmp_subst, [(cons_f2), (cons_f3), (cons_f8), (cons_f29), (cons_f4), (cons_f27), (cons_f20), (cons_f28)]
                                                            if len(subjects2) == 0:
                                                                break
                                                            tmp257.append(subjects2.popleft())
                                                        subjects2.extendleft(reversed(tmp257))
                if pattern_index == 18:
                    pass
                    if 'i2' not in subst1 or 'i2.2' not in subst1 or cons_f19(m=subst1["i2.2"], x=subst1["i2"]):
                        pass
                        if 'i2.2_1' not in subst1 or 'i2' not in subst1 or cons_f4(n=subst1["i2.2_1"], x=subst1["i2"]):
                            pass
                            if 'i2' not in subst1 or 'i2.2.0' not in subst1 or cons_f2(a=subst1["i2.2.0"], x=subst1["i2"]):
                                pass
                                if 'i2' not in subst1 or 'i2.2.1.0_1' not in subst1 or cons_f3(b=subst1["i2.2.1.0_1"], x=subst1["i2"]):
                                    pass
                                    if 'i2' not in subst1 or 'i2.2.0_1' not in subst1 or cons_f8(c=subst1["i2.2.0_1"], x=subst1["i2"]):
                                        pass
                                        if 'i2.2.1.0_2' not in subst1 or 'i2' not in subst1 or cons_f29(d=subst1["i2.2.1.0_2"], x=subst1["i2"]):
                                            pass
                                            if 'i2.2.1.0_2' not in subst1 or 'i2.2.1.0_1' not in subst1 or 'i2.2.0' not in subst1 or 'i2.2.0_1' not in subst1 or cons_f27(a=subst1["i2.2.0"], b=subst1["i2.2.1.0_1"], c=subst1["i2.2.0_1"], d=subst1["i2.2.1.0_2"]):
                                                pass
                                                if 'i2.2.1.0_2' not in subst1 or 'i2.2.1.0_1' not in subst1 or cons_f30(b=subst1["i2.2.1.0_1"], d=subst1["i2.2.1.0_2"]):
                                                    pass
                                                    if 'i2.2_1' not in subst1 or 'i2.2' not in subst1 or cons_f31(m=subst1["i2.2"], n=subst1["i2.2_1"]):
                                                        pass
                                                        # State 2747
                                                        if len(subjects2) >= 1:
                                                            tmp260 = []
                                                            tmp260.append(subjects2.popleft())
                                                            while True:
                                                                if len(tmp260) > 1:
                                                                    tmp261 = create_operation_expression(associative1, tmp260)
                                                                elif len(tmp260) == 1:
                                                                    tmp261 = tmp260[0]
                                                                else:
                                                                    assert False, "Unreachable"
                                                                subst2 = Substitution(subst1)
                                                                try:
                                                                    subst2.try_add_variable('i2', tmp261)
                                                                except ValueError:
                                                                    pass
                                                                else:
                                                                    pass
                                                                    if 'i2' not in subst2 or 'i2.2' not in subst2 or cons_f19(m=subst2["i2.2"], x=subst2["i2"]):
                                                                        pass
                                                                        if 'i2.2_1' not in subst2 or 'i2' not in subst2 or cons_f4(n=subst2["i2.2_1"], x=subst2["i2"]):
                                                                            pass
                                                                            if 'i2' not in subst2 or 'i2.2.0' not in subst2 or cons_f2(a=subst2["i2.2.0"], x=subst2["i2"]):
                                                                                pass
                                                                                if 'i2' not in subst2 or 'i2.2.1.0_1' not in subst2 or cons_f3(b=subst2["i2.2.1.0_1"], x=subst2["i2"]):
                                                                                    pass
                                                                                    if 'i2' not in subst2 or 'i2.2.0_1' not in subst2 or cons_f8(c=subst2["i2.2.0_1"], x=subst2["i2"]):
                                                                                        pass
                                                                                        if 'i2.2.1.0_2' not in subst2 or 'i2' not in subst2 or cons_f29(d=subst2["i2.2.1.0_2"], x=subst2["i2"]):
                                                                                            pass
                                                                                            # State 2748
                                                                                            if len(subjects2) == 0:
                                                                                                pass
                                                                                                # State 2749
                                                                                                if len(subjects) == 0:
                                                                                                    pass
                                                                                                    tmp_subst = Substitution()
                                                                                                    tmp_subst['v'] = subst2['i2.2.1.0']
                                                                                                    tmp_subst['b'] = subst2['i2.2.1.0_1']
                                                                                                    tmp_subst['a'] = subst2['i2.2.0']
                                                                                                    tmp_subst['m'] = subst2['i2.2']
                                                                                                    tmp_subst['d'] = subst2['i2.2.1.0_2']
                                                                                                    tmp_subst['c'] = subst2['i2.2.0_1']
                                                                                                    tmp_subst['n'] = subst2['i2.2_1']
                                                                                                    tmp_subst['u'] = subst2['i2.0']
                                                                                                    tmp_subst['x'] = subst2['i2']
                                                                                                    # 20: Integral(u*(a + b*v)**m*(c + d*v)**n, x) /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f19) and (cons_f4) and (cons_f27) and (cons_f30) and (cons_f31)
                                                                                                    yield replacement21, tmp_subst, [(cons_f2), (cons_f3), (cons_f8), (cons_f29), (cons_f19), (cons_f4), (cons_f27), (cons_f30), (cons_f31)]
                                                                if len(subjects2) == 0:
                                                                    break
                                                                tmp260.append(subjects2.popleft())
                                                            subjects2.extendleft(reversed(tmp260))
                if pattern_index == 19:
                    pass
                    if 'i2' not in subst1 or 'i2.2' not in subst1 or cons_f19(m=subst1["i2.2"], x=subst1["i2"]):
                        pass
                        if 'i2.2_1' not in subst1 or 'i2' not in subst1 or cons_f4(n=subst1["i2.2_1"], x=subst1["i2"]):
                            pass
                            if 'i2' not in subst1 or 'i2.2.0' not in subst1 or cons_f2(a=subst1["i2.2.0"], x=subst1["i2"]):
                                pass
                                if 'i2' not in subst1 or 'i2.2.1.0_1' not in subst1 or cons_f3(b=subst1["i2.2.1.0_1"], x=subst1["i2"]):
                                    pass
                                    if 'i2' not in subst1 or 'i2.2.0_1' not in subst1 or cons_f8(c=subst1["i2.2.0_1"], x=subst1["i2"]):
                                        pass
                                        if 'i2.2.1.0_2' not in subst1 or 'i2' not in subst1 or cons_f29(d=subst1["i2.2.1.0_2"], x=subst1["i2"]):
                                            pass
                                            if 'i2.2.1.0_2' not in subst1 or 'i2.2.1.0_1' not in subst1 or 'i2.2.0' not in subst1 or 'i2.2.0_1' not in subst1 or cons_f27(a=subst1["i2.2.0"], b=subst1["i2.2.1.0_1"], c=subst1["i2.2.0_1"], d=subst1["i2.2.1.0_2"]):
                                                pass
                                                if 'i2.2_1' not in subst1 or 'i2.2.1.0_2' not in subst1 or 'i2.2.1.0_1' not in subst1 or 'i2.2' not in subst1 or cons_f32(b=subst1["i2.2.1.0_1"], d=subst1["i2.2.1.0_2"], m=subst1["i2.2"], n=subst1["i2.2_1"]):
                                                    pass
                                                    # State 2756
                                                    if len(subjects2) >= 1:
                                                        tmp263 = []
                                                        tmp263.append(subjects2.popleft())
                                                        while True:
                                                            if len(tmp263) > 1:
                                                                tmp264 = create_operation_expression(associative1, tmp263)
                                                            elif len(tmp263) == 1:
                                                                tmp264 = tmp263[0]
                                                            else:
                                                                assert False, "Unreachable"
                                                            subst2 = Substitution(subst1)
                                                            try:
                                                                subst2.try_add_variable('i2', tmp264)
                                                            except ValueError:
                                                                pass
                                                            else:
                                                                pass
                                                                if 'i2' not in subst2 or 'i2.2' not in subst2 or cons_f19(m=subst2["i2.2"], x=subst2["i2"]):
                                                                    pass
                                                                    if 'i2.2_1' not in subst2 or 'i2' not in subst2 or cons_f4(n=subst2["i2.2_1"], x=subst2["i2"]):
                                                                        pass
                                                                        if 'i2' not in subst2 or 'i2.2.0' not in subst2 or cons_f2(a=subst2["i2.2.0"], x=subst2["i2"]):
                                                                            pass
                                                                            if 'i2' not in subst2 or 'i2.2.1.0_1' not in subst2 or cons_f3(b=subst2["i2.2.1.0_1"], x=subst2["i2"]):
                                                                                pass
                                                                                if 'i2' not in subst2 or 'i2.2.0_1' not in subst2 or cons_f8(c=subst2["i2.2.0_1"], x=subst2["i2"]):
                                                                                    pass
                                                                                    if 'i2.2.1.0_2' not in subst2 or 'i2' not in subst2 or cons_f29(d=subst2["i2.2.1.0_2"], x=subst2["i2"]):
                                                                                        pass
                                                                                        # State 2757
                                                                                        if len(subjects2) == 0:
                                                                                            pass
                                                                                            # State 2758
                                                                                            if len(subjects) == 0:
                                                                                                pass
                                                                                                tmp_subst = Substitution()
                                                                                                tmp_subst['v'] = subst2['i2.2.1.0']
                                                                                                tmp_subst['b'] = subst2['i2.2.1.0_1']
                                                                                                tmp_subst['a'] = subst2['i2.2.0']
                                                                                                tmp_subst['m'] = subst2['i2.2']
                                                                                                tmp_subst['d'] = subst2['i2.2.1.0_2']
                                                                                                tmp_subst['c'] = subst2['i2.2.0_1']
                                                                                                tmp_subst['n'] = subst2['i2.2_1']
                                                                                                tmp_subst['u'] = subst2['i2.0']
                                                                                                tmp_subst['x'] = subst2['i2']
                                                                                                # 21: Integral(u*(a + b*v)**m*(c + d*v)**n, x) /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f19) and (cons_f4) and (cons_f27) and (cons_f32)
                                                                                                yield replacement22, tmp_subst, [(cons_f2), (cons_f3), (cons_f8), (cons_f29), (cons_f19), (cons_f4), (cons_f27), (cons_f32)]
                                                            if len(subjects2) == 0:
                                                                break
                                                            tmp263.append(subjects2.popleft())
                                                        subjects2.extendleft(reversed(tmp263))
                if pattern_index == 20:
                    pass
                    if 'i2' not in subst1 or 'i2.2.0_1' not in subst1 or cons_f2(a=subst1["i2.2.0_1"], x=subst1["i2"]):
                        pass
                        if 'i2.1.1.0_1' not in subst1 or 'i2' not in subst1 or cons_f3(b=subst1["i2.1.1.0_1"], x=subst1["i2"]):
                            pass
                            if 'i2' not in subst1 or 'i2.1.1.0' not in subst1 or cons_f8(c=subst1["i2.1.1.0"], x=subst1["i2"]):
                                pass
                                if 'i2.2' not in subst1 or cons_f33(m=subst1["i2.2"]):
                                    pass
                                    if 'i2.2' not in subst1 or cons_f34(m=subst1["i2.2"]):
                                        pass
                                        # State 2772
                                        if len(subjects2) >= 1:
                                            tmp266 = []
                                            tmp266.append(subjects2.popleft())
                                            while True:
                                                if len(tmp266) > 1:
                                                    tmp267 = create_operation_expression(associative1, tmp266)
                                                elif len(tmp266) == 1:
                                                    tmp267 = tmp266[0]
                                                else:
                                                    assert False, "Unreachable"
                                                subst2 = Substitution(subst1)
                                                try:
                                                    subst2.try_add_variable('i2', tmp267)
                                                except ValueError:
                                                    pass
                                                else:
                                                    pass
                                                    if 'i2' not in subst2 or 'i2.2.0_1' not in subst2 or cons_f2(a=subst2["i2.2.0_1"], x=subst2["i2"]):
                                                        pass
                                                        if 'i2.1.1.0_1' not in subst2 or 'i2' not in subst2 or cons_f3(b=subst2["i2.1.1.0_1"], x=subst2["i2"]):
                                                            pass
                                                            if 'i2' not in subst2 or 'i2.1.1.0' not in subst2 or cons_f8(c=subst2["i2.1.1.0"], x=subst2["i2"]):
                                                                pass
                                                                # State 2773
                                                                if len(subjects2) == 0:
                                                                    pass
                                                                    # State 2774
                                                                    if len(subjects) == 0:
                                                                        pass
                                                                        tmp_subst = Substitution()
                                                                        tmp_subst['v'] = subst2['i2.2.0']
                                                                        tmp_subst['a'] = subst2['i2.2.0_1']
                                                                        tmp_subst['m'] = subst2['i2.2']
                                                                        tmp_subst['c'] = subst2['i2.1.1.0']
                                                                        tmp_subst['b'] = subst2['i2.1.1.0_1']
                                                                        tmp_subst['u'] = subst2['i2.0']
                                                                        tmp_subst['x'] = subst2['i2']
                                                                        # 22: Integral(u*(a*v)**m*(b*v + c*v**2), x) /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f33) and (cons_f34)
                                                                        yield replacement23, tmp_subst, [(cons_f2), (cons_f3), (cons_f8), (cons_f33), (cons_f34)]
                                                if len(subjects2) == 0:
                                                    break
                                                tmp266.append(subjects2.popleft())
                                            subjects2.extendleft(reversed(tmp266))
                if pattern_index == 21:
                    pass
                    if 'i2' not in subst1 or 'i2.2.0' not in subst1 or cons_f2(a=subst1["i2.2.0"], x=subst1["i2"]):
                        pass
                        if 'i2' not in subst1 or 'i2.2.1.0_1' not in subst1 or cons_f3(b=subst1["i2.2.1.0_1"], x=subst1["i2"]):
                            pass
                            if 'i2.2' not in subst1 or cons_f33(m=subst1["i2.2"]):
                                pass
                                if 'i2.2' not in subst1 or cons_f34(m=subst1["i2.2"]):
                                    pass
                                    if 'i2' not in subst1 or 'i2.1.0' not in subst1 or cons_f36(A=subst1["i2.1.0"], x=subst1["i2"]):
                                        pass
                                        if 'i2.1.1.0_1' not in subst1 or 'i2' not in subst1 or cons_f37(B=subst1["i2.1.1.0_1"], x=subst1["i2"]):
                                            pass
                                            if 'i2' not in subst1 or 'i2.1.1.0' not in subst1 or cons_f38(C=subst1["i2.1.1.0"], x=subst1["i2"]):
                                                pass
                                                if 'i2.1.0' not in subst1 or 'i2.2.0' not in subst1 or 'i2.1.1.0_1' not in subst1 or 'i2.1.1.0' not in subst1 or 'i2.2.1.0_1' not in subst1 or cons_f35(A=subst1["i2.1.0"], B=subst1["i2.1.1.0_1"], C=subst1["i2.1.1.0"], a=subst1["i2.2.0"], b=subst1["i2.2.1.0_1"]):
                                                    pass
                                                    # State 2788
                                                    if len(subjects2) >= 1:
                                                        tmp269 = []
                                                        tmp269.append(subjects2.popleft())
                                                        while True:
                                                            if len(tmp269) > 1:
                                                                tmp270 = create_operation_expression(associative1, tmp269)
                                                            elif len(tmp269) == 1:
                                                                tmp270 = tmp269[0]
                                                            else:
                                                                assert False, "Unreachable"
                                                            subst2 = Substitution(subst1)
                                                            try:
                                                                subst2.try_add_variable('i2', tmp270)
                                                            except ValueError:
                                                                pass
                                                            else:
                                                                pass
                                                                if 'i2' not in subst2 or 'i2.2.0' not in subst2 or cons_f2(a=subst2["i2.2.0"], x=subst2["i2"]):
                                                                    pass
                                                                    if 'i2' not in subst2 or 'i2.2.1.0_1' not in subst2 or cons_f3(b=subst2["i2.2.1.0_1"], x=subst2["i2"]):
                                                                        pass
                                                                        if 'i2' not in subst2 or 'i2.1.0' not in subst2 or cons_f36(A=subst2["i2.1.0"], x=subst2["i2"]):
                                                                            pass
                                                                            if 'i2.1.1.0_1' not in subst2 or 'i2' not in subst2 or cons_f37(B=subst2["i2.1.1.0_1"], x=subst2["i2"]):
                                                                                pass
                                                                                if 'i2' not in subst2 or 'i2.1.1.0' not in subst2 or cons_f38(C=subst2["i2.1.1.0"], x=subst2["i2"]):
                                                                                    pass
                                                                                    # State 2789
                                                                                    if len(subjects2) == 0:
                                                                                        pass
                                                                                        # State 2790
                                                                                        if len(subjects) == 0:
                                                                                            pass
                                                                                            tmp_subst = Substitution()
                                                                                            tmp_subst['v'] = subst2['i2.2.1.0']
                                                                                            tmp_subst['b'] = subst2['i2.2.1.0_1']
                                                                                            tmp_subst['a'] = subst2['i2.2.0']
                                                                                            tmp_subst['m'] = subst2['i2.2']
                                                                                            tmp_subst['C'] = subst2['i2.1.1.0']
                                                                                            tmp_subst['B'] = subst2['i2.1.1.0_1']
                                                                                            tmp_subst['A'] = subst2['i2.1.0']
                                                                                            tmp_subst['u'] = subst2['i2.0']
                                                                                            tmp_subst['x'] = subst2['i2']
                                                                                            # 23: Integral(u*(a + b*v)**m*(A + B*v + C*v**2), x) /; (cons_f2) and (cons_f3) and (cons_f36) and (cons_f37) and (cons_f38) and (cons_f35) and (cons_f33) and (cons_f34)
                                                                                            yield replacement24, tmp_subst, [(cons_f2), (cons_f3), (cons_f36), (cons_f37), (cons_f38), (cons_f35), (cons_f33), (cons_f34)]
                                                            if len(subjects2) == 0:
                                                                break
                                                            tmp269.append(subjects2.popleft())
                                                        subjects2.extendleft(reversed(tmp269))
                if pattern_index == 22:
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
                                                if 'i2.2_1' not in subst1 or cons_f40(p=subst1["i2.2_1"]):
                                                    pass
                                                    if 'i2.2.1.0_1' not in subst1 or 'i2.2.1.0' not in subst1 or 'i2.2.0' not in subst1 or 'i2.2.0_1' not in subst1 or cons_f41(a=subst1["i2.2.0"], b=subst1["i2.2.1.0"], c=subst1["i2.2.0_1"], d=subst1["i2.2.1.0_1"]):
                                                        pass
                                                        if 'i2.2.1.2' not in subst1 or 'i2.2' not in subst1 or cons_f42(m=subst1["i2.2"], n=subst1["i2.2.1.2"]):
                                                            pass
                                                            # State 2816
                                                            if len(subjects2) >= 1:
                                                                tmp272 = []
                                                                tmp272.append(subjects2.popleft())
                                                                while True:
                                                                    if len(tmp272) > 1:
                                                                        tmp273 = create_operation_expression(associative1, tmp272)
                                                                    elif len(tmp272) == 1:
                                                                        tmp273 = tmp272[0]
                                                                    else:
                                                                        assert False, "Unreachable"
                                                                    subst2 = Substitution(subst1)
                                                                    try:
                                                                        subst2.try_add_variable('i2.2.1.1', tmp273)
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
                                                                                                # State 2817
                                                                                                if len(subjects2) == 0:
                                                                                                    pass
                                                                                                    # State 2818
                                                                                                    if len(subjects) == 0:
                                                                                                        pass
                                                                                                        tmp_subst = Substitution()
                                                                                                        tmp_subst['x'] = subst2['i2.2.1.1']
                                                                                                        tmp_subst['n'] = subst2['i2.2.1.2']
                                                                                                        tmp_subst['b'] = subst2['i2.2.1.0']
                                                                                                        tmp_subst['a'] = subst2['i2.2.0']
                                                                                                        tmp_subst['m'] = subst2['i2.2']
                                                                                                        tmp_subst['q'] = subst2['i2.2.1.2_1']
                                                                                                        tmp_subst['d'] = subst2['i2.2.1.0_1']
                                                                                                        tmp_subst['c'] = subst2['i2.2.0_1']
                                                                                                        tmp_subst['p'] = subst2['i2.2_1']
                                                                                                        tmp_subst['u'] = subst2['i2.0']
                                                                                                        # 24: Integral(u*(a + b*x**n)**m*(c + d*x**q)**p, x) /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f19) and (cons_f4) and (cons_f39) and (cons_f40) and (cons_f41) and (cons_f42)
                                                                                                        yield replacement25, tmp_subst, [(cons_f2), (cons_f3), (cons_f8), (cons_f29), (cons_f19), (cons_f4), (cons_f39), (cons_f40), (cons_f41), (cons_f42)]
                                                                    if len(subjects2) == 0:
                                                                        break
                                                                    tmp272.append(subjects2.popleft())
                                                                subjects2.extendleft(reversed(tmp272))
                if pattern_index == 23:
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
                                                    if 'i2.2_1' not in subst1 or 'i2.2' not in subst1 or cons_f43(m=subst1["i2.2_1"], p=subst1["i2.2"]):
                                                        pass
                                                        if 'i2.2.0' not in subst1 or 'i2.2.0_1' not in subst1 or 'i2.2.1.0_1' not in subst1 or 'i2.2.1.0' not in subst1 or cons_f44(a=subst1["i2.2.0_1"], b=subst1["i2.2.1.0_1"], c=subst1["i2.2.0"], d=subst1["i2.2.1.0"]):
                                                            pass
                                                            if 'i2.2.0_1' not in subst1 or cons_f45(a=subst1["i2.2.0_1"]):
                                                                pass
                                                                if 'i2.2.1.0' not in subst1 or cons_f46(d=subst1["i2.2.1.0"]):
                                                                    pass
                                                                    # State 2839
                                                                    if len(subjects2) >= 1:
                                                                        tmp275 = []
                                                                        tmp275.append(subjects2.popleft())
                                                                        while True:
                                                                            if len(tmp275) > 1:
                                                                                tmp276 = create_operation_expression(associative1, tmp275)
                                                                            elif len(tmp275) == 1:
                                                                                tmp276 = tmp275[0]
                                                                            else:
                                                                                assert False, "Unreachable"
                                                                            subst2 = Substitution(subst1)
                                                                            try:
                                                                                subst2.try_add_variable('i2.2.1.1', tmp276)
                                                                            except ValueError:
                                                                                pass
                                                                            else:
                                                                                pass
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
                                                                                                            # State 2840
                                                                                                            if len(subjects2) == 0:
                                                                                                                pass
                                                                                                                # State 2841
                                                                                                                if len(subjects) == 0:
                                                                                                                    pass
                                                                                                                    tmp_subst = Substitution()
                                                                                                                    tmp_subst['x'] = subst2['i2.2.1.1']
                                                                                                                    tmp_subst['j'] = subst2['i2.2.1.2']
                                                                                                                    tmp_subst['d'] = subst2['i2.2.1.0']
                                                                                                                    tmp_subst['c'] = subst2['i2.2.0']
                                                                                                                    tmp_subst['p'] = subst2['i2.2']
                                                                                                                    tmp_subst['n'] = subst2['i2.2.1.2_1']
                                                                                                                    tmp_subst['b'] = subst2['i2.2.1.0_1']
                                                                                                                    tmp_subst['a'] = subst2['i2.2.0_1']
                                                                                                                    tmp_subst['m'] = subst2['i2.2_1']
                                                                                                                    tmp_subst['u'] = subst2['i2.0']
                                                                                                                    # 25: Integral(u*(a + b*x**n)**m*(c + d*x**j)**p, x) /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f19) and (cons_f4) and (cons_f5) and (cons_f7) and (cons_f43) and (cons_f44) and (cons_f45) and (cons_f46)
                                                                                                                    yield replacement26, tmp_subst, [(cons_f2), (cons_f3), (cons_f8), (cons_f29), (cons_f19), (cons_f4), (cons_f5), (cons_f7), (cons_f43), (cons_f44), (cons_f45), (cons_f46)]
                                                                            if len(subjects2) == 0:
                                                                                break
                                                                            tmp275.append(subjects2.popleft())
                                                                        subjects2.extendleft(reversed(tmp275))
                if pattern_index == 24:
                    pass
                    if 'i2.2.0' not in subst1 or 'i2.2.1.1' not in subst1 or cons_f2(a=subst1["i2.2.0"], x=subst1["i2.2.1.1"]):
                        pass
                        if 'i2.2.1.0_1' not in subst1 or 'i2.2.1.1' not in subst1 or cons_f3(b=subst1["i2.2.1.0_1"], x=subst1["i2.2.1.1"]):
                            pass
                            if 'i2.2.1.0' not in subst1 or 'i2.2.1.1' not in subst1 or cons_f8(c=subst1["i2.2.1.0"], x=subst1["i2.2.1.1"]):
                                pass
                                if 'i2.2.1.0' not in subst1 or 'i2.2.1.0_1' not in subst1 or 'i2.2.0' not in subst1 or cons_f47(a=subst1["i2.2.0"], b=subst1["i2.2.1.0_1"], c=subst1["i2.2.1.0"]):
                                    pass
                                    if 'i2.2' not in subst1 or cons_f40(p=subst1["i2.2"]):
                                        pass
                                        # State 2882
                                        if len(subjects2) >= 1:
                                            tmp278 = []
                                            tmp278.append(subjects2.popleft())
                                            while True:
                                                if len(tmp278) > 1:
                                                    tmp279 = create_operation_expression(associative1, tmp278)
                                                elif len(tmp278) == 1:
                                                    tmp279 = tmp278[0]
                                                else:
                                                    assert False, "Unreachable"
                                                subst2 = Substitution(subst1)
                                                try:
                                                    subst2.try_add_variable('i2.2.1.1', tmp279)
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
                                                                # State 2883
                                                                if len(subjects2) == 0:
                                                                    pass
                                                                    # State 2884
                                                                    if len(subjects) == 0:
                                                                        pass
                                                                        tmp_subst = Substitution()
                                                                        tmp_subst['x'] = subst2['i2.2.1.1']
                                                                        tmp_subst['c'] = subst2['i2.2.1.0']
                                                                        tmp_subst['b'] = subst2['i2.2.1.0_1']
                                                                        tmp_subst['a'] = subst2['i2.2.0']
                                                                        tmp_subst['p'] = subst2['i2.2']
                                                                        tmp_subst['u'] = subst2['i2.0']
                                                                        # 26: Integral(u*(a + b*x + c*x**2)**p, x) /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f47) and (cons_f40)
                                                                        yield replacement27, tmp_subst, [(cons_f2), (cons_f3), (cons_f8), (cons_f47), (cons_f40)]
                                                if len(subjects2) == 0:
                                                    break
                                                tmp278.append(subjects2.popleft())
                                            subjects2.extendleft(reversed(tmp278))
                if pattern_index == 25:
                    pass
                    if 'i2.2.0' not in subst1 or 'i2.2.1.1' not in subst1 or cons_f2(a=subst1["i2.2.0"], x=subst1["i2.2.1.1"]):
                        pass
                        if 'i2.2.1.0' not in subst1 or 'i2.2.1.1' not in subst1 or cons_f3(b=subst1["i2.2.1.0"], x=subst1["i2.2.1.1"]):
                            pass
                            if 'i2.2.1.2' not in subst1 or 'i2.2.1.1' not in subst1 or cons_f4(n=subst1["i2.2.1.2"], x=subst1["i2.2.1.1"]):
                                pass
                                if 'i2.2' not in subst1 or cons_f40(p=subst1["i2.2"]):
                                    pass
                                    if 'i2.2.1.0_1' not in subst1 or 'i2.2.1.1' not in subst1 or cons_f8(c=subst1["i2.2.1.0_1"], x=subst1["i2.2.1.1"]):
                                        pass
                                        if 'i2.2.1.2' not in subst1 or 'i2.2.1.2_1' not in subst1 or cons_f48(n=subst1["i2.2.1.2"], n2=subst1["i2.2.1.2_1"]):
                                            pass
                                            if 'i2.2.1.0_1' not in subst1 or 'i2.2.1.0' not in subst1 or 'i2.2.0' not in subst1 or cons_f47(a=subst1["i2.2.0"], b=subst1["i2.2.1.0"], c=subst1["i2.2.1.0_1"]):
                                                pass
                                                # State 2913
                                                if len(subjects2) >= 1:
                                                    tmp281 = []
                                                    tmp281.append(subjects2.popleft())
                                                    while True:
                                                        if len(tmp281) > 1:
                                                            tmp282 = create_operation_expression(associative1, tmp281)
                                                        elif len(tmp281) == 1:
                                                            tmp282 = tmp281[0]
                                                        else:
                                                            assert False, "Unreachable"
                                                        subst2 = Substitution(subst1)
                                                        try:
                                                            subst2.try_add_variable('i2.2.1.1', tmp282)
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
                                                                            # State 2914
                                                                            if len(subjects2) == 0:
                                                                                pass
                                                                                # State 2915
                                                                                if len(subjects) == 0:
                                                                                    pass
                                                                                    tmp_subst = Substitution()
                                                                                    tmp_subst['x'] = subst2['i2.2.1.1']
                                                                                    tmp_subst['n'] = subst2['i2.2.1.2']
                                                                                    tmp_subst['b'] = subst2['i2.2.1.0']
                                                                                    tmp_subst['n2'] = subst2['i2.2.1.2_1']
                                                                                    tmp_subst['c'] = subst2['i2.2.1.0_1']
                                                                                    tmp_subst['a'] = subst2['i2.2.0']
                                                                                    tmp_subst['p'] = subst2['i2.2']
                                                                                    tmp_subst['u'] = subst2['i2.0']
                                                                                    # 27: Integral(u*(a + b*x**n + c*x**n2)**p, x) /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f4) and (cons_f48) and (cons_f47) and (cons_f40)
                                                                                    yield replacement28, tmp_subst, [(cons_f2), (cons_f3), (cons_f8), (cons_f4), (cons_f48), (cons_f47), (cons_f40)]
                                                        if len(subjects2) == 0:
                                                            break
                                                        tmp281.append(subjects2.popleft())
                                                    subjects2.extendleft(reversed(tmp281))
                if pattern_index == 26:
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
                                                # State 2925
                                                if len(subjects2) >= 1:
                                                    tmp284 = []
                                                    tmp284.append(subjects2.popleft())
                                                    while True:
                                                        if len(tmp284) > 1:
                                                            tmp285 = create_operation_expression(associative1, tmp284)
                                                        elif len(tmp284) == 1:
                                                            tmp285 = tmp284[0]
                                                        else:
                                                            assert False, "Unreachable"
                                                        subst2 = Substitution(subst1)
                                                        try:
                                                            subst2.try_add_variable('i2.2.1.1', tmp285)
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
                                                                                    # State 2926
                                                                                    if len(subjects2) == 0:
                                                                                        pass
                                                                                        # State 2927
                                                                                        if len(subjects) == 0:
                                                                                            pass
                                                                                            tmp_subst = Substitution()
                                                                                            tmp_subst['x'] = subst2['i2.2.1.1']
                                                                                            tmp_subst['c'] = subst2['i2.2.1.0']
                                                                                            tmp_subst['b'] = subst2['i2.2.1.0_1']
                                                                                            tmp_subst['a'] = subst2['i2.2.0']
                                                                                            tmp_subst['p'] = subst2['i2.2']
                                                                                            tmp_subst['e'] = subst2['i2.1.1.0']
                                                                                            tmp_subst['d'] = subst2['i2.1.0']
                                                                                            # 28: Integral((d + e*x)*(a + b*x + c*x**2)**p, x) /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f50) and (cons_f5) and (cons_f49)
                                                                                            yield replacement29, tmp_subst, [(cons_f2), (cons_f3), (cons_f8), (cons_f29), (cons_f50), (cons_f5), (cons_f49)]
                                                        if len(subjects2) == 0:
                                                            break
                                                        tmp284.append(subjects2.popleft())
                                                    subjects2.extendleft(reversed(tmp284))
                if pattern_index == 27:
                    pass
                    if 'i2.2.1.0_1' not in subst1 or 'i2.2.1.1' not in subst1 or cons_f3(b=subst1["i2.2.1.0_1"], x=subst1["i2.2.1.1"]):
                        pass
                        if 'i2.2' not in subst1 or cons_f20(m=subst1["i2.2"]):
                            pass
                            if 'i2.2.1.0' not in subst1 or 'i2.2.1.1' not in subst1 or cons_f2(a=subst1["i2.2.1.0"], x=subst1["i2.2.1.1"]):
                                pass
                                if 'i2.2.1.2' not in subst1 or 'i2.2.1.1' not in subst1 or cons_f5(p=subst1["i2.2.1.2"], x=subst1["i2.2.1.1"]):
                                    pass
                                    if 'i2.2.1.2_1' not in subst1 or 'i2.2.1.1' not in subst1 or cons_f52(q=subst1["i2.2.1.2_1"], x=subst1["i2.2.1.1"]):
                                        pass
                                        if 'i2.2.1.2' not in subst1 or 'i2.2.1.2_1' not in subst1 or cons_f51(p=subst1["i2.2.1.2"], q=subst1["i2.2.1.2_1"]):
                                            pass
                                            # State 2948
                                            if len(subjects2) >= 1:
                                                tmp287 = []
                                                tmp287.append(subjects2.popleft())
                                                while True:
                                                    if len(tmp287) > 1:
                                                        tmp288 = create_operation_expression(associative1, tmp287)
                                                    elif len(tmp287) == 1:
                                                        tmp288 = tmp287[0]
                                                    else:
                                                        assert False, "Unreachable"
                                                    subst2 = Substitution(subst1)
                                                    try:
                                                        subst2.try_add_variable('i2.2.1.1', tmp288)
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
                                                                        # State 2949
                                                                        if len(subjects2) == 0:
                                                                            pass
                                                                            # State 2950
                                                                            if len(subjects) == 0:
                                                                                pass
                                                                                tmp_subst = Substitution()
                                                                                tmp_subst['x'] = subst2['i2.2.1.1']
                                                                                tmp_subst['p'] = subst2['i2.2.1.2']
                                                                                tmp_subst['a'] = subst2['i2.2.1.0']
                                                                                tmp_subst['q'] = subst2['i2.2.1.2_1']
                                                                                tmp_subst['b'] = subst2['i2.2.1.0_1']
                                                                                tmp_subst['m'] = subst2['i2.2']
                                                                                tmp_subst['u'] = subst2['i2.0']
                                                                                # 29: Integral(u*(a*x**p + b*x**q)**m, x) /; (cons_f2) and (cons_f3) and (cons_f5) and (cons_f52) and (cons_f20) and (cons_f51)
                                                                                yield replacement30, tmp_subst, [(cons_f2), (cons_f3), (cons_f5), (cons_f52), (cons_f20), (cons_f51)]
                                                    if len(subjects2) == 0:
                                                        break
                                                    tmp287.append(subjects2.popleft())
                                                subjects2.extendleft(reversed(tmp287))
                if pattern_index == 28:
                    pass
                    if 'i2.2.1.0_1' not in subst1 or 'i2.2.1.1' not in subst1 or cons_f3(b=subst1["i2.2.1.0_1"], x=subst1["i2.2.1.1"]):
                        pass
                        if 'i2.2' not in subst1 or cons_f20(m=subst1["i2.2"]):
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
                                                        # State 3015
                                                        if len(subjects2) >= 1:
                                                            tmp290 = []
                                                            tmp290.append(subjects2.popleft())
                                                            while True:
                                                                if len(tmp290) > 1:
                                                                    tmp291 = create_operation_expression(associative1, tmp290)
                                                                elif len(tmp290) == 1:
                                                                    tmp291 = tmp290[0]
                                                                else:
                                                                    assert False, "Unreachable"
                                                                subst2 = Substitution(subst1)
                                                                try:
                                                                    subst2.try_add_variable('i2.2.1.1', tmp291)
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
                                                                                            # State 3016
                                                                                            if len(subjects2) == 0:
                                                                                                pass
                                                                                                # State 3017
                                                                                                if len(subjects) == 0:
                                                                                                    pass
                                                                                                    tmp_subst = Substitution()
                                                                                                    tmp_subst['x'] = subst2['i2.2.1.1']
                                                                                                    tmp_subst['p'] = subst2['i2.2.1.2']
                                                                                                    tmp_subst['a'] = subst2['i2.2.1.0']
                                                                                                    tmp_subst['q'] = subst2['i2.2.1.2_1']
                                                                                                    tmp_subst['b'] = subst2['i2.2.1.0_1']
                                                                                                    tmp_subst['r'] = subst2['i2.2.1.2_2']
                                                                                                    tmp_subst['c'] = subst2['i2.2.1.0_2']
                                                                                                    tmp_subst['m'] = subst2['i2.2']
                                                                                                    tmp_subst['u'] = subst2['i2.0']
                                                                                                    # 30: Integral(u*(a*x**p + b*x**q + c*x**r)**m, x) /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f5) and (cons_f52) and (cons_f54) and (cons_f20) and (cons_f51) and (cons_f53)
                                                                                                    yield replacement31, tmp_subst, [(cons_f2), (cons_f3), (cons_f8), (cons_f5), (cons_f52), (cons_f54), (cons_f20), (cons_f51), (cons_f53)]
                                                                if len(subjects2) == 0:
                                                                    break
                                                                tmp290.append(subjects2.popleft())
                                                            subjects2.extendleft(reversed(tmp290))
                if pattern_index == 29:
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
                                        # State 3026
                                        if len(subjects2) >= 1:
                                            tmp293 = []
                                            tmp293.append(subjects2.popleft())
                                            while True:
                                                if len(tmp293) > 1:
                                                    tmp294 = create_operation_expression(associative1, tmp293)
                                                elif len(tmp293) == 1:
                                                    tmp294 = tmp293[0]
                                                else:
                                                    assert False, "Unreachable"
                                                subst2 = Substitution(subst1)
                                                try:
                                                    subst2.try_add_variable('i2.2.1.1', tmp294)
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
                                                                if 'i2.2' not in subst2 or 'i2.2.1.1' not in subst2 or cons_f19(m=subst2["i2.2"], x=subst2["i2.2.1.1"]):
                                                                    pass
                                                                    # State 3027
                                                                    if len(subjects2) == 0:
                                                                        pass
                                                                        # State 3028
                                                                        if len(subjects) == 0:
                                                                            pass
                                                                            tmp_subst = Substitution()
                                                                            tmp_subst['x'] = subst2['i2.2.1.1']
                                                                            tmp_subst['n'] = subst2['i2.2.1.2']
                                                                            tmp_subst['b'] = subst2['i2.2.1.0']
                                                                            tmp_subst['a'] = subst2['i2.2.0']
                                                                            tmp_subst['m'] = subst2['i2.2']
                                                                            # 31: Integral(x**m/(a + b*x**n), x) /; (cons_f2) and (cons_f3) and (cons_f19) and (cons_f4) and (cons_f55)
                                                                            yield replacement32, tmp_subst, [(cons_f2), (cons_f3), (cons_f19), (cons_f4), (cons_f55)]
                                                if len(subjects2) == 0:
                                                    break
                                                tmp293.append(subjects2.popleft())
                                            subjects2.extendleft(reversed(tmp293))
                if pattern_index == 30:
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
                                            if 'i2.2' not in subst1 or cons_f56(p=subst1["i2.2"]):
                                                pass
                                                # State 3036
                                                if len(subjects2) >= 1:
                                                    tmp296 = []
                                                    tmp296.append(subjects2.popleft())
                                                    while True:
                                                        if len(tmp296) > 1:
                                                            tmp297 = create_operation_expression(associative1, tmp296)
                                                        elif len(tmp296) == 1:
                                                            tmp297 = tmp296[0]
                                                        else:
                                                            assert False, "Unreachable"
                                                        subst2 = Substitution(subst1)
                                                        try:
                                                            subst2.try_add_variable('i2.2.1.1', tmp297)
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
                                                                                # State 3037
                                                                                if len(subjects2) == 0:
                                                                                    pass
                                                                                    # State 3038
                                                                                    if len(subjects) == 0:
                                                                                        pass
                                                                                        tmp_subst = Substitution()
                                                                                        tmp_subst['x'] = subst2['i2.2.1.1']
                                                                                        tmp_subst['n'] = subst2['i2.2.1.2']
                                                                                        tmp_subst['b'] = subst2['i2.2.1.0']
                                                                                        tmp_subst['a'] = subst2['i2.2.0']
                                                                                        tmp_subst['p'] = subst2['i2.2']
                                                                                        tmp_subst['m'] = subst2['i2.2_1']
                                                                                        # 32: Integral(x**m*(a + b*x**n)**p, x) /; (cons_f2) and (cons_f3) and (cons_f19) and (cons_f4) and (cons_f5) and (cons_f55) and (cons_f56)
                                                                                        yield replacement33, tmp_subst, [(cons_f2), (cons_f3), (cons_f19), (cons_f4), (cons_f5), (cons_f55), (cons_f56)]
                                                        if len(subjects2) == 0:
                                                            break
                                                        tmp296.append(subjects2.popleft())
                                                    subjects2.extendleft(reversed(tmp296))
                if pattern_index == 31:
                    pass
                    if 'i2.2.1.2' not in subst1 or 'i2.2.1.1' not in subst1 or cons_f4(n=subst1["i2.2.1.2"], x=subst1["i2.2.1.1"]):
                        pass
                        if 'i2.2' not in subst1 or 'i2.2.1.1' not in subst1 or cons_f5(p=subst1["i2.2"], x=subst1["i2.2.1.1"]):
                            pass
                            if 'i2.2_1' not in subst1 or 'i2.2.1.1' not in subst1 or cons_f19(m=subst1["i2.2_1"], x=subst1["i2.2.1.1"]):
                                pass
                                if 'i2.2' not in subst1 or cons_f56(p=subst1["i2.2"]):
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
                                                            # State 3051
                                                            if len(subjects2) >= 1:
                                                                tmp299 = []
                                                                tmp299.append(subjects2.popleft())
                                                                while True:
                                                                    if len(tmp299) > 1:
                                                                        tmp300 = create_operation_expression(associative1, tmp299)
                                                                    elif len(tmp299) == 1:
                                                                        tmp300 = tmp299[0]
                                                                    else:
                                                                        assert False, "Unreachable"
                                                                    subst2 = Substitution(subst1)
                                                                    try:
                                                                        subst2.try_add_variable('i2.2.1.1', tmp300)
                                                                    except ValueError:
                                                                        pass
                                                                    else:
                                                                        pass
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
                                                                                                    # State 3052
                                                                                                    if len(subjects2) == 0:
                                                                                                        pass
                                                                                                        # State 3053
                                                                                                        if len(subjects) == 0:
                                                                                                            pass
                                                                                                            tmp_subst = Substitution()
                                                                                                            tmp_subst['x'] = subst2['i2.2.1.1']
                                                                                                            tmp_subst['n'] = subst2['i2.2.1.2']
                                                                                                            tmp_subst['b1'] = subst2['i2.2.1.0']
                                                                                                            tmp_subst['a1'] = subst2['i2.2.0']
                                                                                                            tmp_subst['p'] = subst2['i2.2']
                                                                                                            tmp_subst['b2'] = subst2['i2.2.1.0_1']
                                                                                                            tmp_subst['a2'] = subst2['i2.2.0_1']
                                                                                                            tmp_subst['m'] = subst2['i2.2_1']
                                                                                                            # 33: Integral(x**m*(a1 + b1*x**n)**p*(a2 + b2*x**n)**p, x) /; (cons_f59) and (cons_f60) and (cons_f61) and (cons_f62) and (cons_f19) and (cons_f4) and (cons_f5) and (cons_f57) and (cons_f58) and (cons_f56)
                                                                                                            yield replacement34, tmp_subst, [(cons_f59), (cons_f60), (cons_f61), (cons_f62), (cons_f19), (cons_f4), (cons_f5), (cons_f57), (cons_f58), (cons_f56)]
                                                                    if len(subjects2) == 0:
                                                                        break
                                                                    tmp299.append(subjects2.popleft())
                                                                subjects2.extendleft(reversed(tmp299))
                if pattern_index == 32:
                    pass
                    if 'i2' not in subst1 or 'i2.2.0' not in subst1 or cons_f2(a=subst1["i2.2.0"], x=subst1["i2"]):
                        pass
                        if 'i2' not in subst1 or 'i2.2.1.0' not in subst1 or cons_f3(b=subst1["i2.2.1.0"], x=subst1["i2"]):
                            pass
                            if 'i2.2.1.2' not in subst1 or 'i2' not in subst1 or cons_f4(n=subst1["i2.2.1.2"], x=subst1["i2"]):
                                pass
                                if 'i2' not in subst1 or 'i2.2' not in subst1 or cons_f5(p=subst1["i2.2"], x=subst1["i2"]):
                                    pass
                                    if 'i2' not in subst1 or 'i2.2.1.1' not in subst1 or cons_f11(Pm=subst1["i2.2.1.1"], x=subst1["i2"]):
                                        pass
                                        if 'i2' not in subst1 or 'i2.0' not in subst1 or cons_f63(Qm=subst1["i2.0"], x=subst1["i2"]):
                                            pass
                                            if 'i2' not in subst1 or 'i2.2.1.1' not in subst1 or 'i2.2.1.0' not in subst1 or 'i2.2.0' not in subst1 or 'i2.0' not in subst1 or 'i2.2' not in subst1 or 'i2.2.1.2' not in subst1 or With35(Pm=subst1["i2.2.1.1"], Qm=subst1["i2.0"], a=subst1["i2.2.0"], b=subst1["i2.2.1.0"], n=subst1["i2.2.1.2"], p=subst1["i2.2"], x=subst1["i2"]):
                                                pass
                                                # State 3064
                                                if len(subjects2) >= 1:
                                                    tmp302 = []
                                                    tmp302.append(subjects2.popleft())
                                                    while True:
                                                        if len(tmp302) > 1:
                                                            tmp303 = create_operation_expression(associative1, tmp302)
                                                        elif len(tmp302) == 1:
                                                            tmp303 = tmp302[0]
                                                        else:
                                                            assert False, "Unreachable"
                                                        subst2 = Substitution(subst1)
                                                        try:
                                                            subst2.try_add_variable('i2', tmp303)
                                                        except ValueError:
                                                            pass
                                                        else:
                                                            pass
                                                            if 'i2' not in subst2 or 'i2.2.0' not in subst2 or cons_f2(a=subst2["i2.2.0"], x=subst2["i2"]):
                                                                pass
                                                                if 'i2' not in subst2 or 'i2.2.1.0' not in subst2 or cons_f3(b=subst2["i2.2.1.0"], x=subst2["i2"]):
                                                                    pass
                                                                    if 'i2.2.1.2' not in subst2 or 'i2' not in subst2 or cons_f4(n=subst2["i2.2.1.2"], x=subst2["i2"]):
                                                                        pass
                                                                        if 'i2' not in subst2 or 'i2.2' not in subst2 or cons_f5(p=subst2["i2.2"], x=subst2["i2"]):
                                                                            pass
                                                                            if 'i2' not in subst2 or 'i2.2.1.1' not in subst2 or cons_f11(Pm=subst2["i2.2.1.1"], x=subst2["i2"]):
                                                                                pass
                                                                                if 'i2' not in subst2 or 'i2.0' not in subst2 or cons_f63(Qm=subst2["i2.0"], x=subst2["i2"]):
                                                                                    pass
                                                                                    if 'i2' not in subst2 or 'i2.2.1.1' not in subst2 or 'i2.2.1.0' not in subst2 or 'i2.2.0' not in subst2 or 'i2.0' not in subst2 or 'i2.2' not in subst2 or 'i2.2.1.2' not in subst2 or With35(Pm=subst2["i2.2.1.1"], Qm=subst2["i2.0"], a=subst2["i2.2.0"], b=subst2["i2.2.1.0"], n=subst2["i2.2.1.2"], p=subst2["i2.2"], x=subst2["i2"]):
                                                                                        pass
                                                                                        # State 3065
                                                                                        if len(subjects2) == 0:
                                                                                            pass
                                                                                            # State 3066
                                                                                            if len(subjects) == 0:
                                                                                                pass
                                                                                                tmp_subst = Substitution()
                                                                                                tmp_subst['Pm'] = subst2['i2.2.1.1']
                                                                                                tmp_subst['n'] = subst2['i2.2.1.2']
                                                                                                tmp_subst['b'] = subst2['i2.2.1.0']
                                                                                                tmp_subst['a'] = subst2['i2.2.0']
                                                                                                tmp_subst['p'] = subst2['i2.2']
                                                                                                tmp_subst['Qm'] = subst2['i2.0']
                                                                                                tmp_subst['x'] = subst2['i2']
                                                                                                # 34: Integral(Qm*(Pm**n*b + a)**p, x) /; (cons_f2) and (cons_f3) and (cons_f4) and (cons_f5) and (cons_f11) and (cons_f63) and (With35)
                                                                                                yield replacement35, tmp_subst, [(cons_f2), (cons_f3), (cons_f4), (cons_f5), (cons_f11), (cons_f63), (With35)]
                                                        if len(subjects2) == 0:
                                                            break
                                                        tmp302.append(subjects2.popleft())
                                                    subjects2.extendleft(reversed(tmp302))
                if pattern_index == 33:
                    pass
                    if 'i2' not in subst1 or 'i2.2.0' not in subst1 or cons_f2(a=subst1["i2.2.0"], x=subst1["i2"]):
                        pass
                        if 'i2.2.1.2' not in subst1 or 'i2.2.1.2_1' not in subst1 or cons_f48(n=subst1["i2.2.1.2"], n2=subst1["i2.2.1.2_1"]):
                            pass
                            if 'i2' not in subst1 or 'i2.2.1.0' not in subst1 or cons_f3(b=subst1["i2.2.1.0"], x=subst1["i2"]):
                                pass
                                if 'i2.2.1.2' not in subst1 or 'i2' not in subst1 or cons_f4(n=subst1["i2.2.1.2"], x=subst1["i2"]):
                                    pass
                                    if 'i2' not in subst1 or 'i2.2' not in subst1 or cons_f5(p=subst1["i2.2"], x=subst1["i2"]):
                                        pass
                                        if 'i2' not in subst1 or 'i2.2.1.1' not in subst1 or cons_f11(Pm=subst1["i2.2.1.1"], x=subst1["i2"]):
                                            pass
                                            if 'i2' not in subst1 or 'i2.0' not in subst1 or cons_f63(Qm=subst1["i2.0"], x=subst1["i2"]):
                                                pass
                                                if 'i2' not in subst1 or 'i2.2.1.0_1' not in subst1 or cons_f8(c=subst1["i2.2.1.0_1"], x=subst1["i2"]):
                                                    pass
                                                    if 'i2' not in subst1 or 'i2.2.1.1' not in subst1 or 'i2.2.1.0' not in subst1 or 'i2.2.0' not in subst1 or 'i2.0' not in subst1 or 'i2.2.1.2_1' not in subst1 or 'i2.2.1.2' not in subst1 or 'i2.2' not in subst1 or 'i2.2.1.0_1' not in subst1 or With36(Pm=subst1["i2.2.1.1"], Qm=subst1["i2.0"], a=subst1["i2.2.0"], b=subst1["i2.2.1.0"], c=subst1["i2.2.1.0_1"], n=subst1["i2.2.1.2"], n2=subst1["i2.2.1.2_1"], p=subst1["i2.2"], x=subst1["i2"]):
                                                        pass
                                                        # State 3075
                                                        if len(subjects2) >= 1:
                                                            tmp305 = []
                                                            tmp305.append(subjects2.popleft())
                                                            while True:
                                                                if len(tmp305) > 1:
                                                                    tmp306 = create_operation_expression(associative1, tmp305)
                                                                elif len(tmp305) == 1:
                                                                    tmp306 = tmp305[0]
                                                                else:
                                                                    assert False, "Unreachable"
                                                                subst2 = Substitution(subst1)
                                                                try:
                                                                    subst2.try_add_variable('i2', tmp306)
                                                                except ValueError:
                                                                    pass
                                                                else:
                                                                    pass
                                                                    if 'i2' not in subst2 or 'i2.2.0' not in subst2 or cons_f2(a=subst2["i2.2.0"], x=subst2["i2"]):
                                                                        pass
                                                                        if 'i2' not in subst2 or 'i2.2.1.0' not in subst2 or cons_f3(b=subst2["i2.2.1.0"], x=subst2["i2"]):
                                                                            pass
                                                                            if 'i2.2.1.2' not in subst2 or 'i2' not in subst2 or cons_f4(n=subst2["i2.2.1.2"], x=subst2["i2"]):
                                                                                pass
                                                                                if 'i2' not in subst2 or 'i2.2' not in subst2 or cons_f5(p=subst2["i2.2"], x=subst2["i2"]):
                                                                                    pass
                                                                                    if 'i2' not in subst2 or 'i2.2.1.1' not in subst2 or cons_f11(Pm=subst2["i2.2.1.1"], x=subst2["i2"]):
                                                                                        pass
                                                                                        if 'i2' not in subst2 or 'i2.0' not in subst2 or cons_f63(Qm=subst2["i2.0"], x=subst2["i2"]):
                                                                                            pass
                                                                                            if 'i2' not in subst2 or 'i2.2.1.0_1' not in subst2 or cons_f8(c=subst2["i2.2.1.0_1"], x=subst2["i2"]):
                                                                                                pass
                                                                                                if 'i2' not in subst2 or 'i2.2.1.1' not in subst2 or 'i2.2.1.0' not in subst2 or 'i2.2.0' not in subst2 or 'i2.0' not in subst2 or 'i2.2.1.2_1' not in subst2 or 'i2.2.1.2' not in subst2 or 'i2.2' not in subst2 or 'i2.2.1.0_1' not in subst2 or With36(Pm=subst2["i2.2.1.1"], Qm=subst2["i2.0"], a=subst2["i2.2.0"], b=subst2["i2.2.1.0"], c=subst2["i2.2.1.0_1"], n=subst2["i2.2.1.2"], n2=subst2["i2.2.1.2_1"], p=subst2["i2.2"], x=subst2["i2"]):
                                                                                                    pass
                                                                                                    # State 3076
                                                                                                    if len(subjects2) == 0:
                                                                                                        pass
                                                                                                        # State 3077
                                                                                                        if len(subjects) == 0:
                                                                                                            pass
                                                                                                            tmp_subst = Substitution()
                                                                                                            tmp_subst['Pm'] = subst2['i2.2.1.1']
                                                                                                            tmp_subst['n'] = subst2['i2.2.1.2']
                                                                                                            tmp_subst['b'] = subst2['i2.2.1.0']
                                                                                                            tmp_subst['n2'] = subst2['i2.2.1.2_1']
                                                                                                            tmp_subst['c'] = subst2['i2.2.1.0_1']
                                                                                                            tmp_subst['a'] = subst2['i2.2.0']
                                                                                                            tmp_subst['p'] = subst2['i2.2']
                                                                                                            tmp_subst['Qm'] = subst2['i2.0']
                                                                                                            tmp_subst['x'] = subst2['i2']
                                                                                                            # 35: Integral(Qm*(Pm**n2*c + Pm**n*b + a)**p, x) /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f4) and (cons_f5) and (cons_f48) and (cons_f11) and (cons_f63) and (With36)
                                                                                                            yield replacement36, tmp_subst, [(cons_f2), (cons_f3), (cons_f8), (cons_f4), (cons_f5), (cons_f48), (cons_f11), (cons_f63), (With36)]
                                                                if len(subjects2) == 0:
                                                                    break
                                                                tmp305.append(subjects2.popleft())
                                                            subjects2.extendleft(reversed(tmp305))
                if pattern_index == 34:
                    pass
                    if 'i2.2' not in subst1 or cons_f64(m=subst1["i2.2"]):
                        pass
                        if 'i2.2_1' not in subst1 or cons_f65(p=subst1["i2.2_1"]):
                            pass
                            if 'i2.1' not in subst1 or 'i2' not in subst1 or cons_f66(Pq=subst1["i2.1"], x=subst1["i2"]):
                                pass
                                if 'i2.1_1' not in subst1 or 'i2' not in subst1 or cons_f67(Qr=subst1["i2.1_1"], x=subst1["i2"]):
                                    pass
                                    if 'i2' not in subst1 or 'i2.1' not in subst1 or 'i2.0' not in subst1 or 'i2.2' not in subst1 or 'i2.1_1' not in subst1 or 'i2.2_1' not in subst1 or With37(Pq=subst1["i2.1"], Qr=subst1["i2.1_1"], m=subst1["i2.2"], p=subst1["i2.2_1"], u=subst1["i2.0"], x=subst1["i2"]):
                                        pass
                                        # State 3081
                                        if len(subjects2) >= 1:
                                            tmp308 = []
                                            tmp308.append(subjects2.popleft())
                                            while True:
                                                if len(tmp308) > 1:
                                                    tmp309 = create_operation_expression(associative1, tmp308)
                                                elif len(tmp308) == 1:
                                                    tmp309 = tmp308[0]
                                                else:
                                                    assert False, "Unreachable"
                                                subst2 = Substitution(subst1)
                                                try:
                                                    subst2.try_add_variable('i2', tmp309)
                                                except ValueError:
                                                    pass
                                                else:
                                                    pass
                                                    if 'i2.1' not in subst2 or 'i2' not in subst2 or cons_f66(Pq=subst2["i2.1"], x=subst2["i2"]):
                                                        pass
                                                        if 'i2.1_1' not in subst2 or 'i2' not in subst2 or cons_f67(Qr=subst2["i2.1_1"], x=subst2["i2"]):
                                                            pass
                                                            if 'i2' not in subst2 or 'i2.1' not in subst2 or 'i2.0' not in subst2 or 'i2.2' not in subst2 or 'i2.1_1' not in subst2 or 'i2.2_1' not in subst2 or With37(Pq=subst2["i2.1"], Qr=subst2["i2.1_1"], m=subst2["i2.2"], p=subst2["i2.2_1"], u=subst2["i2.0"], x=subst2["i2"]):
                                                                pass
                                                                # State 3082
                                                                if len(subjects2) == 0:
                                                                    pass
                                                                    # State 3083
                                                                    if len(subjects) == 0:
                                                                        pass
                                                                        tmp_subst = Substitution()
                                                                        tmp_subst['Pq'] = subst2['i2.1']
                                                                        tmp_subst['m'] = subst2['i2.2']
                                                                        tmp_subst['Qr'] = subst2['i2.1_1']
                                                                        tmp_subst['p'] = subst2['i2.2_1']
                                                                        tmp_subst['u'] = subst2['i2.0']
                                                                        tmp_subst['x'] = subst2['i2']
                                                                        # 36: Integral(Pq**m*Qr**p*u, x) /; (cons_f64) and (cons_f65) and (cons_f66) and (cons_f67) and (With37)
                                                                        yield replacement37, tmp_subst, [(cons_f64), (cons_f65), (cons_f66), (cons_f67), (With37)]
                                                if len(subjects2) == 0:
                                                    break
                                                tmp308.append(subjects2.popleft())
                                            subjects2.extendleft(reversed(tmp308))
                if pattern_index == 35:
                    pass
                    if 'i2.2' not in subst1 or cons_f65(p=subst1["i2.2"]):
                        pass
                        if 'i2' not in subst1 or 'i2.0' not in subst1 or cons_f66(Pq=subst1["i2.0"], x=subst1["i2"]):
                            pass
                            if 'i2.1' not in subst1 or 'i2' not in subst1 or cons_f67(Qr=subst1["i2.1"], x=subst1["i2"]):
                                pass
                                if 'i2' not in subst1 or 'i2.1' not in subst1 or 'i2.0_1' not in subst1 or 'i2.2' not in subst1 or 'i2.0' not in subst1 or With38(Pq=subst1["i2.0"], Qr=subst1["i2.1"], p=subst1["i2.2"], u=subst1["i2.0_1"], x=subst1["i2"]):
                                    pass
                                    # State 3084
                                    if len(subjects2) >= 1:
                                        tmp311 = []
                                        tmp311.append(subjects2.popleft())
                                        while True:
                                            if len(tmp311) > 1:
                                                tmp312 = create_operation_expression(associative1, tmp311)
                                            elif len(tmp311) == 1:
                                                tmp312 = tmp311[0]
                                            else:
                                                assert False, "Unreachable"
                                            subst2 = Substitution(subst1)
                                            try:
                                                subst2.try_add_variable('i2', tmp312)
                                            except ValueError:
                                                pass
                                            else:
                                                pass
                                                if 'i2' not in subst2 or 'i2.0' not in subst2 or cons_f66(Pq=subst2["i2.0"], x=subst2["i2"]):
                                                    pass
                                                    if 'i2.1' not in subst2 or 'i2' not in subst2 or cons_f67(Qr=subst2["i2.1"], x=subst2["i2"]):
                                                        pass
                                                        if 'i2' not in subst2 or 'i2.1' not in subst2 or 'i2.0_1' not in subst2 or 'i2.2' not in subst2 or 'i2.0' not in subst2 or With38(Pq=subst2["i2.0"], Qr=subst2["i2.1"], p=subst2["i2.2"], u=subst2["i2.0_1"], x=subst2["i2"]):
                                                            pass
                                                            # State 3085
                                                            if len(subjects2) == 0:
                                                                pass
                                                                # State 3086
                                                                if len(subjects) == 0:
                                                                    pass
                                                                    tmp_subst = Substitution()
                                                                    tmp_subst['Qr'] = subst2['i2.1']
                                                                    tmp_subst['p'] = subst2['i2.2']
                                                                    tmp_subst['Pq'] = subst2['i2.0']
                                                                    tmp_subst['u'] = subst2['i2.0_1']
                                                                    tmp_subst['x'] = subst2['i2']
                                                                    # 37: Integral(Pq*Qr**p*u, x) /; (cons_f65) and (cons_f66) and (cons_f67) and (With38)
                                                                    yield replacement38, tmp_subst, [(cons_f65), (cons_f66), (cons_f67), (With38)]
                                            if len(subjects2) == 0:
                                                break
                                            tmp311.append(subjects2.popleft())
                                        subjects2.extendleft(reversed(tmp311))
            subjects2.appendleft(tmp203)
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
from .generated_part000002 import *
from .generated_part000003 import *
from .generated_part000004 import *
from .generated_part000005 import *
from .generated_part000006 import *
from .generated_part000007 import *
from .generated_part000008 import *
from .generated_part000009 import *
from .generated_part000010 import *
from .generated_part000011 import *
from .generated_part000012 import *
from .generated_part000013 import *
from .generated_part000014 import *
from .generated_part000015 import *
from .generated_part000016 import *
from .generated_part000017 import *
from .generated_part000018 import *
from .generated_part000019 import *
