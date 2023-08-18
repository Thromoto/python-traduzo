import json
from src.models.history_model import HistoryModel


# Req. 7
def test_request_history():
    json_list = json.loads(HistoryModel.list_as_json())

    assert len(json_list) == 2
    assert json_list[0]["text_to_translate"] == "Hello, I like videogame"
    assert json_list[0]["translate_from"] == "en"
    assert json_list[0]["translate_to"] == "pt"
