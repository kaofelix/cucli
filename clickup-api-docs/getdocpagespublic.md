# Fetch Pages belonging to a Doc

View the pages belonging to a Doc.

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
    "/api/v3/workspaces/{workspace_id}/docs/{doc_id}/pages": {
      "get": {
        "operationId": "getDocPagesPublic",
        "summary": "Fetch Pages belonging to a Doc",
        "description": "View the pages belonging to a Doc.",
        "parameters": [
          {
            "name": "workspace_id",
            "in": "path",
            "description": "The ID of the Workspace.",
            "required": true,
            "schema": {
              "type": "number",
              "x-readme-ref-name": "PublicDocsGetDocPagesPublicWorkspaceIdPath"
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
              "x-readme-ref-name": "PublicDocsGetDocPagesPublicMaxPageDepthQuery"
            }
          },
          {
            "name": "content_format",
            "in": "query",
            "description": "The format to return the page content in.",
            "required": false,
            "schema": {
              "type": "string",
              "default": "text/md",
              "enum": [
                "text/md",
                "text/plain"
              ],
              "x-readme-ref-name": "PublicDocsGetDocPagesPublicContentFormatQuery"
            }
          }
        ],
        "responses": {
          "200": {
            "description": "Pages found",
            "content": {
              "application/json": {
                "schema": {
                  "$ref": "#/components/schemas/PublicDocsGetDocPagesPublic200Response"
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
    "schemas": {
      "PublicDocsGetDocPagesPublic200Response": {
        "type": "array",
        "items": {
          "$ref": "#/components/schemas/PublicDocsPageV3Dto"
        },
        "x-readme-ref-name": "PublicDocsGetDocPagesPublic200Response"
      },
      "PublicDocsPageV3Dto": {
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
              "$ref": "#/components/schemas/PublicDocsPageV3Dto"
            }
          },
          "sub_title": {
            "type": "string"
          },
          "date_created": {
            "type": "number"
          },
          "date_updated": {
            "type": "number"
          },
          "content": {
            "type": "string"
          },
          "avatar": {
            "type": "object",
            "properties": {
              "color": {
                "type": "string"
              },
              "value": {
                "type": "string"
              },
              "source": {
                "type": "string"
              }
            },
            "x-readme-ref-name": "PublicDocsAvatarDto"
          },
          "creator_id": {
            "type": "number"
          },
          "deleted": {
            "type": "boolean"
          },
          "deleted_by": {
            "type": "number"
          },
          "date_deleted": {
            "type": "number"
          },
          "date_edited": {
            "type": "number"
          },
          "edited_by": {
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
          },
          "authors": {
            "type": "array",
            "items": {
              "type": "number"
            }
          },
          "contributors": {
            "type": "array",
            "items": {
              "type": "number"
            }
          },
          "cover": {
            "type": "object",
            "properties": {
              "color": {
                "type": "string"
              },
              "image_url": {
                "type": "string"
              },
              "position": {
                "type": "object",
                "properties": {
                  "x": {
                    "type": "number"
                  },
                  "y": {
                    "type": "number"
                  }
                },
                "required": [
                  "x",
                  "y"
                ],
                "x-readme-ref-name": "PublicDocsPositionDto"
              }
            },
            "x-readme-ref-name": "PublicDocsPageCoverDto"
          },
          "protected": {
            "type": "boolean"
          },
          "protected_by": {
            "type": "number"
          },
          "protected_note": {
            "type": "string"
          },
          "presentation_details": {
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
          "doc_id",
          "workspace_id",
          "name",
          "date_created",
          "content",
          "creator_id",
          "authors"
        ],
        "x-readme-ref-name": "PublicDocsPageV3Dto"
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