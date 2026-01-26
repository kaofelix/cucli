# Create a message reaction

This endpoint creates a message reaction using lower case emoji names.

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
    "/api/v3/workspaces/{workspace_id}/chat/messages/{message_id}/reactions": {
      "post": {
        "operationId": "createChatReaction",
        "summary": "Create a message reaction",
        "description": "This endpoint creates a message reaction using lower case emoji names.",
        "parameters": [
          {
            "name": "workspace_id",
            "in": "path",
            "description": "The ID of the Workspace.",
            "required": true,
            "schema": {
              "type": "integer",
              "x-readme-ref-name": "CommentPublicApiChatMessagesControllerCreateChatReactionWorkspaceIdPath"
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
          }
        ],
        "requestBody": {
          "required": true,
          "content": {
            "application/json": {
              "schema": {
                "type": "object",
                "properties": {
                  "reaction": {
                    "description": "The name of the emoji to use for the reaction.",
                    "type": "string"
                  }
                },
                "required": [
                  "reaction"
                ],
                "x-readme-ref-name": "CommentCreateChatReaction"
              }
            }
          }
        },
        "responses": {
          "201": {
            "description": "The message reaction is created.",
            "content": {
              "application/json": {
                "schema": {
                  "type": "object",
                  "properties": {
                    "date": {
                      "description": "The date & time the reaction was created (Unix epoch milliseconds timestamp).",
                      "type": "number"
                    },
                    "reaction": {
                      "description": "The reaction to the message.",
                      "type": "string"
                    },
                    "user_id": {
                      "description": "The ID of the user who created the reaction.",
                      "type": "string"
                    }
                  },
                  "required": [
                    "date",
                    "reaction",
                    "user_id"
                  ],
                  "x-readme-ref-name": "ChatReaction"
                }
              }
            }
          },
          "400": {
            "description": "Returns when the reaction {reaction} is not supported or already exists.",
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
            "description": "Returns when the message {messageId} is not found.",
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