text = """  Line1
  {x}
  Line2"""  # Rule triggers: becomes f"""  Line1
  {x}
  Line2"""
x = 42
print(repr(text))  # Shows indentation preserved; f-string doesn't change dedent by itself.
# But if combined with textwrap.dedent:
import textwdedent = textwrap.dedent
normal = textdedent("""  Line1
  {x}
  Line2""")  # Not triggered
fix_dedent = textdedent(f"""  Line1
  {x}
  Line2""")  # Triggered: f-string first, then dedent
print(f"Normal dedent: {repr(normal)}")
print(f"Fix dedent:   {repr(fix_dedent)}")
