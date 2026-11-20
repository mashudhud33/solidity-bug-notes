"""A very simple rule-based checker, just to have a baseline.

It looks for a few patterns I am learning to spot:
- a .call{value:} that happens before the balance is cleared
- tx.origin used for auth
- a withdraw function with no access check at all
- a .call whose return value is ignored
- block.timestamp used to decide something important

Run: python3 scripts/baseline.py <contract.sol>
It prints what it found, nothing more.
"""
import sys
from pathlib import Path

def strip_comments(code):
    lines = []
    for line in code.splitlines():
        if "//" in line:
            line = line[:line.index("//")]
        lines.append(line)
    return "\n".join(lines)

def check(code):
    code = strip_comments(code)
    findings = []
    if "tx.origin" in code:
        findings.append("uses tx.origin for auth")
    if ".call{value:" in code and "balances[msg.sender] = 0" in code:
        # crude check: is the balance cleared after the call?
        if code.index(".call{value:") < code.index("balances[msg.sender] = 0"):
            findings.append("possible reentrancy: balance cleared after external call")
    if ".call{value:" in code and "(bool ok" not in code:
        findings.append("unchecked call: return value is ignored")
    if "transfer(address(this).balance)" in code and "require(msg.sender" not in code and "require(tx.origin" not in code:
        findings.append("withdraw has no access check")
    if "block.timestamp" in code:
        findings.append("uses block.timestamp for a decision")
    if "function init()" in code:
        findings.append("has an init function anyone can call")
    return findings

def main():
    path = Path(sys.argv[1])
    findings = check(path.read_text())
    print(f"{path}:")
    if not findings:
        print("  no issues found by these simple rules")
    for finding in findings:
        print(f"  - {finding}")

if __name__ == "__main__":
    main()
