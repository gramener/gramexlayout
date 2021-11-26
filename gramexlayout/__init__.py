'''
This is the module content
'''

import pandas as pd

__all__ = ['subtotal']


def subtotal(data, columns, agg='sum', calc={}, sort_by=None, ascending=True,
             total_label='', total_position='first'):
    '''
    Aggregates a DataFrame using one or more columns, with subtotals at every level.

    It follows 3 steps at each level:

    1. Aggregate the data
    2. Calculate derived columns
    3. Sort the result

    Examples:

    >>> df = pd.DataFrame({
    ...     "Country": ["US", "US", "UK", "UK"],
    ...     "City": ["Miami", "Mesa", "Leeds", "Derby"],
    ...     "Sales": [10, 20, 30, 40],
    ... })

    >>> df
      Country   City  Sales
    0      US  Miami     10
    1      US  Omaha     20
    2      UK  Leeds     30
    3      UK  Derby     40

    Calculate subtotals by Country and City:

    >>> subtotal(df, columns=['Country', 'City'])
                   Sales
    Country City
                     100        # Global total
    UK                70        #   Subtotal for Country=UK
    US                30        #   Subtotal for Country=US
    UK      Derby     40        #     Subtotal for Country=UK, City=Derby
            Leeds     30        #     Subtotal for Country=UK, City=Leeds
    US      Omaha     20        #     Subtotal for Country=US, City=Omaha
            Miami     10        #     Subtotal for Country=UK, City=Miami

    Calculate subtotals by Country and City, with a custom aggregation function:

    TODO

    Calculate subtotals by Country and City with custom labels:

    >>> subtotal(df, columns=['Country', 'City'], total_label='Total')
                   Sales
    Country City
    Total   Total    100
    UK      Total     70
    US      Total     30
    UK      Derby     40
            Leeds     30
    US      Mesa      20
            Miami     10

    Calculate subtotals by Country and City with custom labels, adding totals at the end:
    TODO: I should be able to add the total at the top or bottom of EACH level

    >>> subtotal(df, columns=['Country', 'City'], total_label='Total', total_position='last')


    Operations: sum, count, mean, any named aggregation.

    Document agg

    Document calcs:
    - 'end': lambda x: x.Size.cumsum() / x.Size.sum()
    - 'start': lambda x: x.end.shift(1).fillna(0)
    - 'growth': lambda x: x.Size / x.Prev - 1

    Document sorting mechanics
    '''
    result = []
    for i in range(len(columns) + 1):
        # 1. Aggregate the data
        blanked = data.assign(**{col: total_label for col in columns[i:]})
        # 2. Calculate derived columns
        total = blanked.groupby(columns, sort=bool(sort_by)).aggregate(agg).assign(**calc)
        # 3. Sort the result
        if sort_by:
            total = total.sort_values(sort_by, ascending=ascending)
        result.append(total)
    return pd.concat(result)


def newfunc():
    '''
    New function
    '''
    return 'Hello'
