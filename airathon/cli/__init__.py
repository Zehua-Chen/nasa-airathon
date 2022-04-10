# import airathon.data
import os
import os.path as path
import airathon.paths as paths

from argparse import ArgumentParser, Namespace


def tfrecord(options: Namespace) -> None:
    from airathon.data import tfrecord
    import pandas as pd
    import os.path as path

    x = pd.read_csv(options.label)

    if options.sample > 0:
        x = x.sample(
            n=options.sample,
            axis=0,
            random_state=0)

        out = path.join(
            paths.dataset(),
            options.split,
            "maiac",
            f"maiac-{options.sample}.tfrecord")
    else:
        out = path.join(
            paths.dataset(), options.split, "maiac", "maiac.tfrecord")

    tfrecord.create_tfrecord(x, options.split, out)


def main() -> None:
    parser = ArgumentParser()
    subparsers = parser.add_subparsers()

    tfrecord_parser = subparsers.add_parser("tfrecord")
    tfrecord_parser.add_argument("label")
    tfrecord_parser.add_argument("split")
    tfrecord_parser.add_argument("--sample", "-s", type=int, default=0)
    tfrecord_parser.set_defaults(func=tfrecord)

    args = parser.parse_args()
    args.func(args)
