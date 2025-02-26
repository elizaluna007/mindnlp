# Copyright 2022 Huawei Technologies Co., Ltd
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
# http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
# ============================================================================
"""
Test MobileBert
"""
import unittest

import mindspore
from mindspore import Tensor
import numpy as np

from mindnlp.models.mobilebert import MobileBertSelfAttention, MobileBertSelfOutput,\
    MobileBertAttention, MobileBertIntermediate, OutputBottleneck, MobileBertOutput,\
    BottleneckLayer, Bottleneck, FFNOutput, FFNLayer, MobileBertLayer, MobileBertEncoder,\
    MobileBertEmbeddings, MobileBertConfig

class TestMobileBert(unittest.TestCase):
    """
    Test TinyBert Models
    """

    def setUp(self):
        """
        Set up config
        """

        self.input=None

    def test_mobilebert_embedding(self):
        """
        Test MobileBertEmbeddings
        """
        model = MobileBertEmbeddings(MobileBertConfig())
        input_ids = Tensor(np.random.randint(0, 1000, (2, 128)))
        output = model(input_ids)
        assert output.shape == (2, 128, 512)

    def test_mobilebert_selfattention(self):
        """
        Test MobileBertEmbeddings
        """
        model = MobileBertSelfAttention(MobileBertConfig())
        query_tensor = Tensor(np.random.randint(0, 1000, (2, 8, 128)), dtype=mindspore.float32)
        key_tensor = Tensor(np.random.randint(0, 1000, (2, 8, 128)), dtype=mindspore.float32)
        value_tensor = Tensor(np.random.randint(0, 1000, (2, 8, 512)), dtype=mindspore.float32)
        output = model(query_tensor, key_tensor, value_tensor)
        assert output[0].shape == (2, 8, 128)

    def test_mobilebert_selfoutput(self):
        """
        Test MobileBertSelfOutput
        """
        model = MobileBertSelfOutput(MobileBertConfig())
        hidden_states = Tensor(np.random.randint(0, 1000, (2, 128)),dtype=mindspore.float32)
        residual_tensor = Tensor(np.random.randint(0, 1000, (2, 128)))
        output = model(hidden_states, residual_tensor)
        assert output.shape == (2, 128)


    def test_mobilebert_attention(self):
        """
        Test MobileBertAttention
        """
        model = MobileBertAttention(MobileBertConfig())
        query_tensor = Tensor(np.random.randint(0, 1000, (2, 8, 128)), dtype=mindspore.float32)
        key_tensor = Tensor(np.random.randint(0, 1000, (2, 8, 128)), dtype=mindspore.float32)
        value_tensor = Tensor(np.random.randint(0, 1000, (2, 8, 512)), dtype=mindspore.float32)
        layer_input = Tensor(np.random.randint(0, 1000, (2, 8, 128)), dtype=mindspore.float32)
        output = model(query_tensor, key_tensor, value_tensor, layer_input)
        assert output[0].shape == (2, 8, 128)

    def test_mobilebert_intermediate(self):
        """
        Test MobileBertIntermediate
        """
        model = MobileBertIntermediate(MobileBertConfig())
        hidden_states = Tensor(np.random.randint(0, 1000, (512, 128)), dtype=mindspore.float32)
        output = model(hidden_states)
        assert output.shape == (512,512)

    def test_mobilebert_outputbottleneck(self):
        """
        Test OutputBottleneck
        """
        model = OutputBottleneck(MobileBertConfig())
        hidden_states = Tensor(np.random.randint(0, 1000, (512, 128)), dtype=mindspore.float32)
        residual_tensor = Tensor(np.random.randint(0, 1000, (512, 512)), dtype=mindspore.float32)
        output = model(hidden_states, residual_tensor)
        assert output.shape == (512, 512)

    def test_mobilebert_mobilebertoutput(self):
        """
        Test MobileBertOutput
        """
        model = MobileBertOutput(MobileBertConfig())
        intermediate_states = Tensor(np.random.randint(0, 1000, (128, 512)), dtype=mindspore.float32)
        residual_tensor_1 = Tensor(np.random.randint(0, 1000, (128, 128)), dtype=mindspore.float32)
        residual_tensor_2 = Tensor(np.random.randint(0, 1000, (128, 512)), dtype=mindspore.float32)
        output = model(intermediate_states, residual_tensor_1, residual_tensor_2)
        assert output.shape == (128, 512)

    def test_mobilebert_bottlenecklayer(self):
        """
        Test BottleneckLayer
        """
        model = BottleneckLayer(MobileBertConfig())
        hidden_states = Tensor(np.random.randint(0, 1000, (128, 512)), dtype=mindspore.float32)
        output = model(hidden_states)
        assert output.shape == (128, 128)

    def test_mobilebert_bottleneck(self):
        """
        Test Bottleneck
        """
        model = Bottleneck(MobileBertConfig())
        hidden_states = Tensor(np.random.randint(0, 1000, (128, 512)), dtype=mindspore.float32)
        output = model(hidden_states)
        assert output[0].shape == (128, 128)
        assert output[1].shape == (128, 128)
        assert output[2].shape == (128, 512)
        assert output[3].shape == (128, 128)

    def test_mobilebert_ffnoutput(self):
        """
        Test FFNOutput
        """
        model = FFNOutput(MobileBertConfig())
        hidden_states = Tensor(np.random.randint(0, 1000, (128, 512)), dtype=mindspore.float32)
        residual_tensor = Tensor(np.random.randint(0, 1000, (128, 128)), dtype=mindspore.float32)
        output = model(hidden_states, residual_tensor)
        assert output.shape == (128, 128)

    def test_mobilebert_ffnlayer(self):
        """
        Test FFNLayer
        """
        model = FFNLayer(MobileBertConfig())
        hidden_states = Tensor(np.random.randint(0, 1000, (512, 128)), dtype=mindspore.float32)
        output = model(hidden_states)
        assert output.shape == (512,128)

    def test_mobilebert_mobilebertlayer(self):
        """
        Test MobileBertLayer
        """
        model = MobileBertLayer(MobileBertConfig())
        hidden_states = Tensor(np.random.randint(0, 1000, (2, 128, 512)), dtype=mindspore.float32)
        output = model(hidden_states)
        assert output[0].shape == (2, 128, 512)
        assert output[1].shape == ()
        for i in range(2, 12):
            if i in (4, 7):
                assert output[i].shape == (2, 128, 512)
            else:
                assert output[i].shape == (2, 128, 128)

    def test_mobilebert_mobilebertencoder(self):
        """
        Test MobileBertEncoder
        """
        model = MobileBertEncoder(MobileBertConfig())
        hidden_states = Tensor(np.random.randint(0, 1000, (2, 128, 512)), dtype=mindspore.float32)
        head_mask = Tensor(np.random.randint(0, 1000, (128, 128, 128)), dtype=mindspore.float32)
        output = model(hidden_states, head_mask=head_mask)
        assert output[0].shape == (2, 128, 512)
