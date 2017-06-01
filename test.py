import ca4
import unittest

class TestAssignment4(unittest.TestCase):
    def test_get_hours_with_good_data(self):
        result = ca4.get_hours([{'hour': 2}, {'hour': 4}])
        self.assertEqual([0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], result)
        result = ca4.get_hours([{'hour': 2}, {'hour': 4}, {'hour': 2}, {'hour': 2}, {'hour': 23}])
        self.assertEqual([0, 0, 3, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1], result)
    
    def test_get_weekday_with_good_data(self):
        result = ca4.get_weekday([{'weekday': 'Mon'}])
        self.assertEqual([1, 0, 0, 0, 0, 0, 0], result)
    
    def test_get_hours_returns_error_message_if_args_out_of_range(self):
        self.assertRaises(ValueError, ca4.get_hours, [{'hour': 25}])
    
    def test_get_hours_returns_error_message_if_not_numeric(self):
        self.assertRaises(ValueError, ca4.get_hours, [{'hour': 'two'}])
       
    def test_get_average_lines_with_good_data(self):
        result = ca4.get_avg_lines ([{'number_of_lines': 2}, {'author': 'Mike'}])
        self.assertEqual({'Mike': 2}, result)
  
    def test_number_of_timezones(self):
        commits = ca4.get_commits()
        timezones = ca4.get_timezones(commits)
        self.asserEqual(2,len(timezones))   
if __name__ == '__main__':
    unittest.main()
