from Nuevooptimizar import Optimizar

def test_add():
    c =  Optimizar();
    c.add(1)
    assert len(c.array)== 1

def test_media():
    d = Optimizar();
    d.add(4)
    d.add(4)
    assert d.media() == 4