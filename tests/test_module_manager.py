"""
Unit tests for module manager.
"""

import pytest
from gaia_framework.module_manager import ModuleManager


class MockModule:
    """Mock module for testing."""
    
    def __init__(self, result="success"):
        self.result = result
    
    def execute(self):
        """Execute the mock module."""
        return self.result


def test_module_manager_init():
    """Test that ModuleManager initializes correctly."""
    manager = ModuleManager()
    assert manager.modules == []


def test_register_module():
    """Test module registration."""
    manager = ModuleManager()
    module = MockModule()
    manager.register_module(module)
    assert len(manager.modules) == 1


def test_execute_modules():
    """Test module execution."""
    manager = ModuleManager()
    module1 = MockModule("result1")
    module2 = MockModule("result2")
    manager.register_module(module1)
    manager.register_module(module2)
    results = manager.execute_modules()
    assert results == ["result1", "result2"]
