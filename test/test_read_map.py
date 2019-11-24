from src.read_map import extract_city, extract_neighbors

def test_extract_city():
    assert extract_city('Foo north=Bar west=Baz south=Qu-ux') == 'Foo'
    assert extract_city('Bar south=Foo west=Bee') == 'Bar'

def test_extract_neighbors():
    assert extract_neighbors('Foo north=Bar west=Baz south=Qu-ux') == ['Bar','Baz','Qu-ux'] 
    assert extract_neighbors('Bar south=Foo west=Bee') == ['Foo','Bee'] 
