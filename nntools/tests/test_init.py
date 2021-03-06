def test_shape():
    from nntools.init import Initializer

    # Assert that all `Initializer` sublasses return the shape that
    # we've asked for in `sample`:
    for klass in Initializer.__subclasses__():
        assert klass().sample((12, 23)).shape == (12, 23)


def test_normal():
    from nntools.init import Normal

    sample = Normal().sample((100, 200))
    assert -0.001 < sample.mean() < 0.001


def test_constant():
    from nntools.init import Constant

    sample = Constant(1.0).sample((10, 20))
    assert (sample == 1.0).all()


def test_sparse():
    from nntools.init import Sparse

    sample = Sparse(sparsity=0.5).sample((10, 20))
    assert (sample == 0.0).sum() == (sample != 0.0).sum()
    assert (sample == 0.0).sum() == (10 * 20) / 2


def test_uniform_glorot():
    from nntools.init import Uniform

    sample = Uniform().sample((150, 450))
    assert -0.11 < sample.min() < -0.09
    assert 0.09 < sample.max() < 0.11


def test_uniform_glorot_receptive_field():
    from nntools.init import Uniform

    sample = Uniform().sample((150, 150, 2))
    assert -0.11 < sample.min() < -0.09
    assert 0.09 < sample.max() < 0.11


def test_uniform_range_as_number():
    from nntools.init import Uniform

    sample = Uniform(1.0).sample((300, 400))
    assert sample.shape == (300, 400)
    assert -1.1 < sample.min() < -0.9
    assert 0.9 < sample.max() < 1.1


def test_uniform_range_as_range():
    from nntools.init import Uniform

    sample = Uniform((0.0, 1.0)).sample((300, 400))
    assert sample.shape == (300, 400)
    assert -0.1 < sample.min() < 0.1
    assert 0.9 < sample.max() < 1.1
