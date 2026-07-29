import json

from modules.helpers import clear_resume_state, load_resume_state, save_resume_state


def test_resume_state_round_trip(tmp_path):
    state_path = tmp_path / "automation_state.json"
    state = {"url": "https://www.linkedin.com/jobs/search/", "search_term": "python", "search_term_index": 2}

    save_resume_state(state, str(state_path))
    loaded = load_resume_state(str(state_path))

    assert loaded == state

    clear_resume_state(str(state_path))
    assert load_resume_state(str(state_path)) is None
