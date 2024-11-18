import numpy as np
import pandas as pd
import unittest
from src.saggital_brain.sagittal_brain import process_brain_data  # Replace with the actual function from Charlene's code

class TestSagittalBrain(unittest.TestCase):

    def setUp(self):
        # Read the CSV file into a DataFrame
        self.df = pd.read_csv('brain_sample.csv', header=None)

        # Convert DataFrame to numpy array
        self.input_array = self.df.to_numpy()

        # Calculate the expected output as the average of each row
        self.expected_output_array = np.mean(self.input_array, axis=1)

    def test_process_brain_data(self):
        # Call the function from Charlene's code
        output_array = process_brain_data(self.input_array)

        # Assert the output matches the expected output
        np.testing.assert_array_almost_equal(output_array, self.expected_output_array)

if __name__ == '__main__':
    unittest.main()
