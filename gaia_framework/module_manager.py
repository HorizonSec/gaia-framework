"""
Module manager for orchestrating security modules.
"""


class ModuleManager:
    """Orchestrates security modules within the GAIA Framework."""

    def __init__(self):
        """Initialize the module manager."""
        self.modules = []

    def register_module(self, module):
        """Register a new module.
        
        Args:
            module: The module to register.
        """
        self.modules.append(module)

    def execute_modules(self):
        """Execute all registered modules."""
        results = []
        for module in self.modules:
            result = module.execute()
            results.append(result)
        return results
