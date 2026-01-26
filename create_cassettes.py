#!/usr/bin/env python3
"""Create VCR cassettes for time tracking tests."""

import yaml

# Templates for each test
cassettes = {
    "TestTimeTrackingAPI.test_get_running_time_entry.yaml": {
        "version": 1,
        "interactions": [
            {
                "request": {
                    "body": "",
                    "headers": {
                        "Accept": ["*/*"],
                        "Accept-Encoding": ["gzip", "deflate"],
                        "Connection": ["keep-alive"],
                        "Host": ["api.clickup.com"],
                        "User-Agent": ["python-httpx/0.28.1"],
                    },
                    "method": "GET",
                    "uri": "https://api.clickup.com/api/v2/team/90152245421/time_entries/current",
                },
                "response": {
                    "body": {
                        "string": '{"data":{"id":"test_timer_id","task":null,"wid":"90152245421","user":{"id":272627274,"username":"Test User","email":"test@example.com","color":"#595d66","profilePicture":null,"initials":"TU"},"billable":false,"start":"1737925200000","duration":-12345,"description":"Test running entry","tags":[],"at":"1737925200000"}}'
                    },
                    "headers": {
                        "Access-Control-Allow-Origin": ["*"],
                        "Connection": ["keep-alive"],
                        "Content-Length": ["400"],
                        "Content-Type": ["application/json; charset=utf-8"],
                        "Date": ["Sun, 26 Jan 2026 20:42:53 GMT"],
                        "Server": ["nginx"],
                        "access-control-allow-credentials": ["true"],
                        "cache-control": ["no-cache, no-store"],
                        "expires": ["0"],
                        "pragma": ["no-cache"],
                        "x-datadog-trace-id": ["123456789"],
                        "x-ratelimit-limit": ["100"],
                        "x-ratelimit-remaining": ["99"],
                        "x-ratelimit-reset": ["1737928800"],
                    },
                    "status": {"code": 200, "message": "OK"},
                },
            },
        ],
    },
    "TestTimeTrackingAPI.test_start_time_entry.yaml": {
        "version": 1,
        "interactions": [
            {
                "request": {
                    "body": '{"billable": false, "description": "Test time entry"}',
                    "headers": {
                        "Accept": ["*/*"],
                        "Accept-Encoding": ["gzip", "deflate"],
                        "Connection": ["keep-alive"],
                        "Content-Length": ["48"],
                        "Content-Type": ["application/json"],
                        "Host": ["api.clickup.com"],
                        "User-Agent": ["python-httpx/0.28.1"],
                    },
                    "method": "POST",
                    "uri": "https://api.clickup.com/api/v2/team/90152245421/time_entries/start",
                },
                "response": {
                    "body": {
                        "string": '{"data":{"id":"new_timer_id","task":null,"wid":"90152245421","user":{"id":272627274,"username":"Test User","email":"test@example.com","color":"#595d66","profilePicture":null,"initials":"TU"},"billable":false,"start":"1737925200000","duration":-1000,"description":"Test time entry","tags":[],"at":"1737925200000}}'
                    },
                    "headers": {
                        "Access-Control-Allow-Origin": ["*"],
                        "Connection": ["keep-alive"],
                        "Content-Length": ["498"],
                        "Content-Type": ["application/json; charset=utf-8"],
                        "Date": ["Sun, 26 Jan 2026 20:42:53 GMT"],
                        "Server": ["nginx"],
                        "access-control-allow-credentials": ["true"],
                        "cache-control": ["no-cache, no-store"],
                        "expires": ["0"],
                        "pragma": ["no-cache"],
                        "x-datadog-trace-id": ["123456789"],
                        "x-ratelimit-limit": ["100"],
                        "x-ratelimit-remaining": ["99"],
                        "x-ratelimit-reset": ["1737928800"],
                    },
                    "status": {"code": 200, "message": "OK"},
                },
            },
        ],
    },
    "TestTimeTrackingAPI.test_start_time_entry_with_task.yaml": {
        "version": 1,
        "interactions": [
            {
                "request": {
                    "body": '{"billable": false, "tid": "86c7mc19h"}',
                    "headers": {
                        "Accept": ["*/*"],
                        "Accept-Encoding": ["gzip", "deflate"],
                        "Connection": ["keep-alive"],
                        "Content-Length": ["43"],
                        "Content-Type": ["application/json"],
                        "Host": ["api.clickup.com"],
                        "User-Agent": ["python-httpx/0.28.1"],
                    },
                    "method": "POST",
                    "uri": "https://api.clickup.com/api/v2/team/90152245421/time_entries/start",
                },
                "response": {
                    "body": {
                        "string": '{"data":{"id":"timer_with_task_id","task":{"id":"86c7mc19h","name":"Test Task","status":{"status":"to do","color":"#d3d3d3","type":"open","orderindex":0},"custom_type":null},"wid":"90152245421","user":{"id":272627274,"username":"Test User","email":"test@example.com","color":"#595d66","profilePicture":null,"initials":"TU"},"billable":false,"start":"1737925200000","duration":-2000,"description":"","tags":[],"at":"1737925200000}}'
                    },
                    "headers": {
                        "Access-Control-Allow-Origin": ["*"],
                        "Connection": ["keep-alive"],
                        "Content-Length": ["510"],
                        "Content-Type": ["application/json; charset=utf-8"],
                        "Date": ["Sun, 26 Jan 2026 20:42:53 GMT"],
                        "Server": ["nginx"],
                        "access-control-allow-credentials": ["true"],
                        "cache-control": ["no-cache, no-store"],
                        "expires": ["0"],
                        "pragma": ["no-cache"],
                        "x-datadog-trace-id": ["123456789"],
                        "x-ratelimit-limit": ["100"],
                        "x-ratelimit-remaining": ["99"],
                        "x-ratelimit-reset": ["1737928800"],
                    },
                    "status": {"code": 200, "message": "OK"},
                },
            },
        ],
    },
    "TestTimeTrackingAPI.test_stop_time_entry.yaml": {
        "version": 1,
        "interactions": [
            {
                "request": {
                    "body": "",
                    "headers": {
                        "Accept": ["*/*"],
                        "Accept-Encoding": ["gzip", "deflate"],
                        "Connection": ["keep-alive"],
                        "Host": ["api.clickup.com"],
                        "User-Agent": ["python-httpx/0.28.1"],
                    },
                    "method": "POST",
                    "uri": "https://api.clickup.com/api/v2/team/90152245421/time_entries/stop",
                },
                "response": {
                    "body": {
                        "string": '{"data":{"id":"stopped_timer_id","task":null,"wid":"90152245421","user":{"id":272627274,"username":"Test User","email":"test@example.com","color":"#595d66","profilePicture":null,"initials":"TU"},"billable":false,"start":"1737925200000","end":1737928800000,"duration":3600000,"description":"","tags":[],"source":"clickup","at":1737925200000}}'
                    },
                    "headers": {
                        "Access-Control-Allow-Origin": ["*"],
                        "Connection": ["keep-alive"],
                        "Content-Length": ["495"],
                        "Content-Type": ["application/json; charset=utf-8"],
                        "Date": ["Sun, 26 Jan 2026 20:42:53 GMT"],
                        "Server": ["nginx"],
                        "access-control-allow-credentials": ["true"],
                        "cache-control": ["no-cache, no-store"],
                        "expires": ["0"],
                        "pragma": ["no-cache"],
                        "x-datadog-trace-id": ["123456789"],
                        "x-ratelimit-limit": ["100"],
                        "x-ratelimit-remaining": ["99"],
                        "x-ratelimit-reset": ["1737928800"],
                    },
                    "status": {"code": 200, "message": "OK"},
                },
            },
        ],
    },
    "TestTimeTrackingAPI.test_get_time_entries.yaml": {
        "version": 1,
        "interactions": [
            {
                "request": {
                    "body": "",
                    "headers": {
                        "Accept": ["*/*"],
                        "Accept-Encoding": ["gzip", "deflate"],
                        "Connection": ["keep-alive"],
                        "Host": ["api.clickup.com"],
                        "User-Agent": ["python-httpx/0.28.1"],
                    },
                    "method": "GET",
                    "uri": "https://api.clickup.com/api/v2/team/90152245421/time_entries?start_date=1736904000000&end_date=1737766400000",
                },
                "response": {
                    "body": {"string": '{"data":[]}'},
                    "headers": {
                        "Access-Control-Allow-Origin": ["*"],
                        "Connection": ["keep-alive"],
                        "Content-Length": ["11"],
                        "Content-Type": ["application/json; charset=utf-8"],
                        "Date": ["Sun, 26 Jan 2026 20:42:53 GMT"],
                        "Server": ["nginx"],
                        "access-control-allow-credentials": ["true"],
                        "cache-control": ["no-cache, no-store"],
                        "expires": ["0"],
                        "pragma": ["no-cache"],
                        "x-datadog-trace-id": ["123456789"],
                        "x-ratelimit-limit": ["100"],
                        "x-ratelimit-remaining": ["99"],
                        "x-ratelimit-reset": ["1737928800"],
                    },
                    "status": {"code": 200, "message": "OK"},
                },
            },
        ],
    },
    "TestTimeTrackingAPI.test_create_time_entry.yaml": {
        "version": 1,
        "interactions": [
            {
                "request": {
                    "body": '{"start": 1737925200000, "duration": 3600000, "billable": false, "description": "Test manual entry", "tid": ""}',
                    "headers": {
                        "Accept": ["*/*"],
                        "Accept-Encoding": ["gzip", "deflate"],
                        "Connection": ["keep-alive"],
                        "Content-Length": ["92"],
                        "Content-Type": ["application/json"],
                        "Host": ["api.clickup.com"],
                        "User-Agent": ["python-httpx/0.28.1"],
                    },
                    "method": "POST",
                    "uri": "https://api.clickup.com/api/v2/team/90152245421/time_entries",
                },
                "response": {
                    "body": {
                        "string": '{"data":{"id":"created_entry_id","task":null,"wid":"90152245421","user":{"id":272627274,"username":"Test User","email":"test@example.com","color":"#595d66","profilePicture":null,"initials":"TU"},"billable":false,"start":"1737925200000","end":null,"duration":"3600000","description":"Test manual entry","tags":[],"source":"clickup","at":1737925200000}}'
                    },
                    "headers": {
                        "Access-Control-Allow-Origin": ["*"],
                        "Connection": ["keep-alive"],
                        "Content-Length": ["503"],
                        "Content-Type": ["application/json; charset=utf-8"],
                        "Date": ["Sun, 26 Jan 2026 20:42:53 GMT"],
                        "Server": ["nginx"],
                        "access-control-allow-credentials": ["true"],
                        "cache-control": ["no-cache, no-store"],
                        "expires": ["0"],
                        "pragma": ["no-cache"],
                        "x-datadog-trace-id": ["123456789"],
                        "x-ratelimit-limit": ["100"],
                        "x-ratelimit-remaining": ["99"],
                        "x-ratelimit-reset": ["1737928800"],
                    },
                    "status": {"code": 200, "message": "OK"},
                },
            },
        ],
    },
    "TestTimeTrackingAPI.test_create_time_entry_with_task.yaml": {
        "version": 1,
        "interactions": [
            {
                "request": {
                    "body": '{"start": 1737925200000, "duration": 1800000, "billable": false, "tid": "86c7mc19h"}',
                    "headers": {
                        "Accept": ["*/*"],
                        "Accept-Encoding": ["gzip", "deflate"],
                        "Connection": ["keep-alive"],
                        "Content-Length": ["76"],
                        "Content-Type": ["application/json"],
                        "Host": ["api.clickup.com"],
                        "User-Agent": ["python-httpx/0.28.1"],
                    },
                    "method": "POST",
                    "uri": "https://api.clickup.com/api/v2/team/90152245421/time_entries",
                },
                "response": {
                    "body": {
                        "string": '{"data":{"id":"created_entry_with_task_id","task":{"id":"86c7mc19h","name":"Test Task","status":{"status":"to do","color":"#d3d3d3","type":"open","orderindex":0},"custom_type":null},"wid":"90152245421","user":{"id":272627274,"username":"Test User","email":"test@example.com","color":"#595d66","profilePicture":null,"initials":"TU"},"billable":false,"start":"1737925200000","end":null,"duration":"1800000,"description":"","tags":[],"source":"clickup","at":1737925200000}}'
                    },
                    "headers": {
                        "Access-Control-Allow-Origin": ["*"],
                        "Connection": ["keep-alive"],
                        "Content-Length": ["530"],
                        "Content-Type": ["application/json; charset=utf-8"],
                        "Date": ["Sun, 26 Jan 2026 20:42:53 GMT"],
                        "Server": ["nginx"],
                        "access-control-allow-credentials": ["true"],
                        "cache-control": ["no-cache, no-store"],
                        "expires": ["0"],
                        "pragma": ["no-cache"],
                        "x-datadog-trace-id": ["123456789"],
                        "x-ratelimit-limit": ["100"],
                        "x-ratelimit-remaining": ["99"],
                        "x-ratelimit-reset": ["1737928800"],
                    },
                    "status": {"code": 200, "message": "OK"},
                },
            },
        ],
    },
    "TestTimeTrackingAPI.test_update_time_entry.yaml": {
        "version": 1,
        "interactions": [
            {
                "request": {
                    "body": '{"start": 1737925200000, "duration": 3600000, "billable": false, "description": "Original description", "tid": ""}',
                    "headers": {
                        "Accept": ["*/*"],
                        "Accept-Encoding": ["gzip", "deflate"],
                        "Connection": ["keep-alive"],
                        "Content-Length": ["103"],
                        "Content-Type": ["application/json"],
                        "Host": ["api.clickup.com"],
                        "User-Agent": ["python-httpx/0.28.1"],
                    },
                    "method": "POST",
                    "uri": "https://api.clickup.com/api/v2/team/90152245421/time_entries",
                },
                "response": {
                    "body": {
                        "string": '{"data":{"id":"timer_id_to_update","task":null,"wid":"90152245421","user":{"id":272627274,"username":"Test User","email":"test@example.com","color":"#595d66","profilePicture":null,"initials":"TU"},"billable":false,"start":"1737925200000","end":null,"duration":"3600000","description":"Original description","tags":[],"source":"clickup","at":1737925200000}}'
                    },
                    "headers": {
                        "Access-Control-Allow-Origin": ["*"],
                        "Connection": ["keep-alive"],
                        "Content-Length": ["503"],
                        "Content-Type": ["application/json; charset=utf-8"],
                        "Date": ["Sun, 26 Jan 2026 20:42:53 GMT"],
                        "Server": ["nginx"],
                        "access-control-allow-credentials": ["true"],
                        "cache-control": ["no-cache, no-store"],
                        "expires": ["0"],
                        "pragma": ["no-cache"],
                        "x-datadog-trace-id": ["123456789"],
                        "x-ratelimit-limit": ["100"],
                        "x-ratelimit-remaining": ["99"],
                        "x-ratelimit-reset": ["1737928800"],
                    },
                    "status": {"code": 200, "message": "OK"},
                },
            },
            {
                "request": {
                    "body": '{"description": "Updated description", "billable": true, "tags": [], "tid": ""}',
                    "headers": {
                        "Accept": ["*/*"],
                        "Accept-Encoding": ["gzip", "deflate"],
                        "Connection": ["keep-alive"],
                        "Content-Length": ["61"],
                        "Content-Type": ["application/json"],
                        "Host": ["api.clickup.com"],
                        "User-Agent": ["python-httpx/0.28.1"],
                    },
                    "method": "PUT",
                    "uri": "https://api.clickup.com/api/v2/team/90152245421/time_entries/timer_id_to_update",
                },
                "response": {
                    "body": {
                        "string": '{"data":{"id":"timer_id_to_update","task":null,"wid":"90152245421","user":{"id":272627274,"username":"Test User","email":"test@example.com","color":"#595d66","profilePicture":null,"initials":"TU"},"billable":true,"start":"1737925200000","end":null,"duration":"3600000","description":"Updated description","tags":[],"source":"clickup","at":1737925200000}}'
                    },
                    "headers": {
                        "Access-Control-Allow-Origin": ["*"],
                        "Connection": ["keep-alive"],
                        "Content-Length": ["503"],
                        "Content-Type": ["application/json; charset=utf-8"],
                        "Date": ["Sun, 26 Jan 2026 20:42:53 GMT"],
                        "Server": ["nginx"],
                        "access-control-allow-credentials": ["true"],
                        "cache-control": ["no-cache, no-store"],
                        "expires": ["0"],
                        "pragma": ["no-cache"],
                        "x-datadog-trace-id": ["123456789"],
                        "x-ratelimit-limit": ["100"],
                        "x-ratelimit-remaining": ["99"],
                        "x-ratelimit-reset": ["1737928800"],
                    },
                    "status": {"code": 200, "message": "OK"},
                },
            },
        ],
    },
    "TestTimeTrackingAPI.test_delete_time_entry.yaml": {
        "version": 1,
        "interactions": [
            {
                "request": {
                    "body": '{"start": 1737925200000, "duration": 3600000, "billable": false, "description": "Entry to delete", "tid": ""}',
                    "headers": {
                        "Accept": ["*/*"],
                        "Accept-Encoding": ["gzip", "deflate"],
                        "Connection": ["keep-alive"],
                        "Content-Length": ["96"],
                        "Content-Type": ["application/json"],
                        "Host": ["api.clickup.com"],
                        "User-Agent": ["python-httpx/0.28.1"],
                    },
                    "method": "POST",
                    "uri": "https://api.clickup.com/api/v2/team/90152245421/time_entries",
                },
                "response": {
                    "body": {
                        "string": '{"data":{"id":"timer_id_to_delete","task":null,"wid":"90152245421","user":{"id":272627274,"username":"Test User","email":"test@example.com","color":"#595d66","profilePicture":null,"initials":"TU"},"billable":false,"start":"1737925200000","end":null,"duration":"3600000,"description":"Entry to delete","tags":[],"source":"clickup","at":1737925200000}}'
                    },
                    "headers": {
                        "Access-Control-Allow-Origin": ["*"],
                        "Connection": ["keep-alive"],
                        "Content-Length": ["500"],
                        "Content-Type": ["application/json; charset=utf-8"],
                        "Date": ["Sun, 26 Jan 2026 20:42:53 GMT"],
                        "Server": ["nginx"],
                        "access-control-allow-credentials": ["true"],
                        "cache-control": ["no-cache, no-store"],
                        "expires": ["0"],
                        "pragma": ["no-cache"],
                        "x-datadog-trace-id": ["123456789"],
                        "x-ratelimit-limit": ["100"],
                        "x-ratelimit-remaining": ["99"],
                        "x-ratelimit-reset": ["1737928800"],
                    },
                    "status": {"code": 200, "message": "OK"},
                },
            },
            {
                "request": {
                    "body": "",
                    "headers": {
                        "Accept": ["*/*"],
                        "Accept-Encoding": ["gzip", "deflate"],
                        "Connection": ["keep-alive"],
                        "Host": ["api.clickup.com"],
                        "User-Agent": ["python-httpx/0.28.1"],
                    },
                    "method": "DELETE",
                    "uri": "https://api.clickup.com/api/v2/team/90152245421/time_entries/timer_id_to_delete",
                },
                "response": {
                    "body": {
                        "string": '{"data":{"id":"timer_id_to_delete","task":null,"wid":"90152245421","user":{"id":272627274,"username":"Test User","email":"test@example.com","color":"#595d66","profilePicture":null,"initials":"TU"},"billable":false,"start":"1737925200000","end":1737928800000,"duration":3600000,"description":"Entry to delete","tags":[],"source":"clickup","at":1737925200000}}'
                    },
                    "headers": {
                        "Access-Control-Allow-Origin": ["*"],
                        "Connection": ["keep-alive"],
                        "Content-Length": ["500"],
                        "Content-Type": ["application/json; charset=utf-8"],
                        "Date": ["Sun, 26 Jan 2026 20:42:53 GMT"],
                        "Server": ["nginx"],
                        "access-control-allow-credentials": ["true"],
                        "cache-control": ["no-cache, no-store"],
                        "expires": ["0"],
                        "pragma": ["no-cache"],
                        "x-datadog-trace-id": ["123456789"],
                        "x-ratelimit-limit": ["100"],
                        "x-ratelimit-remaining": ["99"],
                        "x-ratelimit-reset": ["1737928800"],
                    },
                    "status": {"code": 200, "message": "OK"},
                },
            },
        ],
    },
}

import os

os.makedirs("tests/cassettes/test_time_tracking_api", exist_ok=True)

for filename, cassette in cassettes.items():
    filepath = os.path.join("tests/cassettes/test_time_tracking_api", filename)
    with open(filepath, "w") as f:
        yaml.dump(cassette, f, default_flow_style=False, sort_keys=False)

print(f"Created {len(cassettes)} cassettes")
