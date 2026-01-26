# Fetch a Doc

View information about a Doc.

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
    "/api/v3/workspaces/{workspace_id}/docs/{doc_id}": {
      "get": {
        "operationId": "getDocPublic",
        "summary": "Fetch a Doc",
        "description": "View information about a Doc.",
        "parameters": [
          {
            "name": "workspace_id",
            "in": "path",
            "description": "The ID of the Workspace.",
            "required": true,
            "schema": {
              "type": "number",
              "x-readme-ref-name": "PublicDocsGetDocPublicWorkspaceIdPath"
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
          }
        ],
        "responses": {
          "200": {
            "description": "Doc found",
            "content": {
              "application/json": {
                "schema": {
                  "type": "object",
                  "properties": {
                    "id": {
                      "type": "string"
                    },
                    "date_created": {
                      "type": "number"
                    },
                    "date_updated": {
                      "type": "number"
                    },
                    "name": {
                      "type": "string"
                    },
                    "type": {
                      "type": "number",
                      "enum": [
                        1,
                        2
                      ]
                    },
                    "parent": {
                      "type": "object",
                      "properties": {
                        "id": {
                          "type": "string"
                        },
                        "type": {
                          "description": "The parent Doc type. Use `4` for Space, `5` for Folder, `6` for List, `7` for Everything, and `12` for Workspace.",
                          "type": "number"
                        }
                      },
                      "required": [
                        "id",
                        "type"
                      ],
                      "x-readme-ref-name": "PublicDocsParentDto"
                    },
                    "public": {
                      "type": "boolean"
                    },
                    "workspace_id": {
                      "type": "number"
                    },
                    "archived": {
                      "type": "boolean"
                    },
                    "archived_by": {
                      "type": "number"
                    },
                    "creator": {
                      "type": "number"
                    },
                    "date_archived": {
                      "type": "number"
                    },
                    "date_deleted": {
                      "type": "number"
                    },
                    "deleted": {
                      "type": "boolean"
                    },
                    "deleted_by": {
                      "type": "number"
                    },
                    "page_defaults": {
                      "type": "object",
                      "properties": {
                        "font": {
                          "type": "string"
                        },
                        "font_size": {
                          "type": "number"
                        },
                        "line_height": {
                          "type": "number"
                        },
                        "page_width": {
                          "type": "number"
                        },
                        "paragraph_spacing": {
                          "type": "number"
                        },
                        "show_author_header": {
                          "type": "boolean"
                        },
                        "show_contributor_header": {
                          "type": "boolean"
                        },
                        "show_cover_header": {
                          "type": "boolean"
                        },
                        "show_date_header": {
                          "type": "boolean"
                        },
                        "show_page_outline": {
                          "type": "boolean"
                        },
                        "show_sub_pages": {
                          "type": "boolean"
                        },
                        "sub_page_size": {
                          "type": "string"
                        },
                        "show_sub_title_header": {
                          "type": "boolean"
                        },
                        "show_title_icon_header": {
                          "type": "boolean"
                        },
                        "show_relationships": {
                          "type": "boolean"
                        },
                        "show_relationships_compact": {
                          "type": "boolean"
                        },
                        "show_sub_pages_author": {
                          "type": "boolean"
                        },
                        "show_sub_pages_thumbnail": {
                          "type": "boolean"
                        },
                        "show_sub_pages_compact": {
                          "type": "boolean"
                        },
                        "sub_pages_style": {
                          "type": "string"
                        }
                      },
                      "x-readme-ref-name": "PublicDocsPresentationDetailsDto"
                    }
                  },
                  "required": [
                    "id",
                    "date_created",
                    "name",
                    "type",
                    "parent",
                    "public",
                    "workspace_id",
                    "creator"
                  ],
                  "x-readme-ref-name": "PublicDocsDocDto"
                }
              }
            }
          },
          "404": {
            "description": "Doc not found",
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