# 31_dynamic_docstrings.py

header = "Say hello in Python"

def hello(name: str) -> str:
    """
    %s
    
    Python is amazing!
    """
    return f"Hello {name}. Nice to meet you!"

hello.__doc__ %= header
help(hello)