employees = (
    (1, "CEO", "Madeline Bemelmans"),
    (2, "CTO", "Emily Elizabeth"),
    (3, "VP Ops", "François Borgot")
)
for employee in employees:
    if not employee[1].startswith('C'):
        employee[1] = 'COO'
        print(f"Promoted {employee[2]} to COO.")

# The error here is that individual employees should be represented by lists and not tuples,
# in order to support item assignments