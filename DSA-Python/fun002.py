def parse_sequence(raw_text):
	"""Parse numbers from text; placeholders like '_' are ignored."""
	cleaned = raw_text.replace(",", " ").split()
	numbers = []
	for item in cleaned:
		if item in {"_", "x", "X", "none", "None"}:
			continue
		numbers.append(int(item))
	return numbers


def find_missing_numbers(numbers, start=None, end=None):
	"""Return all missing integers in the expected range."""
	if not numbers and (start is None or end is None):
		return []

	left = min(numbers) if start is None else start
	right = max(numbers) if end is None else end

	present = set(numbers)
	return [value for value in range(left, right + 1) if value not in present]


raw_sequence = input(
	"Enter sequence (space/comma separated, use _ for empty): "
)
values = parse_sequence(raw_sequence)

raw_start = input("Expected start number (Enter to auto): ").strip()
raw_end = input("Expected end number (Enter to auto): ").strip()

start_value = int(raw_start) if raw_start else None
end_value = int(raw_end) if raw_end else None

missing = find_missing_numbers(values, start_value, end_value)

if missing:
	print("Missing number(s):", missing)
else:
	print("No missing numbers found in the selected range.")
