import os 
import sys

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from scanner.security import scan_code_for_security

if __name__ == "__main__":
    results = scan_code_for_security("tests/test_vulnerability.py")
    for result in results:
        #print(result.__dict__)
        print(f"Issue: {result.text}")
        print(f"Severity: {result.severity}")
        print(f"Confidence: {result.confidence}")
        print(f"File: {result.fname}, Line: {result.lineno}")
        print("-" * 40)
