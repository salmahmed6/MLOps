from unittest.mock import MagicMock

import pytest

from src.model import RideDurationModel


def test_predict_returns_float():
    model = RideDurationModel()

    model._model = MagicMock()
    model._model.predict.return_value = [23.5]

    result = model.predict([5.0, 1])

    assert result == 23.5
    assert isinstance(result, float)


def test_predict_raises_when_model_not_loaded():
    model = RideDurationModel()

    with pytest.raises(RuntimeError, match="Model is not loaded"):
        model.predict([5.0, 1])


@pytest.mark.parametrize(
    "features, expected",
    [
        ([1.0, 1], 5.2),
        ([10.0, 2], 24.8),
        ([0.5, 4], 3.1),
    ],
)
def test_predict_inputs(features, expected):
    model = RideDurationModel()

    model._model = MagicMock()
    model._model.predict.return_value = [expected]

    result = model.predict(features)

    assert result == expected