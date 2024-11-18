import numpy as np
import pandas as pd
import unittest
import sys
import os
from pathlib import Path

# Add the src directory to the Python path
current_dir = Path(__file__).resolve().parent
src_dir = current_dir.parents[1] / 'src'
sys.path.append(str(src_dir))

from sagittal_brain.sagittal_brain import run_averages  # Replace with the actual function from Charlene's code

class TestSagittalBrain(unittest.TestCase):

    def setUp(self):
        # Create an input dataset
        self.data_input = np.zeros((20, 20))
        self.data_input[-1, :] = 1

        # Save it into a file
        np.savetxt("brain_sample.csv", self.data_input, fmt='%d', delimiter=',')

        # Create an array with expected result
        self.expected = np.zeros(20)
        self.expected[-1] = 1

    def test_run_averages(self):
        # Call the function with the files
        run_averages(file_input="brain_sample.csv", file_output="brain_average.csv")

        # Load the result
        result = np.loadtxt("brain_average.csv", delimiter=',')

        # Compare the result with the expected values
        np.testing.assert_array_equal(result, self.expected)

    def tearDown(self):
        # Clean up the files
        os.remove("brain_sample.csv")
        os.remove("brain_average.csv")