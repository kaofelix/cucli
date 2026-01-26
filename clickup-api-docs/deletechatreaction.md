# Delete a message reaction

This endpoint deletes a message reaction.

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
    "/api/v3/workspaces/{workspace_id}/chat/messages/{message_id}/reactions/{reaction}": {
      "delete": {
        "operationId": "deleteChatReaction",
        "summary": "Delete a message reaction",
        "description": "This endpoint deletes a message reaction.",
        "parameters": [
          {
            "name": "workspace_id",
            "in": "path",
            "description": "The ID of the Workspace.",
            "required": true,
            "schema": {
              "type": "integer",
              "x-readme-ref-name": "CommentPublicApiChatMessagesControllerDeleteChatReactionWorkspaceIdPath"
            }
          },
          {
            "name": "message_id",
            "in": "path",
            "description": "The ID of the specified message.",
            "required": true,
            "schema": {
              "type": "string"
            }
          },
          {
            "name": "reaction",
            "in": "path",
            "description": "The name of the reaction to be deleted.",
            "required": true,
            "schema": {
              "type": "string"
            }
          }
        ],
        "responses": {
          "204": {
            "description": "The message reaction was deleted.",
            "content": {
              "application/json": {}
            }
          },
          "400": {
            "description": "Returns when the reaction {reaction} is not supported.",
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
                  "x-readme-ref-name": "CommentPublicApiErrorResponse"
                }
              }
            }
          },
          "404": {
            "description": "Returns when the message {messageId} or the reaction {reaction} is not found.",
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
                  "x-readme-ref-name": "CommentPublicApiErrorResponse"
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
                  "x-readme-ref-name": "CommentPublicApiErrorResponse"
                }
              }
            }
          }
        },
        "tags": [
          "Chat"
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
      "description": "Chat API",
      "name": "Chat"
    }
  ],
  "security": [
    {
      "authHeader": []
    }
  ]
}
```