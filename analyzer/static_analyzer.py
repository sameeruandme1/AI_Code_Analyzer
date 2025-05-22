import ast
import radon.complexity as cc
import subprocess

def get_complexity(file_path):
    try:
        with open(file_path, 'r') as file:
            code = file.read()
        visitor = cc.cc_visit(code)
        return [{"name": v.name, "complexity": v.complexity} for v in visitor]
    except Exception as e:
        return [str(e)]

def get_pylint_issues(file_path):
    try:
        result = subprocess.run(
            ['pylint', file_path, '--disable=R,C'],
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True
        )
        return result.stdout.strip().split('\n')
    except Exception as e:
        return [str(e)]

def get_complexity_per_function(file_path):
    with open(file_path, 'r') as f:
        code = f.read()
    try:
        visitor = cc.cc_visit(code)
        return [{"name": func.name, "complexity": func.complexity} for func in visitor.functions + visitor.methods]
    except Exception as e:
        return [{"name": "Error", "complexity": str(e)}]
