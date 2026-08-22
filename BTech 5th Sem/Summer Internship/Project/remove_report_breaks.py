with open("generate_final_report.py", "r", encoding="utf-8") as f:
    lines = f.readlines()

# Line numbers to remove (1-indexed, so we subtract 1)
lines_to_remove = [406, 439, 457, 480, 497, 534, 575, 596, 640, 678, 713, 725, 736, 777, 814, 850, 863, 876]

for idx in lines_to_remove:
    # Double check that we are commenting out doc.add_page_break()
    line_content = lines[idx - 1]
    if "doc.add_page_break()" in line_content:
        lines[idx - 1] = "# " + line_content
        print(f"Commented out page break on line {idx}")
    else:
        print(f"Warning: Line {idx} content did not match: {line_content.strip()}")

# Write back the modified script
with open("generate_final_report.py", "w", encoding="utf-8") as f:
    f.writelines(lines)

print("Saved generate_final_report.py updates successfully.")
