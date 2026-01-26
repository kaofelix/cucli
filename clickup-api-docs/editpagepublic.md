# Edit a Page

Edit a page in a Doc.

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
    "/api/v3/workspaces/{workspace_id}/docs/{doc_id}/pages/{page_id}": {
      "put": {
        "operationId": "editPagePublic",
        "summary": "Edit a Page",
        "description": "Edit a page in a Doc.",
        "parameters": [
          {
            "name": "workspace_id",
            "in": "path",
            "description": "The ID of the Workspace.",
            "required": true,
            "schema": {
              "type": "number",
              "x-readme-ref-name": "PublicDocsEditPagePublicWorkspaceIdPath"
            }
          },
          {
            "name": "doc_id",
            "in": "path",
            "description": "The ID of the doc.",
            "required": true,
            "schema": {
              "type": "string"
            }
          },
          {
            "name": "page_id",
            "in": "path",
            "description": "The ID of the page",
            "required": true,
            "schema": {
              "type": "string"
            }
          }
        ],
        "requestBody": {
          "required": true,
          "content": {
            "application/json": {
              "schema": {
                "type": "object",
                "properties": {
                  "name": {
                    "description": "The updated name of the page.",
                    "type": "string",
                    "default": ""
                  },
                  "sub_title": {
                    "description": "The updateds ubtitle of the page.",
                    "type": "string"
                  },
                  "content": {
                    "default": "",
                    "description": "The updated content of the page.",
                    "type": "string"
                  },
                  "content_edit_mode": {
                    "description": "The strategy for updating content on the page. For example, `replace`, `append`, or `prepend`.",
                    "type": "string",
                    "default": "replace",
                    "enum": [
                      "replace",
                      "append",
                      "prepend"
                    ]
                  },
                  "content_format": {
                    "description": "The format the page content is in. For example, `text/md` for markdown or `text/plain` for plain text.",
                    "type": "string",
                    "default": "text/md",
                    "enum": [
                      "text/md",
                      "text/plain"
                    ]
                  }
                },
                "x-readme-ref-name": "PublicDocsPublicEditPageOptionsDto"
              }
            }
          }
        },
        "responses": {
          "200": {
            "description": "Page updated",
            "content": {
              "application/json": {}
            }
          }
        },
        "tags": [
          "Docs"
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
      "description": "Docs API",
      "name": "Docs"
    }
  ],
  "security": [
    {
      "authHeader": []
    }
  ]
}
```