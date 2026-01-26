# Get Post Subtype IDs

Get the ID of each post subtype (Announcement, Discussion, Idea, and Update) for your Workspace, to use when [sending a message](https://developer.clickup.com/reference/createchatmessage) with `type: post`. \
 \
Subtype IDs are unique to each Workspace.

# OpenAPI definition

```json
{
  "openapi": "3.0.0",
  "info": {
    "title": "ClickUp Public API v3",
    "version": "version",
    "description": "This API is exposed to the public internet and is meant to be accessed by third-party integrations."
  },
  "servers": [
    {
      "url": "https://api.clickup.com/",
      "description": "ClickUp"
    }
  ],
  "paths": {
    "/api/v3/workspaces/{workspace_id}/comments/types/{comment_type}/subtypes": {
      "get": {
        "operationId": "getSubtypes",
        "summary": "Get Post Subtype IDs",
        "description": "Get the ID of each post subtype (Announcement, Discussion, Idea, and Update) for your Workspace, to use when [sending a message](https://developer.clickup.com/reference/createchatmessage) with `type: post`. \\\n \\\nSubtype IDs are unique to each Workspace.",
        "parameters": [
          {
            "name": "workspace_id",
            "in": "path",
            "description": "ID of the logged-in user's Workspace.",
            "required": true,
            "schema": {
              "type": "integer",
              "x-readme-ref-name": "CommentPublicApiCommentsControllerGetSubtypesWorkspaceIdPath"
            }
          },
          {
            "name": "comment_type",
            "in": "path",
            "required": true,
            "schema": {
              "type": "string",
              "enum": [
                "post",
                "ai",
                "syncup",
                "ai_via_brain"
              ],
              "x-readme-ref-name": "CommentPublicApiCommentsControllerGetSubtypesCommentTypePath"
            }
          }
        ],
        "responses": {
          "200": {
            "description": "",
            "content": {
              "application/json": {}
            }
          }
        },
        "tags": [
          "Comments",
          "Chat (Experimental)"
        ],
        "x-is-workspace-endpoint": true
      }
    }
  },
  "components": {
    "securitySchemes": {
      "authHeader": {
        "in": "header",
        "type": "apiKey",
        "name": "Authorization"
      }
    }
  },
  "tags": [
    {
      "description": "Comments API",
      "name": "Comments"
    }
  ],
  "security": [
    {
      "authHeader": []
    }
  ]
}
```