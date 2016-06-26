
import re

pattern = r"^[-+]?[0-9]*\.[0-9]+$"
for _ in range(int(raw_input().strip())):
    print bool(re.search(pattern, raw_input().strip()))