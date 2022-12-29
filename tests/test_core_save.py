from pathlib import Path

import pytest
from flax.core.frozen_dict import FrozenDict

from safejax import serialize


@pytest.mark.parametrize(
    "params",
    [
        pytest.lazy_fixture("single_layer_params"),
        pytest.lazy_fixture("flax_resnet50_params"),
    ],
)
def test_serialize(params: FrozenDict) -> None:
    encoded_params = serialize(params=params)
    assert isinstance(encoded_params, bytes)
    assert len(encoded_params) > 0


@pytest.mark.parametrize(
    "params",
    [
        pytest.lazy_fixture("single_layer_params"),
        pytest.lazy_fixture("flax_resnet50_params"),
    ],
)
@pytest.mark.usefixtures("safetensors_file")
def test_serialize_to_file(params: FrozenDict, safetensors_file: Path) -> None:
    safetensors_file = serialize(params=params, filename=safetensors_file)
    assert isinstance(safetensors_file, Path)
    assert safetensors_file.exists()
