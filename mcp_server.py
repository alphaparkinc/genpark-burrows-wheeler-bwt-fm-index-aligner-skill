import sys
import json
from client import FMIndex

def main():
    fm = FMIndex()
    while True:
        line = sys.stdin.readline()
        if not line:
            break
        req = json.loads(line)
        method = req.get("method")
        params = req.get("params", {})
        if method == "bwt":
            res = {"bwt": fm.bwt_transform(params.get("text", ""))}
        elif method == "count":
            res = {"count": fm.count_matches(params.get("bwt", ""), params.get("pattern", ""))}
        else:
            res = {"error": "unknown method"}
        sys.stdout.write(json.dumps({"id": req.get("id"), "result": res}) + "\n")
        sys.stdout.flush()

if __name__ == "__main__":
    main()
