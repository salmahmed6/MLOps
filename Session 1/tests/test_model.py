import pytest
from unittest.mock import MagicMock

from src.model import RideDurationModel


@pytest.mark.parametrize(
    "distance, passengers, expected",
    [
        (1.0, 1, 5.2),
        (10.0, 2, 24.8),
        (0.5, 4, 3.1),
    ],
)
def test_predict_inputs(distance, passengers, expected):
    model = RideDurationModel()

    model._model = MagicMock()
    model._model.predict.return_value = [expected]

    assert model.predict([distance, passengers]) == expected