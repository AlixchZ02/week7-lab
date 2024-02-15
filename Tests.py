import unittest
from Employee import EmployeeManagementSystem

class TestEmployeeManagementSystem(unittest.TestCase):
    def setUp(self):
        self.emp_sys = EmployeeManagementSystem()

    def test_add_employee(self):
        self.emp_sys.add_employee("John Doe", 30, 1, "Engineering")
        self.assertEqual(len(self.emp_sys.employees), 1)

    def test_get_employee_by_id(self):
        self.emp_sys.add_employee("John Doe", 30, 1, "Engineering")
        employee = self.emp_sys.get_employee_by_id(1)
        self.assertIsNotNone(employee)
        self.assertEqual(employee.name, "John Doe")

    def test_delete_employee_by_id(self):
        self.emp_sys.add_employee("John Doe", 30, 1, "Engineering")
        self.assertTrue(self.emp_sys.delete_employee_by_id(1))
        self.assertEqual(len(self.emp_sys.employees), 0)
        self.assertFalse(self.emp_sys.delete_employee_by_id(1))

if __name__ == "__main__":
    unittest.main()

