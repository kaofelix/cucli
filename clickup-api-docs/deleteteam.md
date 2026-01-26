# Delete Group

This endpoint is used to remove a [User Group](https://docs.clickup.com/en/articles/4010016-teams-how-to-create-user-groups) from your Workspace.\
 \
In our API documentation, `team_id` refers to the id of a Workspace, and `group_id` refers to the id of a user group.

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
    "/v2/group/{group_id}": {
      "delete": {
        "summary": "Delete Group",
        "tags": [
          "User Groups"
        ],
        "description": "This endpoint is used to remove a [User Group](https://docs.clickup.com/en/articles/4010016-teams-how-to-create-user-groups) from your Workspace.\\\n \\\nIn our API documentation, `team_id` refers to the id of a Workspace, and `group_id` refers to the id of a user group.",
        "operationId": "DeleteTeam",
        "parameters": [
          {
            "name": "group_id",
            "in": "path",
            "description": "User Group ID",
            "required": true,
            "style": "simple",
            "schema": {
              "type": "string",
              "examples": [
                "C9C58BE9"
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
      "name": "User Groups"
    }
  ]
}
```