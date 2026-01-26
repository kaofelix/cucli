# Merge Tasks

Merge multiple tasks into a target task. The target task is specified by the task_id parameter, while the source tasks to be merged are provided in the request body. Custom Task IDs are not supported.

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
    "/v2/task/{task_id}/merge": {
      "post": {
        "summary": "Merge Tasks",
        "description": "Merge multiple tasks into a target task. The target task is specified by the task_id parameter, while the source tasks to be merged are provided in the request body. Custom Task IDs are not supported.",
        "tags": [
          "Tasks"
        ],
        "operationId": "mergeTasks",
        "parameters": [
          {
            "name": "task_id",
            "in": "path",
            "description": "ID of the target task that other tasks will be merged into.",
            "required": true,
            "style": "simple",
            "schema": {
              "type": "string",
              "examples": [
                "9hv"
              ]
            }
          }
        ],
        "requestBody": {
          "required": true,
          "content": {
            "application/json": {
              "schema": {
                "type": "object",
                "required": [
                  "source_task_ids"
                ],
                "properties": {
                  "source_task_ids": {
                    "type": "array",
                    "description": "Array of task IDs to merge into the target task.",
                    "items": {
                      "type": "string"
                    },
                    "examples": [
                      [
                        "abc123",
                        "def456"
                      ]
                    ]
                  }
                }
              }
            }
          }
        },
        "responses": {
          "200": {
            "description": "Tasks merged successfully"
          },
          "400": {
            "description": "Bad request - invalid task IDs or other validation errors"
          },
          "403": {
            "description": "Unauthorized to merge these tasks"
          },
          "404": {
            "description": "One or more tasks not found"
          }
        }
      }
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
      "name": "Tasks"
    }
  ]
}
```