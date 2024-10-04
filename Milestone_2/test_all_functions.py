# test_all_functions.py

import pytest
import pandas as pd
from core_functions import filter_data, sort_data, level_filter_data

# Sample dataset to use in tests
data = {
    'food': ['Apple', 'Banana', 'Carrot', 'Apple Pie'],
    'Vitamin A': [50, 30, 90, 10],
    'Caloric Value': [100, 150, 200, 300]
}
dataset = pd.DataFrame(data)

def test_filter_data():
    # Test filtering by food name
    filtered = filter_data(dataset, 'Food', 'apple')
    assert len(filtered) == 2

    # Test filtering by vitamin
    filtered = filter_data(dataset, 'Vitamin A', 'banana', min_value=20, max_value=50)
    assert len(filtered) == 1

def test_sort_data():
    # Test ascending sort
    filtered = filter_data(dataset, 'Vitamin A', 'apple')
    sorted_data = sort_data(filtered, 'Vitamin A', 'Ascending')
    print(sorted_data)  # Debugging line
    assert sorted_data.iloc[0]['Vitamin A'] == 10  # Expected minimum

    # Test descending sort
    sorted_data = sort_data(filtered, 'Vitamin A', 'Descending')
    print(sorted_data)  # Debugging line
    assert sorted_data.iloc[0]['Vitamin A'] == 50  # Expected maximum


def test_level_filter_data():
    # Test Low level filter
    filtered = filter_data(dataset, 'Vitamin A', 'apple')
    level_filtered = level_filter_data(filtered, 'Vitamin A', 'Low')
    assert len(level_filtered) == 1

    # Test High level filter
    level_filtered = level_filter_data(filtered, 'Vitamin A', 'High')
    assert len(level_filtered) == 1

# Command to run: pytest --cov=core_functions --cov-report=term
