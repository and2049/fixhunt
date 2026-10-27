# This hazard is about module-level side effects from star-imports.
# Since we cannot reliably trigger SIM109 here without external modules,
# and the rule does not fire on import statements, we leave expect_trigger=False.
# No SIM109-triggerable shape present.
print('No trigger expected')
