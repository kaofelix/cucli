# Search for Docs

View the Docs in your Workspace. You can only view information of Docs you can access.

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
    "/api/v3/workspaces/{workspace_id}/docs": {
      "get": {
        "operationId": "searchDocsPublic",
        "summary": "Search for Docs",
        "description": "View the Docs in your Workspace. You can only view information of Docs you can access.",
        "parameters": [
          {
            "name": "workspace_id",
            "in": "path",
            "description": "The ID of the Workspace.",
            "required": true,
            "schema": {
              "type": "number",
              "x-readme-ref-name": "PublicDocsSearchDocsPublicWorkspaceIdPath"
            }
          },
          {
            "name": "id",
            "in": "query",
            "description": "Filter results to a single Doc with the given ID.",
            "required": false,
            "schema": {
              "type": "string"
            }
          },
          {
            "name": "creator",
            "in": "query",
            "description": "Filter results to Docs created by the user with the given ID.",
            "required": false,
            "schema": {
              "type": "number",
              "x-readme-ref-name": "PublicDocsSearchDocsPublicCreatorQuery"
            }
          },
          {
            "name": "deleted",
            "in": "query",
            "description": "Filter results to deleted Docs.",
            "required": false,
            "schema": {
              "type": "boolean",
              "default": false,
              "x-readme-ref-name": "PublicDocsSearchDocsPublicDeletedQuery"
            }
          },
          {
            "name": "archived",
            "in": "query",
            "description": "Filter results to archived Docs.",
            "required": false,
            "schema": {
              "type": "boolean",
              "default": false,
              "x-readme-ref-name": "PublicDocsSearchDocsPublicArchivedQuery"
            }
          },
          {
            "name": "parent_id",
            "in": "query",
            "description": "Filter results to Docs that are children of the parent with the given ID.",
            "required": false,
            "schema": {
              "type": "string"
            }
          },
          {
            "name": "parent_type",
            "in": "query",
            "description": "Filter results to Docs that are children to parents of the given type.",
            "required": false,
            "schema": {
              "type": "string",
              "enum": [
                "4",
                "5",
                "6",
                "7",
                "12",
                "SPACE",
                "FOLDER",
                "LIST",
                "EVERYTHING",
                "WORKSPACE"
              ],
              "x-readme-ref-name": "PublicDocsSearchDocsPublicParentTypeQuery"
            }
          },
          {
            "name": "limit",
            "in": "query",
            "description": "The maximum number of results to fetch for this page.",
            "required": false,
            "schema": {
              "type": "number",
              "default": 50,
              "maximum": 100,
              "minimum": 10,
              "x-readme-ref-name": "PublicDocsSearchDocsPublicLimitQuery"
            }
          },
          {
            "name": "cursor",
            "in": "query",
            "description": "The cursor to use to fetch the next page of results.",
            "required": false,
            "schema": {
              "type": "string"
            }
          },
          {
            "name": "next_cursor",
            "in": "query",
            "description": "The cursor to use to fetch the next page of results. [deprecated]",
            "required": false,
            "schema": {
              "type": "string"
            },
            "deprecated": true
          }
        ],
        "responses": {
          "200": {
            "description": "Search results",
            "content": {
              "application/json": {
                "schema": {
                  "type": "object",
                  "properties": {
                    "docs": {
                      "type": "array",
                      "items": {
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
                          "creator": {
                            "type": "number"
                          },
                          "deleted": {
                            "type": "boolean"
                          },
                          "date_deleted": {
                            "type": "number"
                          },
                          "deleted_by": {
                            "type": "number"
                          },
                          "archived": {
                            "type": "boolean"
                          },
                          "archived_by": {
                            "type": "number"
                          },
                          "date_archived": {
                            "type": "number"
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
                          "creator",
                          "deleted",
                          "archived"
                        ],
                        "x-readme-ref-name": "PublicDocsDocCoreDto"
                      }
                    },
                    "next_cursor": {
                      "type": "string"
                    }
                  },
                  "required": [
                    "docs"
                  ],
                  "x-readme-ref-name": "PublicDocsDocsSearchResultDto"
                }
              }
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