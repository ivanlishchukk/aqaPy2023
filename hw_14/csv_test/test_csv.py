from hw_14.csv_manipulations_code import CSVManipulation


class TestCSV:

    def test_add_row(self):
        csv_file = CSVManipulation()
        len_before = csv_file.csv_len('example.csv')
        csv_file.add_row('example.csv', row_data='Ivan, Lishchuk, age, Male, salary')
        len_after = csv_file.csv_len('example.csv')
        assert len_after - len_before == 1

    def test_delete_row(self):
        csv_file = CSVManipulation()
        len_before = csv_file.csv_len('example.csv')
        csv_file.delete_row('example.csv', row_index=len_before-2)
        len_after = csv_file.csv_len('example.csv')
        assert len_before - len_after == 1