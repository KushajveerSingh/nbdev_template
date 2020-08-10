from torch.testing._internal.common_utils import TestCase, run_tests


class Test(TestCase):
    def test_second(self):
        self.assertNotEqual(2, 2)


if __name__ == "__main__":
    run_tests()
