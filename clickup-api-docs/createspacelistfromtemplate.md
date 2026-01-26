# Create List From Template in Space.

Create a new List using a List template within a Space. Publicly shared templates must be [added to your Workspace](https://help.clickup.com/hc/en-us/articles/6326023965591-Add-a-template-to-your-library) before you can use them with the public API.
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
    "/v2/space/{space_id}/list_template/{template_id}": {
      "post": {
        "summary": "Create List From Template in Space.",
        "tags": [
          "Lists"
        ],
        "description": "Create a new List using a List template within a Space. Publicly shared templates must be [added to your Workspace](https://help.clickup.com/hc/en-us/articles/6326023965591-Add-a-template-to-your-library) before you can use them with the public API.\nThis request can be run asynchronously or synchronously via the `return_immediately` parameter.\n",
        "operationId": "CreateSpaceListFromTemplate",
        "parameters": [
          {
            "in": "path",
            "name": "space_id",
            "required": true,
            "schema": {
              "type": "string"
            },
            "description": "ID of the Space where the List will be created"
          },
          {
            "in": "path",
            "name": "template_id",
            "required": true,
            "schema": {
              "type": "string"
            },
            "description": "ID of the template to use"
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
                    "description": "Name of the new List"
                  },
                  "options": {
                    "type": "object",
                    "description": "Options for creating the List",
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
                        "type": "number",
                        "description": "Include time (hours, minutes and seconds)"
                      },
                      "automation": {
                        "type": "boolean",
                        "description": "Import automation settings"
                      },
                      "include_views": {
                        "type": "boolean",
                        "description": "Import views"
                      },
                      "old_due_date": {
                        "type": "boolean",
                        "description": "Import tasks' due dates"
                      },
                      "old_start_date": {
                        "type": "boolean",
                        "description": "Import tasks' start dates"
                      },
                      "old_followers": {
                        "type": "boolean",
                        "description": "Import tasks' watchers"
                      },
                      "comment_attachments": {
                        "type": "boolean",
                        "description": "Import tasks' comment attachments"
                      },
                      "recur_settings": {
                        "type": "boolean",
                        "description": "Import tasks' recurring settings"
                      },
                      "old_tags": {
                        "type": "boolean",
                        "description": "Import tasks' tags"
                      },
                      "old_statuses": {
                        "type": "boolean",
                        "description": "Import tasks' status settings"
                      },
                      "subtasks": {
                        "type": "boolean",
                        "description": "Import tasks' subtasks"
                      },
                      "custom_type": {
                        "type": "boolean",
                        "description": "Import tasks' task types"
                      },
                      "old_assignees": {
                        "type": "boolean",
                        "description": "Import tasks' assignees"
                      },
                      "attachments": {
                        "type": "boolean",
                        "description": "Import tasks' attachments"
                      },
                      "comment": {
                        "type": "boolean",
                        "description": "Import tasks' comments"
                      },
                      "old_status": {
                        "type": "boolean",
                        "description": "Import tasks' current statuses"
                      },
                      "external_dependencies": {
                        "type": "boolean",
                        "description": "Import tasks' external dependencies"
                      },
                      "internal_dependencies": {
                        "type": "boolean",
                        "description": "Import tasks' internal dependencies"
                      },
                      "priority": {
                        "type": "boolean",
                        "description": "Import tasks' priorities"
                      },
                      "custom_fields": {
                        "type": "boolean",
                        "description": "Import tasks' Custom Fields"
                      },
                      "old_checklists": {
                        "type": "boolean",
                        "description": "Import tasks' checklists"
                      },
                      "relationships": {
                        "type": "boolean",
                        "description": "Import tasks' relationships"
                      },
                      "old_subtask_assignees": {
                        "type": "boolean",
                        "description": "Import tasks' subtask assignees"
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
                        "description": "Include archived tasks"
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
            "description": "List created successfully",
            "content": {
              "application/json": {
                "schema": {
                  "type": "object",
                  "description": "Response object returned when a new List is created from a template in a Folder or Space.",
                  "properties": {
                    "id": {
                      "type": "string",
                      "description": "Unique identifier of the newly created List",
                      "example": "901107394085"
                    },
                    "list": {
                      "type": "object",
                      "description": "Detailed information about the created List",
                      "properties": {
                        "id": {
                          "type": "string",
                          "description": "Unique identifier of the List (matches parent id)",
                          "example": "901107394085"
                        },
                        "name": {
                          "type": "string",
                          "description": "Display name of the List",
                          "example": "API Folder in Space"
                        },
                        "deleted": {
                          "type": "boolean",
                          "description": "Indicates if the List has been marked as deleted",
                          "example": true
                        },
                        "orderindex": {
                          "type": "integer",
                          "description": "Position of the List relative to other Lists in the same container",
                          "example": 0
                        },
                        "priority": {
                          "type": "string",
                          "description": "Priority level of the List, if applicable",
                          "nullable": true,
                          "example": null
                        },
                        "assignee": {
                          "type": "string",
                          "description": "Default assignee for the List, if applicable",
                          "nullable": true,
                          "example": null
                        },
                        "due_date": {
                          "type": "string",
                          "format": "date-time",
                          "description": "Default due date for tasks in the List",
                          "nullable": true,
                          "example": null
                        },
                        "start_date": {
                          "type": "string",
                          "format": "date-time",
                          "description": "Default start date for tasks in the List",
                          "nullable": true,
                          "example": null
                        },
                        "folder": {
                          "type": "object",
                          "description": "Information about the parent Folder containing this List, if applicable",
                          "properties": {
                            "id": {
                              "type": "string",
                              "description": "Unique identifier of the parent Folder",
                              "example": "90114317916"
                            },
                            "name": {
                              "type": "string",
                              "description": "Display name of the parent Folder",
                              "example": "hidden"
                            },
                            "hidden": {
                              "type": "boolean",
                              "description": "Indicates if the Folder is hidden from standard views",
                              "example": true
                            },
                            "access": {
                              "type": "boolean",
                              "description": "Indicates if the current user has access to this Folder",
                              "example": true
                            }
                          }
                        },
                        "space": {
                          "type": "object",
                          "description": "Information about the Workspace Space containing this List",
                          "properties": {
                            "id": {
                              "type": "string",
                              "description": "Unique identifier of the Space",
                              "example": "90112667046"
                            },
                            "name": {
                              "type": "string",
                              "description": "Display name of the Space",
                              "example": "API Test Space"
                            },
                            "access": {
                              "type": "boolean",
                              "description": "Indicates if the current user has access to this Space",
                              "example": true
                            }
                          }
                        },
                        "inbound_address": {
                          "type": "string",
                          "description": "Email address that can be used to create tasks in this List via email",
                          "example": "abc-list@tasks.clickup.com"
                        },
                        "archived": {
                          "type": "boolean",
                          "description": "Indicates if the List is archived",
                          "example": false
                        },
                        "override_statuses": {
                          "type": "boolean",
                          "description": "Indicates if this List uses custom statuses instead of Space default statuses",
                          "example": true
                        },
                        "statuses": {
                          "type": "array",
                          "description": "List of available statuses for tasks in this List",
                          "items": {
                            "type": "object",
                            "description": "Status configuration object",
                            "properties": {
                              "id": {
                                "type": "string",
                                "description": "Unique identifier for the status",
                                "example": "sc901107394085_DCnaeiSB"
                              },
                              "status": {
                                "type": "string",
                                "description": "Display name of the status",
                                "example": "to do"
                              },
                              "orderindex": {
                                "type": "integer",
                                "description": "Position of this status in the status list",
                                "example": 0
                              },
                              "color": {
                                "type": "string",
                                "description": "Color code associated with this status",
                                "example": "#87909e"
                              },
                              "type": {
                                "type": "string",
                                "description": "Category of the status (e.g., open, closed, in progress)",
                                "example": "open"
                              },
                              "status_group": {
                                "type": "string",
                                "description": "TODO - Identifier for grouping related statuses",
                                "example": "subcat_901107394085"
                              }
                            }
                          }
                        },
                        "permission_level": {
                          "type": "string",
                          "description": "Access level the current user has for this List (e.g., create, edit, view)",
                          "example": "create"
                        }
                      }
                    }
                  }
                }
              }
            }
          },
          "400": {
            "description": "Bad request - Name is required, or is already taken",
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
                      "example": "OAUTH_117"
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
            "description": "Template, folder, or space not found"
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
      "name": "Lists"
    }
  ]
}
```