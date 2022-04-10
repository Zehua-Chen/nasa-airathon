from unittest import TestCase, main

import numpy as np
from airathon.metrics import R2


class R2Tests(TestCase):
    def test(self) -> None:
        # Test case from https://www.tensorflow.org/addons/api_docs/python/tfa/metrics/RSquare
        y_true = np.array([1, 4, 3], dtype=np.float32)
        y_pred = np.array([2, 4, 4], dtype=np.float32)

        r2 = R2()
        r2.update_state(y_true, y_pred)

        result = r2.result().numpy()

        np.testing.assert_almost_equal(0.57142854, result)


if __name__ == "__main__":
    main()
