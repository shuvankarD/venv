import report
import json
import pytest

@pytest.fixture(scope="module")

def report_json():
    report.generate_report()
    print("\n [Fixture ]: requested...")

    with open("report.json") as file:
       print("\n [Fixture ]: return report...")
       return json.load(file)
    

def test_report_json(report_json):
    print("\n [Test ]: received-",report_json )

    assert type(report_json) == dict

def test_report_fields(report_json):
      print("\n [Test ]: received-", report_json)
      assert "timestamp" in report_json
      assert "status" in report_json