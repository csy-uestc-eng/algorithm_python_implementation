from unittest import TestCase
from serialize_and_deserialize_binary_tree297 import Codec


class TestBinaryTreeSerialize(TestCase):
    def test_level_order(self):
        data = '[1, 2, 3, null, null, 4, 5]'
        codec = Codec()
        self.assertEqual(data, codec.serialize(codec.deserialize(data)))

    def test_level_order01(self):
        data = '[]'
        codec = Codec()
        self.assertEqual(data, codec.serialize(codec.deserialize(data)))
