# Create a Direct Message

This endpoint creates a new Direct Message between up to 15 users. If a Direct Message between those users already exists it returns it.

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
    "/api/v3/workspaces/{workspace_id}/chat/channels/direct_message": {
      "post": {
        "operationId": "createDirectMessageChatChannel",
        "summary": "Create a Direct Message",
        "description": "This endpoint creates a new Direct Message between up to 15 users. If a Direct Message between those users already exists it returns it.",
        "parameters": [
          {
            "name": "workspace_id",
            "in": "path",
            "description": "The ID of the Workspace.",
            "required": true,
            "schema": {
              "type": "integer",
              "x-readme-ref-name": "ChatPublicApiChatChannelsControllerCreateDirectMessageChatChannelWorkspaceIdPath"
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
                  "user_ids": {
                    "description": "The unique user IDs of participants in the direct message Chat, up to 15. A Self DM is created when no user IDs are provided",
                    "type": "array",
                    "items": {
                      "type": "string"
                    },
                    "maxItems": 15,
                    "uniqueItems": true
                  }
                },
                "x-readme-ref-name": "ChatCreateDirectMessageChatChannel"
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
                  "description": "The existing Direct Message that is matching the creation request.",
                  "type": "object",
                  "properties": {
                    "data": {
                      "type": "object",
                      "properties": {
                        "id": {
                          "type": "string"
                        },
                        "name": {
                          "type": "string"
                        },
                        "description": {
                          "description": "The full Description of the Channel.",
                          "type": "string",
                          "format": "RichText"
                        },
                        "topic": {
                          "type": "string"
                        },
                        "type": {
                          "description": "The type of the room",
                          "type": "string",
                          "enum": [
                            "CHANNEL",
                            "DM",
                            "GROUP_DM"
                          ],
                          "x-readme-ref-name": "ChatRoomType"
                        },
                        "visibility": {
                          "description": "The visibility of the room",
                          "type": "string",
                          "enum": [
                            "PUBLIC",
                            "PRIVATE"
                          ],
                          "x-readme-ref-name": "ChatRoomVisibility"
                        },
                        "parent": {
                          "description": "Parent information",
                          "allOf": [
                            {
                              "type": "object",
                              "properties": {
                                "id": {
                                  "type": "string"
                                },
                                "type": {
                                  "type": "number"
                                }
                              },
                              "required": [
                                "id",
                                "type"
                              ],
                              "x-readme-ref-name": "ChatRoomParentDTO"
                            }
                          ]
                        },
                        "creator": {
                          "description": "ID of the user who created this room",
                          "type": "string"
                        },
                        "created_at": {
                          "description": "Timestamp of when this room was created",
                          "type": "string"
                        },
                        "updated_at": {
                          "description": "Timestamp of the last update in this room - Deprecated in favor of latest_comment_at",
                          "type": "string",
                          "deprecated": true
                        },
                        "workspace_id": {
                          "description": "Workspace ID of the chat room",
                          "type": "string"
                        },
                        "archived": {
                          "type": "boolean"
                        },
                        "latest_comment_at": {
                          "description": "Timestamp of the last comment in this room. Optional in the case of a new room with no comments yet",
                          "type": "string"
                        },
                        "is_canonical_channel": {
                          "description": "Is this the canonical channel for the parent location?",
                          "type": "boolean"
                        },
                        "is_hidden": {
                          "description": "Has the user hidden this room from their sidebar? Currently only an option for DM/Group DM.",
                          "type": "boolean"
                        },
                        "default_view": {
                          "description": "Data about the default view that the room should open in",
                          "allOf": [
                            {
                              "type": "object",
                              "properties": {
                                "type": {
                                  "type": "number"
                                },
                                "view_id": {
                                  "type": "string"
                                },
                                "standard": {
                                  "type": "boolean"
                                }
                              },
                              "required": [
                                "type",
                                "view_id",
                                "standard"
                              ],
                              "x-readme-ref-name": "ChatDefaultViewDTO"
                            }
                          ]
                        },
                        "channel_type": {
                          "description": "Type of channel (chat, project, etc.) aka subcategory_type",
                          "type": "number",
                          "enum": [
                            1,
                            2,
                            3,
                            4
                          ],
                          "x-readme-ref-name": "ChatSubcategoryType"
                        },
                        "counts": {
                          "description": "Counts relevant to the user requesting the chat room",
                          "allOf": [
                            {
                              "type": "object",
                              "properties": {
                                "parent_id": {
                                  "type": "string"
                                },
                                "parent_type": {
                                  "description": "Any object that can be shared in a Workspace. For example, `customField`, `dashboard`, `folder`, `goal`, `goalFolder`, `list`, `space`, `task`, and `view`.",
                                  "type": "string",
                                  "enum": [
                                    "attachment",
                                    "attachmentAccess",
                                    "approval",
                                    "banWorkspace",
                                    "checklist",
                                    "checklistItem",
                                    "checklistTemplateAccess",
                                    "comment",
                                    "commentsLastReadAt",
                                    "customField",
                                    "customFieldAccess",
                                    "customItem",
                                    "customPermissionLevel",
                                    "dashboard",
                                    "dashboardAccess",
                                    "doc",
                                    "docAccess",
                                    "folder",
                                    "folderDescendantsSet",
                                    "folderTemplateAccess",
                                    "form",
                                    "formulaValue",
                                    "foundationalJob",
                                    "goal",
                                    "goalAccess",
                                    "goalFolder",
                                    "goalFolderAccess",
                                    "hierarchy",
                                    "list",
                                    "listDescendantsSet",
                                    "listDescendantsPoints",
                                    "listDescendantsTimeEstimates",
                                    "listTemplateAccess",
                                    "notepad",
                                    "page",
                                    "pageAccess",
                                    "post",
                                    "reminder",
                                    "reminderAccess",
                                    "rolledUpFieldValue",
                                    "scheduledComment",
                                    "space",
                                    "spaceDescendantsSet",
                                    "spaceTemplateAccess",
                                    "task",
                                    "taskAccess",
                                    "taskHistory",
                                    "taskProperty",
                                    "taskTemplateAccess",
                                    "template",
                                    "user",
                                    "userAccess",
                                    "userGroup",
                                    "userHierarchy",
                                    "userPresence",
                                    "view",
                                    "viewAccess",
                                    "viewTemplateAccess",
                                    "whiteboard",
                                    "whiteboardAccess",
                                    "widget",
                                    "workspace",
                                    "workspaceDescendantsSet",
                                    "workscheduleWorkweekSchedule",
                                    "workscheduleScheduleExceptions"
                                  ],
                                  "x-readme-ref-name": "ObjectType"
                                },
                                "root_parent_id": {
                                  "type": "string"
                                },
                                "root_parent_type": {
                                  "description": "Any object that can be shared in a Workspace. For example, `customField`, `dashboard`, `folder`, `goal`, `goalFolder`, `list`, `space`, `task`, and `view`.",
                                  "type": "string",
                                  "enum": [
                                    "attachment",
                                    "attachmentAccess",
                                    "approval",
                                    "banWorkspace",
                                    "checklist",
                                    "checklistItem",
                                    "checklistTemplateAccess",
                                    "comment",
                                    "commentsLastReadAt",
                                    "customField",
                                    "customFieldAccess",
                                    "customItem",
                                    "customPermissionLevel",
                                    "dashboard",
                                    "dashboardAccess",
                                    "doc",
                                    "docAccess",
                                    "folder",
                                    "folderDescendantsSet",
                                    "folderTemplateAccess",
                                    "form",
                                    "formulaValue",
                                    "foundationalJob",
                                    "goal",
                                    "goalAccess",
                                    "goalFolder",
                                    "goalFolderAccess",
                                    "hierarchy",
                                    "list",
                                    "listDescendantsSet",
                                    "listDescendantsPoints",
                                    "listDescendantsTimeEstimates",
                                    "listTemplateAccess",
                                    "notepad",
                                    "page",
                                    "pageAccess",
                                    "post",
                                    "reminder",
                                    "reminderAccess",
                                    "rolledUpFieldValue",
                                    "scheduledComment",
                                    "space",
                                    "spaceDescendantsSet",
                                    "spaceTemplateAccess",
                                    "task",
                                    "taskAccess",
                                    "taskHistory",
                                    "taskProperty",
                                    "taskTemplateAccess",
                                    "template",
                                    "user",
                                    "userAccess",
                                    "userGroup",
                                    "userHierarchy",
                                    "userPresence",
                                    "view",
                                    "viewAccess",
                                    "viewTemplateAccess",
                                    "whiteboard",
                                    "whiteboardAccess",
                                    "widget",
                                    "workspace",
                                    "workspaceDescendantsSet",
                                    "workscheduleWorkweekSchedule",
                                    "workscheduleScheduleExceptions"
                                  ],
                                  "x-readme-ref-name": "ObjectType"
                                },
                                "date": {
                                  "description": "When the user last read comments to this object, set in the past to mark comments as unread. Should be a timestamp in milliseconds.",
                                  "type": "number"
                                },
                                "_version_vector": {
                                  "allOf": [
                                    {
                                      "type": "object",
                                      "properties": {
                                        "object_id": {
                                          "type": "string"
                                        },
                                        "object_type": {
                                          "type": "string"
                                        },
                                        "vector": {
                                          "type": "array",
                                          "items": {
                                            "type": "object",
                                            "properties": {
                                              "master_id": {
                                                "type": "number"
                                              },
                                              "version": {
                                                "type": "number"
                                              },
                                              "deleted": {
                                                "type": "boolean"
                                              }
                                            },
                                            "required": [
                                              "master_id",
                                              "version",
                                              "deleted"
                                            ],
                                            "x-readme-ref-name": "ChatCommentVector"
                                          }
                                        },
                                        "workspace_id": {
                                          "type": "number"
                                        }
                                      },
                                      "required": [
                                        "object_id",
                                        "object_type",
                                        "vector",
                                        "workspace_id"
                                      ],
                                      "x-readme-ref-name": "ChatCommentVersionVector"
                                    }
                                  ],
                                  "deprecated": true
                                },
                                "version": {
                                  "description": "The version of the object when the last read at object was last updated.",
                                  "type": "number"
                                },
                                "has_unread": {
                                  "description": "Whether the user has unread comments on this object. (Optional)",
                                  "type": "boolean"
                                },
                                "num_unread": {
                                  "description": "How many unread comments there are on this object. (Optional)",
                                  "type": "number"
                                },
                                "latest_comment_at": {
                                  "description": "The date of the latest comment on this object. (Optional)",
                                  "type": "number"
                                },
                                "badge_count": {
                                  "description": "The badge count for this object. (Optional)",
                                  "type": "number"
                                },
                                "thread_count": {
                                  "description": "The number of unread threads on this object. (Optional)",
                                  "type": "number"
                                },
                                "mention_count": {
                                  "description": "The number of mentions on this object. (Optional)",
                                  "type": "number"
                                },
                                "last_updated_at": {
                                  "description": "The date of the last update to this object. (Optional)",
                                  "type": "number"
                                }
                              },
                              "required": [
                                "parent_id",
                                "parent_type",
                                "root_parent_id",
                                "root_parent_type",
                                "date",
                                "_version_vector"
                              ],
                              "x-readme-ref-name": "ChatLastReadAtData"
                            }
                          ]
                        },
                        "chat_room_category": {
                          "description": "The category of the chat room, e.g. a welcome channel, (in the future, maybe) a ClickBot channel, etc.",
                          "type": "string",
                          "enum": [
                            "WELCOME_CHANNEL"
                          ]
                        },
                        "canvas_id": {
                          "description": "The id of the canvas owned by the chat room, if any",
                          "type": "string"
                        },
                        "links": {
                          "description": "The links to elements of the Channel.",
                          "allOf": [
                            {
                              "type": "object",
                              "properties": {
                                "members": {
                                  "description": "The link to the members of the Channel.",
                                  "type": "string"
                                },
                                "followers": {
                                  "description": "The link to the followers of the Channel.",
                                  "type": "string"
                                }
                              },
                              "required": [
                                "members",
                                "followers"
                              ],
                              "x-readme-ref-name": "ChatChannelLinks"
                            }
                          ]
                        }
                      },
                      "required": [
                        "id",
                        "name",
                        "type",
                        "visibility",
                        "parent",
                        "creator",
                        "created_at",
                        "updated_at",
                        "workspace_id",
                        "archived",
                        "links"
                      ],
                      "x-readme-ref-name": "ChatChannel"
                    }
                  },
                  "required": [
                    "data"
                  ],
                  "x-readme-ref-name": "ChatPublicApiChatChannelsControllerCreateDirectMessageChatChannel200Response"
                }
              }
            }
          },
          "201": {
            "description": "",
            "content": {
              "application/json": {
                "schema": {
                  "description": "The new Direct Message.",
                  "type": "object",
                  "properties": {
                    "data": {
                      "type": "object",
                      "properties": {
                        "id": {
                          "type": "string"
                        },
                        "name": {
                          "type": "string"
                        },
                        "description": {
                          "description": "The full Description of the Channel.",
                          "type": "string",
                          "format": "RichText"
                        },
                        "topic": {
                          "type": "string"
                        },
                        "type": {
                          "description": "The type of the room",
                          "type": "string",
                          "enum": [
                            "CHANNEL",
                            "DM",
                            "GROUP_DM"
                          ],
                          "x-readme-ref-name": "ChatRoomType"
                        },
                        "visibility": {
                          "description": "The visibility of the room",
                          "type": "string",
                          "enum": [
                            "PUBLIC",
                            "PRIVATE"
                          ],
                          "x-readme-ref-name": "ChatRoomVisibility"
                        },
                        "parent": {
                          "description": "Parent information",
                          "allOf": [
                            {
                              "type": "object",
                              "properties": {
                                "id": {
                                  "type": "string"
                                },
                                "type": {
                                  "type": "number"
                                }
                              },
                              "required": [
                                "id",
                                "type"
                              ],
                              "x-readme-ref-name": "ChatRoomParentDTO"
                            }
                          ]
                        },
                        "creator": {
                          "description": "ID of the user who created this room",
                          "type": "string"
                        },
                        "created_at": {
                          "description": "Timestamp of when this room was created",
                          "type": "string"
                        },
                        "updated_at": {
                          "description": "Timestamp of the last update in this room - Deprecated in favor of latest_comment_at",
                          "type": "string",
                          "deprecated": true
                        },
                        "workspace_id": {
                          "description": "Workspace ID of the chat room",
                          "type": "string"
                        },
                        "archived": {
                          "type": "boolean"
                        },
                        "latest_comment_at": {
                          "description": "Timestamp of the last comment in this room. Optional in the case of a new room with no comments yet",
                          "type": "string"
                        },
                        "is_canonical_channel": {
                          "description": "Is this the canonical channel for the parent location?",
                          "type": "boolean"
                        },
                        "is_hidden": {
                          "description": "Has the user hidden this room from their sidebar? Currently only an option for DM/Group DM.",
                          "type": "boolean"
                        },
                        "default_view": {
                          "description": "Data about the default view that the room should open in",
                          "allOf": [
                            {
                              "type": "object",
                              "properties": {
                                "type": {
                                  "type": "number"
                                },
                                "view_id": {
                                  "type": "string"
                                },
                                "standard": {
                                  "type": "boolean"
                                }
                              },
                              "required": [
                                "type",
                                "view_id",
                                "standard"
                              ],
                              "x-readme-ref-name": "ChatDefaultViewDTO"
                            }
                          ]
                        },
                        "channel_type": {
                          "description": "Type of channel (chat, project, etc.) aka subcategory_type",
                          "type": "number",
                          "enum": [
                            1,
                            2,
                            3,
                            4
                          ],
                          "x-readme-ref-name": "ChatSubcategoryType"
                        },
                        "counts": {
                          "description": "Counts relevant to the user requesting the chat room",
                          "allOf": [
                            {
                              "type": "object",
                              "properties": {
                                "parent_id": {
                                  "type": "string"
                                },
                                "parent_type": {
                                  "description": "Any object that can be shared in a Workspace. For example, `customField`, `dashboard`, `folder`, `goal`, `goalFolder`, `list`, `space`, `task`, and `view`.",
                                  "type": "string",
                                  "enum": [
                                    "attachment",
                                    "attachmentAccess",
                                    "approval",
                                    "banWorkspace",
                                    "checklist",
                                    "checklistItem",
                                    "checklistTemplateAccess",
                                    "comment",
                                    "commentsLastReadAt",
                                    "customField",
                                    "customFieldAccess",
                                    "customItem",
                                    "customPermissionLevel",
                                    "dashboard",
                                    "dashboardAccess",
                                    "doc",
                                    "docAccess",
                                    "folder",
                                    "folderDescendantsSet",
                                    "folderTemplateAccess",
                                    "form",
                                    "formulaValue",
                                    "foundationalJob",
                                    "goal",
                                    "goalAccess",
                                    "goalFolder",
                                    "goalFolderAccess",
                                    "hierarchy",
                                    "list",
                                    "listDescendantsSet",
                                    "listDescendantsPoints",
                                    "listDescendantsTimeEstimates",
                                    "listTemplateAccess",
                                    "notepad",
                                    "page",
                                    "pageAccess",
                                    "post",
                                    "reminder",
                                    "reminderAccess",
                                    "rolledUpFieldValue",
                                    "scheduledComment",
                                    "space",
                                    "spaceDescendantsSet",
                                    "spaceTemplateAccess",
                                    "task",
                                    "taskAccess",
                                    "taskHistory",
                                    "taskProperty",
                                    "taskTemplateAccess",
                                    "template",
                                    "user",
                                    "userAccess",
                                    "userGroup",
                                    "userHierarchy",
                                    "userPresence",
                                    "view",
                                    "viewAccess",
                                    "viewTemplateAccess",
                                    "whiteboard",
                                    "whiteboardAccess",
                                    "widget",
                                    "workspace",
                                    "workspaceDescendantsSet",
                                    "workscheduleWorkweekSchedule",
                                    "workscheduleScheduleExceptions"
                                  ],
                                  "x-readme-ref-name": "ObjectType"
                                },
                                "root_parent_id": {
                                  "type": "string"
                                },
                                "root_parent_type": {
                                  "description": "Any object that can be shared in a Workspace. For example, `customField`, `dashboard`, `folder`, `goal`, `goalFolder`, `list`, `space`, `task`, and `view`.",
                                  "type": "string",
                                  "enum": [
                                    "attachment",
                                    "attachmentAccess",
                                    "approval",
                                    "banWorkspace",
                                    "checklist",
                                    "checklistItem",
                                    "checklistTemplateAccess",
                                    "comment",
                                    "commentsLastReadAt",
                                    "customField",
                                    "customFieldAccess",
                                    "customItem",
                                    "customPermissionLevel",
                                    "dashboard",
                                    "dashboardAccess",
                                    "doc",
                                    "docAccess",
                                    "folder",
                                    "folderDescendantsSet",
                                    "folderTemplateAccess",
                                    "form",
                                    "formulaValue",
                                    "foundationalJob",
                                    "goal",
                                    "goalAccess",
                                    "goalFolder",
                                    "goalFolderAccess",
                                    "hierarchy",
                                    "list",
                                    "listDescendantsSet",
                                    "listDescendantsPoints",
                                    "listDescendantsTimeEstimates",
                                    "listTemplateAccess",
                                    "notepad",
                                    "page",
                                    "pageAccess",
                                    "post",
                                    "reminder",
                                    "reminderAccess",
                                    "rolledUpFieldValue",
                                    "scheduledComment",
                                    "space",
                                    "spaceDescendantsSet",
                                    "spaceTemplateAccess",
                                    "task",
                                    "taskAccess",
                                    "taskHistory",
                                    "taskProperty",
                                    "taskTemplateAccess",
                                    "template",
                                    "user",
                                    "userAccess",
                                    "userGroup",
                                    "userHierarchy",
                                    "userPresence",
                                    "view",
                                    "viewAccess",
                                    "viewTemplateAccess",
                                    "whiteboard",
                                    "whiteboardAccess",
                                    "widget",
                                    "workspace",
                                    "workspaceDescendantsSet",
                                    "workscheduleWorkweekSchedule",
                                    "workscheduleScheduleExceptions"
                                  ],
                                  "x-readme-ref-name": "ObjectType"
                                },
                                "date": {
                                  "description": "When the user last read comments to this object, set in the past to mark comments as unread. Should be a timestamp in milliseconds.",
                                  "type": "number"
                                },
                                "_version_vector": {
                                  "allOf": [
                                    {
                                      "type": "object",
                                      "properties": {
                                        "object_id": {
                                          "type": "string"
                                        },
                                        "object_type": {
                                          "type": "string"
                                        },
                                        "vector": {
                                          "type": "array",
                                          "items": {
                                            "type": "object",
                                            "properties": {
                                              "master_id": {
                                                "type": "number"
                                              },
                                              "version": {
                                                "type": "number"
                                              },
                                              "deleted": {
                                                "type": "boolean"
                                              }
                                            },
                                            "required": [
                                              "master_id",
                                              "version",
                                              "deleted"
                                            ],
                                            "x-readme-ref-name": "ChatCommentVector"
                                          }
                                        },
                                        "workspace_id": {
                                          "type": "number"
                                        }
                                      },
                                      "required": [
                                        "object_id",
                                        "object_type",
                                        "vector",
                                        "workspace_id"
                                      ],
                                      "x-readme-ref-name": "ChatCommentVersionVector"
                                    }
                                  ],
                                  "deprecated": true
                                },
                                "version": {
                                  "description": "The version of the object when the last read at object was last updated.",
                                  "type": "number"
                                },
                                "has_unread": {
                                  "description": "Whether the user has unread comments on this object. (Optional)",
                                  "type": "boolean"
                                },
                                "num_unread": {
                                  "description": "How many unread comments there are on this object. (Optional)",
                                  "type": "number"
                                },
                                "latest_comment_at": {
                                  "description": "The date of the latest comment on this object. (Optional)",
                                  "type": "number"
                                },
                                "badge_count": {
                                  "description": "The badge count for this object. (Optional)",
                                  "type": "number"
                                },
                                "thread_count": {
                                  "description": "The number of unread threads on this object. (Optional)",
                                  "type": "number"
                                },
                                "mention_count": {
                                  "description": "The number of mentions on this object. (Optional)",
                                  "type": "number"
                                },
                                "last_updated_at": {
                                  "description": "The date of the last update to this object. (Optional)",
                                  "type": "number"
                                }
                              },
                              "required": [
                                "parent_id",
                                "parent_type",
                                "root_parent_id",
                                "root_parent_type",
                                "date",
                                "_version_vector"
                              ],
                              "x-readme-ref-name": "ChatLastReadAtData"
                            }
                          ]
                        },
                        "chat_room_category": {
                          "description": "The category of the chat room, e.g. a welcome channel, (in the future, maybe) a ClickBot channel, etc.",
                          "type": "string",
                          "enum": [
                            "WELCOME_CHANNEL"
                          ]
                        },
                        "canvas_id": {
                          "description": "The id of the canvas owned by the chat room, if any",
                          "type": "string"
                        },
                        "links": {
                          "description": "The links to elements of the Channel.",
                          "allOf": [
                            {
                              "type": "object",
                              "properties": {
                                "members": {
                                  "description": "The link to the members of the Channel.",
                                  "type": "string"
                                },
                                "followers": {
                                  "description": "The link to the followers of the Channel.",
                                  "type": "string"
                                }
                              },
                              "required": [
                                "members",
                                "followers"
                              ],
                              "x-readme-ref-name": "ChatChannelLinks"
                            }
                          ]
                        }
                      },
                      "required": [
                        "id",
                        "name",
                        "type",
                        "visibility",
                        "parent",
                        "creator",
                        "created_at",
                        "updated_at",
                        "workspace_id",
                        "archived",
                        "links"
                      ],
                      "x-readme-ref-name": "ChatChannel"
                    }
                  },
                  "required": [
                    "data"
                  ],
                  "x-readme-ref-name": "ChatPublicApiChatChannelsControllerCreateDirectMessageChatChannel201Response"
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
                  "x-readme-ref-name": "ChatPublicApiErrorResponse"
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