"""Basic tests for CodeForge platform."""

import pytest
from codeforge.core.engine import SDLCEngine


def test_engine_initialization():
    """Test that the SDLC engine can be initialized."""
    engine = SDLCEngine()
    assert engine is not None
    assert hasattr(engine, 'blueprints')
    assert hasattr(engine, 'projects')


def test_engine_create_project():
    """Test basic project creation."""
    engine = SDLCEngine()
    project_id = engine.create_project(
        blueprint_name="test-blueprint",
        project_config={"name": "Test Project"}
    )
    assert project_id.startswith("proj_")
    assert len(engine.list_projects()) == 1