from __future__ import print_function

import sys

import argparse

DEFAULT_PERCENT_MISSING = 0.33


def main():
    args = _init_args()
    if args.method == "simple":
        simple_imputation(args)
    elif args.method == "knn":
        knn_imputation(args)
    else:
        assert False, args.method


def _init_args():
    p = argparse.ArgumentParser()
    p.add_argument("method", choices=["simple", "knn"])
    p.add_argument("--percent-missing", type=float, default=DEFAULT_PERCENT_MISSING)
    p.add_argument("--missingness-mechanism", choices=["MCAR", "MAR", "MNAR"])
    p.add_argument("--knn-only-flag")
    return p.parse_args()


def simple_imputation(args):
    if args.knn_only_flag:
        raise SystemExit("knn-only-flag-specified for simple method, quitting")
    print("SIMPLE:", args)


def knn_imputation(args):
    print("KNN:", args)


if __name__ == "__main__":
    main()
