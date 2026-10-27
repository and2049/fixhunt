for i in range(2):
    x = x + i if 'x' in locals() else 0 + i  # Trigger on second iter
    print(f'line={i}, x={x}')
# After fix: line attribution shifts; if debugger breaks on 'x = x + i', it may not trigger
