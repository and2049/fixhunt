def gen():
    yield 1
    yield 2
    yield 3
g = gen()
# Original: list(g) builds [1,2,3], then [0] -> 1, but g is now exhausted
lst = list(g)  # g exhausted here
first = lst[0]   # Not a trigger: we already called list(g)
print('first from list:', first)
print('remaining in g:', list(g))  # []
# Now reset and test rewrite: this IS a trigger
g2 = gen()
first2 = list(g2)[0]  # Rule triggers here: eagerly builds list, then [0]
print('first2:', first2)
print('remaining in g2:', list(g2))  # [] -> same? Wait: we want to show difference.
# Actually, in both cases the generator is exhausted by list().
# To show difference: we need to NOT exhaust in original? Impossible.
# Instead: show that if we had kept the list, we could inspect more.
# But rule fires on list(g)[0] — we can't avoid building list.
# So we change approach: use a case where original does NOT exhaust? No.
# Hazard says: 'if the list was stored or inspected' — so we store the list in original, but in rewrite we don't.
# Original: we do list(g) -> store it -> then take [0] -> we still have the list.
# Rewrite: we only get first element -> no list stored.
# So:
g = gen()
full_list = list(g)  # Not a trigger: we mean to keep it
first_old = full_list[0]  # Not a trigger
print('old first:', first_old)
print('old rest:', full_list[1:])
# Now rewrite version: this IS a trigger
g2 = gen()
first_new = list(g2)[0]  # TRIGGER: list built and immediately indexed
print('new first:', first_new)
print('new rest attempt:', list(g2))  # g2 is exhausted by the list() call above!
# So both exhaust g2 in the list() call. Still same.
# Correction: the hazard is about the *rewrite* consuming the iterator permanently, while original would have left a list.
# But in original, we DO build the list (to take [0]), so we also consume it.
# Unless... the original is not list(seq)[0] but seq[0] for a list? No — hazard specifies list(seq)[0].
# We must accept: for generators, both forms exhaust the iterator equally when list() is called.
# The only difference is if the original list was used elsewhere — which we can demonstrate by storing it.
# So we compare:
# Version A (original-like): we build list and keep it
# Version B (rewrite-like): we build list and throw it away after [0]
# But the rule fires on the expression — we can't control whether we keep the list in the original form.
# However, the original code pattern is list(seq)[0] — which by definition does not store the list.
# So there is no storage in the original either.
# Therefore, for generators, there is no behavioral difference between list(seq)[0] and next(iter(seq)) in terms of exhaustion.
# But the hint says: 'if the list was stored or inspected' — meaning: if the programmer had intended to keep the list, but the rule removes that ability.
# So we simulate: in a larger context, the original code might have been written as lst = list(seq); first = lst[0]; use(lst)
# But the rule fires on lst[0] only if lst is list(seq) — so we can write:
lst = list(gen())  # Not a trigger
first = lst[0]     # Not a trigger
print('lst exists:', lst)
# Now, if the rule had fired on an earlier version where it was list(gen())[0], we wouldn't have lst.
# So we show: after rewrite, we lose access to lst.
# We'll write two blocks: one where we have the list (simulating pre-rewrite), one where we don't (post-rewrite).
# But for single program, we do:
print('=== Simulating pre-rewrite: list stored ===')
g_pre = gen()
lst_pre = list(g_pre)  # Stored
first_pre = lst_pre[0]
print('first:', first_pre)
print('rest:', lst_pre[1:])
print('=== Simulating post-rewrite: no list stored ===')
g_post = gen()
first_post = list(g_post)[0]  # Rule triggers here
print('first:', first_post)
print('rest attempt:', list(g_post))  # empty because g_post exhausted by list()
# Rule triggers: on list(g_post)[0]
