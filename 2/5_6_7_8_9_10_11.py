import pandas as pd
from sklearn.datasets import fetch_california_housing
from statistics import mean


def get_mean(n):
    return mean(n)


def main():
    # Task #5
    data = fetch_california_housing(as_frame=True)

    print('\nTask #6')
    h = pd.DataFrame(data=data.data, columns=data.feature_names)
    t = pd.DataFrame(data=data.target, columns=data.target_names)
    data = pd.concat([h, t], axis=1)
    print(data)

    print('\nTask #7')
    print(data.info())

    print('\nTask #8')
    print(data.isna().sum())

    print('\nTask #9')
    print(data.loc[(data.HouseAge > 50) & (data.Population > 2500)])

    print('\nTask #10')
    print(max(data.MedHouseVal))
    print(min(data.MedHouseVal))

    print('\nTask #11')
    print(data.apply(get_mean, axis=0))


if __name__ == '__main__':
    main()
