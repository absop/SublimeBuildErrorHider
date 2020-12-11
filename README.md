# SublimeBuildErrorHider

A SublimeText3 plugin to hide build error phantoms with the <kbd>ESC</kbd> key.


## Introduce

**SublimeBuildErrorHider** uses the <kbd>Esc</kbd> key to hide phantoms and it has no conflicts with other commands and plugins.

**SublimeBuildErrorHider** does this by adding a subclass of `ViewEventListener`, with only one member function named `on_query_context` to check if a view has a `"error_phantom_visible"` entry in it settings or not, to satisfy context checking of ST; and making some changes to the default ExecCommand class of ST's build system, with changing its member functions `update_phantoms` and `hide_phantoms`, to add 2 extra jobs:

- Add a `"error_phantom_visible"` entry to settings of the involved views when `update_phantoms` is called.

- Erase the `"error_phantom_visible"` entry from settings of the involved views when `hide_phantoms` is called.


## Key Binding
```json
[
    {
        "keys": ["escape"],
        "command": "exec",
        "args": { "hide_phantoms_only": true },
        "context":
        [
            { "key": "error_phantom_visible", "operator": "equal", "operand": true }
        ]
    }
]
```
