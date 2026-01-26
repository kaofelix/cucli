# Retrieve message reactions

This endpoint retrieves the reactions to a message.

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
      "get": {
        "operationId": "getChatMessageReactions",
        "summary": "Retrieve message reactions",
        "description": "This endpoint retrieves the reactions to a message.",
        "parameters": [
          {
            "name": "workspace_id",
            "in": "path",
            "description": "The ID of the Workspace.",
            "required": true,
            "schema": {
              "type": "integer",
              "x-readme-ref-name": "CommentPublicApiChatMessagesControllerGetChatMessageReactionsWorkspaceIdPath"
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
            "name": "cursor",
            "in": "query",
            "description": "The cursor to use to fetch the next page of results.",
            "required": false,
            "schema": {
              "type": "string"
            }
          },
          {
            "name": "limit",
            "in": "query",
            "description": "The maximum number of results to fetch for this page.",
            "required": false,
            "schema": {
              "type": "integer",
              "default": 50,
              "maximum": 100,
              "minimum": 1,
              "x-readme-ref-name": "CommentPublicApiChatMessagesControllerGetChatMessageReactionsLimitQuery"
            }
          }
        ],
        "responses": {
          "200": {
            "description": "",
            "content": {
              "application/json": {
                "schema": {
                  "allOf": [
                    {
                      "type": "object",
                      "properties": {
                        "next_cursor": {
                          "description": "The next cursor to use for pagination.",
                          "type": "string"
                        }
                      },
                      "required": [
                        "next_cursor"
                      ],
                      "x-readme-ref-name": "CommentPaginatedResponse"
                    },
                    {
                      "type": "object",
                      "description": "The list of message reactions.",
                      "properties": {
                        "data": {
                          "type": "array",
                          "items": {
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
                    }
                  ],
                  "x-readme-ref-name": "CommentPublicApiChatMessagesControllerGetChatMessageReactions200Response"
                }
              }
            }
          },
          "404": {
            "description": "Returns when the specified {messageId} was not found.",
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