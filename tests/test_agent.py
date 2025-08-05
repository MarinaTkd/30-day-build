import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import pytest
from agent import create_summary, extract_topics

def test_create_summary_returns_string(monkeypatch):
    def mock_response(text):
        return "Mocked summary"
    
    monkeypatch.setattr("agent.create_summary", mock_response)  #Hey, during this test, whenever the code tries to use the function create_summary from the agent module — don’t use the real one. Instead, use my mock_response function instead.
    result = create_summary("Some long text to summarise")
    assert isinstance(result, str)
    assert "summary" in result.lower()

def test_extract_topics_return_list(monkeypatch):
    def mock_topics(text):
        return "1.topic1, 2.topic2, 3.topic3"
    
    monkeypatch.setattr("agent.extract_topics", mock_topics)
    result = extract_topics("Po dvaceti letech se Meryl Streepová vrátila k roli démonické šéfredaktorky módního časopisu Mirandy Priestlyové. Natáčení snímku Ďábel nosí Pradu 2 právě probíhá v New Yorku. Jisté také je, že do role se vrátí i Emily Bluntová a Anne Hathawayová. Mihnout se má v komedii i česká topmodelka Karolína Kurková.")
    print(result)
    assert isinstance(result, str)
    assert len(result) > 0 