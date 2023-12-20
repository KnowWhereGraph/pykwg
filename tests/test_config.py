from pykwg.config import Config


def test_missing_var():
    """
    Test that the default production address is used when an env var is missing

    :return: None
    """
    config = Config()
    assert config.base_address == "http://stko-kwg.geog.ucsb.edu/"


def test_base_address_var(monkeypatch):
    """
    Test that the base address is respected via env var

    :return: None
    """
    mock_url = "http://aFakeBaseURL"
    monkeypatch.setenv("KWG_BASE_ADDRESS", mock_url)
    config = Config()
    assert config.base_address == mock_url
