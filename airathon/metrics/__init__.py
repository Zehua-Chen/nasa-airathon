import tensorflow as tf
from tensorflow.keras.metrics import Metric


class R2(Metric):
    def __init__(self, name='R2', **kwargs):
        super().__init__(name, **kwargs)

        self.r2 = self.add_weight(name="r2", initializer="zeros")

    def update_state(
            self,
            y_true,
            y_pred,
            sample_weight=None):
        numerator = tf.math.reduce_sum(tf.math.square(y_true - y_pred))

        y_true_mean = tf.math.reduce_mean(y_true)
        denominator = tf.math.reduce_sum(tf.math.square(y_true - y_true_mean))

        new_r2 = 1 - (numerator / denominator)

        self.r2.assign(new_r2)

    def result(self):
        return self.r2
