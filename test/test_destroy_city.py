from src.destroy_city import remove_city_references, remove_city, destroy_city

def test_remove_city_references():
    assert remove_city_references({'Foo': ['Bar', 'Baz', 'Qu-ux'], 'Bar': ['Foo', 'Bee']},
    {'Foo': [1, 2, 3, 4]}) == {'Foo': ['Bar', 'Baz', 'Qu-ux'], 'Bar': ['Bee']}
    assert remove_city_references({'Foo': ['Bar', 'Baz', 'Qu-ux'], 'Bar': ['Foo', 'Bee']},
    {'Foo': [1, 2], 'Bar':[3, 4]}) == {'Foo':['Baz','Qu-ux'], 'Bar':['Bee']}

def test_remove_city():
    assert remove_city({'Foo': ['Bar', 'Baz', 'Qu-ux'], 'Bar': ['Foo', 'Bee']},
    {'Foo': [1, 2, 3, 4]}) == {'Bar': ['Foo', 'Bee']}
    assert remove_city({'Foo': ['Bar', 'Baz', 'Qu-ux'], 'Bar': ['Foo', 'Bee']},
    {'Foo': [1, 2], 'Bar':[3, 4]}) == {}

def test_destroy_city():
    assert destroy_city({'Foo': ['Bar', 'Baz', 'Qu-ux'], 'Bar': ['Foo', 'Bee']},
    {'Foo': [1, 2, 3, 4]}) == {'Bar':['Bee']}
    assert destroy_city({'Foo': ['Bar', 'Baz', 'Qu-ux'], 'Bar': ['Foo', 'Bee']},
    {'Foo': [1, 2], 'Bar':[3, 4]}) == {}