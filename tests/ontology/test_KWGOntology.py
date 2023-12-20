from pykwg.ontology.KWGOntology import KWGOntology


def test_kwg_base_default():
    """
    Tests that the kwgr and kwg-ont prefixes use the fallback base path

    :return: None
    """
    onto = KWGOntology()
    assert onto.prefix["kwgr"] == "http://stko-kwg.geog.ucsb.edu/lod/resource"
    assert onto.prefix["kwg-ont"] == "http://stko-kwg.geog.ucsb.edu/lod/ontology"


def test_kwg_base_custom(monkeypatch):
    """
    Tests that the kwgr and kwg-ont prefixes use the custom base path

    :return: None
    """
    mock_url = "http://aFakeBaseURL/"
    monkeypatch.setenv("KWG_BASE_ADDRESS", mock_url)
    onto = KWGOntology()
    assert onto.prefix["kwgr"] == f"{mock_url}lod/resource"
    assert onto.prefix["kwg-ont"] == f"{mock_url}lod/ontology"
