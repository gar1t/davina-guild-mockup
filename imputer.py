import argparse

DEFAULT_PERCENT_MISSING = 0.33


def main():
    args = _init_args()
    simple_imputation(args)


def _init_args():
    p = argparse.ArgumentParser()
    p.add_argument("--percent-missing", type=float, default=DEFAULT_PERCENT_MISSING)
    p.add_argument("--missingness-mechanism", choices=["MCAR", "MAR", "MNAR"])
    return p.parse_args()


def simple_imputation(args):
    print(args)


if __name__ == "__main__":
    main()
