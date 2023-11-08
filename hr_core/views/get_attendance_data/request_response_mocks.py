


RESPONSE_200_JSON = """
{
    "attendance_data": [
        {
            "clock_in_date_time": "string",
            "clock_out_date_time": "string",
            "status": "PRESENT"
        }
    ]
}
"""

RESPONSE_400_JSON = """
{
    "response": "string",
    "http_status_code": 1,
    "res_status": "INVALID_MONTH"
}
"""

RESPONSE_404_JSON = """
{
    "response": "string",
    "http_status_code": 1,
    "res_status": "INVALID_EMPLOYEE_ID"
}
"""

