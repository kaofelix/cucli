# Get Custom Task Types

View the custom task types available in a Workspace.

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
    "/v2/team/{team_id}/custom_item": {
      "get": {
        "summary": "Get Custom Task Types",
        "tags": [
          "Custom Task Types"
        ],
        "description": "View the custom task types available in a Workspace.",
        "operationId": "GetCustomItems",
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
        "responses": {
          "200": {
            "description": "",
            "headers": {},
            "content": {
              "application/json": {
                "schema": {
                  "title": "GetCustomItemsResponse",
                  "type": "object",
                  "properties": {
                    "custom_items": {
                      "type": "array",
                      "items": {
                        "title": "Custom Item",
                        "type": "object",
                        "properties": {
                          "id": {
                            "type": "integer",
                            "contentEncoding": "int32",
                            "description": "Custom task type ID."
                          },
                          "name": {
                            "type": "string",
                            "description": "Custom task type name."
                          },
                          "name_plural": {
                            "type": "string",
                            "description": "Custom task type plural name."
                          },
                          "description": {
                            "type": "string",
                            "description": "Custom task type description."
                          }
                        },
                        "examples": [
                          {
                            "id": 1300,
                            "name": "Bug",
                            "name_plural": "Bugs",
                            "description": "Custom task type for bugs."
                          }
                        ]
                      },
                      "description": "Array of custom task types."
                    }
                  },
                  "examples": [
                    {
                      "custom_items": [
                        {
                          "id": "1300-900e-462d-a849-4a216b06d930",
                          "name": "Bug",
                          "name_plural": "Bugs",
                          "description": "Custom item type for bugs."
                        }
                      ]
                    }
                  ]
                },
                "example": [
                  {
                    "custom_items": [
                      {
                        "id": 1300,
                        "name": "Bug",
                        "name_plural": "Bugs",
                        "description": "Custom item type for bugs."
                      }
                    ]
                  }
                ]
              }
            }
          }
        },
        "deprecated": false
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
      "name": "Custom Task Types"
    }
  ]
}
```