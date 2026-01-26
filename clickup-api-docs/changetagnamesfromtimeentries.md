# Change tag names from time entries

Rename an time entry label.

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
    "/v2/team/{team_id}/time_entries/tags": {
      "put": {
        "summary": "Change tag names from time entries",
        "tags": [
          "Time Tracking"
        ],
        "description": "Rename an time entry label.",
        "operationId": "Changetagnamesfromtimeentries",
        "parameters": [
          {
            "name": "team_id",
            "in": "path",
            "description": "Workspace ID",
            "required": true,
            "style": "simple",
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
          "description": "",
          "content": {
            "application/json": {
              "schema": {
                "title": "Changetagnamesfromtimeentriesrequest",
                "required": [
                  "name",
                  "new_name",
                  "tag_bg",
                  "tag_fg"
                ],
                "type": "object",
                "properties": {
                  "name": {
                    "type": "string"
                  },
                  "new_name": {
                    "type": "string"
                  },
                  "tag_bg": {
                    "type": "string"
                  },
                  "tag_fg": {
                    "type": "string"
                  }
                },
                "examples": [
                  {
                    "name": "old tag name",
                    "new_name": "new tag name",
                    "tag_bg": "#000000",
                    "tag_fg": "#000000"
                  }
                ]
              },
              "example": {
                "name": "old tag name",
                "new_name": "new tag name",
                "tag_bg": "#000000",
                "tag_fg": "#000000"
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
                  "type": "object",
                  "examples": [
                    {}
                  ],
                  "contentMediaType": "application/json"
                },
                "example": {}
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
      "name": "Time Tracking"
    }
  ]
}
```