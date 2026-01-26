# Send a message

This endpoint creates a top level message.

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
    "/api/v3/workspaces/{workspace_id}/chat/channels/{channel_id}/messages": {
      "post": {
        "operationId": "createChatMessage",
        "summary": "Send a message",
        "description": "This endpoint creates a top level message.",
        "parameters": [
          {
            "name": "workspace_id",
            "in": "path",
            "description": "The ID of the Workspace.",
            "required": true,
            "schema": {
              "type": "integer",
              "x-readme-ref-name": "CommentPublicApiChatMessagesControllerCreateChatMessageWorkspaceIdPath"
            }
          },
          {
            "name": "channel_id",
            "in": "path",
            "description": "The ID of the Channel where the messages live.",
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
                  "assignee": {
                    "description": "The possible assignee of the message.",
                    "type": "string"
                  },
                  "group_assignee": {
                    "description": "The possible group assignee of the message.",
                    "type": "string"
                  },
                  "triaged_action": {
                    "description": "The triaged action applied to the message.",
                    "type": "number",
                    "enum": [
                      1,
                      2
                    ]
                  },
                  "triaged_object_id": {
                    "description": "The message triaged action object id.",
                    "type": "string"
                  },
                  "triaged_object_type": {
                    "description": "The message triaged action object type.",
                    "type": "number"
                  },
                  "type": {
                    "description": "The type of message.",
                    "type": "string",
                    "enum": [
                      "message",
                      "post"
                    ]
                  },
                  "content": {
                    "description": "The full content of the message to be created. Note: Some code examples may display additional backslashes.",
                    "format": "RichText",
                    "maxLength": 40000,
                    "type": "string"
                  },
                  "reactions": {
                    "description": "The reactions to the message that exist at creation time",
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
                    },
                    "maxItems": 10
                  },
                  "followers": {
                    "description": "The ids of the followers of the message",
                    "type": "array",
                    "items": {
                      "type": "string"
                    },
                    "maxItems": 10
                  },
                  "content_format": {
                    "description": "The format of the Chat Message content (Default: text/md)",
                    "type": "string",
                    "default": "text/md",
                    "enum": [
                      "text/md",
                      "text/plain"
                    ]
                  },
                  "post_data": {
                    "description": "The data of the post message.",
                    "allOf": [
                      {
                        "type": "object",
                        "properties": {
                          "title": {
                            "description": "The title of the chat post.",
                            "type": "string",
                            "maxLength": 255
                          },
                          "subtype": {
                            "description": "The subtype of the chat post.",
                            "allOf": [
                              {
                                "type": "object",
                                "properties": {
                                  "id": {
                                    "description": "The subtype ID of the chat post. You can retrieve the available subtypes for your Workspace using the [Get Post Subtype IDs](https://developer.clickup.com/reference/getsubtypes) endpoint.",
                                    "type": "string"
                                  }
                                },
                                "required": [
                                  "id"
                                ],
                                "x-readme-ref-name": "CommentChatPostSubtypeCreate"
                              }
                            ]
                          }
                        },
                        "required": [
                          "title",
                          "subtype"
                        ],
                        "x-readme-ref-name": "CommentChatPostDataCreate"
                      }
                    ]
                  }
                },
                "required": [
                  "type",
                  "content"
                ],
                "x-readme-ref-name": "CommentCreateChatMessage"
              }
            }
          }
        },
        "responses": {
          "201": {
            "description": "The message is created.",
            "content": {
              "application/json": {
                "schema": {
                  "type": "object",
                  "properties": {
                    "post_data": {
                      "description": "The data of the post message.",
                      "allOf": [
                        {
                          "type": "object",
                          "properties": {
                            "title": {
                              "description": "The title of the chat post.",
                              "type": "string",
                              "maxLength": 255
                            },
                            "subtype": {
                              "description": "The subtype of the chat post.",
                              "allOf": [
                                {
                                  "type": "object",
                                  "properties": {
                                    "id": {
                                      "description": "The subtype ID of the chat post. You can retrieve the available subtypes for your Workspace using the [Get Post Subtype IDs](https://developer.clickup.com/reference/getsubtypes) endpoint.",
                                      "type": "string"
                                    }
                                  },
                                  "required": [
                                    "id"
                                  ],
                                  "x-readme-ref-name": "CommentChatPostSubtypeCreate"
                                }
                              ]
                            }
                          },
                          "required": [
                            "title",
                            "subtype"
                          ],
                          "x-readme-ref-name": "CommentChatPostDataCreate"
                        }
                      ]
                    },
                    "assignee": {
                      "description": "The possible assignee of the message.",
                      "type": "string"
                    },
                    "assigned_by": {
                      "description": "The user who assigned the message.",
                      "type": "string"
                    },
                    "content": {
                      "description": "The full content of the message.",
                      "format": "RichText",
                      "type": "string"
                    },
                    "date": {
                      "description": "The date & time the message was created (Unix epoch milliseconds timestamp).",
                      "type": "number"
                    },
                    "date_assigned": {
                      "description": "The date & time the message was assigned (Unix epoch milliseconds timestamp).",
                      "type": "number"
                    },
                    "date_resolved": {
                      "description": "The date & time the message was resolved (Unix epoch milliseconds timestamp).",
                      "type": "number"
                    },
                    "date_updated": {
                      "description": "The date & time the message was updated (Unix epoch milliseconds timestamp).",
                      "type": "number"
                    },
                    "group_assignee": {
                      "description": "The possible group assignee of the message.",
                      "type": "string"
                    },
                    "id": {
                      "description": "The ID of the message.",
                      "type": "string"
                    },
                    "parent_channel": {
                      "description": "The ID of the chat this message belongs to.",
                      "type": "string"
                    },
                    "parent_message": {
                      "description": "The ID of the message this message is a reply to.",
                      "type": "string"
                    },
                    "resolved": {
                      "description": "The resolved status of the message.",
                      "type": "boolean"
                    },
                    "resolved_by": {
                      "description": "The user who resolved the message.",
                      "type": "string"
                    },
                    "triaged_action": {
                      "description": "The triaged action applied to the message.",
                      "type": "number",
                      "enum": [
                        1,
                        2
                      ]
                    },
                    "triaged_object_id": {
                      "description": "The message triaged action object id.",
                      "type": "string"
                    },
                    "triaged_object_type": {
                      "description": "The message triaged action object type.",
                      "type": "number"
                    },
                    "type": {
                      "description": "The type of message.",
                      "type": "string",
                      "enum": [
                        "message",
                        "post"
                      ]
                    },
                    "user_id": {
                      "description": "The ID of the user who created the message.",
                      "type": "string"
                    },
                    "links": {
                      "description": "The links to elements of the message.",
                      "allOf": [
                        {
                          "type": "object",
                          "properties": {
                            "reactions": {
                              "description": "The link to the reactions of this message.",
                              "type": "string"
                            },
                            "replies": {
                              "description": "The link to the replies of this message.",
                              "type": "string"
                            },
                            "tagged_users": {
                              "description": "The link to the tagged users of this message.",
                              "type": "string"
                            }
                          },
                          "required": [
                            "reactions",
                            "replies",
                            "tagged_users"
                          ],
                          "x-readme-ref-name": "CommentChatMessageLinks2"
                        }
                      ]
                    },
                    "replies_count": {
                      "description": "The number of replies to the message.",
                      "type": "number"
                    }
                  },
                  "required": [
                    "content",
                    "date",
                    "id",
                    "parent_channel",
                    "resolved",
                    "type",
                    "user_id",
                    "links",
                    "replies_count"
                  ],
                  "x-readme-ref-name": "CommentCreateChatMessageResponse"
                }
              }
            }
          },
          "404": {
            "description": "Returns when {channelId} was not found.",
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