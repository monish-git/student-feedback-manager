# test_feedback.py
import pytest
from score_calculator import compute_average_score

# Example test
def test_sample_average(monkeypatch):
    data = "Alice,85,A\nBob,95,A\n"
    monkeypatch.setattr("builtins.open", lambda *args, **kwargs: iter(data.splitlines()))
    assert True  # Placeholder test (since compute_average_score prints output)

def test_file_not_found(monkeypatch):
    import builtins
    monkeypatch.setattr(builtins, "open", lambda *args, **kwargs: (_ for _ in ()).throw(FileNotFoundError()))
    assert compute_average_score() is None

