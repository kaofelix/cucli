# Fetch PageListing for a Doc

View the PageListing for a Doc.

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
    "/api/v3/workspaces/{workspace_id}/docs/{doc_id}/page_listing": {
      "get": {
        "operationId": "getDocPageListingPublic",
        "summary": "Fetch PageListing for a Doc",
        "description": "View the PageListing for a Doc.",
        "parameters": [
          {
            "name": "workspace_id",
            "in": "path",
            "description": "The ID of the Workspace.",
            "required": true,
            "schema": {
              "type": "number",
              "x-readme-ref-name": "PublicDocsGetDocPageListingPublicWorkspaceIdPath"
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
            "name": "max_page_depth",
            "in": "query",
            "description": "The maximum depth to fetch pages/subpages. A value less than 0 does not limit the depth.",
            "required": false,
            "schema": {
              "type": "number",
              "default": -1,
              "x-readme-ref-name": "PublicDocsGetDocPageListingPublicMaxPageDepthQuery"
            }
          }
        ],
        "responses": {
          "200": {
            "description": "PageListing found",
            "content": {
              "application/json": {
                "schema": {
                  "$ref": "#/components/schemas/PublicDocsGetDocPageListingPublic200Response"
                }
              }
            }
          },
          "404": {
            "description": "PageListing not found",
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
    "schemas": {
      "PublicDocsGetDocPageListingPublic200Response": {
        "type": "array",
        "items": {
          "$ref": "#/components/schemas/PublicDocsPageV3ReferenceDto"
        },
        "x-readme-ref-name": "PublicDocsGetDocPageListingPublic200Response"
      },
      "PublicDocsPageV3ReferenceDto": {
        "type": "object",
        "properties": {
          "id": {
            "type": "string"
          },
          "doc_id": {
            "type": "string"
          },
          "parent_page_id": {
            "type": "string"
          },
          "workspace_id": {
            "type": "number"
          },
          "name": {
            "type": "string"
          },
          "pages": {
            "type": "array",
            "items": {
              "$ref": "#/components/schemas/PublicDocsPageV3ReferenceDto"
            }
          }
        },
        "example": [
          {
            "id": "8cht190-271",
            "doc_id": "8cht190-831",
            "workspace_id": 9011234080,
            "name": "Fantastic Marketing doc"
          },
          {
            "id": "8cht190-311",
            "doc_id": "8cht190-831",
            "workspace_id": 9011234080,
            "name": "Another doc",
            "pages": [
              {
                "id": "8cht190-331",
                "doc_id": "8cht190-831",
                "parent_page_id": "8cht190-311",
                "workspace_id": 9011234080,
                "name": "sub page",
                "pages": [
                  {
                    "id": "8cht190-351",
                    "doc_id": "8cht190-831",
                    "parent_page_id": "8cht190-331",
                    "workspace_id": 9011234080,
                    "name": "2nd sub page"
                  }
                ]
              }
            ]
          }
        ],
        "required": [
          "id",
          "doc_id",
          "workspace_id",
          "name"
        ],
        "x-readme-ref-name": "PublicDocsPageV3ReferenceDto"
      }
    },
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