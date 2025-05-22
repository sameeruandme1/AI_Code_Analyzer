def rank_issues(issue_list):
    severity = {"bug": 3, "complexity": 2, "lint": 1}
    return sorted(issue_list, key=lambda x: severity.get(x["type"], 0), reverse=True)
