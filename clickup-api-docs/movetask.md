# Move a task to a new List

Move a task to a new List. For Tasks in Multiple Lists, this endpoint only moves the task to a new home List.
 
[Learn more](doc:move-a-task-to-a-new-list) about the options available when moving a task to a new List.

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
    "/api/v3/workspaces/{workspace_id}/tasks/{task_id}/home_list/{list_id}": {
      "put": {
        "operationId": "moveTask",
        "summary": "Move a task to a new List",
        "description": "Move a task to a new List. For Tasks in Multiple Lists, this endpoint only moves the task to a new home List.\n \n[Learn more](https://developer.clickup.com/docs/move-a-task-to-a-new-list) about the options available when moving a task to a new List.",
        "parameters": [
          {
            "name": "workspace_id",
            "in": "path",
            "description": "The ID of the Workspace.",
            "required": true,
            "schema": {
              "type": "integer",
              "x-readme-ref-name": "TaskPublicApiTaskControllerMoveTaskWorkspaceIdPath"
            }
          },
          {
            "name": "task_id",
            "in": "path",
            "description": "The ID of the requested Task.",
            "required": true,
            "schema": {
              "type": "string"
            }
          },
          {
            "name": "list_id",
            "in": "path",
            "description": "The ID of the List to move the task to.",
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
                  "move_custom_fields": {
                    "description": "Add Custom Fields from the current List to the new List.",
                    "type": "boolean"
                  },
                  "custom_fields_to_move": {
                    "description": "An array of Custom Fields IDs to move. This parameter is not required to move all Custom Fields to the new List.",
                    "type": "array",
                    "items": {
                      "type": "string"
                    }
                  },
                  "status_mappings": {
                    "description": "Map the current List statuses to the statuses in the new List. You only need to include the ID of the task's current status and the ID of it's new status. **Note:** This parameter is required if the task's current status is not available in the new List.",
                    "type": "array",
                    "items": {
                      "type": "object",
                      "properties": {
                        "source_status_id": {
                          "description": "The ID of a status from the task's current List.",
                          "type": "string"
                        },
                        "destination_status_id": {
                          "description": "The ID of the respective status in the new List.",
                          "type": "string"
                        }
                      },
                      "required": [
                        "source_status_id",
                        "destination_status_id"
                      ],
                      "x-readme-ref-name": "TaskSingleStatusMappingDto"
                    }
                  }
                },
                "x-readme-ref-name": "TaskMoveTaskBodyParamsDto"
              }
            }
          }
        },
        "responses": {
          "200": {
            "description": "",
            "content": {
              "application/json": {
                "schema": {
                  "description": "Successfully updated the task home list",
                  "type": "object",
                  "properties": {
                    "data": {
                      "type": "object",
                      "properties": {
                        "task_id": {
                          "description": "The ID of the task.",
                          "type": "string",
                          "example": "123"
                        },
                        "new_list_id": {
                          "description": "The ID of the newlist.",
                          "type": "string",
                          "example": "123"
                        }
                      },
                      "required": [
                        "task_id",
                        "new_list_id"
                      ],
                      "x-readme-ref-name": "TaskMoveTaskResultRto"
                    }
                  },
                  "required": [
                    "data"
                  ],
                  "x-readme-ref-name": "TaskPublicApiTaskControllerMoveTask200Response"
                }
              }
            }
          },
          "400": {
            "description": "Returns when the request is invalid.",
            "content": {
              "application/json": {
                "schema": {
                  "type": "object",
                  "properties": {
                    "status": {
                      "description": "The HTTP Status code for the error",
                      "type": "integer"
                    },
                    "message": {
                      "description": "The message describing the error",
                      "type": "string",
                      "example": "Generic error message"
                    },
                    "trace_id": {
                      "description": "Unique trace ID for tracking the request. Used for troubleshooting errors",
                      "type": "integer",
                      "example": 123456789,
                      "nullable": true
                    },
                    "timestamp": {
                      "description": "The time of the error (Unix epoch milliseconds timestamp).",
                      "type": "integer",
                      "example": 1671534256138
                    }
                  },
                  "required": [
                    "status",
                    "message",
                    "trace_id",
                    "timestamp"
                  ],
                  "x-readme-ref-name": "TaskPublicApiErrorResponse"
                }
              }
            }
          },
          "404": {
            "description": "Returns when the task or list is not found.",
            "content": {
              "application/json": {
                "schema": {
                  "type": "object",
                  "properties": {
                    "status": {
                      "description": "The HTTP Status code for the error",
                      "type": "integer"
                    },
                    "message": {
                      "description": "The message describing the error",
                      "type": "string",
                      "example": "Generic error message"
                    },
                    "trace_id": {
                      "description": "Unique trace ID for tracking the request. Used for troubleshooting errors",
                      "type": "integer",
                      "example": 123456789,
                      "nullable": true
                    },
                    "timestamp": {
                      "description": "The time of the error (Unix epoch milliseconds timestamp).",
                      "type": "integer",
                      "example": 1671534256138
                    }
                  },
                  "required": [
                    "status",
                    "message",
                    "trace_id",
                    "timestamp"
                  ],
                  "x-readme-ref-name": "TaskPublicApiErrorResponse"
                }
              }
            }
          },
          "default": {
            "description": "Generic Error response",
            "content": {
              "application/json": {
                "schema": {
                  "type": "object",
                  "properties": {
                    "status": {
                      "description": "The HTTP Status code for the error",
                      "type": "integer"
                    },
                    "message": {
                      "description": "The message describing the error",
                      "type": "string",
                      "example": "Generic error message"
                    },
                    "trace_id": {
                      "description": "Unique trace ID for tracking the request. Used for troubleshooting errors",
                      "type": "integer",
                      "example": 123456789,
                      "nullable": true
                    },
                    "timestamp": {
                      "description": "The time of the error (Unix epoch milliseconds timestamp).",
                      "type": "integer",
                      "example": 1671534256138
                    }
                  },
                  "required": [
                    "status",
                    "message",
                    "trace_id",
                    "timestamp"
                  ],
                  "x-readme-ref-name": "TaskPublicApiErrorResponse"
                }
              }
            }
          }
        },
        "tags": [
          "Tasks"
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
      "description": "Tasks API",
      "name": "Tasks"
    }
  ],
  "security": [
    {
      "authHeader": []
    }
  ]
}
```