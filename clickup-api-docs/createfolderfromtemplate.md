# Create Folder from template

Create a new Folder using a Folder template within a Space. This endpoint allows you to create a folder with all its nested assets (lists, tasks, etc.) from a predefined template available in your Workspace. Publicly shared templates must be [added to your Workspace](https://help.clickup.com/hc/en-us/articles/6326023965591-Add-a-template-to-your-library) before you can use them with the public API.
This request can be run asynchronously or synchronously via the `return_immediately` parameter.


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
    "/v2/space/{space_id}/folder_template/{template_id}": {
      "post": {
        "summary": "Create Folder from template",
        "description": "Create a new Folder using a Folder template within a Space. This endpoint allows you to create a folder with all its nested assets (lists, tasks, etc.) from a predefined template available in your Workspace. Publicly shared templates must be [added to your Workspace](https://help.clickup.com/hc/en-us/articles/6326023965591-Add-a-template-to-your-library) before you can use them with the public API.\nThis request can be run asynchronously or synchronously via the `return_immediately` parameter.\n",
        "operationId": "CreateFolderFromTemplate",
        "tags": [
          "Folders"
        ],
        "parameters": [
          {
            "in": "path",
            "name": "space_id",
            "required": true,
            "schema": {
              "type": "string"
            },
            "description": "ID of the Space where the Folder will be created"
          },
          {
            "in": "path",
            "name": "template_id",
            "required": true,
            "schema": {
              "type": "string"
            },
            "description": "ID of the Folder template to use."
          }
        ],
        "requestBody": {
          "required": true,
          "content": {
            "application/json": {
              "schema": {
                "type": "object",
                "required": [
                  "name"
                ],
                "properties": {
                  "name": {
                    "type": "string",
                    "description": "Name of the new Folder"
                  },
                  "options": {
                    "type": "object",
                    "description": "Options for creating the Folder",
                    "properties": {
                      "return_immediately": {
                        "type": "boolean",
                        "description": "Flag if newly created Object ID should be returned without waiting for the asset itself and all its nested assets to be applied. If set to true, access checks are performed before returning, but the object might not be fully created yet. In case of a timeout on syncronous requests, the of objects from the template will continue to be created past the timeout.\n",
                        "default": true
                      },
                      "content": {
                        "type": "string",
                        "description": "List description"
                      },
                      "time_estimate": {
                        "type": "boolean",
                        "description": "Include time (hours, minutes and seconds)"
                      },
                      "automation": {
                        "type": "boolean",
                        "description": "Import automation options"
                      },
                      "include_views": {
                        "type": "boolean",
                        "description": "Import views"
                      },
                      "old_due_date": {
                        "type": "boolean",
                        "description": "Import tasks due dates"
                      },
                      "old_start_date": {
                        "type": "boolean",
                        "description": "Import tasks start dates"
                      },
                      "old_followers": {
                        "type": "boolean",
                        "description": "Import tasks watchers"
                      },
                      "comment_attachments": {
                        "type": "boolean",
                        "description": "Import tasks comment attachments"
                      },
                      "recur_settings": {
                        "type": "boolean",
                        "description": "Import tasks recurring settings"
                      },
                      "old_tags": {
                        "type": "boolean",
                        "description": "Import tasks tags"
                      },
                      "old_statuses": {
                        "type": "boolean",
                        "description": "Import tasks status settings"
                      },
                      "subtasks": {
                        "type": "boolean",
                        "description": "Import tasks subtasks"
                      },
                      "custom_type": {
                        "type": "boolean",
                        "description": "Import tasks types"
                      },
                      "old_assignees": {
                        "type": "boolean",
                        "description": "Import tasks assignees"
                      },
                      "attachments": {
                        "type": "boolean",
                        "description": "Import tasks attachments"
                      },
                      "comment": {
                        "type": "boolean",
                        "description": "Import tasks comments"
                      },
                      "old_status": {
                        "type": "boolean",
                        "description": "Import tasks current statuses"
                      },
                      "external_dependencies": {
                        "type": "boolean",
                        "description": "Import tasks external dependencies"
                      },
                      "internal_dependencies": {
                        "type": "boolean",
                        "description": "Import tasks internal dependencies"
                      },
                      "priority": {
                        "type": "boolean",
                        "description": "Import tasks priority"
                      },
                      "custom_fields": {
                        "type": "boolean",
                        "description": "Import tasks Custom Fields"
                      },
                      "old_checklists": {
                        "type": "boolean",
                        "description": "Import tasks checklists"
                      },
                      "relationships": {
                        "type": "boolean",
                        "description": "Import tasks relationships"
                      },
                      "old_subtask_assignees": {
                        "type": "boolean",
                        "description": "Import tasks subtasks and assignees combination"
                      },
                      "start_date": {
                        "type": "string",
                        "format": "date-time",
                        "description": "Project start date for remapping dates"
                      },
                      "due_date": {
                        "type": "string",
                        "format": "date-time",
                        "description": "Project due date for remapping dates"
                      },
                      "remap_start_date": {
                        "type": "boolean",
                        "description": "Remap start dates"
                      },
                      "skip_weekends": {
                        "type": "boolean",
                        "description": "Skip weekends when remapping dates"
                      },
                      "archived": {
                        "type": "integer",
                        "enum": [
                          1,
                          2,
                          null
                        ],
                        "description": "Include archived tasks (1 or 2 or null)"
                      }
                    }
                  }
                }
              }
            }
          }
        },
        "responses": {
          "200": {
            "description": "Folder created successfully",
            "content": {
              "application/json": {
                "schema": {
                  "type": "object",
                  "properties": {
                    "id": {
                      "type": "integer",
                      "description": "ID of the created Folder"
                    },
                    "folder": {
                      "type": "object",
                      "properties": {
                        "id": {
                          "type": "string",
                          "description": "Unique identifier of the Folder"
                        },
                        "name": {
                          "type": "string",
                          "description": "Name of the Folder"
                        },
                        "orderindex": {
                          "type": "integer",
                          "description": "Order index of the Folder"
                        },
                        "override_statuses": {
                          "type": "boolean",
                          "description": "Whether the Folder overrides default statuses"
                        },
                        "hidden": {
                          "type": "boolean",
                          "description": "Whether the Folder is hidden"
                        },
                        "space": {
                          "type": "object",
                          "properties": {
                            "id": {
                              "type": "string",
                              "description": "ID of the Space containing the Folder"
                            },
                            "name": {
                              "type": "string",
                              "description": "Name of the Space"
                            },
                            "access": {
                              "type": "boolean",
                              "description": "Whether the user has access to the Space"
                            }
                          }
                        },
                        "task_count": {
                          "type": "string",
                          "description": "Number of tasks in the Folder"
                        },
                        "archived": {
                          "type": "boolean",
                          "description": "Whether the Folder is archived"
                        },
                        "statuses": {
                          "type": "array",
                          "description": "List of statuses available in the Folder",
                          "items": {
                            "type": "object",
                            "properties": {
                              "id": {
                                "type": "string",
                                "description": "Unique identifier of the status"
                              },
                              "status": {
                                "type": "string",
                                "description": "Name of the status"
                              },
                              "orderindex": {
                                "type": "integer",
                                "description": "Order index of the status"
                              },
                              "color": {
                                "type": "string",
                                "description": "Color code for the status"
                              },
                              "type": {
                                "type": "string",
                                "description": "Type of the status (closed, custom, open)"
                              }
                            }
                          }
                        },
                        "lists": {
                          "type": "array",
                          "description": "Lists contained in the Folder",
                          "items": {
                            "type": "object"
                          }
                        },
                        "permission_level": {
                          "type": "string",
                          "description": "Permission level for the current user"
                        }
                      }
                    }
                  },
                  "example": {
                    "id": 90114316773,
                    "folder": {
                      "id": "90114316773",
                      "name": "Projects",
                      "orderindex": 0,
                      "override_statuses": true,
                      "hidden": false,
                      "space": {
                        "id": "90112667046",
                        "name": "Client Facing",
                        "access": true
                      },
                      "task_count": "0",
                      "archived": false,
                      "statuses": [
                        {
                          "id": "c90114316773_syqLtYOY",
                          "status": "complete",
                          "orderindex": 2,
                          "color": "#008844",
                          "type": "closed"
                        },
                        {
                          "id": "c90114316773_g9uxhsQM",
                          "status": "in progress",
                          "orderindex": 1,
                          "color": "#1090e0",
                          "type": "custom"
                        },
                        {
                          "id": "c90114316773_DCnaeiSB",
                          "status": "to do",
                          "orderindex": 0,
                          "color": "#87909e",
                          "type": "open"
                        }
                      ],
                      "lists": [],
                      "permission_level": "create"
                    }
                  }
                }
              }
            }
          },
          "400": {
            "description": "Bad request - Name is required",
            "content": {
              "application/json": {
                "schema": {
                  "type": "object",
                  "properties": {
                    "error": {
                      "type": "string",
                      "example": "Name is required"
                    },
                    "ECODE": {
                      "type": "string",
                      "example": "OAUTH_119"
                    }
                  }
                }
              }
            }
          },
          "401": {
            "description": "Unauthorized"
          },
          "403": {
            "description": "Forbidden"
          },
          "404": {
            "description": "Template or space not found"
          },
          "500": {
            "description": "Internal server error"
          }
        }
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
      "name": "Folders"
    }
  ]
}
```