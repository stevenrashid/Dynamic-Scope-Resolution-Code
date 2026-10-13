# Dynamic Scope Resolution in Python

An educational implementation of a dynamic reference environment using Python stack introspection.

`get_dynamic_re()` examines active caller frames and collects function-local bindings into a read-only mapping interface. The nearest active binding wins, allowing explicit exploration of dynamic scope while Python's normal name resolution remains unchanged.

## Implementation

| Component | Behavior |
| --- | --- |
| `DynamicScope` | Implements `collections.abc.Mapping` over the captured environment. |
| `get_dynamic_re()` | Walks outward through caller frames using `inspect.stack()`. |
| `_UNBOUND` | Marks a syntactically local name that has no assigned value. |

The implementation considers local and cell-variable names. It deliberately excludes closure free variables. Missing names raise `NameError`; a nearest local binding that has not been assigned raises `UnboundLocalError` instead of falling through to a more distant binding.

## Try it

Python 3 is required; the implementation uses only the standard library.

```bash
git clone https://github.com/stevenrashid/Dynamic-Scope-Resolution-Code.git
cd Dynamic-Scope-Resolution-Code
python
```

From the repository root:

```python
from __init__ import get_dynamic_re

def read_caller():
    return get_dynamic_re()["message"]

def caller():
    message = "Hello from the caller"
    return read_caller()

print(caller())
# Hello from the caller
```

The import reflects the repository's current flat layout: the implementation is stored directly in [__init__.py](__init__.py).

## Behavior and limits

- The returned environment captures bindings when the function is called; it is not a live replacement for Python scope.
- The implementation collects function-local and cell-variable names, not a general lookup of module globals or built-ins.
- Shadowing follows call-stack proximity.
- `skeleton_test.py` contains a unittest runner scaffold but no actual test cases, so running it does not establish coverage.
- There is no package metadata or installation configuration.

## Learning focus

Call-stack inspection, mappings, local-variable metadata, shadowing, and the distinction between lexical and dynamic scope.
