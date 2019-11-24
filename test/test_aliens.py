from src.aliens import unleash_aliens

def test_aliens():
    assert unleash_aliens(4, {'Foo': ['Bar', 'Baz', 'Qu-ux'], 'Bar': ['Foo', 'Bee']}) == {1: 'Foo', 2: 'Foo', 3: 'Foo'}