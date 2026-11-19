"""A very simple rule-based checker, just to have a baseline.

It looks for two patterns I am learning to spot:
- a .call{value:} that happens before the balance is cleared
- tx.origin used for auth

Run: python3 scripts/baseline.py <contract.sol>
It prints what it found, nothing more.
"""
import sys
from pathlib import Path

def check(code):
    findings = []
    if "tx.origin" in code:
        findings.append("uses tx.origin for auth")
    if ".call{value:" in code and "balances[msg.sender] = 0" in code:
        # crude check: is the balance cleared after the call?
        if code.index(".call{value:") < code.index("balances[msg.sender] = 0"):
            findings.append("possible reentrancy: balance cleared after external call")
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
