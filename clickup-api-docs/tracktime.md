# Track time

***Note:** This is a legacy time tracking endpoint. We recommend using the Time Tracking API endpoints to manage time entries.*

# OpenAPI definition

```json
{
  "openapi": "3.1.0",
  "info": {
    "title": "ClickUp API v2 Reference",
    "description": "The ClickUp API enables you to programmatically access and manage your ClickUp resources.\n\n## Authentication\nThe API supports two authentication methods:\n- **Personal API Token**: Use for testing and personal integrations. Add token to requests with header: `Authorization: pk_...`\n- **OAuth 2.0**: Required for building apps for other users. Uses authorization code flow.\n\n## Getting Started\nOur [Getting Started Guide](https://developer.clickup.com/docs/index) provides a comprehensive overview of how to use the ClickUp API.\n",
    "contact": {},
    "version": "2.0"
  },
  "jsonSchemaDialect": "https://json-schema.org/draft/2020-12/schema",
  "servers": [
    {
      "url": "https://api.clickup.com/api",
      "description": "ClickUp",
      "variables": {}
    }
  ],
  "paths": {
    "/v2/task/{task_id}/time": {
      "post": {
        "summary": "Track time",
        "tags": [
          "Time Tracking (Legacy)"
        ],
        "description": "***Note:** This is a legacy time tracking endpoint. We recommend using the Time Tracking API endpoints to manage time entries.*",
        "operationId": "Tracktime",
        "parameters": [
          {
            "name": "task_id",
            "in": "path",
            "description": "",
            "required": true,
            "style": "simple",
            "schema": {
              "type": "string",
              "examples": [
                "9hv"
              ]
            }
          },
          {
            "name": "custom_task_ids",
            "in": "query",
            "description": "If you want to reference a task by it's custom task id, this value must be `true`.",
            "style": "form",
            "explode": true,
            "schema": {
              "type": "boolean",
              "examples": [
                true
              ]
            }
          },
          {
            "name": "team_id",
            "in": "query",
            "description": "When the `custom_task_ids` parameter is set to `true`, the Workspace ID must be provided using the `team_id` parameter.\n \\\nFor example: `custom_task_ids=true&team_id=123`.",
            "style": "form",
            "explode": true,
            "schema": {
              "type": "number",
              "contentEncoding": "double",
              "examples": [
                123
              ]
            }
          }
        ],
        "requestBody": {
          "description": "Include the total time or the start time and end time.\\\n \\\nThe total time is in milliseconds and `\"start\"` and `\"end\"` values are Unix time in milliseconds.",
          "content": {
            "application/json": {
              "schema": {
                "title": "Tracktimerequest",
                "required": [
                  "start",
                  "end",
                  "time"
                ],
                "type": "object",
                "properties": {
                  "start": {
                    "type": "integer",
                    "contentEncoding": "int64"
                  },
                  "end": {
                    "type": "integer",
                    "contentEncoding": "int64"
                  },
                  "time": {
                    "type": "integer",
                    "contentEncoding": "int32"
                  }
                },
                "examples": [
                  {
                    "start": 1567780450202,
                    "end": 1508369194377,
                    "time": 8640000
                  }
                ]
              },
              "example": {
                "start": 1567780450202,
                "end": 1508369194377,
                "time": 8640000
              }
            }
          },
          "required": true
        },
        "responses": {
          "200": {
            "description": "",
            "headers": {},
            "content": {
              "application/json": {
                "schema": {
                  "title": "Tracktimeresponse",
                  "required": [
                    "id"
                  ],
                  "type": "object",
                  "properties": {
                    "id": {
                      "type": "string"
                    }
                  },
                  "examples": [
                    {
                      "id": "123"
                    }
                  ]
                },
                "example": {
                  "id": "123"
                }
              }
            }
          }
        },
        "deprecated": false
      },
      "parameters": []
    }
  },
  "components": {
    "securitySchemes": {
      "Authorization_Token": {
        "name": "Authorization",
        "type": "apiKey",
        "in": "header",
        "description": "API token required for authentication. Two types of tokens are supported:\n**Personal API Key** Obtain from ClickUp's settings page under 'Apps' and add it to the header as `Authorization: pk_...`\n**OAuth2 Access Token** Generated through the OAuth2 flow and add it to the header as `Authorization: Bearer {access_token}`"
      }
    }
  },
  "security": [
    {
      "Authorization_Token": []
    }
  ],
  "tags": [
    {
      "name": "Time Tracking (Legacy)"
    }
  ]
}
```