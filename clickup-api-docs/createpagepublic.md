# Create a Page

Create a page in a Doc.

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
      "post": {
        "operationId": "createPagePublic",
        "summary": "Create a Page",
        "description": "Create a page in a Doc.",
        "parameters": [
          {
            "name": "workspace_id",
            "in": "path",
            "description": "The ID of the Workspace.",
            "required": true,
            "schema": {
              "type": "number",
              "x-readme-ref-name": "PublicDocsCreatePagePublicWorkspaceIdPath"
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
        "requestBody": {
          "required": true,
          "content": {
            "application/json": {
              "schema": {
                "type": "object",
                "properties": {
                  "parent_page_id": {
                    "description": "The ID of the parent page. If this is a root page in the Doc, `parent_page_id` will not be returned.",
                    "type": "string"
                  },
                  "name": {
                    "description": "The name of the new page.",
                    "type": "string",
                    "default": ""
                  },
                  "sub_title": {
                    "description": "The subtitle of the new page.",
                    "type": "string"
                  },
                  "content": {
                    "default": "",
                    "description": "The content of the new page.",
                    "type": "string"
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
                "x-readme-ref-name": "PublicDocsPublicCreatePageOptionsDto"
              }
            }
          }
        },
        "responses": {
          "201": {
            "description": "Page created",
            "content": {
              "application/json": {
                "schema": {
                  "$ref": "#/components/schemas/PublicDocsPageV3Dto"
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