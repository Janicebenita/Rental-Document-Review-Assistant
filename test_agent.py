import unittest
from agent import review_documents


class RentalTests(unittest.TestCase):
    def test_missing_document_does_not_create_eligibility_decision(self):
        result = review_documents({"documents": {}})
        self.assertIn("application", result["missing_documents"])
        self.assertIsNone(result["eligibility_decision"])


if __name__ == "__main__":
    unittest.main()
